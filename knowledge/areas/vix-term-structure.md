# VIX term structure: worker B, cycle 24 (2026-10-22 ~12:59 ET)
Cross-refs: M-004 (Fassas & Hourvouliades: backwardation precedes positive returns), DD-R1, risk-sizing.md.

## Key findings
- Now: VIX 18.9 and VIX3M 20.1 give a ratio of 0.94. The curve is in contango and not inverted, even on today's selloff (VX-001).
- Direction: the ratio barely separates 10-day mean SPY returns (+0.68% inverted vs +0.47% normal; t=1.33 on inversion starts). This is weak agreement with M-004 (VX-002).
- Risk: the 10-day SD of SPY rises from 2.0% (ratio ≤0.85) to 3.3% (0.90–0.95) to 6.6% (inverted). The worst case was -15% in Feb 2020 (VX-003).

## Evidence strength
- B: own test on 18 years of daily data. Overlapping windows in the day-level stats inflate effective n; episode-level n=79. One regime class (2008 GFC, 2020 COVID) dominates the tails.

## What doesn't apply
- Trading VIX products (VXX, UVXY). They are not useful for long-only beat-SPY, and leveraged/inverse versions fall under LE-R1.

## Rule candidates
- **VX-R1:** Check VIX/VIX3M daily. If the ratio is >1, treat it as an EVENT-GUARD state: no new satellites, and hold the core (DD-R1, M-004). Never sell the core because of an inversion.
- **VX-R2:** Set position-size expectations from the bucket SD. At ratio 0.90–0.95, a 10% satellite (beta ~1.5) has a 10-day 1-SD swing of about ±$5, and the core about ±$23 (VX-003).
- **VX-R3:** A ratio crossing from ≤0.90 to >0.95 is a cue to re-run the pre-mortem (BP-R2), not a cue to trade.

## Addendum, cycle 36: drawdown odds for the rest of the window
- From VIX 15-20, a 70/30 SPY/QQQ book has a ~30% chance of a ≥3% dip within 10 sessions, ~10% for ≥5% and ~2% for ≥8%. At VIX 20-25 these roughly double or triple (VX-004).
- **VX-R4 (new):** Pre-commit now: a ≥3% book drawdown before Nov 5 is a ~1-in-3 base-rate event and triggers nothing beyond the existing rules. Re-read VX-004 if the VIX closes above 20.

## Addendum, cycle 58 (13:24 ET): VX-R3 trigger reached (VX-005)
- The VIX/VIX3M ratio is 0.950. The VX-R3 pre-mortem re-run:
  - (a) The expected 10-day SPY SD rises to ~3.7%, so P(3% drawdown) moves above VX-004's 29.5% (VIX 15-20 bucket). VIX is now ~19, at the top of that bucket.
  - (b) The term structure is not inverted (VX-R1 EVENT-GUARD not triggered).
  - (c) No change to the core decision. MS-R3 forbids forming or rebalancing the momentum sleeve while the ratio is >0.95, so A3 is on hold if the ratio closes above 0.95.
- Re-check the ratio at the close and at the 9:45 re-check.
- **Cycle 59 (VX-006):** in today's state (VIX 17-22, ratio 0.93-0.98), P(≥3% drawdown in 10 sessions) is ~40% vs 31% unconditional. P(≥8%) is still ~5%.
- **VX-R2 refined:** use the ratio-conditional figure in the pre-mortem. B-F10 = 0.38 (B-F06 = 0.30 is kept as the original record).
- **Cycle 65 (MS-005):** the 0.95 ratio doesn't predict momentum-sleeve underperformance. VX-R3 and MS-R3 are precautionary, not evidence-based.
- **Cycle 81 (VX-007):** P(ratio >1.0 on some close before Nov 5) ≈ 37-39%. Forecast B-F14 = 0.38.
