# Pre-trade checklist: worker B synthesis, cycle 33 (2026-10-22 13:06 ET)
Status: proposal. It maps evidence onto the rules in force (lilies-repo/rules.md). Nothing here overrides Wuyue's rules, and every order still needs Wuyue's explicit OK and a screenshot.

## Order of checks (stop at the first NO)
1. **Is there a reason beyond the story?** The default is no trade (BP-R1). Write a pre-mortem (BP-R2) and log a forecast row first (FT-R1, tools/forecast_log.py add). Keep the probability within ±0.10 of the market or base rate (FT-R2).
2. **Evidence bar:** does the claimed edge meet MA-R1 (|t|≥3, or ≥2 with replication, plus literature sign, plus surviving costs)? Today none of our own tests pass (MA-001). Apply a ≥50% haircut to any LLM or backtest edge (BP-R5, L-006).
3. **Event calendar (EVENT-GUARD):**
   - FOMC Wed Oct 28, 2pm (M-012).
   - MSFT/GOOGL Oct 28 AMC, AMZN Oct 29 AMC, AAPL Nov 2 AMC (M-014). The rules in force already block new positions within 2 trading days before earnings, so no new MSFT/GOOGL from Mon Oct 26, AMZN from Tue Oct 27, AAPL from Thu Oct 29.
   - GDP and PCE Oct 29 (M-020). Midterms Nov 3 (EL-002). SPCX unlock tradable Oct 26 (BC-006).
   - Brent moving >5% in a day (OIL-R2). VIX/VIX3M >1 (VX-R1).
4. **Gap test** for anything held through an event: weight × implied move × 2 ≤ $15–20 (EH-R1, proposed numbers). Stops do NOT protect after hours (EH-001, re-verified in MA-006), so size the position instead of relying on the stop.
5. **Sizing and structure:** core SPY/QQQ ≥70%, each satellite ≤10% (rules.md, PC-001/002). Set the core split once on risk preference (OE-R5); it can't be timed (OE-006). No leveraged ETFs (LE-R1, a policy question for Wuyue). No parking cash in bills (CS-R3); idle cash defaults to the core (CS-R1).
6. **Settlement:** a cash account can't reuse sale proceeds until T+1, so rotations take two days (CS-001/CS-R2). Never sell a position bought with unsettled funds before settlement (E-008).
7. **Temptation vetoes (today-specific):**
   - No semis/NVDA dip-buy (DD-R4).
   - No read-through trades off META (RT-R1).
   - No energy chase (OIL-R1).
   - No buying on X spikes (B7: S-002/007/016).
   - No SPCX "index will buy" trade (BC-R4).
   - No core de-risking after a down day above the 200DMA (DD-R1).
8. **After the trade:** tilt audit (BP-R3). Score process, not P&L (OE-R1). Expect a ~1/3 base-rate chance of beating both benchmarks (OE-004).

## Gaps and tensions vs rules in force (proposals for Wuyue; not applied)
- **G1:** The rules-in-force stop (2× ATR, trailing) is ineffective through overnight earnings gaps (EH-001/002). The pre-earnings entry block covers new positions only, so add "existing satellites must pass the EH-R1 gap test or be trimmed before the print."
- **G2:** "Beat SPY and QQQ" is impossible for any pure index mix (OE-004). Suggest an explicit process benchmark, the 50/50 blend (OE-R4).
- **G3:** The rules don't mention leveraged ETFs (LE-R1) or extended-hours orders (EH-R2/R3). Suggest explicit "not allowed" defaults.
- **G4:** Add a forecast log entry as a precondition of any order (FT-R1). The tool exists (tools/forecast_log.py).

## Evidence strength
- Synthesis only. Each line inherits the grade of the IDs it cites.

## Rule candidates
- **PT-R1:** Run checklist steps 1–8 in order and record the step reached in the trade log.
- **PT-R2:** Propose G1 (gap test for existing positions before earnings) as a rules.md amendment. It has the highest expected-loss reduction of the gaps.

## Addendum: reconciliation with the trader's proposals (PT-003)
- Trader #10 (hold through earnings because of an "earnings premium"): the premium is not found in mega caps (ES-009). This is harmless at ~3% per name (gap ≈ \$3.6) but binding at ≥10%.
- Trader A1 (70% SPY / 30% QQQ): consistent with OE-R5 (set once, don't time). It can't beat both benchmarks (OE-004); the trader acknowledges this.

## Addendum, cycle 44 (13:15 ET): more gaps vs rules.md
- **G5:** The 2×ATR stop applies to the index core too. It fires in ~50% of 14-session windows and costs ~0.3% per window (SL-001/002). Proposed fix: SL-R1, exempt the index core.
- **G6:** The stop and wash-sale rules interact, so a core stop-out can't be undone before Nov 5 (SL-004).
- **G7:** "Never add to a losing position" blocks planned cash deployment into the core (conflicts with CS-R1 and DD-R1). Proposed fix: exempt pre-planned index-core deployment.

## Addendum, cycle 46 (13:17 ET): clarifications needed before the first fill (PT-004)
1. Do index ETFs count toward the 10% "per stock" cap? A1's 30% QQQ breaches both the 10% cap and proposal #7's trim-above-15%, because #7 exempts only SPY.
2. Should the stop apply to the index core? The current 2×ATR stop fires about half the time on SPY/QQQ (SL-001/005). Trader #5's 5×ATR/-20% stop fires about 5% of the time (SL-006), so adopting #5 largely settles this.
3. Should "never add to a losing position" exempt planned core deployment (G7)?
4. Does the 200DMA/$10B screen apply to ETFs? It doesn't bind today.

## Cycle 71 (PT-005): PT-004(d) is live
- P(QQQ closes below its 200DMA by ~Nov 5) ≈ 17%; SPY ≈ 6%.
- Get Wuyue's ruling now. Recommendation: the screen applies to single stocks only, not the index core.
- **Cycle 77 (PT-006):** the index 200DMA switch costs -0.4 to -6 pts/yr (worse after 2009) and halves max drawdown. This supports trader #6 and the recommendation 'no 200DMA screen on the core' for PT-004(d).
- **Cycle 79 (PT-007):** the -2% day breaker costs about 15bp on the deferred amount (t 1.6). It's cheap discipline; delay the buy, don't cancel it.
- **Cycle 88 (PT-008):** the trigger series for trader #8 matters. A QQQ trigger fires about 17/yr recently vs about 10/yr on the book; the cost is cheap either way (15-30bp of the deferred amount). Recommend the book or SPY. Today QQQ fires and the book does not, so a ruling is needed.
