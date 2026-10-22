# lilies of the field: knowledge system

## The loop (for each area)
1. **Plan.** Write down what we need to learn, which sources are good, and which strategies to test. Put it in `cycles/<n>-<area>.md`.
2. **Do.** Research it, take notes with sources and dates, and turn the findings into rule candidates.
3. **Log.** Record the findings in every tier below.

The outer loop repeats this across areas: fundamentals, technicals, news and catalysts, prediction markets and sentiment, and more. After each cycle, re-score what belongs in HOT.

## Memory tiers
| Tier | Analogy | Where | What goes there | Size |
|---|---|---|---|---|
| Hot | RAM | Notion "Condensed rules" section, mirrored in `HOT.md` | The condensed rules and facts currently driving decisions. Read at the start of every run. | ≤ 15 rules |
| Warm | cache | `areas/<area>.md` + Notion "Knowledge base" | Per-area digests: findings, evidence strength, rule candidates | 1 to 3 pages per area |
| Cold | index | `INDEX.md` (areas table) + `INDEX.tsv` (one row per finding) + `cycles/` + `plans/` | Every learning, one row each: id, date, area, claim, evidence, source, tier | Unbounded |
| Durable | SSD | GitHub `knowledge/` | Condensed copy of HOT plus area digests, committed at the end of a loop | n/a |

## Promotion and demotion (re-evaluated every cycle and weekly)
- **Promote to HOT** when the evidence is strong (multiple independent or peer-reviewed sources), it applies to our setup (long-only cash, about $1k, daily cadence, US equities), and it changes a decision.
- **Demote** when a rule is stale, contradicted by our own paper results, or hasn't been used in 2 weeks.
- Every HOT rule cites the INDEX ids behind it.

Evidence grades: A = peer-reviewed or replicated; B = solid practitioner or data-backed; C = anecdote or social post.
