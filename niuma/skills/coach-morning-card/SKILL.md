---
name: coach-morning-card
description: >-
  Use this when delivering the weekday morning training call (or a one-off call)
  so Oura + Garmin numbers render as a designed PNG card instead of a prose wall.
---
# Coach morning card

## When
Every weekday morning call after 11:30am ET. Also any on-demand push/maintain/recover call.

## Hard rules
- **Today only.** Card metrics must be today's scored Oura readiness/sleep and today's Garmin figures. If a feed is unscored or missing, set `has_data: false` and show "no data" — never fill with yesterday.
- Never invent numbers or 训记 sets.
- Chat: one short recommendation line, then attach the PNG. Numbers live on the card.

## Render
1. Write JSON to `/workspace/coach-card/today.json` matching the schema below.
2. Run:
```bash
node /home/box/agent-data/workflows/coach-morning-card/render.mjs \
  --data /workspace/coach-card/today.json \
  --out /workspace/coach-card/morning-call.png
```
3. Attach `file:///workspace/coach-card/morning-call.png` with the call.

Template HTML: `card.html` in this folder. Palette: black `#000`, Push `#16ec06`, Maintain `#ffde00`, Recover `#ff3b30`, Oura accent `#7ec8ff`, Garmin accent `#7dffb3`.

## JSON schema
```json
{
  "date_label": "Fri Sep 11 · ET",
  "call": "Maintain",
  "why": "one dry clause",
  "oura": {
    "has_data": true,
    "readiness": 78,
    "sleep_score": 88,
    "duration": "7h 45m",
    "hrv": 80,
    "rhr": 51,
    "bed_wake": "1:26am → 9:45am"
  },
  "garmin": {
    "has_data": true,
    "status": "Recovery",
    "acute_load": 139,
    "acute_label": "Low",
    "load_ratio": "0.6",
    "vo2max": 56,
    "hrv_7d": 87,
    "last_session": "Sep 9 Strength"
  },
  "xunji": { "status": "blocked", "note": "no data" }
}
```
If `oura.has_data` or `garmin.has_data` is false, that column shows "no data".
