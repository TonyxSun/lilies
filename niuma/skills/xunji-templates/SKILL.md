---
name: xunji-templates
description: >-
  Use when managing 训记 Agent personal templates (list/sync/create/update/delete)
  — confirm every mutation; one folder max 14 templates.
---
# 训记 Agent 个人模版

## Principles
- Only the single Agent-owned folder. Never create a second folder. Max 14 templates, 15 movements, 20 sets.
- Confirm every mutation (rename/upsert/delete) with the user before `confirmed: true`.
- Token: `/home/box/.config/xunji-coach/token_templates`. Never log or show it.
- Persist sync cursor in `/home/box/.config/xunji-coach/templates_cursor.json`. First sync `cursor: 0` only if cache lost or `cursor invalid`.

## Endpoints (Base `https://trains.xunjiapp.cn`)
- Sync: `POST /api_agent_templates_sync_for_llm_v1` — `limit: 15`, gzip responses.
- Mutate: `POST /api_agent_templates_mutate_for_llm_v1` — unique `mutation_id`, `confirmed: true` after user OK.

## Rules
- Names: Chinese/letters/digits/spaces only (max 32 for folder). No emoji/punctuation.
- Prefer public `movements` on create; on edit, may round-trip native `movement`/`rules`.
- On version conflict: re-sync, show conflict, ask user.
