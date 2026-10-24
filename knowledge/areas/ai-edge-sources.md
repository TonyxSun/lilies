# AI edge: published evidence (sources) — task LOTF-AIEDGE-1023
Author: 牛马 (research bot) · date 2026-10-23 (written ~1:10am ET) · **facts only, no scores, no recommendations, no orders.**
Companion to `areas/ai-edge.md` (Trader's own tests AE-001..AE-004; not edited). INDEX ids for new rows: **AS-001..AS-030** (area `ai-edge-sources`). Existing ids are reused where a source was already in the book.
Rules for this file: every number below was read on the source page/PDF unless marked **figure not verified**. "OOS" = out of sample. "Costs" = whether the source reports results after trading costs.

---
## A. Ideas Trader already tested (all 4 failed net of costs OOS 2013–2026)

### A1. Overnight-only holding (Trader AE-001)
| id | Source (date) | Finding (as published) | Sample | OOS? | After costs? |
|---|---|---|---|---|---|
| N-018 (existing) | Cliff, Cooper & Gulen, SSRN 2008 | SPY $1 close-to-open → $6.54 vs open-to-close → $0.61, pre-cost | Feb 1993–Dec 2006 | no | no |
| N-003 / N-025 (existing) | Lou, Polk & Skouras JFE 2019; counter-evidence per N-025 | momentum alpha accrues overnight (0.95%/mo vs 0.11% intraday); location contested by N-025 | 1993–2013 | partly | no |
| AS-001 | Boyarchenko, Larsen & Whelan, "The Overnight Drift", RFS 36(9) 2023 (NY Fed SR 917, 2020; published Mar 13 2023) https://doi.org/10.1093/rfs/hhad020 | US equity returns are "large and positive during the opening hours of European markets"; tied to order imbalances at the prior US close; **sell-offs are followed by robust positive overnight reversals, rallies by much smaller ones** (inventory-risk story). Size per night: **figure not verified** (abstract gives none). | not verified from abstract | n/a | not addressed in abstract |
| AS-002 | Knuteson, arXiv 2010.01727 (Oct 2020) and 1912.01708 (Nov 2019), not peer-reviewed | Overnight returns of major indices "wildly positive", intraday negative; e.g. TSX 60 **+1,062% overnight vs −67% intraday** over ~two decades; author attributes it to manipulation (hypothesis, not established) | 1990–2019/2020, 21 indices | n/a | no |
| AS-003 | Lachance, "Night Trading: Lower Risk but Higher Returns?", SSRN 2633476 (Jul 2015, working paper) | ~**one fifth of stocks** show persistent significant overnight bias; holding them overnight next year "yields **twice the market's return for a third of the market beta**". Implementation costs "discussed" — net figure **not verified** | US stocks (period not verified) | yes (next-year) | not verified |
| MX-001, AE-001 (existing, own) | own Yahoo tests | gross overnight real (SPY +0.038%/day OOS) but net loses vs buy-and-hold; cash-account infeasible | 1993/2013–2026 | yes | yes |
**Read:** literature agrees the gross overnight premium exists (and is strongest after sell-offs, AS-001). No source found shows a long-only, retail-cost, overnight-only strategy beating buy-and-hold after costs. Consistent with AE-001.

### A2. Buying when the market closes near its daily low (IBS / close location; Trader AE-002)
| id | Source | Finding | Sample | OOS? | Costs? |
|---|---|---|---|---|---|
| AS-004 | Pagonidis, "The IBS Effect: Mean Reversion in Equity ETFs" (NAAIM paper, Apr 2014; QUSMA working paper Sep 2013) https://naaim.org/wp-content/uploads/2014/04/00V_Alexander_Pagonidis_The-IBS-Effect-Mean-Reversion-in-Equity-ETFs-1.pdf | Next-day close-to-close return averages **+0.35% when IBS < 0.20 vs −0.13% when IBS > 0.80** (equity ETFs); effect present "since the early 90s"; stronger in high volatility and on Mondays; **essentially US-only**; for US ETFs it "completely disappears on low volume days"; "using IBS alone is difficult due to transaction costs" — author recommends it as a filter | equity ETFs, early 1990s–~2013 | no formal OOS | gross; author says standalone is hard net of costs |
| AS-005 | tickfloor.com replication (2025), practitioner site | IBS<0.2 & close<5-day avg rule on QQQ, 2005-01-04 to 2025-03-14, 0.05%/side: **−4.7 pts/yr vs benchmark, 557 trades**, BH-adjusted q = 1.000 (seen in search snippet only; page not opened → treat as **figure not verified**) | 2005–2025 | n/a | yes |
**Read:** no peer-reviewed IBS paper exists (QUSMA itself says "no treatment of the IBS effect specifically in the academic literature"). Practitioner evidence: gross effect real historically, standalone net-of-cost edge weak. Consistent with AE-002.

### A3. Short sharp-dip buying / short-term reversal (Trader AE-003, RSI(2))
| id | Source | Finding | Sample | OOS? | Costs? |
|---|---|---|---|---|---|
| T-009, ST-003 (existing) | Jegadeesh JF 1990; Lehmann QJE 1990 | 1-month / 1-week reversal in the cross-section; extreme deciles ~1.99%/mo (1934–87) | 1934–1987 | — | no |
| T-003 (existing) | Frazzini, Israel & Moskowitz (AQR 2012) | with real institutional costs, short-term reversal does **not** survive | 1998–2011 | — | yes |
| AS-006 | Nagel, "Evaporating Liquidity", RFS 25(7) 2012 https://www.nber.org/papers/w17653 | reversal returns = pay for providing liquidity; expected returns are "strongly time-varying and highly predictable with the VIX"; expected returns and Sharpe ratios "increase enormously" in turmoil (2007–09); even industry-portfolio reversal earns high returns when VIX is high. Magnitudes: **figure not verified** (abstract only) | US stocks (period not verified) | — | gross |
| AS-007 | de Groot, Huij & Zhou, JBF 36(2) 2012 https://ideas.repec.org/a/eee/jbfina/v36y2012i2p371-382.html | counter-evidence: cost drag comes mostly from small caps; large-cap universe + lower-turnover construction → **30–50 bp per week net of trading costs** (long-short, institutional cost model) | not verified | — | yes (institutional) |
| AE-003 (own) | Trader | RSI(2) SPY OOS t 1.90 at 0.05%/side, decayed from IS t 3.16 | 2013–2026 | yes | yes |
**Read:** literature agrees reversal is real but is liquidity-provision pay, concentrated in high-VIX periods (AS-006) and in small/illiquid names; cost survival depends on scale/implementation (T-003 vs AS-007). RSI(2) itself (Connors & Alvarez book, 2008) has no peer-reviewed test found.

### A4. Monthly rotation among stocks / gold / bonds (time-series & dual momentum; Trader AE-004)
| id | Source | Finding | Sample | OOS? | Costs? |
|---|---|---|---|---|---|
| T-004 (existing) | Moskowitz, Ooi & Pedersen JFE 2012 | 12-month TSMOM predicts next month in all 58 futures | 1985–2009 | — | — |
| AS-008 | Huang, Li, Wang & Zhou, "Time series momentum: Is it there?", JFE 135(3) Mar 2020 https://ideas.repec.org/a/eee/jfinec/v135y2020i3p774-794.html | same data as MOP: asset-by-asset, **47 of 55 assets have t < 1.65**; only **3 assets** have significant OOS R²; pooled t = **4.34** but below bootstrap critical values; TSM strategy performs "virtually the same" as a strategy using historical sample means | MOP data | yes | — |
| AS-009 | Kim, Tse & Wald, JFM 30 2016 https://ideas.repec.org/a/eee/finmar/v30y2016icp103-124.html | MOP alpha is "largely driven by volatility-scaling"; **without vol scaling, TSMOM and buy-and-hold have similar cumulative returns and alphas not significantly different** | futures | — | — |
| AS-010 | Hurst, Ooi & Pedersen, "A Century of Evidence on Trend-Following Investing", JPM Fall 2017 (AQR) https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing | TSMOM built back to 1880, 67 markets: positive average return in each market, **average per-market Sharpe ≈ 0.4**; does best in extreme up/down equity years ("smile"); pre-1985 period acts as OOS vs MOP. Net-of-fee CAGR/Sharpe numbers: **figure not verified** (in exhibits) | 1880–2016 | yes (pre-1985) | simulated costs + 2/20 fees |
| AS-011 | Faber, "A Quantitative Approach to Tactical Asset Allocation" (2013 update) https://mebfaber.com/wp-content/uploads/2016/05/SSRN-id962461.pdf | post-publication OOS 2006–2012: 10-month-SMA timing beat **its equal-weight 5-asset buy-and-hold by "over two percentage points per year"**, with less vol and drawdown, but **outperformed in only 3 of 7 years** (benchmark is not SPY) | 2006–2012 OOS | yes | pre-tax; fees discussed |
| M-001, T-010 (existing) | Faber 1901–2012 | CAGR 10.18% vs 9.32%, maxDD 42.24% vs 83.66%, pre-cost | — | — | no |
**Read:** published evidence is split: trend is robust as a **drawdown reducer** (AS-010, AS-011, M-001), while its **return edge** is statistically weak once vol scaling/pooling is handled (AS-008, AS-009). Consistent with AE-004 (drawdown cut, no excess return). Antonacci "dual momentum": **not researched** this pass (book/practitioner only).

---
## B. Edges not yet tested by Trader

### B1. Speed of absorbing news / filings
| id | Source | Finding | Sample | Costs? |
|---|---|---|---|---|
| AS-012 | Busse & Green, "Market efficiency in real time", JFE 65 2002 https://ideas.repec.org/a/eee/jfinec/v65y2002i3p415-437.html | CNBC Morning/Midday Call, **322 stocks**: prices respond "within seconds"; **positive reports fully incorporated within one minute**, negative ones over ~15 minutes; trading intensity doubles in first minute; only traders executing **within 15 seconds** make small significant profits | Jun–Oct 2000 | pre-cost |
| AS-013 | Rogers, Skinner & Zechman, "Run EDGAR Run", J. Accounting Research 55(2) 2017 https://ideas.repec.org/a/bla/joares/v55y2017i2p459-505.html | Form 4 filings reached **paying PDS-feed subscribers before the EDGAR website**; prices, volumes and spreads respond **~30 seconds before public posting**; SEC then agreed to remove the PDS timing advantage | sample of Form 4s (period not verified) | — |
| AS-014 | Groß-Klußmann & Hautsch, "When machines read the news", J. Empirical Finance 18(2) 2011 https://ideas.repec.org/a/eee/empfin/v18y2011i2p321-340.html | machine-read company news (20-second VAR, LSE stocks): returns, vol, volume and **spreads** react; relevance filter is crucial; sentiment predicts trends but **profitability is eroded by wider bid-ask spreads** at news times | LSE (period not verified) | yes (qualitative) |
| AS-015 | Cao, Jiang, Yang & Zhang, "How to Talk When a Machine Is Listening", RFS 2023 (NBER w27950) https://doi.org/10.1093/rfs/hhad021 | firms facing more machine readership write filings that are easier for machines and avoid words algorithms score negative. Machine downloads of 10-K/10-Q **360,861 (2003) → 165,318,719 (2016)**: **figure not verified** (search summary of the NBER draft) | 2003–2016 | — |
| N-017, N-019, L-001, L-015, L-016 (existing) | large-cap news priced in milliseconds to seconds (N-017); LLM news strategy Sharpe 6.54 → 1.22 by 2024 (L-015) and 2.97 → −0.39 at 20 bp costs (L-016) | | |
**Read:** prices absorb public news in seconds to minutes; the fast edge goes to paid feeds / co-located traders (AS-012/013). A bot polling free EDGAR/RSS at minute latency is structurally late. The remaining room is *interpretation over days*, which L-015/16 show decays and dies at retail costs.

### B2. PEAD after 2010
- **F-003 (existing, A):** Martineau CFR 2022: no 60-day PEAD in non-microcaps since 2006.
- **F-004 (existing, C)** counter (HHS thesis, large-cap 1.99% 2021–24, long-short). **F-005 (existing):** Subrahmanyam 2025, t = 1.43 ex-microcaps. **NS-001 (existing):** costs eat 70–100% of PEAD (Chordia et al. FAJ 2009). **F-015/T-018 (existing):** McLean–Pontiff 58% post-publication decay.
- **AS-016 (A):** Chordia, Subrahmanyam & Tong, JAE 58(1) 2014 https://ideas.repec.org/a/eee/jaecon/v58y2014i1p41-58.html — majority of prominent anomalies attenuated; returns of a prominent-anomaly portfolio **"approximately halved after decimalization"**, linked to hedge-fund AUM, short interest and turnover.
- No newer peer-reviewed counter-evidence found this pass.

### B3. Scanning technicals across many tickers
| id | Source | Finding | OOS? | Costs? |
|---|---|---|---|---|
| T-011, T-012, T-013 (existing) | Brock-Lakonishok-LeBaron 1992; Bajgrowicz-Scaillet 2012; Park-Irwin 2007 | BLL rules worked 1897–1986; FDR-corrected they are offset by low costs; survey: 56/95 positive but data-snooped | | |
| AS-017 | Sullivan, Timmermann & White, JF 54(5) 1999 https://ideas.repec.org/a/bla/jfinan/v54y1999i5p1647-1691.html ; full text https://www.fmg.ac.uk/sites/default/files/2020-11/dp303.pdf | White's Reality Check on an expanded BLL universe, DJIA: some rules beat the benchmark 1897–1986 **even after** snooping adjustment, but in the next 10 years (**1987–1996**) "the probability that the best-performing trading rule did not outperform the benchmark … is nearly **12 percent**" → "scant evidence"; **S&P 500 futures 1984–96: no evidence** | yes | futures test addresses costs |
| AS-018 | Hsu & Kuan, JFEc 3(4) 2005 https://econpapers.repec.org/RePEc:oup:jfinec:v:3:y:2005:i:4:p:606-628 | Reality Check + SPA: profitable rules found for **NASDAQ Composite and Russell 2000**, not for **DJIA or S&P 500** (via search summary of abstract; magnitudes **not verified**) | partial | not verified |
**Read:** breadth scanning raises the number of trials, which raises false discoveries (see B6). Where effects survive snooping tests, they are in younger/smaller markets, not SPY/DJIA.

### B4. Rules discipline / the behavior gap
| id | Source | Finding | Sample |
|---|---|---|---|
| AS-019 | Morningstar "Mind the Gap 2025" (Ptak, Aug 13 2025) https://www.morningstar.com/financial-advisors/volatility-bedevils-fund-investors | average dollar in US funds/ETFs earned **7.0%/yr vs 8.2%** total return → **gap 1.2 pts/yr (~15% of return)**, persistent in prior 10-yr windows; lowest-trading (most stable cash-flow) funds gap **0.8%**, 1 pt narrower than the most-traded quintile; sector equity funds 7.0% vs 8.5%; allocation funds captured ~97% | 10 yrs to Dec 31 2024 |
| AS-020 | DALBAR QAIB 2025 press release (Mar 31 2025) https://www.dalbar.com/press-release/investors-missed-the-best-of-2024s-market-gains-latest-dalbar-investor-behavior-report-finds/ | average equity investor **16.54% vs S&P 500 25.02%** in 2024 → **848 bp** gap, second-largest of the decade. Caveat: DALBAR's method is disputed by some researchers (critique not reviewed here) | 2024 |
| R-003 (existing) | Barber & Odean JF 2000 "Trading is hazardous" | highest-turnover households 11.4%/yr vs 17.9% market (1991–96) | |
| R-004 (existing) | Barber, Lee, Liu & Odean 2014 | <1% of Taiwan day traders reliably profitable | |
| AS-021 | Chague, De-Losso & Giovannetti, "Day Trading for a Living?", SSRN 3423101 (2019) | Brazilian mini-index futures day traders who persisted >300 days: **97% lost money**; ~1.1% earned more than minimum wage — **figure not verified** (SSRN/FGV pages blocked; numbers from search summary) | period not verified |
| S-002, N-008, N-031 (existing) | Barber, Huang, Odean & Schwarz JF 2022 | Robinhood herding events → ~−4.7% next month | 2018–2020 |
| AS-022 | Eaton, Green, Roseman & Wu, JFE 146(2) 2022 https://ideas.repec.org/a/eee/jfinec/v146y2022i2p502-528.html | during **Robinhood outages**, retail-heavy stocks show lower order imbalances, better liquidity and lower volatility; the opposite during outages at traditional brokers → herding inexperienced investors add inventory risk | period not verified |
**Read:** the best-documented "edge" available to a rule-following bot is avoiding the retail behavior gap (≈1.2 pts/yr in Morningstar's measure; larger for high-trading/high-vol/sector funds). It is an edge vs the *average investor*, not vs the index.

### B5. Geopolitical / event-shock reactions
| id | Source | Finding | Sample |
|---|---|---|---|
| AS-023 | Caldara & Iacoviello, "Measuring Geopolitical Risk", AER 112(4) Apr 2022 https://www.aeaweb.org/articles?id=10.1257/aer.20191823 ; PDF https://www.matteoiacoviello.com/gpr_files/GPR_PAPER.pdf | US VAR: a 2-SD GPR shock is followed by a **short-lived VIX rise and a decline in stock prices** and oil; investment bottoms at **−1.5% after ~1 year**, hours **−0.6%** at 1 year; both threats and acts matter. Stock-price magnitude: **figure not verified** (in a chart) | 1985–2019 |
| AS-024 | Berkman, Jacobsen & Lee, JFE 101(2) 2011 https://ideas.repec.org/a/eee/jfinec/v101y2011i2p313-332.html | **447 international political crises**: changes in a crisis index have a "large impact on both the mean and volatility of world stock market returns"; crisis-sensitive industries earn higher returns (priced risk) | 1918–2006 |
| AS-025 | Brune, Hens, Rieger & Wang, "The war puzzle", Int. Review of Economics 2015 https://doi.org/10.1007/s12232-014-0215-7 | rising war probability lowers prices; the **actual outbreak often raises them**, unless the war starts unexpectedly (via abstract summary; magnitudes not verified) | historical wars |
| AS-026 | LPL Research blog (practitioner) https://www.lpl.com/research/blog/middle-east-conflict-how-stocks-react-to-geopolitical-shock.html | 24 events 1941–2023: S&P avg 1-day −1.1%, drawdown −4.7%, 19.2 days to bottom, 41.4 days to recover — **figure not verified** (page blocked; search summary only) | 1941–2023 |
| OIL-002 (existing) | Kilian & Park 2009 | oil supply/precautionary shocks hurt stocks; demand-driven oil rises don't | |
**Read:** geopolitical risk is a priced, mostly short-lived equity-price shock in the academic papers; "sell the threat, buy the outbreak" appears in AS-025, and practitioner tables show typical recovery within weeks (unverified). No source found tests a retail long-only rule net of costs.

### B6. Where a bot has no edge
| id | Source | Finding |
|---|---|---|
| AS-027 | Budish, Cramton & Shim, QJE 130(4) Nov 2015 https://academic.oup.com/qje/article/130/4/1547/1916146 | ES–SPY median return correlation in 2011 is **0.1016 at 10 ms and 0.0080 at 1 ms** (≈1 at minutes) → mechanical arbitrage "available to whoever is fastest" |
| AS-028 | Aquilina, Budish & O'Neill, QJE 137(1) 2022 https://www.nber.org/papers/w29011 | FTSE 100 latency-arbitrage races ~**1 per minute per symbol**, modal duration **5–10 microseconds**, ~**20% of volume**, top 6 firms >80% of race wins/losses; ~**0.5 bp tax** on trading, ~one-third of effective spread/price impact; ~**$5bn/yr** globally |
| AS-029 | Bailey, Borwein, López de Prado & Zhu, "Pseudo-Mathematics and Financial Charlatanism", Notices AMS 61(5) May 2014 https://www.ams.org/notices/201405/rnoti-p458.pdf | with **5 years** of data, no more than **45 independent configurations** should be tried; at 45 the expected max IS Sharpe is 1 while expected OOS Sharpe is 0; with **2 years**, **7** configurations already give IS Sharpe 1 |
| AS-030 | Bailey et al., "The Probability of Backtest Overfitting", J. Computational Finance 2016 https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf | random-walk example: **8,800** monthly-rule configs on 1,000 daily prices → best IS Sharpe **1.27** (PSR stat 2.83) yet ~**53%** of OOS Sharpes negative and **PBO ≈ 55%**; hold-out testing called unreliable |
| MA-003, T-019, T-018/F-015, CA-001 (existing) | deflated Sharpe; Harvey-Liu-Zhu t>3; McLean-Pontiff 26% OOS / 58% post-publication decay |
| E-001, E-002, E-013, E-014 (existing) | retail execution: round-trip 0.07–0.46% across brokers (Schwarz et al. JF 2025); SEC Robinhood order $34.1M inferior execution 2015–18 |
Crowding: not researched this pass.
**Read:** a bot has no speed edge (microseconds, paid feeds), and its tirelessness at testing many rules is a liability unless the number of trials is counted (AS-029/030).

---
## Possible HOT-rule candidates (flag only, NOT adopted; Trader decides)
1. **Count trials.** Every backtest batch logs the number of variants tried (N); a pass needs a deflated-Sharpe / PBO check or t ≥ 3, not just t ≥ 2. With ~13 years of OOS data, a few dozen independent variants already manufacture a Sharpe ≈ 1 by luck. (AS-029, AS-030, MA-003, T-019)
2. **No speed trades.** Never size a trade on being first to a headline or filing; public news is priced in seconds to a minute, and the fast edge belongs to paid feeds and co-located HFT. (AS-012, AS-013, AS-027, AS-028, N-017, L-016)
3. **The measurable bot edge is not trading.** Treat avoided discretionary trades as the main edge; behavior gap ≈1.2 pts/yr in funds, bigger with more trading. (AS-019, AS-020, R-003, AS-022)
4. **Dip-buying is liquidity provision paid mostly in high-VIX regimes.** Any dip/reversal rule should be read as conditional on stress, not unconditional. (AS-006, AS-001)
5. **Trend/rotation = drawdown tool, not return engine.** (AS-008, AS-009, AS-010, AS-011; matches AE-004, AE-R2)

## Still backtestable by Trader (free data; facts on what to test, no recommendation)
1. **VIX-conditioned dip buying (Nagel):** RSI(2)<10 or IBS<0.2 on SPY/QQQ, split by ^VIX above/below its trailing 1-yr 80th percentile (or VIX>25). Yahoo ^VIX, SPY, QQQ.
2. **Sell-off-conditioned next-day hold (Boyarchenko):** after an SPY close-to-close drop ≤ −1.5% (or a close in the bottom 10% of range on a down day), hold to next close vs an average day; cash-account-feasible version (buy at close, sell next close or later).
3. **Vol-scaled buy-and-hold vs AE-004 rotation (Kim-Tse-Wald):** inverse-vol weighted SPY/QQQ/GLD/TLT/IEF/DBC with monthly rebalance, no momentum filter, vs AE-004 → tells whether AE-004's drawdown cut came from momentum or from vol scaling.
4. **Faber GTAA replication 2013–2026:** 10-month SMA on SPY/EFA/IEF/VNQ/DBC (+GLD variant), vs equal-weight buy-and-hold and vs SPY/QQQ.
5. **Geopolitical-risk spikes:** daily GPR index (free CSV, matteoiacoviello.com/gpr.htm) → SPY/QQQ forward 5/20/60-day excess returns after top-1%/top-5% GPR days vs unconditional; and after GPR acts (GPA) vs threats (GPT).
6. **PBO/deflated-Sharpe audit of our own tests:** CSCV PBO across the AE-002/AE-003 parameter grid and deflated Sharpe for AE-003 given the number of variants the team has tried (INDEX MA-001 counts ~25 t-stats).
7. **Hsu-Kuan market split:** same IBS/RSI(2) rules on IWM and QQQ vs SPY with a Reality-Check / SPA bootstrap.
8. **Own behavior-gap meter:** weekly dollar-weighted vs time-weighted return of vs a 70/30 SPY/QQQ buy-and-hold of the same deposits (needs only our fills).

## Not covered / gaps
Antonacci dual momentum; crowding (e.g. Lou-Polk comomentum); SEC Rule 605 amendments (2024); Knuteson's claims are not peer-reviewed; several numbers marked **figure not verified** above.
