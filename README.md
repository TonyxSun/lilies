# lilies of the field

Audit trail for Wuyue's investing system: what it decided each day, and why.

## How to read it
Start at `days/`. Each file is one trading day and stands on its own. It covers what the system saw, what it decided, the reasoning, and the sources, all in that one file. You never need another file to follow a day's decision.

## Layout
```
days/YYYY-MM-DD.md   one file per day: state, decisions, rationale, sources, open questions
rules.md             Wuyue's rules and the mechanical risk limits currently in force
strategy.md          the current strategy, with a dated changelog of every change and why
system/              how the system runs: daily schedule (routine prompts) and memory snapshot
sources/             raw source notes, kept for reference only (day files quote what they use)
```

## Conventions
- All times are US Eastern.
- Every number carries a source and a date. If something wasn't available, the file says so instead of guessing.
- One commit per trading day, after that day's steps finish: `day: YYYY-MM-DD`.
- No secrets, tokens, passwords or account numbers are ever committed.
- Live working notes also live on the shared Notion page "lilies of the field 投资决策（共享）". This repo is the permanent record.
