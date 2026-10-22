---
name: Shared activity log
description: >-
  Use after finishing, deciding, sending, handing off, getting blocked or
  failing on any task, before flagging anything to Wuyue, and before starting
  work that may already be known.
---
# Shared memory + activity log (Notion, CoS area)
General Instructions (standing rules + Closed, don't flag): https://app.notion.com/p/3fec4091fdc3811b88b9db26c34bf6fa
Memories db (one page per bot): https://app.notion.com/p/3f04f392a6b442e395dd23060b8acaf8 (collection://7bfbfd84-531c-48b9-8ad1-73664389e670)
Activity log: https://app.notion.com/p/ebb84070e0b140cfa892411eb165e3aa (collection://8f2650aa-629b-43e8-a58b-2fe5b5a85ec4)
Open asks: https://app.notion.com/p/36eebceb89e447739e80c9061eab31b5 (collection://7c32a8c5-825c-45ff-8b41-162707b34b4b)
Task Desk / Bot Factory board: https://app.notion.com/p/ce62015c4f0747118f569c646f25e15b (collection://a2c09a96-4371-433f-a683-e797bbf3917f)
Decision log: https://app.notion.com/p/bce4a43d331d45409cbedf8f3c1d8fc3 (collection://5d31b99e-3eb7-4063-8bd1-05771b6d774e)
Trips: https://app.notion.com/p/412a50d0ceae4371acd827bb21afc2ad (collection://1b5c1902-fc7d-429e-85cc-6de442fbde46)
Places: https://app.notion.com/p/4cbbe34566df465e907675adb56a47ee (collection://82417ec5-d564-4707-8b10-cc17938335b2)

## Before work
- Read General Instructions and your own Memories page.
- Search the Activity log for the Task ID or topic.
- Before flagging anything to Wuyue, check Closed, don't flag and Open asks. If it's closed, don't raise it. If an Open ask already exists, link to it instead of re-flagging.

## After work: append ONE Activity log row
- Summary: one line, outcome first. Put longer detail in the page body, never the title.
- Fields: Bot, Kind (Done/Decision/Blocked/Failed/Handoff/FYI), Task ID, When (ET), Topic tags, Link.
- Needs Wuyue: check only for a NEW ask that isn't already in Open asks.
- Append only. Never edit or delete other bots' rows.
- No-op runs and repeat briefings: write nothing.
- Never log secrets, codes, or full message bodies.
- Keep any text block under ~1,900 characters.

## Asks and blocks
- Blocked: set your Task Desk row to Blocked (Owner bot, Task ID, Last touched), and add an Open asks row with Type = Blocker.
- Optional question for Wuyue: add an Open asks row with Type = Optional.
- Reminders: remind once after ~12h (set Reminder sent, Status Reminded).
- Blockers never auto-drop; they roll into the weekly summary. Optional asks drop after 48h.
- Decision by Wuyue: also add a Decision log row. If it closes something, add it to Closed, don't flag.

## Memory sync (weekdays)
Each weekday morning, copy any new durable facts from your built-in memory into Key facts on your Memories page, and set Last synced. Write nothing if nothing changed.

## Trips and Places
- Booked travel goes in Trips: dates, flights, hotel, confirmation numbers.
- Verified recommendations go in Places: Maps link, booking link, Verified on.

## CoS
- Lookup order: Memories/General Instructions, then Activity log, Task Desk, Decision log, Trips/Places, mem0, and last the bot's own chat.
- Sunday: rewrite the CoS Desk weekly stack for the coming week. Add one Weekly summary row with counts (rows per bot, open blockers, closed items). Promote repeated facts to General Instructions.
- Wednesday self-check: list bots with zero Activity log rows that week.
