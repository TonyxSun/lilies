# Macro regime & calendar — warm digest (owner 牛马; refreshed 2026-10-22 12:40pm ET, pass 3: calendar completed 12:34pm ET)

Scope: rates, VIX, breadth and credit spreads as in-market vs cash/SPY filters; FOMC, CPI, jobs and earnings dates as no-trade or size-down windows.
(Reinstated as 牛马's for good on 2026-10-22; the earlier "Trader-owned" notes are superseded.)

## Key findings
- **Trend filters cut drawdowns; they don't add return in bull decades.** Faber's 10-month SMA rule (1901–2012): CAGR 10.18% vs 9.32%, max drawdown 42% vs 84%, but it trails in about half of all years (M-001, A). On SPY in 2010–2026 the 200-day rule returned about 9.5% vs 12.8% buy-and-hold, or 7.2% vs 12.5% with 10 bp per switch (M-008, B). It works over years. Over a two-week window it is mostly a whipsaw risk.
- **Volatility timing doesn't survive out of sample.** Across 103 strategies, Cederburg et al. find vol-managed versions win only 53 to 50, and real-time versions lose Sharpe (M-003, A).
- **High fear is followed by higher returns, not lower.** VIX backwardation is followed by positive S&P returns (M-004, B). After VIX closes above 30, 12-month returns were positive more than 90% of the time (M-011, B).
- **Scheduled macro days carry the premium.** CPI/PPI, jobs and FOMC days average about 11 bp vs about 1 bp on other days, which is 60–71% of the equity premium (1958–2023) (M-006, A). Going to cash on those days throws away the premium (M-007). **Pass 2:** the premium is robust over six decades. It was weak for FOMC only in 2016–19, then *above* average at 16.33 bp per announcement in 2020–Aug 2023 (M-016, A, verified).
- **The pre-FOMC drift is gone.** It averaged +49 bp in 1994–2011 and about 9 bp, insignificant, in 2016–19 after publication (M-002, A). Don't trade it.
- **Credit (EBP / HY OAS) is a recession and drawdown warning measured in months to quarters.** A 1-SD EBP shock (about 20 bp) is followed by stocks about 7 pp below trend (M-005, A). That's a slow signal. Pass 2: HY spread changes don't significantly predict next-month returns, and stocks lead spreads at daily and weekly frequency (M-018, C).
- **Short-horizon trend has no support.** For the S&P, time-series momentum is insignificant below ~9-month lookbacks, and short horizons mean-revert (M-019, A). A 1–4 week SPY trend filter is noise.
- **Earnings-implied moves are roughly fair in large caps** (M-017, B). Use the implied move to size earnings risk; don't bet on it.
- **Yield-curve inversion was useless for timing.** The 2s10s curve was inverted from July 2022 to September 2024 while the S&P rose 46% (M-010, B).
- **Breadth evidence is weak and mixed in sign** (M-009, C).

## Calendar through 2026-11-05 (all times ET)
| Date | Event | Source |
|---|---|---|
| Wed Oct 28 | FOMC decision (statement usually 2:00pm, presser 2:30pm). MSFT and GOOGL report after the close | M-012 (A), M-014 (B) |
| Thu Oct 29 | GDP Q3 advance + Sep PCE 8:30am; AMZN reports after the close | M-020 (A), M-014 |
| Fri Oct 30 | Employment Cost Index Q3, 8:30am | M-013 (A) |
| Mon Nov 2 | AAPL reports after the close | M-014 |
| Tue Nov 3 | US midterm election (results overnight) | M-022 (C) |
| Nov 6 / Nov 10 | Oct jobs report and Oct CPI, both after project end | M-013 |
BEA dates verified on bea.gov (M-020). Turn-of-month (Oct 30–Nov 4) is not a usable edge any more (M-021). Midterm-year Q4 strength is n≈18, grade C (M-022). It supports staying invested; it isn't a trade.

## Current regime (M-015, FRED close 10/21)
- The S&P is 6.5% above its 200-day average and VIX is 16.7, so the regime reads risk-on.
- HY OAS has widened 46 bp in three months to 3.27%. That's worth watching but isn't stress.

## What doesn't apply to a $1k long-only daily book
- Leverage or vol targeting, and shorting on regime signals.
- Monthly or annual signals as daily triggers. Our horizon is 10 trading days, so switching costs and whipsaw dominate.
- Since the benchmark is SPY/QQQ, holding cash is itself an active bet against the benchmark.

## Rule candidates (testable)
- **MR-1 Default is invested.** Hold SPY/QQQ-like beta unless at least two of these hold:
  - S&P below its 200-day average
  - HY OAS more than 100 bp above its 3-month low
  - VIX term structure inverted *and* S&P below its 200-day average

  Even then, cut new single-stock entries rather than selling index exposure. (M-001, M-003, M-005, M-008)
- **MR-2 Never sell into a VIX spike just because of the spike.** VIX above 30 or backwardation is not an exit signal. (M-004, M-011)
- **MR-3 No forced cash around FOMC, CPI or jobs.** Hold index exposure through announcement days. The only restriction: no new single-stock entry between 1:30pm and 3:00pm ET on Oct 28. (M-006, M-007, M-012)
- **MR-4 Earnings cluster, Oct 28 to Nov 2.** Don't open or add to MSFT, GOOGL, AMZN or AAPL in the two sessions before each one's report (this applies FC-5). Owning QQQ or SPY through the cluster is fine. Log each name's day-1 reaction vs QQQ. (M-014)
- **MR-6 Election night (Nov 3):** no new single-name entry on Nov 3 after 3:00pm ET; index exposure holds. Untested; a risk-control rule (C). [M-022]
- **MR-5 Don't use the pre-FOMC drift or the yield curve as signals.** (M-002, M-010)

## Pass 4: own FOMC-day test (12:41pm ET; tools/macro_day_test.py)
- **Sample:** 44 scheduled FOMC decision days, 2021–26.
- **SPY:** −3.3 bp on decision days vs +6.1 bp on other days (t −0.5).
- **QQQ:** +15.1 bp vs +6.3 bp (t +0.3).
- **Variance:** the decision-day sd is about 26% higher. There's no pre-FOMC drift (M-023).
- **What it means:** the 10/28 FOMC is a variance event, not a premium to chase or avoid. This is consistent with MR rules that keep calendar windows from forcing index exposure to cash (M-006, M-016).

## Pass 5: base rate for this exact window (1:24pm ET)
- **Oct 21 to Nov 5, 1994–2025:** SPY is up in 23 of 32 years, with a mean of +1.45%. Any 10-day window averages +0.46% and is up 62% of the time.
- **Midterm years:** +1.94%, up in 5 of 8, which isn't distinguishable from other years.
- **QQQ vs SPY:** QQQ is ahead in 18 of 27 years, by +0.58% on average (M-024, C).
- **What it means:** being invested has a seasonal tailwind, which supports MR's default-invested stance. The midterm (Nov 3) is not a timing trigger.
