# Agent behavior: pitfalls for an LLM trader (worker B) — created 2026-10-22 (cycle 10)
Scope: how an LLM agent (us) is predictably biased when picking stocks or trading, and the guardrails the evidence supports. Human-investor pitfalls live elsewhere: R-003/E-012 (turnover costs), R-013 (disposition), S-002/N-008 (attention herding).

## Key findings
- **LLM advice concentrates and chases trends (BP-001, A).** Across three chatbots and newer models: >93% US equity, overweight tech and consumer cyclical, up to 28% in the 3 most-traded recent names, >51% active, higher fees. Debiasing prompts help only partly. A broad "avoid concentration/active/cluster risk" instruction worked best and removed trend-chasing, but there was still no risk-adjusted outperformance.
- **Latent tilts plus confirmation bias (BP-002, B; BP-005).** Models favor tech, large caps and contrarian views, and lean toward "buy". When evidence is mixed they stick with their prior, even against majority or stronger counter-evidence (most models flip less than 60% of the time).
- **Extrapolation and optimism (BP-003, B).** GPT-4o projects recent returns forward even though short-horizon reversal is real. It expects ~2.2%/month vs ~1.15% realized, and its intervals are slightly too narrow.
- **Sycophancy and vacillation (BP-004, B).** Judgments flip under pushback ("are you sure?") and depend on the path of the conversation. Combined with BP-002, an agent is both stubborn about its prior and pliable under social pressure, so neither re-asking nor arguing is a reliable check.
- **Linked evidence in other areas:** FINSABER shows LLM agents are too timid in bull markets and too aggressive in bear markets (L-004). Alpha Arena shows live LLMs overtrade and lose 42–59% (L-007/L-023). Costs erase the overnight-news alpha (L-016).

## Evidence strength
BP-001 is A (peer-reviewed, open data and code). BP-002 is B (conference paper; the evidence it used was LLM-generated). BP-003 and BP-004 are B and were verified from summaries only, not full text.

## What doesn't apply
- Most studies test chat advice or toy buy/sell prompts, not a rules-bound agent with tools. Hard-coded caps (PC-R1) already neutralize much of the concentration risk.
- Our tech/mega-cap tilt is partly intended: the core is SPY/QQQ. The danger is the *satellite* repeating the model's priors (NVDA/AAPL/MSFT) with no evidence behind them.

## Rule candidates
- **BP-R1 Default = no trade.** Every buy or sell needs a written trigger from a pre-registered rule (from HOT or the areas). "It looks good" or a story is not a trigger. This counters the action and buy bias (BP-005, BP-001, L-007).
- **BP-R2 Pre-mortem with balanced evidence.** Before any satellite buy, write the 2 strongest counter-arguments with numbers, and state what price or event would make the trade wrong (the stop/exit). If the decision would not flip on any evidence, treat it as a prior, not analysis (BP-002, BP-004).
- **BP-R3 Tilt audit.** Check the satellite against model priors each week. If it is all large-cap tech, or names chosen because of recent gains, cap it or justify it with non-price evidence (BP-001, BP-003).
- **BP-R4 No self-argued reversals.** Change a position only on new data (a price hitting the stop, an earnings print, a rule flag), never because the agent re-asked itself or was challenged in conversation (BP-004).
- **BP-R5 Haircut own return forecasts.** Shrink any LLM-generated expected return by at least 50% toward the SPY base rate before sizing (BP-003, CA-R2, L-006).

## Addendum, cycle 56 (worker B, 13:23 ET): myopic loss aversion (BP-006)
- A 70/30 book is underwater on ~37% of days in a 2-week window and ends underwater 34% of the time. It is behind the better benchmark essentially every day by construction.
- **BP-R3:** Pre-commit in writing (with the day-1 split, OE-R2) that being "behind QQQ" or "down on the day" triggers no action. Only a rule breach (the -8% pause) or a thesis-level fact does.
- **BP-R4:** In the Friday retro, show the expected-frequency figures next to the result, so that a red week isn't read as failure (OE-R1).
