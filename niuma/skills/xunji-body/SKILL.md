---
name: xunji-body
description: >-
  Use when the user explicitly asks to read, export, compare, or log 训记 body
  metrics (weight, bodyfat, circumferences) — confirm before write; no medical
  diagnosis.
---
# 训记身体数据 Open API

## Principles
- Call only on explicit user ask. Confirm writes (date, type, value, unit) before `confirmed: true`.
- Cache by date range + types. Token: `/home/box/.config/xunji-coach/token_body`. Never log/show.
- Not medical advice. Coach is not a nutritionist/therapist — summarize numbers only.

## Endpoints (Base `https://api.xunjiapp.cn`)
- Query: `POST /open/body/query_gzip`
- Upsert: `POST /open/body/upsert_gzip` — dry_run first, then `dry_run: false` + `confirmed: true`.

## Types
`weight` (kg), `bodyfat` (%), `neck`/`chest`/`weist`/`shoulder`/`bot` (cm; waist is historically `weist`), limb sides `arm_*`/`forearm_*`/`leg_*`/`cav_*`.
