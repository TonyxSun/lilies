# Leveraged ETFs (2x/3x long) — worker B, cycle 11 (2026-10-22 ~12:44 ET)

## Key findings
- Over 10-trading-day windows (2010–2026), 2x/3x long ETFs beat their own benchmark ~61% of the time, with a mean excess of +0.4% to +1.3% (LE-001). This is purely a bet on direction. They beat in ~96% of up windows and ~0.1% of down windows.
- The tail is the cost. TQQQ's 10-day p5 is -17.4% and its worst window was -57%. Excess vs QQQ at p5 is -11.7% (LE-002).
- Decay vs a naive k× return is small at 2 weeks (~-0.25% for 3x) but grows with variance × time (LE-003, LE-004).
- Regulators say these funds are built for one-day holds (LE-005).

## Evidence strength
- The own test is B: one data source, overlapping windows (so effective n is much smaller than 4,200), and survivorship is not an issue for these 4 funds.
- Mechanics are A (Cheng–Madhavan; SEC/FINRA).

## What doesn't apply
- Inverse ETFs: they are bets on decline, and our book is long-only in spirit.
- Intraday leveraged-ETF rebalancing-flow trades: we trade on a daily cadence and can't capture them.

## Rule candidates
- **LE-R1 (policy question for Wuyue/Trader):** Is a leveraged ETF "margin by another name"? The brief bans margin. Default: treat 2x/3x ETFs as **not allowed** unless Wuyue explicitly permits them. If they win, the "beat" would be beta, not research.
- **LE-R2:** If permitted, cap the gross leveraged notional (multiple × weight) at ≤30% of equity, size so the p5 10-day loss is ≤$40, and use 2x rather than 3x (similar beat rate with half the tail) (LE-001/002).
- **LE-R3:** Never hold leveraged ETFs through EVENT-GUARD days (FOMC Oct 28, midterms Nov 3). Event gaps hit k× the underlying move (LE-002; P-011).
- **LE-R4:** When scoring the experiment, report beta-adjusted excess, so a leveraged "win" is not counted as skill (LE-001).

## Update 2026-10-22 ~4:30pm ET (Trader, AG-001..AG-005)
- Long-history stress via synthetic 2x/3x QQQ from 1999 (calibrated to QLD/TQQQ, corr ≥0.996): 2x held 10.1% CAGR / −98.8% DD vs QQQ 10.6% / −83%; 3x 2.8% / −100%. The 2010+ "win" (2x 32.7%, 3x 42.6% vs 19.4%) is a bull-sample beta bet.
- Month-end QQQ>200DMA switch (2x on / QQQ off): 13.7% vs 10.6% full history; daily checking worse (whipsaw). Proposed as BOOK-A core (proposals/trader-2026-10-22.md Round 8), ⚑ pending Wuyue's LE-R1 permission. Proposal drops LE-R3 (event-guard) for the core.
