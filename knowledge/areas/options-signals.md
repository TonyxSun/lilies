# Options-implied signals (read-only): warm digest
Owner: worker B. Updated 2026-10-22 12:35pm ET. Rows: OS-001..OS-007, plus S-005 and S-013. Tool: tools/os_check.py (CBOE delayed chain + Yahoo prices).

## Key findings
1. **The classic option signals have stopped working as stock pickers.** These are skew, the call–put IV spread, RV−IV and the option/stock volume ratio. Their original papers are all pre-2010 (OS-003, S-013, A). Since 2008, the combined signal's Sharpe fell from 1.18 to 0.16, and its alpha is insignificant. Part of the old "alpha" was a timestamp look-ahead in the data (OS-001, B).
2. **What remains is mostly borrow fees.** Most of the leftover predictability comes from hard-to-borrow stocks. Excluding them cuts it by ≥2/3 (OS-002, A). It's irrelevant to long-only large caps except as a "crowded short, avoid" flag.
3. **Earnings moves are underpriced, not overpriced.** Straddles earn about +3.3% through earnings (OS-006, A). Treat the implied move as a floor on the gap risk.
4. **Public "unusual options activity" alerts are an attention trap.** Names jump on the day they're covered, then reverse. Only truly unusual near-expiry OTM calls carry information, and that edge is fading (OS-007, B).
5. **Free data works.** The CBOE delayed chain gives IV, delta, volume and iv30 (OS-004). Today, ~12:32pm ET:
   - IV/RV is about 1.5 across AAPL, NVDA, MSFT and SPY.
   - Straddles imply AAPL ±2.4% to Oct 28, NVDA ±3.9%, MSFT ±5.3% to Oct 30 (the window spans its earnings), and SPY ±1.2%.

## Evidence strength
- **A:** OS-002, OS-003, OS-006, S-013.
- **B:** OS-001 (via a review of a working paper), OS-004, OS-007.
- **C:** OS-005.

## What doesn't apply to our setup
- We can't trade options or go short, so long-short skew strategies are out.
- Monthly cross-sectional sorts across ~3,000 stocks are out of scope for a portfolio of 2–5 names.

## Rule candidates
- **OS-R1:** Options data is used for risk, never as a reason to buy (OS-001, OS-002).
- **OS-R2:** Before holding through earnings, read the straddle-implied move from `tools/os_check.py`. If the implied move is larger than the stop distance, expect the stop to gap: size down or wait until after the report. This is a note for the Trader (OS-004, OS-006).
- **OS-R3:** Don't act on public unusual-options-activity alerts. Treat them as attention spikes under S-R1 (OS-007, S-002).

## Addendum, cycle 37 (2026-10-22 13:09 ET): live implied moves for the window's mega-cap prints
- Implied moves: MSFT ±5.5%, GOOGL ±6.2%, AMZN ±7.6% (all Oct 30 expiry), AAPL ±5.1% (Nov 6). META, post-print, is ±2.7% (OS-008, A: CBOE delayed).
- Maximum size passing the $15 gap test: MSFT 13.7%, GOOGL 12.1%, AMZN 9.9%, AAPL 14.7% (OS-009).
- **OS-R4 (new):** An AMZN position held through Oct 29 should be ≤~9.9% (gap test). The others fit under the 10% cap. Re-pull implied moves on the morning of each print, because they drift.

## Addendum, cycle 51 (13:21 ET): skew feed and snapshot (OS-010..012)
- **Feed:** tools/skew_check.py, a working free per-stock IV and 25-delta skew feed (CBOE delayed). It unblocks S-R5's data dependency; the full-universe decile still needs to be run.
- **Today:** index skew is steep (SPY +3.7, QQQ +4.7 pts), while momentum-name skews are flat (+0.6 to +2.8). No skew veto would fire.
- **Momentum IVs are 55-79%,** which implies 15-22% one-month 1-SD moves per name (OS-012).
- **OS-R5:** Run skew_check at the 9:45 re-check on any satellite candidate. A put25−ATM skew above the universe's 90th percentile means skip (S-R5, pending the decile calibration).
- **Cycle 52 calibration (OS-013):** across the top 100 SPY names, the median skew is +1.3 pts and the 90th percentile is +3.2.
- Today's top decile: MRK, PH, PLTR, VRTX, LIN, NVDA, TXN, KLAC, C, ORCL.
- **OS-R5 (refined):** a satellite candidate with skew ≥ the universe p90 (≈+3.2 today) is skipped. For names reporting before the expiry, measure skew on the first expiry after the print.

## Cycle 64: aggregate put/call ratio (OS-014)
- Equity and total PCR deciles give conflicting signs, all with |t|<1.2. A null.
- **OS-R6:** ignore "PCR at an extreme" posts on X. They are not a buy or sell timer.
