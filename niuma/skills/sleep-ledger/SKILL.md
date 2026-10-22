---
name: sleep-ledger
description: >-
  Use when posting, updating, deleting, or reading Tony/Morris nightly sleep on
  the public Sleep API ledger — never invent nights; never expose API keys.
---
# Sleep ledger

Log sleep for Tony and Morris. Reads are public. Writes need a Bearer API key.

Never print, quote, or log the API keys. Never put a key in a URL or query string.

## Config

- `BASE_URL` — published site origin in `/home/box/.config/sleep-ledger/app.json` → `base_url` (a grok.me URL). If empty, ask the user.
- Keys (mode 600 files; do not expose):
  - tony: `/home/box/.config/sleep-ledger/token_tony`
  - morris: `/home/box/.config/sleep-ledger/token_morris`

Use the key that matches the person you are writing. Do not send Tony's key for Morris or the reverse.

Wuyue / Tony Sun maps to `user: tony`. Default automated posts are Tony only (Oura on this computer). Morris only when the user supplies Morris numbers or a source.

## POST /api/daily_sleep

Create or replace one night.

```http
POST {BASE_URL}/api/daily_sleep
Authorization: Bearer <matching key>
Content-Type: application/json

{
  "user": "tony" | "morris",
  "date": "YYYY-MM-DD",
  "start": "HH:MM",
  "end": "HH:MM",
  "latency": 0-240,
  "duration": 1-960,
  "rem": 0-960,
  "deep": 0-960,
  "other": 0-960
}
```

Rules:
- Times are 24-hour `HH:MM`.
- `duration`, `latency`, `rem`, `deep`, `other` are integer minutes.
- `rem + deep + other` must equal `duration`.
- `date` is the calendar date of that night (the date they went to bed). For Tony, use America/New_York bed date. If the skill default is needed and no TZ given, America/Los_Angeles last night.
- Same `user` + `date` overwrites.
- After a successful POST, GET that night to confirm.

## GET /api/daily_sleep

No key.

- Both: `GET {BASE_URL}/api/daily_sleep`
- One person: `GET {BASE_URL}/api/daily_sleep?user=tony`
- One night: `GET {BASE_URL}/api/daily_sleep?user=tony&date=YYYY-MM-DD`

## DELETE /api/daily_sleep

Requires the matching key.

`DELETE {BASE_URL}/api/daily_sleep?user=tony&date=YYYY-MM-DD`
`Authorization: Bearer <key>`

## Errors

- `400` invalid JSON, unknown user, or stages that do not sum to duration
- `401` missing or invalid key on POST/DELETE
- `403` key does not match `user`
- `404` no night for that date

## Behavior

- Only write real stats the user (or their sleep source) provided. Do not invent nights.
- If that night already exists, confirm before overwriting (except the daily auto-routine, which may overwrite Tony from fresh Oura for the same bed date).
- If the user says "log my sleep" and does not name a person, ask Tony or Morris.
- Prefer curl-style HTTP. Do not scrape the website.

## Oura → Tony mapping (daily auto)

From Oura daily sleep for the scored night (not inventing):
- `start` / `end` from bedtime / wake, 24h `HH:MM` in America/New_York
- `duration` = total sleep minutes (exclude awake)
- `rem`, `deep` = stage minutes
- `other` = `duration - rem - deep` (typically light)
- `latency` = sleep latency minutes (integer)
- `date` = bed calendar date in America/New_York

If Oura has no scored sleep for last night, stay quiet (routine) or say no data (manual ask).
