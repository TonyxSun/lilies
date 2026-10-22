---
name: xunji-food
description: >-
  Use when the user explicitly asks to read, search, log, or template 训记
  diet/food data — confirm before any write; coach is not a nutritionist.
---
# 训记饮食数据 Open API

## Principles
- Call only on explicit user ask. Confirm before write/custom food/template apply.
- Cache by query. Date window: past year to +3 months.
- Tokens: records `/home/box/.config/xunji-coach/token_food`; search `/home/box/.config/xunji-coach/token_food_search`. Never log/show.
- Coach anti-job: not a nutritionist — do not invent meal plans; only fetch/log what they ask.

## Endpoints
- Records base `https://eatings.xunjiapp.cn`: query/upsert/custom/templates gzip routes under `/open/food/...`
- Search base `https://api.xunjiapp.cn`: `POST /open_agent/food/search_gzip`
- Prefer search `uniquekey` + `ntr` before writing. Create custom food only when search fails and user confirms nutrition source.
