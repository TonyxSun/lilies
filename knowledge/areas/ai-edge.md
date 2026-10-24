# AI edge: what an always-on AI can actually exploit (owner Trader; written 2026-10-23 ~12:45am ET)

Question (Wuyue, 10/22 night): as an always-on AI, what real advantages do we have over human traders, and how do we turn them into trades?
Split of work: **literature/sources = 牛马** (areas/ai-edge-sources.md, AS-001..AS-030, plus areas/llm-trading-evidence.md L-001..L-023, areas/x-fast-news.md, areas/news-smallcaps.md). **This file = Trader's tested results** plus a ranking that only uses our own tests and earlier team tests. Literature claims below are pointers, not evidence we produced.

## A. Tested results (our own data, our own code)
New tests tonight: backtests/2026-10-23-ai-edge/ (PREREGISTERED.md frozen 12:39am ET before data was downloaded; backtest.py; results.csv; tables.md). Yahoo daily data through the 10/22 close. Out-of-sample = 2013-2026 (T4: 2016-2026). Pass bar: OOS t >= 2 net of costs, positive, same sign in-sample.

| id | Rule (the "AI advantage" it stands for) | OOS result, net of costs | Verdict |
|---|---|---|---|
| AE-001 | T1 hold SPY/QQQ only overnight (pattern-mining across sessions) | vs buy-and-hold: SPY -0.063%/day (t -4.61) at 0.02%/side; QQQ -0.068%/day (t -3.88). Gross overnight is real (SPY +0.038%/day OOS, t 3.32) but costs and the skipped intraday leg wipe it out | FAIL; also impossible in a cash account (good-faith rule) |
| AE-002 | T2 IBS < 0.2 -> hold 1 day (tireless daily technical scan) | Excess vs an average day: SPY -0.03%/trade (t -0.55), QQQ +0.07% (t 1.05) at 0.05%/side; both negative at 0.15%/side | FAIL |
| AE-003 | T3 RSI(2) < 10 above 200-DMA, exit above 5-DMA (Connors pullback) | SPY +0.25%/trade (t 1.90, n 117, hit 68%) at 0.05%/side; IS was t 3.16, so it decayed. 0.15%/side: t 0.37. QQQ t 1.21 / -0.10 | FAIL (closest miss; watch-list only) |
| AE-004 | T4 cross-asset 12-1 momentum, top 2 of SPY/QQQ/GLD/TLT/IEF/DBC (breadth across asset classes) | Monthly excess vs SPY -0.21% (t -0.62), vs QQQ -0.59% (t -1.41). Full-period CAGR 10.78% vs SPY 10.99% / QQQ 16.15%; maxDD -36% vs -51% / -50% | FAIL on return; real drawdown cut |

Earlier team tests that answer the same question (not redone):
- Faster/early news reading: PEAD on megacaps t 2.0 in-sample, failed robustness (ES-007, ES-011); EARLY-vs-LATE attention read on 3,585 small/mid earnings 8-Ks: EARLY-up -0.19% (t -1.08) (CC-007); gap continuation null (ES-012); guidance raises showed no follow-through live (NS-017).
- Breadth/technical scans: single-stock short-term reversal null (ST-001/002); sector momentum null (SR-006); sector valuation timing null (SR-009); quality screen null (Q-007).
- Macro/event days: FOMC-day trading null (M-023). Oil spike -> buy energy: no (OIL-003, C).
- Only near-miss in the book: SMH after a -5% day, 50d excess vs QQQ +2.03% after costs (t 2.02, PB-004). Meets t≈2 but fails MA-R1 replication (2010+ t 1.37).
- Discipline: trend filter / stops cut drawdowns but don't add return (AG-003, PB-005, M-001/M-008; backtests/2026-10-22-stress).


## A2. Batch 2 tested results (1:13am ET 10/23; backtests/2026-10-23-ai-edge-2/; new bar: OOS t >= 3 at 0.05% AND 0.15% a side; N = 188 preregistered variants, cumulative team trials ~229)
| id | Rule (source that motivated it) | Best OOS cell | Verdict |
|---|---|---|---|
| AE-005 | VIX-conditioned dip buying: RSI(2)<10 or IBS<0.2, VIX > 1y p80 or > 25, exit > 5-DMA or 5 days (Nagel, AS-006) | QQQ IBS<0.2 with VIX>25: +0.80% a trade, t 2.29 (n 76) at 0.05%; t 1.72 at 0.15%. All 4 SPY/QQQ signal pairs do better in stressed regimes than calm ones (direction matches AS-006). IWM doesn't confirm | FAIL (t < 3); direction supports "dips only in stress" |
| AE-006 | Sell-off next-day/3-day hold after a <= -1.5% day (Boyarchenko et al., ai-edge-sources item 2) | OOS t -0.01 to 0.77 at 0.05%, all negative at 0.15% | FAIL (null) |
| AE-007 | GPR top-1%/5% spikes (GPRD/ACT/THREAT) -> SPY/QQQ/GLD/USO 5/20/60-day excess (Caldara-Iacoviello GPR) | 72 cells: OOS t -1.72 to 1.89, 54% positive; every SPY/QQQ cell has |t| < 1.3; best USO 5d after top-1% acts, n 8, t 1.89 | FAIL (null); GPR spike = context, not a trade |

Live at the 10/22 close: VIX 19.03 (1y p80 19.54, 75.8th percentile, so calm regime R0); QQQ -2.86%, IBS 0.19, RSI(2) 17.9 (T2 and calm-regime IBS triggered, both failed rules); SPY and IWM no signal; GPRD 248.7 on 10/19 (97.6th percentile since 1985, a top-5% day). **No Friday candidate.**

- **AE-R5:** Dip/reversal buys (RSI(2), IBS, SMH -5%) can only be scored when VIX > its 1y 80th percentile or > 25 (AE-005, AS-006). In calm regimes they score Evidence 0.
- **AE-R6:** A geopolitical-risk spike (GPR top 5%/1%) isn't a buy or sell signal for SPY/QQQ/GLD/USO (AE-007). It feeds only the existing pre-open geopolitical gate (futures/Brent thresholds).

## B. Ranking of AI advantages (evidence = ours first; literature only as a pointer to 牛马's notes)
| Rank | Advantage | Our evidence | How we'd run it | Cost / capacity at $1k | Status |
|---|---|---|---|---|---|
| 1 | **Discipline: rules and stops followed every time, no panic, no FOMO** | Indirect but solid: trend/stop rules cut max drawdown (T4 -36% vs -51%; AG-003; PB-005). It shows up as lower drawdown, not as excess return | Already live: close-based stops, -2%/-8% breakers, month-end QQQ 200-DMA switch, max 4 signals a day | ~0; no capacity limit | USE (risk control, not alpha) |
| 2 | **Always-on monitoring for big shocks** (geopolitics, Fed, oil) | Event-guard rules come from team tests: oil spike = risk input, not direction (OIL-R2); FOMC day = variance event (M-023) | 牛马 10pm check + 30-minute daytime monitor; act only on gate triggers | ~0 | USE (defensive) |
| 3 | **Low-cost tilts in the core** (e.g. QLD with the 200-DMA switch) | Beta, not skill: AG-002/AG-003 | Core as already planned | ETF spreads ~0.01-0.05% | USE (it's beta) |
| 4 | Mean reversion after sharp index/semis drops (RSI(2), SMH -5%) | AE-003 OOS t 1.90 at tight costs; PB-004 t 2.02; AE-005 best t 2.29 in VIX>25, below the new t>=3 bar; AE-006 null | Watch-list; at most a small bet that scores >=6 under TRADE-SCORING | Needs costs <= ~0.05%/side, so ETFs only, never fractional single names | WATCH, no rule |
| 5 | Reading news/filings faster and more broadly | Our tests: null to negative (CC-007, ES-011, NS-017). Literature (牛马, L-xxx): edges exist but get eaten by costs (L-016) | Use reading for vetoes (ES-R6, NS-R1, junk veto), not for buying on speed | 0.2-0.3% spread on small caps eats it (NS-019) | VETO-ONLY |
| 6 | Breadth scanning of many tickers for technical setups | Nulls: ST, SR-006, T2 IBS, T4 | Don't | — | NO |
| 7 | Session timing (overnight vs intraday) | AE-001: real gross effect, negative net, can't be done in a cash account | Don't; just hold through the night (we already do) | — | NO |
| 8 | Raw headline speed | Not tested. Minute latency loses to HFT and newswire subscribers; see 牛马's literature | Don't | — | NO |

## C. Rules
- **AE-R1:** No new alpha rule tonight. All 4 preregistered tests failed out of sample after costs. Keep the plan as is (core + score >= 6 bets).
- **AE-R2:** Our proven AI advantage is consistency (stops, breakers, gates, checklists), measured as lower drawdown. Don't present it as "beating SPY".
- **AE-R3:** RSI(2) < 10 above the 200-DMA on SPY/QQQ is a watch item only. It can score Evidence 1 (t 1.5-2) under TRADE-SCORING, never 2, unless a forward paper log of >= 20 signals confirms it (CM-001).
- **AE-R4:** Never trade session patterns (overnight/intraday) or daily round trips in. Costs plus the good-faith rule make them strictly worse than holding.

## D. Sources
- Own: backtests/2026-10-23-ai-edge/{PREREGISTERED.md, backtest.py, results.csv, tables.md}; data from Yahoo Finance via yfinance (SPY, QQQ, GLD, TLT, IEF, DBC, ^IRX), pulled 12:39am ET 10/23.
- Rule origins, for context only (no numbers taken from them): overnight/intraday split, Lou, Polk & Skouras, "A tug of war: Overnight versus intraday expected returns," JFE 2019 (https://doi.org/10.1016/j.jfineco.2019.03.011); Cliff, Cooper & Gulen, "Return differences between trading and non-trading hours: Like night and day" (SSRN 2008, https://papers.ssrn.com/abstract=1004081); RSI(2) pullback, Connors & Alvarez, *Short Term Trading Strategies That Work* (2008); time-series momentum, Moskowitz, Ooi & Pedersen, JFE 2012 (T-004).
- Full literature review: areas/ai-edge-sources.md (牛马, AS-001..AS-030), areas/llm-trading-evidence.md.
- Batch 2 data: Caldara & Iacoviello daily GPR, https://www.matteoiacoviello.com/gpr.htm (data_gpr_daily_recent, through 2026-10-19), Yahoo ^VIX/SPY/QQQ/IWM/GLD/USO.
