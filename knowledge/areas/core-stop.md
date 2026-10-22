# Core stop-loss (worker B), created 2026-10-22 13:15 ET, cycle 44

## Key findings
- **The stop costs return on an index core.** Applied to SPY or QQQ, the 2×ATR trailing stop in rules.md fires in about half of all 14-session windows. It costs ~0.28-0.34% per window (t -2.3 to -2.8, both ETFs, both ATR variants) and cuts SD by only about 10% (SL-001).
- **It fits the literature.** Kaminski-Lo: stops hurt under a random walk (SL-002, R-007).
- **It creates tracking error.** We are scored against benchmarks that never stop out, so every fired core stop crystallizes tracking error (SL-002).

## Evidence strength
- Own test (B). Passes MA-R1: replicated across 2 ETFs and 2 window lengths, sign matches the literature.
- Caveats: close-to-close execution with no re-entry. A re-entry rule would cut the cost but add turnover and whipsaw.

## What doesn't apply
- Satellites and single stocks. For a momentum book, R-015 already found tight stops costly, and wider stops (5×ATR) are less damaging. A stop on a single stock can still serve as a risk cap; this finding covers the index core only.

## Rule candidates
- **SL-R1 (proposed rules.md change, needs Wuyue's OK):** Exempt broad index ETF core holdings (SPY, QQQ, VOO and similar) from the 2×ATR trailing stop. Keep the portfolio-level -8% drawdown pause as the core's only risk brake.
- **SL-R2:** If any stop is kept on the core, set it at ≥8% (the rules.md cap) rather than 2×ATR (1.8% on SPY). Grade C: the wider level wasn't tested here.
- **SL-R3:** Satellite stops stay, but at ≥3×ATR (R-015). They don't protect through earnings gaps (EH-002), so the gap test (EH-R1) is the real protection.

## Rule interactions (SL-004)
- Under the current rules a stop-out is followed by the wash-sale ban, so the stopped ETF can't be rebought before Nov 5. The SL-001 "no re-entry" result is the actual rules outcome.
- **SL-R4:** If SL-R1 is not adopted, at least exempt index ETFs from the wash-sale re-entry ban for paper trading. Wash sales only matter for taxes, and a paper account pays none; for live trading, use a near-substitute (e.g. VOO for SPY), noting the "substantially identical" ambiguity. Grade C.

## Robustness, cycle 45 (SL-005)
- The cost is negative in 9 of 9 subsamples (eras, exit at the next open, the 70/30 blend).
- It is significant only in some of them (SPY 1993-2004 t -2.9, QQQ 2010+ t -2.7, SPY all with next-open exit t -2.0). On the 70/30 blend it is only -0.07 to -0.13% (t ≤1.2).
- The stop fires in ~50% of windows in every era.
- Revised evidence statement: the stop has no benefit (no subsample positive) and fires half the time. Under the current rules it locks us out of the benchmark until Nov 5 (SL-004).
- SL-R1 stands on "zero benefit plus forced tracking error". The return-drag figure should be quoted as ~0.1-0.3% per window, not 0.3%.

## Cycle 46: the wider stop (SL-006)
- Trader proposal #5 (5×ATR/-20%) on SPY/QQQ fires in only ~4-5% of 14-session windows, at a cost of ≤0.07%.
- 3×ATR fires in ~26-30% of windows.
- **Updated SL-R1:** the cleanest fix is to adopt #5 for all positions, core included. An explicit core exemption remains an alternative.

## Cycle 67: satellite stops (SL-007)
- A 3×ATR stop fires in 50% of 14-session windows and costs ~45bp per position (t -3.4, date-clustered). It trims p5 from -11.6% to -9.3%.
- A 5×ATR / -20% stop fires 23%, costs ~19bp, and gives little tail benefit.
- The universe is survivorship-biased (current large caps), so the cost is an upper bound.
- **SL-R3 revised (proposal):** the satellite stop's job is tail control, not alpha. Prefer sizing (EH-R1 gap test, ≤10%) over a tight stop. If Wuyue wants a stop, 5×ATR/-20% (trader #5) is the cheaper choice; 3×ATR is defensible only as explicit insurance.
- Either way, it's monitored at 9:45 and executed as a market sell (WS-006).
- **Cycle 68 (SL-008):** the result replicates on sector ETFs with no survivorship. A 3×ATR stop costs -0.22% per position (t -2.3) and fires about half the time.
  - Conclusion: across core and satellite, 2-week trailing stops at 2-3×ATR are a measurable drag.
  - Their only benefit is a thinner p5 tail, and sizing gets that more cheaply.
- **Cycle 80 (SL-009):** a -8% trailing core stop fires 8% of the time and costs about -0.05% (t -1). A -5% stop fires 24% and costs -0.19% (t -2.2). **SL-R2 is upgraded to B:** if the core must have a stop, use ≥8%.
