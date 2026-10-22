# lilies — Jane Street investing group audit log

Private audit trail for Wuyue's investing group: **Trader** (positions, orders, strategy) and **牛马** (research).
Shared working doc: [Jane Street 投资决策（共享）](https://app.notion.com/p/401c4091fdc381deae99d96515e376d8) (Notion).

## Layout
```
niuma/                 牛马 (research bot)
  profile/             name, description, standing rules
  skills/              user-created skills available to this bot (snapshot)
  memory/              memory export relevant to this group + Wuyue's standing rules
  research/            source notes (posts, comments, X threads)
  logs/YYYY-MM-DD.md   daily event log
trader/                Trader's folder (same layout), committed from Trader's daily log lines
```

## Commit policy
- One commit per trading day after the day's steps finish: `log: YYYY-MM-DD`.
- No secrets, tokens, passwords or account numbers are ever committed.
- Platform built-in system prompts are not included; bot profiles, rules, skills and memory are.
