---
name: xunji-trains
description: >-
  Use when reading or writing 训记/TrainNote lifting sessions via Open API (sets,
  volume, plan) — never invent sets; confirm before any write.
---
# 训记训练数据 Open API

## Principles
- Call only when the user (or a coach morning/weekly call) needs training reads, or the user explicitly asks to write back.
- Before any write: show a change summary and wait for confirmation. Never send writes unconfirmed.
- Cache reads by `datestr` under `/workspace/xunji-cache/`. Same day: do not re-request unless `--force`.
- Auth token lives at `/home/box/.config/xunji-coach/token_trains` (mode 600). Never log it, never paste into chat, never put in query/body.

## Endpoints
- Base: `https://trains.xunjiapp.cn`
- Read: `POST /api_trains_for_llm_v2`
- Write: `POST /api_upsert_trains_for_llm_v2`
- Official plans: `https://api.xunjiapp.cn` `POST /open/plan/query_gzip` (same trains token)
- Movement names: https://github.com/Foveluy/Xunji-movements
- Responses may be gzip; decompress before JSON. Core data in `res` (do not require `success === true`).

## Read helper
```bash
python3 /home/box/.config/xunji-coach/read_trains.py YYYY-MM-DD
# optional: --full  --force
```
Default `include_full_data: false`. Use `--full` for unchecked sets, RPE, notes, laterality, rest seconds, heart-rate summaries.

## Write rules (summary)
- Chinese `name` only, no internal keys. Max 4 trains/day, 15 movements, 20 sets each.
- Keep `localid`/`start`/`end` on updates. Native cardio days: one `cardio: true` movement, metrics on movement, no sets.
- Rate limits: read 15s (full 30s), write 45s. On `too frequent`, wait `retry_after_ms`.
- Invalid key: ask user to re-issue from App and resend the skill.
