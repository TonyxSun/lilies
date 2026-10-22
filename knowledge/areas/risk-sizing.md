# Risk, position sizing & portfolio rules — warm digest (Trader, cycle 01, 2026-10-22)

Scope: sizing, stops, concentration, drawdown rules, behavior, and honest base rates for a long-only ~$1k cash account. Plan: `cycles/01-risk-sizing-plan.md`.
Grades: A = peer-reviewed or replicated; B = solid data/practitioner; C = anecdote/weak.

## Bottom line
- **Base rate is brutal.** ~90% of professional large-cap funds trail the S&P 500 over 15–20 years; heavy-trading retail investors trail the market mainly through costs. Our default expectation should be that we underperform unless the retro proves otherwise.
- **Stops and vol-sizing mostly cut risk, not raise return.** Evidence that stops *add* return exists only where returns trend (momentum). For individual stocks, the best study finds no return gain, only lower volatility with a *wide* trailing stop. Our 2×ATR stop looks tight relative to daily noise.
- **Concentration is the main way a 10–12 stock portfolio loses to the index** (return skew: a few stocks make all the gains).
- Kelly sizing is unusable without a measured edge; use it only as a ceiling later.

## Findings

### Base rates: active vs index
- [R-001] SPIVA U.S. Year-End 2025: share of active **large-cap** funds underperforming the S&P 500 — 1y 78.8%, 3y 66.8%, 5y 89.0%, 10y 85.6%, 15y 89.9%, 20y 92.9% (periods ending 2025-12-31). 2025 was the 4th-worst year in SPIVA's 25-year history (B, primary data). S&P Dow Jones Indices, Mar 2026 (mirror of S&P PDF): https://www.ariesadvisors.com/files/spiva-us-year-end-2025.pdf
- [R-002] SPIVA U.S. Mid-Year 2026: 67% of active large-cap funds trailed the S&P 500 in H1 2026 (B; S&P page timed out for me, figure from search summary of the primary + ETF Daily). https://www.spglobal.com/spdji/en/spiva/article/spiva-us/
- [R-003] 66,465 discount-broker households 1991–1996: the highest-turnover quintile netted 11.4%/yr vs 18.5% for the lowest-turnover and 17.9% for the market; gross returns were similar, so **costs from trading** drove the gap (A). Barber & Odean, J. Finance Apr 2000. https://faculty.haas.berkeley.edu/odean/papers/returns/individual_investor_performance_final.pdf
- [R-004] Taiwan day traders: under 1% (~4,000 of ~450,000 a year) reliably earn positive returns net of fees (A). Barber, Lee, Liu & Odean, J. Financial Markets 2014. https://doi.org/10.1016/j.finmar.2013.05.006
- [R-014] Most CRSP stocks since 1926 underperformed one-month T-bills over their lifetimes; the best ~4% of companies created all of the market's net wealth gain (A). Explains why poorly diversified active portfolios often lag. Bessembinder, JFE Sep 2018. https://ideas.repec.org/a/eee/jfinec/v129y2018i3p440-457.html

### Volatility-targeted sizing
- [R-005] Scaling factor portfolios by inverse prior-month variance gives large alphas and higher Sharpe ratios (A, in-sample spanning tests). Moreira & Muir, J. Finance 2017. https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12513 ; for momentum specifically, Barroso & Santa-Clara JFE 2015 (T-006).
- [R-006] **Counterpoint:** implementable out-of-sample versions of vol-managed portfolios generally have *lower* Sharpe ratios and certainty-equivalent returns than the unmanaged portfolios; the alphas come from unstable parameters that can't be used in real time (A). Cederburg, O'Doherty, Wang & Yan, JFE 2020. https://ideas.repec.org/a/eee/jfinec/v138y2020i1p95-117.html
- Our read: at the **position** level, sizing by volatility is mainly risk equalization (so one volatile stock doesn't dominate P&L). Don't expect it to add return. For momentum specifically, scaling *down* in high-vol regimes is the better-supported piece (T-005, T-006).

### Stop-losses
- [R-007] Theory + data (A): under a random walk, stop-losses always reduce expected return; they can add value when returns have momentum or regime-switching. On US index futures, some longer-horizon stop rules raised return and cut volatility. Kaminski & Lo, J. Financial Markets 2014. https://ideas.repec.org/a/eee/finmar/v18y2014icp234-254.html
- [R-008] Individual NYSE/AMEX stocks 1970–2005 (B; refereed per the paper's acknowledgments, journal not verified by me): fixed and trailing stops neither reduce nor increase losses vs buy-and-hold once future paths are simulated; one trailing mechanism reduced risk (a search summary describes it as ~5 standard deviations wide, cutting volatility ~29–48% — not verified in the full text). "Value of stop loss strategies may come largely from risk reduction rather than return improvement." Lei & Li. https://www.smallake.kr/wp-content/uploads/2017/02/SSRN-id1214737.pdf (SSRN 1214737)
- [R-009] On momentum portfolios 1926–2013, a 10% stop cut the worst monthly loss from −49.8% to −11.4% (equal-weight) and more than doubled the Sharpe ratio (A/B, SSRN working paper; later published). Han, Zhou & Zhu. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2407199
- [R-010] I found **no peer-reviewed test of ATR-multiple stops** specifically. Practitioner tests (C) report tight ATR trailing stops hurt and only wide ones (≥5 ATR) helped. https://bettersystemtrader.com/037-cesar-alvarez-studies-stop-losses/
- [R-011] Stop orders become **market orders** when triggered; fills can deviate significantly from the stop price, and short-term fluctuations can trigger them (B, regulator). SEC Investor Bulletin "Understanding Order Types," updated 2026-08-18. https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14
- Our arithmetic (from T-020): SPY ATR(14) ≈ 0.91% while its daily standard deviation (12.8%/√252) ≈ 0.81%, so ATR ≈ 1.1× daily sd. A 2×ATR stop is therefore ≈ 2.2 daily sd. Over a multi-week hold, a stock will often touch that level on noise alone, causing whipsaw turnover — the opposite of what Lei & Li found useful (wide stops).

### Kelly / fractional Kelly
- [R-012] Full Kelly maximizes long-run growth but produces very large, volatile bets and severe drawdowns, and is extremely sensitive to errors in the estimated mean; fractional Kelly trades growth for much lower risk (A/B). MacLean, Thorp & Ziemba, "Good and bad properties of the Kelly criterion." https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf
- Implication: our edge is unmeasured (zero closed trades). Kelly would be fed noise. Do not use it to size *up*; revisit after ≥30 closed trades, at ≤¼ Kelly as a ceiling only.

### Concentration and correlation
- [R-014] (Bessembinder) + momentum clusters by industry (Moskowitz & Grinblatt 1999, cited in Daniel-Moskowitz references; not separately opened). With 10–12 names chosen by momentum, several will often sit in one sector (e.g., semis), so effective diversification is lower than the count suggests. No study I opened gives an optimal sector cap; any cap number is judgment (C).

### Drawdown and daily-loss rules
- No peer-reviewed evidence I found supports the specific thresholds (2% daily stop, 8% drawdown pause). Rationale is behavioral/operational (avoid revenge trading, force a review), plus momentum-crash timing (T-005: losses cluster after market declines with high vol). Grade C for the numbers; keep as circuit breakers, not as alpha sources. Note an 8% portfolio drawdown is small vs SPY's own history (Faber's SPY buy-and-hold max DD −83.5% since 1901, T-010), so an 8% pause will trigger in ordinary corrections — that's intended for a paper-test, but it means "paused" ≠ "strategy broken"; compare against SPY's drawdown over the same window.

### Behavioral pitfalls
- [R-013] Disposition effect: 10,000 discount-broker accounts 1987–93 sold winners far more readily than losers (PGR/PLR > 1.5), hurting after-tax returns (A). Odean, J. Finance 1998. https://onlinelibrary.wiley.com/doi/10.1111/0022-1082.00072
- Our "no adding to losers" + mechanical stops counter the "hold losers" half; the "sell winners too early" half needs a rule too (momentum says winners keep winning for months, T-001).

### Data-snooping discipline for our own rule changes
- McLean-Pontiff (T-018) and Harvey-Liu-Zhu (T-019): most backtested improvements shrink by ~half or vanish. Our weekly retro will be tempted to tweak rules after a few trades — that is exactly the overfitting trap.

## Proposed rules (risk & sizing) — checked against current repo rules
| # | Rule (one line, mechanical) | Evidence | Status |
|---|---|---|---|
| R-R1 | Size each new position so the loss at the stop = 1% of equity: shares = (0.01×equity)/(entry − stop), then cap at 10% of equity. | R-005, R-006 (risk equalization) | Changes existing (adds sizing formula under the 10% cap; at $1k the 10% cap usually binds) |
| R-R2 | Widen the stop: exit on a **close** below max(highest close − 3×ATR(14), highest close × 0.90); evaluate on closes, act next session with a limit order; no resting stop-market orders. | R-007, R-008, R-009, R-010, R-011, T-020 | Changes existing (2×ATR/−8% → 3×ATR/−10%; needs Wuyue's yes/no) |
| R-R3 | Keep max 10% per stock and max 12 positions; add max 3 positions or 30% of equity per GICS sector. | R-014; momentum industry clustering | Confirms existing + new sector cap (number is judgment) |
| R-R4 | Keep 2% daily-loss → no new positions, and 8% drawdown → pause; at pause, report our drawdown next to SPY's over the same dates before deciding anything. | No direct evidence (C); T-005 timing | Confirms existing (adds benchmark context) |
| R-R5 | No Kelly sizing until ≥30 closed trades; afterwards Kelly may only cap size (≤¼ Kelly), never raise it above R-R1/10%. | R-012 | New |
| R-R6 | Turnover cap: at most 3 new positions per week and target median hold ≥ 20 trading days; exits only via stop, rank-drop (falls out of top half on 12-1 momentum), or earnings rule. | R-003, R-013, T-001 | New |
| R-R7 | Never sell a winner just because it's up; trim only if a position exceeds 15% of equity. | R-013, T-001 | New |
| R-R8 | Rule-change discipline: change at most one rule per weekly retro, only with evidence from outside our own last-month P&L, and log each change with date and reason in the changelog. | T-018, T-019 | New |
| R-R9 | Benchmark kill-switch: at each retro compare net return vs SPY and QQQ buy-and-hold on the same cash flows; if behind both by >3 pts after 8 weeks (or at the Nov 5 paper-end), recommend switching to the index. | R-001–R-004 | Confirms existing decision 7 (adds a number) |

## Round 2 (2026-10-22, cycle 02) — adversarial check + gaps
### New findings
- **R-015 (C, our backtest)** Stops on the S&P 100 momentum book (checked on close, exit next close, re-entry at next monthly rebalance): none 26.5% CAGR / −36.9% maxDD / 688% turnover; **2×ATR/−8% (current rule) 8.9% / −34.4% / 1869%**; 3×ATR/−10% (my R-R2) 11.9% / −35.2% / 1470%; 5×ATR/−20% 21.4% / −27.8% / 949%. Same pattern on (c) without the 200DMA filter (10.5%, 13.4%). Tight stops cut return by ~15 pts/yr and barely reduce drawdown; only a very wide stop reduced drawdown. Consistent with Kaminski-Lo (stops help only with serially correlated returns) and with 2×ATR ≈ 2.2 daily σ being noise (T-020).
- **R-016 (C, our backtest)** Breakers bind often: share of days >8% below running peak — SPY 17%, QQQ 22%, momentum (d) 36%; days with >2% loss per year — SPY 7.9, QQQ 14.7, momentum 22.7.
- **R-017 (A)** Moskowitz & Grinblatt (JF 1999): industry momentum accounts for much of individual-stock momentum; industry portfolios are poorly diversified, so momentum books carry concentrated sector risk. https://doi.org/10.1111/0022-1082.00146
- **R-018 (C, our backtest)** Sector cap ≤3 names per GICS sector: vol 27.7%→24.0%, Sharpe 0.99→1.05, CAGR 26.5%→24.8%; ≤2: vol 22.3%, CAGR 23.9% (sector labels are today's — look-ahead).
- **R-019 (A)** Earnings-announcement premium: Frazzini & Lamont (NBER w13090, 2007) — prices rise on average around scheduled announcements; monthly strategies earn 7–18%/yr excess, strong in large caps, lasts ~20 days. Savor & Wilson (JF 2016) — announcers earn 9.9% annualized abnormal return. Barber, De George, Lehavy & Trueman (JFE 2013) — significant in 9 of 20 countries. So skipping earnings windows forgoes a small premium.
- **R-020 (B)** Earnings days concentrate risk: earnings days explain ~11% of annual return variance for large caps (SMU working paper, mean R² 11.08%); Sammon (passive ownership paper) — ~16.7% of annual volatility in 2017 vs 3.0% in 1990, on ~1.6% of trading days (via search synthesis; figures not re-checked in full text). https://marcosammon.com/images/passive_MS_11_1_18.pdf
- **Gap: is 2 days right?** No study found that tests a "no new entry N days before earnings" rule for long-only books. Evidence cuts both ways (R-019 premium vs R-020 gap risk). The rule only delays entry by a few days, so cost is small; 2 days is judgment (C). Holding *through* earnings is not penalised by the evidence.

### Adversarial verdicts on round-1 rules
| Rule | Strongest counter-evidence | Verdict |
|---|---|---|
| R-R1 1%-risk-to-stop sizing | Depends on a tight stop, which R-015 rejects | **Drop**; equal weight ≤10% |
| R-R2 3×ATR/−10% stop | R-015: still −14.6 pts/yr, no drawdown benefit | **Drop**; replace with wide close-based −20% / 5×ATR (tighter of) stop + rank exit; needs Wuyue |
| R-R3 sector cap 3 | Supported by R-017/R-018 (lower vol, small CAGR cost) | Keep (B/C) |
| R-R4 2%/8% breakers | R-016: 8% pause would bind ~1/3 of the time | Keep, but 8% = no new buys + review with Wuyue, never forced liquidation; needs Wuyue |
| R-R5 Kelly | Irrelevant with equal weights | Park |
| R-R6 3 buys/week, 20-day hold | Superseded by monthly + hold buffer (T-027) | **Replace** with buffer |
| R-R7 trim >15% | No counter-evidence | Merge into sizing rule |
| R-R8 one change per retro | No counter-evidence | Confirm |
| R-R9 index kill-switch | Strengthened by T-021 (≈0 edge since 2009) | **Promote to #1** |

### Proposed rules after round 2 (risk & sizing)
- Replace 2×ATR/−8% stop with: exit at next session if close < max(highest close × 0.80, highest close − 5×ATR14) — **changes existing**, C, needs Wuyue.
- Equal weight ≈10% (cap 10%, trim at 15%), max 12 positions, max 3 per GICS sector — **confirms + new sector cap**, B/C.
- 2% daily loss → no new buys that day; 8% from high → no new buys + review with Wuyue (no forced selling); always show SPY/QQQ drawdown alongside — **changes (clarifies) existing**, C, needs Wuyue.
- Earnings: keep "no new position within 2 trading days before earnings"; existing holdings are held through earnings — **confirms existing**, C.

### Round 2 addendum — core-satellite (after parent steering, 12:30 ET)
- **R-021 (C, our backtest)** 70% SPY + 30% momentum (d), month-end re-mix: 17.9% CAGR / 19.0% vol / −34.7% maxDD / 225% turnover; with hold buffer 18.1% / 144%; 50/50: 20.5%; SPY 13.7% / −33.7%. Same mix with the equal-weight-all-members control as satellite: 15.2% — so much of the "edge" is survivorship (and T-021 says the rest is likely ~0 since 2009). Drawdown is not reduced (satellite correlates with SPY); the benefit is that a zero-edge satellite costs only ~0.2–0.3 pt/yr and tracking error vs the benchmark is small. Weekly is worse in every mix.
- Fits other agents' finding that low turnover + index default wins (Lopez-Lira & Tang LLM news strategy Sharpe 2.97 → −0.39 after 0.20% costs; AIEQ 9.6%/yr vs index 14.7% — reported by the other researcher, not re-verified by me; see their area file).
- **Proposed:** core 70% SPY (buy-and-hold, re-mixed monthly only if off target by >5 pts) + satellite 30% momentum picks (≈3% each, 10 names, monthly, hold buffer). The 10%-per-stock cap applies to single stocks, not the SPY core — **changes existing, needs Wuyue** (C for numbers; A for "index default" base rates R-001–R-004).
