# Outcome evaluation: luck vs skill over 2 weeks. Worker B, cycle 28 (2026-10-22 13:02 ET)
Cross-refs: MA-001..004 (evidence bar), PC-004 (single-stock TE), FT-R1..R3 (forecast log), BC-001/005 (benchmark mix).

## Key findings
- A 70% SPY plus 3×10% mega-cap book has a 10-day excess SD of ~1.1% vs SPY and ~1.65% vs QQQ. It beats both only ~33% of the time by chance (OE-001).
- Real skill is invisible at this horizon: +5%/yr alpha gives t≈0.05, and t=2 would take decades (OE-002).
- The core's SPY/QQQ mix dominates the dual-benchmark outcome (OE-003).

## Evidence strength
- B: own simulation with a survivorship-biased universe. The detection math is standard (t = alpha·√n / SD).

## What doesn't apply
- Sharpe-based fund-evaluation literature with multi-year track records. Our window is far too short for any of it.

## Rule candidates
- **OE-R1:** Score the Nov 5 outcome as process plus luck. Report the excess decomposed into core mix, satellite beta/sector, and residual, together with the Brier score. Don't call a win "skill" or a loss "failure" (OE-002).
- **OE-R2:** Since dual-benchmark success is decided mostly by core mix (OE-003), make the SPY:QQQ core split a deliberate, written decision on day 1, with its rationale logged as a forecast (FT-R1).
- **OE-R3:** Don't escalate risk mid-window to "catch up" to a benchmark. With ~1.1% excess SD, a deficit of 1–2% is ordinary noise (BP-R3 tilt audit).

## Addendum, cycle 29: core mix and the dual benchmark
- No SPY/QQQ mix can ever beat both (0% of windows), so beating both needs active exposure outside the SPY-QQQ line (OE-004).
- With 30% mega-cap satellites, P(beat both) is 29-36% by chance. A QQQ-heavy core is highest, but only because of the 2016-2026 regime (OE-004/005).
- **OE-R4 (new):** Report the target honestly: "beat both" has a ~30-35% chance for a no-edge book. A realistic process goal is to beat the 50/50 SPY/QQQ blend after costs, with the dual-beat as a stretch goal. This needs Wuyue's sign-off as a framing change; I have not applied it.

## Addendum, cycle 30: can the SPY:QQQ split be timed?
- No. Momentum (20/60/120-day), reversal, VIX and yield changes don't predict the next 10-day QQQ-SPY spread (all t<2 over 2000-2026). The yields-up/QQQ-down sign appears only post-2010 at t=-2.1, which fails MA-R1 (OE-006).
- **OE-R5 (new):** Set the core split once, on risk preference (QQQ has higher beta and higher variance), and don't rotate it on recent relative performance or rates moves within the window.

## Cross-reference note (added 2026-10-22 13:09 ET)
- OE-001/004 independently replicate the other worker's BR-001..003 (benchmark-base-rates.md): beat-both was 21-27% for equal-weight mega-cap books there and 29-36% for a 70/30 core-satellite book here. Same conclusion. What's new here is the 0%-for-pure-index-mixes structural point (OE-004), the detection-power arithmetic (OE-002), and the non-timeable spread (OE-006).
