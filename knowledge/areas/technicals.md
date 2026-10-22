# Technicals & price signals — warm digest (Trader, cycle 01, 2026-10-22)

Scope: price/volume signals usable by a long-only, ~$1k, ≤12-position, daily-cadence US stock/ETF account. Plan: `cycles/01-technicals-plan.md`.
Grades: A = peer-reviewed or replicated; B = solid data/practitioner research; C = anecdote/weak. INDEX ids in brackets.

## Bottom line
- Only two price signals have strong (A), replicated, cost-surviving evidence: **intermediate-term momentum (12-1 month)** and **trend filters** (mostly as drawdown control, not return boost). Low-volatility is A-grade but works mainly as *risk-adjusted* outperformance and needs leverage to beat the index on raw return.
- Classic chart indicators (RSI, MACD, breakouts on daily data) do **not** survive data-snooping correction plus costs in the strongest tests. Treat them as noise.
- Expect any published signal to deliver roughly **half** its backtest (McLean-Pontiff). Price-only signals decay the most.
- Honest implication: price signals alone probably do **not** beat SPY/QQQ by much after costs for us. Momentum ranking + trend filter is the best-supported tilt; its edge is small and comes with crash risk.

## Findings

### Momentum
- [T-001] **Cross-sectional momentum** (A). Buying past 3–12 month winners / selling losers earned significant returns over 3–12 month holds, NYSE/AMEX 1965–1989; best cited case 12-month formation/3-month hold ≈1.31%/mo (1.49%/mo with a 1-week skip). Part of the gain reverses in years 2–3. Long-short, so overstates a long-only take. Jegadeesh & Titman, J. Finance, Mar 1993. https://bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf
- [T-002] **Momentum works on the long side and in large caps** (A/B). The long side contributes about as much as the short side; momentum is significant in large caps though weaker than in small caps. Asness, Frazzini, Israel & Moskowitz, "Fact, Fiction and Momentum Investing," J. Portfolio Mgmt 2014. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2435323
- [T-003] **Momentum survives real trading costs** (A/B). Using ~$1T of live institutional trades 1998–2011, value and momentum survive costs at very large scale; **short-term reversal does not**. Frazzini, Israel & Moskowitz, AQR working paper, Dec 2012. https://www.aqr.com/Insights/Research/Working-Paper/Trading-Costs-of-Asset-Pricing-Anomalies
- [T-004] **Time-series momentum ("trend")** (A). An asset's own past-12-month excess return predicts its next-month return in all 58 futures markets studied (equity indices, FX, commodities, bonds), partially reversing after ~1 year; does best in extreme markets. Futures, not single stocks. Moskowitz, Ooi & Pedersen, JFE May 2012. https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum
- [T-005] **Momentum crashes** (A). Momentum has rare, persistent losing streaks that are partly forecastable: they happen in "panic states" after market declines with high volatility, and coincide with market rebounds (past losers rip). A dynamic version roughly doubles alpha/Sharpe. Daniel & Moskowitz, JFE 2016. https://ideas.repec.org/a/eee/jfinec/v122y2016i2p221-247.html
- [T-006] **Scaling momentum by its own volatility** nearly doubles the Sharpe ratio and "virtually eliminates crashes" (A, in-sample on the long-short factor). Barroso & Santa-Clara, JFE 2015. https://ideas.repec.org/a/eee/jfinec/v116y2015i1p111-120.html (see risk-sizing.md R-005 for the out-of-sample critique).

### 52-week high
- [T-007] **Nearness to the 52-week high** (A) explains a large share of momentum profits, beats past-return measures as a predictor, and does not reverse long-run. George & Hwang, J. Finance Oct 2004. https://bauer.uh.edu/TGeorge/papers/gh4-paper.pdf
- [T-008] Recency matters (B/A): stocks whose 52-week high was set recently outperform; conditioning on recency roughly doubles the strategy's monthly return (US 1965–2008, no large-cap-only test reported). Bhootra & Hur, J. Banking & Finance 2013. https://ideas.repec.org/a/eee/jbfina/v37y2013i10p3773-3782.html

### Short-term reversal
- [T-009] **One-month reversal** (A): strong negative first-order monthly serial correlation; extreme deciles on one-month lagged return differ ~1.99%/mo (1934–1987). Positive serial correlation at 12 months. Jegadeesh, J. Finance Jul 1990. https://finance.martinsewell.com/stylized-facts/dependence/Jegadeesh1990.pdf
- Implication: (a) skip the most recent month when ranking momentum; (b) do **not** run a reversal ("buy last month's losers") strategy — per [T-003] it doesn't survive costs.

### Moving-average trend filters
- [T-010] **10-month SMA timing** (A, J. Wealth Mgmt 2007, updated 2013): on the total-return S&P 500 1901–2012, gross annualized 10.2% vs 9.3% buy-and-hold, vol 12.0% vs 17.9%, max drawdown −50.3% vs −83.5% (frictions and taxes excluded). Main benefit = drawdown cut, return gain small. Faber; summary of Feb-2013 update by CXO Advisory. https://mebfaber.com/wp-content/uploads/2016/05/SSRN-id962461.pdf ; https://www.cxoadvisory.com/technical-trading/long-term-outperformance-from-trends-defined-by-moving-averages/
- [T-011] **Early evidence for MA/breakout rules** (A but old): on the Dow 1897–1986, buy signals from moving-average and trading-range-break rules beat sell signals; returns after sell signals were negative. Brock, Lakonishok & LeBaron, J. Finance Dec 1992. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1992.tb04681.x
- [T-012] **...but it doesn't survive data-snooping + costs** (A): re-testing on DJIA 1897–2011 with false-discovery-rate control, an investor could never have picked the future best rules ex ante, and even in-sample performance is "completely offset by the introduction of low transaction costs." Bajgrowicz & Scaillet, JFE 2012. https://ideas.repec.org/a/eee/jfinec/v106y2012i3p473-491.html
- Our read: the 200DMA filter is justified as **risk control**, consistent with time-series momentum [T-004], not as a standalone return engine. Evidence is strongest at the index/asset-class level; single-stock 200DMA filters are less tested.

### RSI / MACD / chart indicators
- [T-013] Survey of 95 modern studies (A, survey): 56 positive, 20 negative, 19 mixed, but conclusions are undermined by data snooping, ex-post rule selection and poor treatment of risk/costs. Park & Irwin, J. Economic Surveys 2007. https://ideas.repec.org/a/bla/jecsur/v21y2007i4p786-826.html
- [T-014] RSI/MACD index studies (C): MACD(12,26,0) and RSI(21,50) profitable on Italian and Canadian indices after 1% costs, RSI(14,30/70) on the Dow; Nikkei nothing; no data-snooping correction; lower-tier journal. Chong, Ng & Liew, J. Risk Financial Mgmt (MDPI) Feb 2014. https://www.mdpi.com/1911-8074/7/1/1 . Futures reality-check study with >9,000 rules found almost no significant profits after correction and mostly negative out-of-sample returns (B; seen via academia.edu summary only). https://www.academia.edu/35697004/
- Verdict: **no reliable edge** from RSI/MACD for us. Do not use as entry triggers.

### Volume
- [T-015] Past trading volume (A): high-volume stocks behave like glamour stocks with lower future returns; volume predicts the size and persistence of momentum; high-volume winners reverse faster. Lee & Swaminathan, J. Finance Oct 2000. https://ideas.repec.org/a/bla/jfinan/v55y2000i5p2017-2069.html
- Implication: "volume confirmation" of a breakout is not supported; if anything, very high-turnover winners carry more reversal risk. No rule proposed (effect is complex; too few names for us to exploit it).

### Low volatility / low beta
- [T-016] Low-vs-high-volatility global decile alpha spread ≈12%/yr 1986–2006; holds in US, Europe, Japan; not explained by size/value (A). Blitz & van Vliet, J. Portfolio Mgmt Fall 2007. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=980865
- [T-017] Betting-against-beta: low-beta assets earn higher risk-adjusted returns; the factor is **leveraged** long-low-beta/short-high-beta (A). Frazzini & Pedersen, JFE 2014. https://ideas.repec.org/a/eee/jfinec/v111y2014i1p1-25.html . High idiosyncratic-vol stocks have low returns (Ang, Hodrick, Xing & Zhang, J. Finance 2006 — cited via search summary, not opened).
- Implication for a goal of beating SPY on raw return without leverage: low-vol tilts tend to *lag* in strong bull markets; their edge is per unit of risk. Use it only as an **exclusion** of the most volatile names (where the anomaly is strongest, on the short/avoid side), not as a portfolio tilt.

### Decay and data mining (applies to everything above)
- [T-018] Across 97 published predictors, returns are 26% lower out-of-sample and **58% lower post-publication**; decay is larger for predictors with high in-sample returns and for those built only from price/volume data (A). McLean & Pontiff, J. Finance Feb 2016. https://gwern.net/doc/economics/2016-mclean.pdf
- [T-019] Given hundreds of tested factors, a new one should clear t > 3.0, not 2.0; many published findings are likely false (A). Harvey, Liu & Zhu, RFS 2016. https://academic.oup.com/rfs/article/29/1/5/1843824

### Sanity check with live data (Robinhood market data, daily bars to 2026-10-21 close)
- [T-020] SPY close 773.09; ATR(14) 7.02 = 0.91% of price → 2×ATR = 1.82%. 200DMA 726.29 (SPY +6.4% above). Realized vol 20d 8.8%, 1y 12.8%. ~12-1 return +15.2%. At 98.9% of 52-week high.
- QQQ close 725.20; ATR(14) 10.91 = 1.50% → 2×ATR = 3.01%. 200DMA 676.49 (+7.2%). Realized vol 20d 15.9%, 1y 19.8%. ~12-1 +22.2%. At 95.1% of 52-week high.
- Read: both indices are in an uptrend regime (above 200DMA, positive 12-month momentum), so the momentum-crash conditions in [T-005] are **not** present today. A single stock with 30–40% annual vol has an ATR of roughly 2–3%, so our 2×ATR stop sits about 4–6% away — only ~2 daily standard deviations (see risk-sizing.md).

## Proposed rules (technicals) — checked against current repo rules
| # | Rule (one line, mechanical) | Evidence | Status |
|---|---|---|---|
| T-R1 | Keep the filter: only buy when the stock's close > its 200-day SMA; also only open new positions at full size when SPY close > SPY 200DMA. | T-004, T-010, T-012 (filter = risk control) | Confirms existing (adds SPY regime check) |
| T-R2 | Rank eligible candidates by 12-1 month total return (12 months back, skipping the latest ~21 trading days); only buy names in the top third of the screened universe AND with 12-1 return > SPY's 12-1 return. | T-001, T-002, T-003, T-009 | New |
| T-R3 | Tie-breaker: prefer names closing within 10% of their 52-week high, high set within the last 3 months. | T-007, T-008 | New (threshold is judgment) |
| T-R4 | No buys triggered by RSI, MACD, chart patterns, or "volume confirmation"; no adding any indicator to rules unless it shows out-of-sample, after-cost evidence (t > 3 or replicated). | T-012, T-013, T-014, T-018, T-019 | New |
| T-R5 | No short-term reversal trades: never buy a stock *because* it fell over the last 1–5 days or month. | T-003, T-009 | New |
| T-R6 | Crash guard: if SPY closed below its 200DMA within the last 20 trading days AND its 20-day realized vol > its 1-year realized vol, new momentum buys are half size. | T-005, T-006 | New |
| T-R7 | Exclude stocks whose 1-year realized volatility > 2.5× SPY's. | T-016, T-017 | New (multiple is judgment) |
| T-R8 | Expect ~half of any backtested edge; a signal must show after-cost edge of ≥2× our assumed round-trip cost *after* that haircut before it enters the rules. | T-018 | New |

## Open questions
- Does a single-stock 200DMA filter add anything on top of 12-1 momentum? (Most stocks in the top momentum third are already above their 200DMA.) Test in paper data.
- Industry momentum (Moskowitz-Grinblatt 1999; Hong-Jordan-Liu on 52-week high) might be cheaper to harvest via sector ETFs. Next cycle.

## Round 2 (2026-10-22, cycle 02) — adversarial check + sanity backtest
Backtest: `backtests/2026-10-22-momentum/` (README lists every assumption/bias). It is a **sanity check, not proof**: today's S&P 100 members (survivorship), 2014–2026, 0.30% round trip.

### New findings
- **T-021 (A, data)** Ken French / CRSP 6 portfolios on size × prior (12-2) return, through 2026-08: long-only BIG HiPRIOR (large caps, top 30% momentum, value-weighted) minus market = **+3.0%/yr 1927–2026 (t 4.4), +2.9%/yr 1994–2008 (t 1.5), −0.4%/yr 2009–2026 (t −0.3), 0.0%/yr 2014–2026 (t 0.0)**, gross of costs. Big winners-minus-losers: −2.0%/yr since 2009. Computed by us (`french/french_check.py`) from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html (accessed 2026-10-22).
- **T-022 (B)** "Where Has the Trend Gone?" (Journal of Wealth Management): US decile momentum 1986–2015 has ~1%/month P1–P10 alpha, but **no significant winner–loser difference in 2007–2015**; cites Hwang-Rubesam 2015 on post-1990s decline. https://www.pm-research.com/content/iijwealthmgmt%3A%3A%3A20%3A%3A%3A2%3A%3A%3A29.full.pdf (vol 20 issue 2; authors not recorded)
- **T-023 (C)** Pre-registered replication on ~100 US large caps, 2000–2024 (GitHub, not peer-reviewed): Fama-MacBeth t = −0.67 in-sample; OOS net Sharpe 0.02; flat quintiles. https://github.com/BrandonKKY/cross-sectional-momentum
- **T-024 (B)** 52-week-high strategy does not replicate recently: Lobão (2017, RePEc cuf/journl v18i2) finds it positive but insignificant 1980–2014, **significantly negative 2001–2014**. A practitioner rerun (C; tradingstudio, Apr 2026) of "30 stocks nearest 52-week high", 2000–Oct 2025: 4.57%/yr vs SPY 8.02%; 2.64% vs 11.05% from 2008. https://ideas.repec.org/a/cuf/journl/y2017v18i2lobao.html
- **T-025 (B/C)** 200DMA in V-shaped crashes: Graham Capital (June 2020) Monte Carlo — moving-average-crossover results in Feb–Mar 2020 were worse than ~91% of simulated paths with the same total drop ("unlucky", B practitioner). Hulbert (MarketWatch, 2020-02-28) cites an HFD study: the 200DMA strategy lagged buy-and-hold over the past century even risk-adjusted after costs (C). UBS (via news, 2020-06-09): 10 signals 2010–2019 with no bear market (C).
- **T-026 (C, our backtest)** On the biased S&P 100 universe: stock>200DMA filter added nothing (26.5% vs 28.7% CAGR); SPY<200DMA → all cash cut CAGR 26.5%→16.9% and 2022 was worse (−21.3% vs −11.6%); half-size 21.9%; weekly rebalance worse than monthly (21.3% vs 26.5%) at 2.5× turnover. Momentum top-10 beat the equal-weight-all-members control by 8–10 pts/yr — which T-021 says is mostly hindsight.
- **T-027 (A)** Novy-Marx & Velikov (RFS 2016): a buy/hold spread (stricter to enter than to keep) is the most effective cost mitigation; cutting trading frequency by 2/3 cuts turnover/costs only ~1/3; anomalies with >50%/month turnover rarely survive costs. https://mysimon.rochester.edu/novy-marx/research/ToAatTC.pdf. Our test (C): buy top 10 / hold while rank ≤20 cut turnover 688%→418%/yr with similar CAGR (27.4% vs 26.5%).

### Adversarial verdicts on round-1 rules
| Rule | Strongest counter-evidence | Verdict |
|---|---|---|
| T-R1 stock>200DMA | Adds nothing on top of momentum in our test (T-026); trend-rule evidence is weak after snooping (T-010/T-012) | **Downgrade to C**; keep as existing screen only because it's harmless-ish; Wuyue may drop |
| T-R1 SPY>200DMA full-size | Whipsaws: −10 pts/yr CAGR in our test, no real drawdown benefit; 2020 path "unlucky" (T-025); HFD lagged even risk-adjusted | **Drop** |
| T-R2 12-1 momentum top third | Unbiased large-cap long-only excess ≈0 since 2009 (T-021, T-022, T-023); our backtest's edge is survivorship | **Downgrade A→B (long-run) / ~0 expected edge now**; keep only as the selection method inside a test that must beat the index (R-R9) |
| T-R3 52-week-high tie-breaker | Significantly negative 2001–2014 (T-024) | **Drop** |
| T-R4 no RSI/MACD/patterns | No counter-evidence found | Confirm (B) |
| T-R5 no reversal buys | Reversal is weaker in large caps now; rule is a "don't" so costless | Confirm (B), merged into T-R4 |
| T-R6 crash guard half-size | Not tested exactly; regime switches whipsaw (T-025, T-026 half-size −4.6 pts/yr); Daniel-Moskowitz crashes are mostly the short leg | **Drop** (park) |
| T-R7 vol > 2.5× SPY exclusion | 2014–2026 was led by high-vol mega caps; not tested; multiple is judgment | **Park (C)**, not in final list |
| T-R8 halve backtested edge | Strengthened: biased +8–10 pts → unbiased ~0 | Confirm, add bias-control requirement |

### Proposed rules after round 2 (technicals)
- T-R2′ Monthly: rank screened names by 12-1 return; buy top 10 that also beat SPY's 12-1; hold while rank ≤20 — **changes** (B; edge since 2009 ≈0).
- T-R4′ No RSI/MACD/pattern/volume/52-week-high/reversal triggers — **new** (B).
- No SPY regime filter — **new** (B/C). Stock>200DMA — **confirms existing**, downgraded to C.
- T-R8′ Any backtest on today's index members must report the equal-weight-all-members control; halve what's left; must be ≥2× cost — **new** (A for decay, C for numbers).
