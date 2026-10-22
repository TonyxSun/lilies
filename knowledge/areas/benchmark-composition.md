# Benchmark composition (SPY vs QQQ) — worker B, cycle 16 (2026-10-22 ~12:51 ET)
Cross-refs: BR-002 (P(beat both) ~21–27%), PC-R1 (core-satellite), M-014 (earnings calendar), OS-006 (MSFT implied move).
Data: sources/spy_holdings_2026-10-21.xlsx (official) and sources/benchmark_composition_2026-10-22.txt.

## Key findings
- **SPY concentration:** SPY's top 10 is 38.5% and its top 20 is 49.6% (BC-001).
- **NDX concentration:** by cap weight the NDX top 10 is ~66%, so QQQ-minus-SPY is mostly a ~1.6× bet on the same mega caps (BC-002).
- **Satellite overweights are smaller than they look.** A 10% NVDA satellite on a 70% SPY core is +7.6 pts vs SPY but only ~+3.2 pts vs NDX (BC-001).
- **SpaceX (SPCX) is a QQQ-only name.** It joined in Jul 2026 at a confirmed 2.82% weight from the Sep rebalance. It is not in SPY (BC-003).
- **Earnings week does NOT decide the gap (cycle 22 test).** The four mega caps reporting Oct 28–Nov 2 are 22.6% of SPY and ~38% of NDX (BC-004). But reaction days carry only ~7% of QQQ−SPY spread variance (1.22× normal days). In past Oct 22–Nov 5 windows the race was decided mostly on non-earnings days (BC-005).

## Evidence strength
- SPY weights are A (issuer file).
- NDX weights are B, approximate: these are full-cap weights from a third party, not Invesco's file, which failed to download.

## What doesn't apply
- Equal-weight vs cap-weight debates (RSP etc.): this is a long-horizon question, not a 2-week one.

## Rule candidates
- **BC-R1:** Compute active weight vs BOTH benchmarks before any satellite buy. The trade is really (pick weight + core look-through) − benchmark weight. Anything under ~3 pts of active weight isn't worth the cost and attention (BC-001).
- **BC-R2:** Don't add a mega-cap satellite that reports earnings inside the window just to "beat QQQ". QQQ already holds it at ~1.6× SPY weight. The print adds single-name gap risk (EH-R1) without deciding the benchmark race (BC-004/005).
- **BC-R3:** Pull official holdings (SSGA and Invesco) weekly. Prefer the issuer file over third-party weights (BC-002/003).

## Addendum, cycle 26 (2026-10-22): SpaceX unlocks as QQQ-only event risk
- The largest SPCX lockup release (up to 1.31B shares) became sellable today. Another 328M are tradable from Oct 26, and the rest on Dec 8 (BC-006, B: 424B4 terms via third party).
- SPCX is -6.8% today, about -0.19 pts of QQQ, with no effect on SPY. Its idiosyncratic contribution is ~0.11%/day of QQQ: small but one-sided around Oct 26 (BC-007).
- Index buying of freed float is not until the Dec 21 NDX rebalance, outside our window (BC-008, C).
- **BC-R4 (new):** Treat Oct 26 as a minor QQQ-only event. Don't buy SPCX as a satellite before Nov 5 on the "index will buy" story, and don't choose QQQ over SPY for the core because of SPCX in either direction (BC-005/007).
