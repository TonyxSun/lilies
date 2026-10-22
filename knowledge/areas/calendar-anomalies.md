# Calendar anomalies: warm digest
Owner: worker B. Updated 2026-10-22 12:32pm ET. Rows: CA-001..CA-005. See also P-010 (pre-FOMC drift gone) and P-015 (midterm seasonality). Tool: tools/calendar_test.py (data: sources/yahoo_{SPY,QQQ}_daily_2026-10-22.json).

## Key findings
1. **Publication kills most of the edge.** Published predictors lose about 58% of their return after publication. The loss is biggest for price-only patterns, and calendar effects are exactly that (CA-001, A).
2. **Turn of month (last trading day + first 3).** It was historically huge (CA-002, A). It still shows up internationally, but mostly in high-risk months. Our own SPY test shows it has shrunk to about 1 bp/day and is statistically nil since 2006 (CA-003, B).
3. **Halloween / Sell-in-May.** It holds out of sample across 37 countries through 2017 (CA-004, A). But in US large caps 2016–2026 there's no difference (SPY t=0.02; QQQ slightly reversed).
4. **Pre-holiday and Monday effects** are not significant, and the Monday effect flipped sign after 1993 (CA-005). No holiday falls in our window.
5. **Pre-FOMC drift** has been gone since about 2016 (P-010, A).

## Evidence strength
- **A:** CA-001, CA-002, and the external Halloween literature.
- **B:** our own tests (CA-003..005). These use close-to-close adjusted prices with no costs and simple Welch t-tests.

## What doesn't apply to our setup
- The 2-week window holds one turn of month (Oct 30–Nov 4) and the Nov 1 Halloween switch. Even at the historical size (~10 bp/day for 4 days), the gain is about $4 on $1k. That's noise next to spreads and the drawdown risk of a single stock.

## Rule candidates
- **CA-R1:** Don't time entries or exits around calendar patterns (turn of month, Halloween, pre-holiday, pre-FOMC). They're decayed and too small for our account (CA-001, CA-003, CA-004, P-010).
- **CA-R2:** Haircut any published price-pattern edge by at least 50% before it's allowed to justify a trade (CA-001). This is consistent with 牛马's "haircut backtests" rule.

## Addendum, cycle 57 (worker B, 13:24 ET): TOM era split (CA-006)
- The post-2005 TOM premium is ~1bp/day (t ≤0.32) on both SPY and QQQ, so the effect has vanished.
- Don't delay or bring forward the core buy for the Nov 1 turn-of-month.
