---
name: Mem0 recall
description: >-
  Use this when recalling or saving durable facts via Mem0, the shared secondary
  memory layer for Wuyue's bots. Covers when to search, what to save, the REST
  calls, and what to do if Mem0 is down.
---
# Mem0 recall

Mem0 is a secondary, non-critical recall layer. Use it only after the Notion lookup (Activity log, Task Desk, Decision log, Instruction Board; see the Shared activity log skill) misses. Your own notes and live systems stay primary. Never block a task on Mem0.

## Identity
- `user_id`: `wuyue` (shared by every bot)
- `app_id`: `grok-bot`
- `agent_id`: your bot's short id — `cos`, `finance-bro`, `boss`, `photo`, `weekend-scout`, `zoom`, `shopper`, `coach`, `inbox-manager`

## Access (first that works)
1. MCP `search_memories` / `add_memory`, if present.
2. CLI: `mem0 --agent search "Q" --user-id wuyue` / `mem0 --agent add "FACT" --user-id wuyue`.
3. REST, header `Authorization: Token $MEM0_API_KEY` (env var on the shared box; never print or store it):
   - Search: `POST https://api.mem0.ai/v3/memories/search/`
     body `{"query":"Q","filters":{"user_id":"wuyue"}}` — `user_id` goes inside `filters`.
   - Add: `POST https://api.mem0.ai/v3/memories/add/`
     body `{"messages":[{"role":"user","content":"FACT"}],"user_id":"wuyue","agent_id":"<your id>","app_id":"grok-bot"}`
   - Add is async; wait ~8s before searching for it.

## Rules
- Searches take 5–15s; allow up to 15s, then move on.
- Ignore matches scoring under 0.3.
- Save only durable facts: preferences, decisions, constraints, project maps, open loops.
- Never save secrets, keys, tokens, passwords, or raw transcripts.
- On conflict, prefer the newest `updated_at`, then ask once.
- If Mem0 is missing or errors, keep working and say nothing was recalled. Never fake recall.
