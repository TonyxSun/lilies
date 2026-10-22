---
name: Inbox triage
description: >-
  Use when scanning Outlook (and optionally Gmail) to build a short focus board
  up to 5 items, plus daily unsubscribe candidates for Notion approval. Never
  send. Never unsubscribe without approval.
---
Scan Outlook (main inbox) for a short focus board and daily unsubscribe candidates. Never send. Never answer as the user. Never unsubscribe without approval.

1. Read Outlook first (connector). Gmail only if needed. Skip Slack.
2. VERIFY-BEFORE-ASSERT: read the full live message before flagging unanswered.
3. Lead with up to ~5 important+urgent focus items — fewer or silence if nothing qualifies. Optional: today / waiting / fyi.
4. Fail-closed: empty source = one honest line. Negative search = UNVERIFIED as a search result.
5. Draft 0–5 only when useful, labeled draft. Never send. Never answer as the user.
6. Each run: pick ~2–5 unsubscribe candidates (repeat newsletters/promos). Append to the Notion Outlook unsubscribe candidates doc with sender, subject sample, why — status pending. Never unsubscribe/delete until the human approves.
7. Quiet if nothing qualifies for the fire board (still may append unsubscribe candidates when useful).
