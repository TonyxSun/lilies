# Momentum satellite as it would stand today: worker B, cycle 34 (2026-10-22 13:08 ET)
Cross-refs: trader proposals #3–#7, A3 (paper momentum satellite); T-rows (12-1 backtest); DD-R4; VX-R2.

## Key findings
- Today's 12-1 top 10 (from the top 100 SPY names) is 9/10 AI hardware: SNDK, MU, STX, WDC, DELL, INTC, MRVL, AMD, LRCX, plus VLO. Average beta 2.75, pairwise correlation 0.43, -7.8% today (MS-001).
- Momentum crashes cluster in high-volatility rebounds, and vol-scaling helps (MS-002, A).
- So the paper satellite is effectively a levered semis bet unless sector and beta caps bind (MS-003).

## Evidence strength
- B: live snapshot with 1y betas (an unstable estimate). The universe is the top 100 by weight, not the trader's exact screen. A for the literature (qualitative).

## What doesn't apply
- Long-short momentum factor returns. We are long-only, so a crash shows up as satellite underperformance.

## Rule candidates
- **MS-R1:** Enforce the ≤3-per-GICS-sector cap at formation. Without it, today's book is ~90% one industry (MS-001/003).
- **MS-R2:** Cap the satellite's dollar beta: Σ(weight × beta) ≤ 0.15 of the account (i.e. a 10% sleeve at beta ≤1.5), and scale down when the sleeve's 20-day realised vol is high (MS-002/003).
- **MS-R3:** Don't form or rebalance the momentum sleeve on an EVENT-GUARD day or on a VIX/VIX3M >0.95 day. Formation is month-end anyway, so check Oct 30 against VX-R1.

## Addendum, cycle 35: the sector cap applied
- A ≤3-per-sector proxy cap halves the average beta (2.75 to 1.43), but the sleeve still fell 5.7% today, and it swaps in 3 oil names (VLO, MPC, COP), which collides with OIL-R1 (MS-004).
- **MS-R4 (new):** At formation, run the capped list through the event and regime vetoes (OIL-R1/R2, VX-R1, EVENT-GUARD). If more than 1/3 of the sleeve would come from a single active macro shock (AI capex or oil), leave that slot as SPY. The momentum sleeve is paper-only anyway (trader A3).

## Cycle 65: testing MS-R3's VIX trigger (MS-005)
- Momentum ETFs (MTUM, SPMO) did not underperform SPY in the 10 or 21 days after VIX/VIX3M >0.95. MTUM was +0.41% over 10 days (t 2.1), not replicated by SPMO.
- **MS-R3 revised (proposal):** keep the EVENT-GUARD half. Downgrade the VIX>0.95 half to "precautionary; may be waived by Wuyue." Crash risk applies to post-bear rebound states (MS-002), not just high near-term vol.
- The A3 deferral rests mainly on ER-R2 (the earnings conflict).
