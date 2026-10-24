# NEWS CANDIDATES for Fri 2026-10-23 (LOTF-PREOPEN-1023-news)
Written 2026-10-22 ~4:02pm ET by research executor. Research only. No orders. All candidates are PAPER-ONLY under rules.md / HOT 10
(news sleeve is paper through 2026-11-05); real money in any of these needs Wuyue to change that rule. Trader owns sizing/execution.

## Pass bar (written before screening)
A name qualifies only if ALL hold: (1) dated primary-source catalyst (press release / 8-K) <= 3 sessions old; (2) tools/universe_check.py
TRADABLE (large) or TRADABLE-NEWS (`--profile news` via smallcap_catalysts scan); (3) close above 200DMA (rules.md single-stock rule);
(4) attention read not LATE (HOT 10 late veto); (5) no earnings within next 2 trading days; (6) entry not a gap-chase at the open (HOT 7, HOT 11: 10:00am-3:30pm ET marketable limits).

## Base rate (read first)
No candidate below has a tested edge. Large-cap post-earnings drift is null in our tests (HOT 7); EARLY-attention news names returned
-0.19% vs IWM, t -1.08, n=1,135 (CC-007). Expected excess return after costs ~0. These are the best *expressions* of today's news, not proven alpha.

## Ranked candidates (prices: Yahoo daily bars, pulled ~4:05pm ET 2026-10-22, close may still settle by cents)
| # | Ticker | Dir | Catalyst (dated source) | Last | Entry condition (Oct 23, after 10:00am ET only) | Stop | Exit / horizon | Main risk |
|---|---|---|---|---|---|---|---|---|
| 1 | LMT | Long | Q3 beat + raised FY26 guide (sales $80-82B, EPS $30.35-30.75), record $292B backlog incl. $52.5B PAC-3; press release 2026-10-22 ~7:00am ET: https://investors.lockheedmartin.com/news-releases/news-release-details/lockheed-martin-reports-third-quarter-2026-financial-results/ . Sector backdrop: RTX raised 10/20 (https://www.rtx.com/news/news-center/2026/10/20/rtx-reports-q3-2026-results), NOC raised 10/20 (https://www.sec.gov/Archives/edgar/data/1133421/000113342126000037/noc-09302026xearningsrelea.htm); Brent at 5-mo high on Iran war reports (Reuters/AP 10/22) | 589.43 (+6.9% d/d; 200DMA 565.74) | Only if price holds >= 577.50 (10/22 low) at 10:00am and is <= 601 (no chase > +2% above 10/22 close) | Idea stop: close < 551.51 (pre-earnings close; gap filled, ~-6.4%). Rules.md hard stop from entry ~589: max(0.8x, entry-5xATR14 14.84) = ~514.6 | Re-evaluate Nov 5 (end of paper window) or stop | Gap-and-fade; large-cap PEAD null; crowded war trade -> de-escalation headline; NDAA stalled in Senate (Yahoo 10/20 1:01pm ET) |
| 2 | ELV | Long | Q3 adj EPS $6.99 vs $4.70 est, FY26 adj EPS raised to >= $29.00 vs $27.24 consensus; release 2026-10-21 before open (~6:00am ET): https://www.elevancehealth.com/newsroom/elv-quarterly-earnings-q3-2026 ; 8-K https://www.sec.gov/Archives/edgar/data/1156039/000115603926000068/elv-20261021.htm . Muted reaction (10/21 -1.4%, 10/22 +2.7%) while defensives bid | 445.64 (52w closing high; 200DMA 370.77) | Only if >= 431.67 (10/22 low) at 10:00am and <= 455 | Idea stop: close < 426 (10/21 low, ~-4.4%). Rules hard stop from entry ~446: ~385 | Nov 5 / stop | Managed-care policy/election headline risk (Medicare Advantage, Medicaid exits); NPAs/"one-time investments"; drift null |
| 3 | TXN | Long | Q3 rev $6.06B vs $5.92B, EPS $2.62 vs $2.42, Q4 guide $5.80-6.30B vs $5.73B est (LSEG via Reuters); release 2026-10-21 ~3:00pm CT after close: https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-10-21-ti-reports-third-quarter-2026-financial-results-and-shareholder-returns.html . Price fell -1.8% on 10/22 as SOX fell ~6% (no positive reaction = EARLY type) | 279.50 (200DMA 256.26) | Only if SMH is not down > 2% at 10:00am AND TXN >= 276.59 (10/22 low) | Idea stop: close < 272.01 (10/20 low, ~-2.7%). Rules hard stop: ~233 | Nov 5 / stop | It is a semi: AI-capex unwind (META capex, Huang "AI capital scarce", 10/22) drags it regardless of fundamentals; MSFT/GOOGL 10/28 read-through |
| 4 | R (Ryder) | Long, conditional | Q3 comparable EPS $4.33 vs $4.15, FY26 guide raised to $14.85-15.05 from $14.40-14.80; release 2026-10-22 ~6:55am ET: https://www.businesswire.com/news/home/20261022983731/en/Ryder-Reports-Third-Quarter-2026-Results | 265.45 (+10.5%; 200DMA 235.01) | Pullback-only: buy only if it trades <= 258 (about half the gap) after 10:00am and holds > 250.54 (10/22 low). Do NOT buy at open (HOT 7) | Idea stop: close < 250.54 (~-3% from 258) | Nov 5 / stop | Already +10.5% in one day (MID read); gap-fill; freight-cycle data |

UC evidence: LMT, ELV, TXN TRADABLE (mechanical) via tools/universe_check.py, SEC EDGAR live + market data ~3:52pm and ~4:00pm ET 10/22
(cycles/news-1023/uc-large-v1.md, uc-large-v1-b.md). R: TRADABLE-NEWS in scan cycles/NEWS-scan-2026-10-22-1550.tsv (`--profile news` mode, spread 0.12%).
200DMA/ATR14: yfinance 2y daily, run ~4:01pm ET 10/22. Next earnings for all four: not within 2 trading days (all just reported).
Attention (X recent counts, UTC days, pulled ~4:00pm ET): LMT today 5,509 vs ~3,220/day prior 6 days (1.7x, not LATE); TXN 1,222 vs ~1,374 (no spike);
ELV 914 vs ~1,130 (no spike); R 24 vs ~0 (tiny base, uninformative).

## Considered and dropped (with reason)
- NOC, RTX, ITA: catalysts real (raises 10/20) but closes below 200DMA (NOC 552.75 vs 592.83; RTX 194.46 vs 195.16; ITA 204.45 vs 229.69) -> fail rules.md.
- BX: below 200DMA (118.39 vs 125.28). IONS (FDA approval 8-K 10/21), WFRD, COCO, WH, VMI, SUPN, CASH: below 200DMA.
- PG (+5.6%), CSX (+6.8%), ROP (+9.7%): TRADABLE and above 200DMA but pure gap-up beat names -> HOT 7 no-chase; no pullback level I'd defend. Watch-list only.
- EGBN (+15.6%): beat was from lower credit provisions; NPAs rose $52.9M to $166M, PPNR fell, revenue missed (company release 10/21) -> low-quality beat, relvol 3.8x.
- HCSG (+14.2%): >= 8% move, not EARLY.
- LEN: news credited Berkshire buying, but the Form 4s are Oct 1-2 (stale); today's +7.9% is a rates/housing move.
- SPOT: universe_check NOT TRADABLE (foreign filer, H6/H8).
- MANE, EQPT, FRNM: LATE / NOT TRADABLE in scan.
- After-close 10/22 reporters (WDC, NEM, FIX, BE, VRSN, OMC, SSNC) and before-open 10/23 (AXP, SLB, BAH, etc.): NOT assessed -- releases came out after this was written; any gap there is a HOT 7 no-chase anyway.

## Small caps: honest null
The `--profile news` scan (51 events, 10/18-10/22) produced no small cap that passes all six bars: the TRADABLE-NEWS small caps with positive
news are either below 200DMA, already up >= 8%, or have a low-quality catalyst. Small-cap news slot is EMPTY for Oct 23.


---
## Research: 2026-10-22 收盘研究 (牛马, written ~4:50pm ET; LOTF-RESEARCH-1022)
Ideas only, no orders. Scores use TRADE-SCORING.md (Evidence 0-3, Edge 0-1, Catalyst 0-2, Setup 0-2, Risk/fit 0-2; take only >= 6; 0 on Setup = skip). Trader owns live prices, settled cash, sizing, order types and stops and does not re-score. Setup scores are provisional until the ~7:37am ET pre-market re-score (no open-gap data yet).

**Market state:** risk-off "Black Thursday": AI-capex doubts after META/TSLA plus Iran/oil headlines hit tech and semis hard, while defensives, health care and small caps held up; bonds rallied.

### Index moves (close 2026-10-22; Yahoo Finance daily closes via yfinance, pulled 4:37pm ET)
| | Close | Day | vs 200-day avg (unadjusted closes) |
|---|---|---|---|
| SPY | 763.96 | -1.18% | above (726.65) |
| QQQ | 704.47 | -2.86% | above (676.89) |
| IWM | 276.67 | +0.07% | **below** (278.13; Trader's adjusted figure 277.06) |
| SMH | 523.35 | -5.99% | above (514.73) |
| VIX | 19.03 | +14.1% | |
| RSP (equal weight S&P) | 218.22 | +0.73% | breadth was far better than the cap-weighted index |

**VIX/VIX3M at the close: 19.03 / 20.12 = 0.946, below 0.95** (Yahoo ^VIX and ^VIX3M daily closes via yfinance, pulled 4:37pm ET 10/22). Close to the line; per VX-002 a reading >= 0.95 is not a bearish signal anyway (it preceded slightly higher SPY), and AG-009 found PSQ after a ratio >= 1 lost.

### Rates, dollar, oil, gold
- 2-year Treasury 4.65% (-16 bp from 4.81%), 10-year 4.96% (-17 bp from 5.13%); US Treasury daily par yield curve, 10/22/2026 row, read 4:40pm ET.
- Dollar index (DX-Y.NYB) 101.65, -0.13% (Yahoo via yfinance, 4:37pm ET).
- WTI (CL=F) $99.10, +2.0%; Brent (BZ=F) $112.80, +3.7% (Yahoo front-month futures via yfinance, 4:37pm ET; Brent near its 1-year high per OIL-001).
- Gold (GC=F) $4,037.70, -2.7% (same source).

### Sectors (SPDR sector ETFs, day change, Yahoo via yfinance 4:37pm ET)
- Leaders: staples XLP +3.31%, utilities XLU +2.07%, health care XLV +1.32%, financials XLF +1.09%, real estate XLRE +1.09%.
- Laggards: semis SMH -5.99%, tech XLK -3.29%, communications XLC -1.42%, industrials XLI -0.94%, energy XLE -0.87% (despite oil up). Defense ITA -0.64% (LMT +6.96% on earnings).

### X trend and sentiment (X news summaries, updated 2026-10-22 13:34-20:35 UTC; these are Grok summaries of posts, not verified data)
- Dominant story is "Black Thursday": global selloff tied to Trump saying the US is not negotiating with Iran, Brent above $113, AI-spend doubts after META/TSLA, and China's CSI 300 entering a bear market. The summary cites CNN Fear & Greed near 20 (extreme fear); 暂无可靠数据 from CNN itself.
- Retail pain in leveraged semis: SOXL about -19% after a record ~$3.8B weekly inflow (X summary). Crypto: BTC below $81k.
- SPY traders are watching the 760 put wall; views split between "buy zone above 758" and a head-and-shoulders toward 755.
- Read: fear is elevated but not panic (VIX 19, ratio under 0.95). Sentiment is a context note, not a trade signal (HOT 6).

### Catalysts, next 1-3 trading days (areas/catalyst-calendar.md; macro from the same file)
- Fri 10/23: AXP before the open (S&P core name). Sleeve reporters BAH, ALV, BCPC, RITM, FLG, GNTX before the open; the pre-registered read runs after the 10/23 close.
- Tonight after the close (10/22): WDC, NEM, FIX, BE, VRSN, OMC, SSNC reported; not assessed here. Any gap tomorrow is a no-chase under HOT 7.
- Mon 10/26 after the close: BRX, SSD, ARE, NE, PSMT, PECO. Tue 10/27: KO, NVS before the open, V after the close.
- Coming week: FOMC Wed 10/28 2:00pm; MSFT and GOOGL 10/28 after the close; AMZN 10/29 after the close; GDP and PCE Thu 10/29 8:30am; AAPL 11/2.
- Watchlist names LMT, ELV, TXN and R all just reported, so none has earnings within 2 trading days.

### Key risks
- Middle East escalation and oil: Brent $112.80 and rising feeds inflation fears; a de-escalation headline would instead hit the war trade (LMT).
- AI-capex unwind: semis -6% in a day with the hyperscaler prints (MSFT/GOOGL/AMZN) and FOMC all inside the next week. The planned core is QQQ-heavy (QLD), so this is the main book risk.
- Breadth split: cap-weighted SPY -1.2% while equal-weight RSP +0.7%; leadership is rotating, which hurts QQQ-tilted books.
- Leveraged-ETF path risk for QLD (VXN 29.17 on 10/22 per PREOPEN).

### Scored candidates (ranked; ideas only)
| Rank | Idea | Evid | Edge | Cat | Setup | Risk | Total | Call | Entry range (after 10:00am ET) | Stop | One-line reason | Evidence row |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ELV long | 0 | 0 | 2 | 2 | 2 | **6** | TAKE (borderline) | 431.67-455 (close 445.28) | close < 426 | Big beat + FY26 raise to >= $29 on 10/21 with a muted reaction; above 200-day; ~0.43% of account at risk; no tested edge | CC-007 (EARLY-type null), ES-011; release + 8-K in NEWS-CANDIDATES |
| 2 | SMH after a -6% day | 2 | 1 | 1 | 2 | 0 | **6** | TAKE (borderline) | buy near the 10/23 close only if >= 507.65 (0.97 x 523.35) | close > 12% below entry | Tested t 2.02, +2.03% vs QQQ over 50 days after costs, but 2010+ t 1.37 and it adds more semis to a QQQ-heavy core; 12% stop on 10% = 1.2% risk | PB-004, DD-004 |
| 3 | LMT long | 0 | 0 | 1 | 2 | 2 | 5 | SKIP | 577.50-601 (close 589.91) | close < 551.51 | Real beat-and-raise 10/22, but +7% gap already priced it; large-cap drift is null | ES-011, NS-001 |
| 4 | TXN long | 0 | 0 | 2 | 2 | 1 | 5 | SKIP | >= 276.59 and SMH not down > 2% at 10:00am (close 279.50) | close < 272.01 | Beat + Q4 guide above estimates, but it is semi beta stacked on a QQQ-heavy core | CC-007 |
| 5 | IWM year-end tilt | 2 | 1 | 0 | 0 | 2 | 5 | SKIP | only once IWM closes above its 200-day | IWM close < 200-day | Setup 0: closed 276.67, just under its 200-day; revisit daily through 10/30 | PB-003 |
| 6 | R (Ryder) pullback | 0 | 0 | 1 | 0 | 2 | 3 | SKIP | <= 258, holding > 250.54 | close < 250.54 | Setup 0: closed 265.53, above the pullback range after +10.5% | CC-007 |
| 7 | PSQ / SH (bearish) | 0 | 0 | 0 | 1 | 2 | 3 | SKIP | n/a | n/a | No dated bearish filing; tested triggers lost vs cash | AG-009, AG-008, VX-002 |
| - | Cash | | | | | | | default | | | Any slot without a passing idea stays in cash | HOT 15 |

Scoring notes: Risk for SMH uses the planned $100 (10%) size; at a smaller size the risk score could rise. LMT's Catalyst is 1, not 2, because the +6.96% day priced much of it ("dated but partly priced"). Setup 2 for ELV, LMT, TXN and SMH assumes no >3% gap at Friday's open and must be re-checked pre-market. Tradable checks: LMT, ELV and TXN TRADABLE via tools/universe_check.py, R TRADABLE-NEWS via `--profile news` (cycles/news-1023/uc-large-v1*.md, NEWS-scan-2026-10-22-1550.tsv, run 3:50-4:00pm ET 10/22); no new small-cap news name passed today. X attention (pulled ~4:00pm ET): LMT 1.7x baseline, TXN and ELV no spike; none LATE.

**Differs from the 4:16pm order plan:** Trader's plan includes LMT; it scores 5 here, so it is a SKIP under the rubric. ELV and SMH clear 6 only at the threshold. News trades still have no tested edge (CC-007).

---
## Pre-open addendum 2026-10-23 (牛马, written ~7:40-7:55am ET; LOTF-PREOPEN-1023-addendum)
Facts only. No orders, no scores, rules.md not touched. Trader scores with TRADE-SCORING.md and places orders.
Times are ET. Robinhood = Robinhood MCP get_equity_quotes, pulled 7:41am ET (venue timestamps converted from UTC). Yahoo = Yahoo chart API, pulled ~7:42am ET.

### Overnight market (vs 10/22 close / settle)
| Item | Pre-market | Change | Source, time |
|---|---|---|---|
| S&P 500 futures (ES=F) | 7,682.50 | -0.29% (settle 7,704.50) | Yahoo, 7:31am |
| Nasdaq-100 futures (NQ=F) | 29,091.25 | -0.17% (29,142.00) | Yahoo, 7:31am |
| Dow futures (YM=F) | 52,743 | -0.61% (53,068) | Yahoo, 7:31am |
| Russell 2000 futures (RTY=F) | 2,779.1 | -0.61% (2,796.1) | Yahoo, 7:31am |
| SPY | 762.04 (bid/ask 762.10/762.17) | -0.25% (close 763.96) | Robinhood, 7:41am |
| QQQ | 704.06 (704.08/704.13) | -0.06% (704.47) | Robinhood, 7:41am |
| VIX | 19.62 | +3.1% (19.03) | Yahoo, 7:26am |
| VXN | missing overnight; last 28.72 | n/a | Yahoo, last print 10/22 4:15pm |
| VIX3M | missing overnight; last 20.12 | n/a | Yahoo, 10/22 4:15pm |
| WTI (CL=F) | $100.98 | +1.5% ($99.47) | Yahoo, 7:31am |
| Brent | Yahoo BZ=F $109.98, +1.2% vs $108.66 settle (looks like a rolled contract; yesterday's file had $112.80). Dec Brent "topped $114", +1.1% at 6:00am per Stocktwits/Yahoo article; CBS says $114 | ~+1% | Yahoo 7:31am; [Stocktwits 6:13am](https://stocktwits.com/news-articles/markets/equity/nasdaq-dow-s-and-p-500-futures-drop-premarket-nvda-amd-meta-crwv-mrna-wdc-be-in-focus/cZxyfNARBxI) |
| Gold (GC=F) | $4,038.30 | -0.5% ($4,060.40) | Yahoo, 7:31am |
| 10-year yield | missing overnight; ^TNX last 4.953% (10/22 close; Treasury par 4.96%) | n/a | Yahoo, 10/22 2:59pm |
| Dollar index | 101.81 | +0.2% (101.61) | Yahoo, 7:31am |

**Geopolitical gate inputs (TRADE-SCORING.md):** futures down 0.17-0.61% (not >= 1.5%); Brent up ~1% (not >= 5%). The gate's price legs are not met as of 7:31am ET.

### Order-plan facts (Trader's 6:45pm plan + 1:20am update; SMH dip buy was DROPPED at 1:20am)
| Ticker | Pre-market (Robinhood) | vs 10/22 close | Entry range / condition | Inside? | Evidence (t, after-cost edge, INDEX row) | Dated catalyst | Stop and distance |
|---|---|---|---|---|---|---|---|
| QLD (core) | 86.03 last 7:39am; bid/ask 86.09/86.11 7:41am | -0.27% (86.26) | Limit <= live ask + 0.1%, 10:00-15:30 | n/a (core) | Core, not scored; AG-002/AG-003 for reference | none | Close >= 15% below average entry; no entry yet. QQQ 200-day 676.89 (unadj): QQQ pre-market 704.06 is 4.0% above it |
| SPYM (core) | 89.68 last 7:31am; 89.69/89.71 7:41am | -0.28% (89.93) | Limit <= live ask + 0.1% | n/a (core) | Core, not scored | none | No single stop (account limits only) |
| ELV | No pre-market trade. Last print 445.30 at 9:37pm 10/22; bid/ask 396.90/449.70 at 6:43am (too wide to use) | 0.00% on last print (445.28) | 431.67-455 | Yes on last print; recheck after 10:00am | none tested (base rate CC-007 t -1.08; ES-011 drift null) | Q3 beat + FY26 raise, release and 8-K 2026-10-21 (2 sessions old today) | Close < 426: 4.3% below 445.30. Time stop 5 trading days |
| SMH (dropped) | 526.00 last 7:40am; 525.59/526.48 | +0.51% (523.35) | Guard >= 507.47 | Yes, 3.65% above guard | PB-004/DD-004: t 2.02, +2.03% vs QQQ over 50d after costs (below the t >= 3 bar; VIX 19.62 < 25, so not a stressed regime under the dip rule) | none dated (10/22 -6% day) | Close > 12% below entry; no entry |
| LMT (ref) | 586.00 last 7:26am; 585.02/587.25 7:41am | -0.66% (589.91) | 577.50-601 | Yes | none tested (ES-011, NS-001 null) | Q3 beat + FY26 raise, release 2026-10-22 ~7:00am | Close < 551.51: 5.9% below 586.00 |
| IWM (ref) | 275.19 last 7:41am; 275.18/275.23 | -0.54% (276.67) | Only once it closes above its 200-day 277.06 (adj) | **No**, 0.67% below | PB-003: t 1.97, +1.53% after 0.30% round trip | none | Close < 200-day |
| TXN (ref) | 280.00 last 5:31am; 277.00/279.94 7:29am (wide) | +0.18% (279.50) | >= 276.59 and SMH not down > 2% at 10:00am | Yes on last print; SMH condition checked at 10:00am | none tested (CC-007) | Q3 beat + Q4 guide, release 2026-10-21 after close | Close < 272.01: 2.9% below 280.00 |
| R (ref) | 265.96 last 10:30pm 10/22 (stale); 228.00/280.00 (unusable) | +0.16% (265.53) | <= 258, holding > 250.54 | **No**, above 258 | none tested (CC-007) | Q3 beat + FY raise, release 2026-10-22 ~6:55am | Close < 250.54: 5.8% below 265.96 |
No open gap above 3% in any plan name as of 7:41am ET.

### News screen: last night's and this morning's reporters
Checks: (1) dated release/filing; (2) universe_check.py; (3) above 200-day; (4) not LATE attention; (5) no earnings in 2 days (all just reported, pass); (6) no gap chase.
universe_check.py ran 7:45am ET without --market data, so every name is INCOMPLETE: EDGAR checks H1, H6-H9 pass for all ten; price, cap, volume and spread rows are unchecked (cycles/preopen-1023/addendum/uc-reporters.md). X attention: not pulled (missing).
200-day = simple average of the last 200 unadjusted Yahoo daily closes, pulled 7:44am ET.
| Ticker | Catalyst (dated) | Pre-market (Robinhood) | 10/22 close vs 200-day | Result |
|---|---|---|---|---|
| WDC | Beat + upbeat outlook, 10/22 after close (CNBC after-hours movers 10/22) | 338.48 at 7:40am, -4.4% | 354.19 vs 413.93, below | FAIL (below 200-day) |
| NEM | Q3 results; warned 2027 unit costs trend higher (Reuters via Investing.com 6:45am) | 112.48 at 7:40am, -1.4% | 114.11 vs 112.45, above; pre-market near the line | FAIL (negative guide, no long case) |
| FIX | Beat, 10/22 after close; fell ~5% after hours | 1,239.94 at 7:22am, -3.1% | 1,279.37 vs 1,598.49, below | FAIL (below 200-day) |
| BE | Raised FY26 forecast, 10/22 after close | 210.79 at 7:41am, -3.2% | 217.77 vs 218.86, below | FAIL (below 200-day) |
| VRSN | EPS miss, [release 10/22](https://verisigninc.gcs-web.com/news-releases/news-release-details/verisign-reports-third-quarter-2026-results/) | 293.10 at 12:40am, -3.8% (stale) | 304.59 vs 269.89, above | FAIL (miss, no long case) |
| OMC | Adjusted EPS beat, 10/22 after close | 84.20 at 1:14am, +2.0% (stale; bid/ask 82.56/88.00) | 82.56 vs 78.17, above | No usable pre-market price; any gap is a no-chase. Watch only |
| SSNC | Small EPS beat + raised guide, 10/22 after close; fell ~5% after hours | 86.44 at 1:34am, -3.5% (stale) | 89.54 vs 74.38, above | Negative reaction to a beat; no setup defined. Watch only |
| AXP | Q3 EPS $5.42 GAAP / $4.68 adj, FY26 guide raised; revenue $20.06B vs $20.12B est; [8-K 10/23](https://www.stocktitan.net/sec-filings/AXP/8-k-american-express-co-reports-material-event-703db95903db.html) | 319.86 at 7:38am, -1.6% | 325.17 vs 327.62, below | FAIL (below 200-day) |
| SLB | Adj EPS $0.64 vs $0.62, revenue $9.45B vs $9.27B ([Investing.com 7:05am](https://www.investing.com/news/earnings/slb-tops-q3-expectations-on-broadbased-growth-4968919)) | 49.56 at 7:33am, +0.0% | 49.55 vs 51.20, below | FAIL (below 200-day) |
| BAH | Q2 FY27 adj EPS $1.76 (+18%), revenue $2.8B (-3.9%, below est), adj EPS guide raised; [release 10/23](https://mms.businesswire.com/media/20261023552576/en/2944636/1/BAH_Exhibit_991_Q2_FY27.pdf) | 80.50 at 7:35am, +2.5% | 78.57 vs 76.88, above | Passes 1, 3, 5; 2 incomplete; 4 missing; +2.5% gap is a no-chase at the open. Watch only, not a new candidate |
**New candidates: none.** Nothing passed all six checks.

### Geopolitics and policy (overnight)
- **Iran / Hormuz:** IRGC says 7 tankers were hit or mined overnight 10/22-10/23 (4 set on fire, 3 mines), the most in one day since the war began Feb 28; not independently verified; CENTCOM says lanes are cleared and 95% of vessels cross ([AP](https://apnews.com/article/mideast-yemen-saudi-israel-october-22-2026-dde5b98a8bf961224514994b02babce9), [Al Jazeera 10/22](https://www.aljazeera.com/news/2026/10/22/iran-says-seven-ships-hit-in-hormuz-strait-warns-us-of-wider-response)). IRGC warned it could hit US bases in the region. UAE reported a tanker oil spill off Umm Al Quwain on Fri. US UN ambassador Waltz told the FT the war could last another year ([CBS live, updated 7:18am](https://www.cbsnews.com/live-updates/iran-war-trump-us-oil-gas-prices-strait-of-hormuz-midterms/)). WSJ-reported: US and Israel weighing fresh strikes on Iran after the November midterms (via Stocktwits 6:13am). Aramco's bypass pipeline flow rose to 7M bpd. IMO count: 120 confirmed incidents as of 10/22. **Affects:** QLD and SPYM (oil and inflation into FOMC 10/28), LMT (war trade, supports it; de-escalation is the risk), USO/BNO if anyone looks at them.
- **Chip export controls:** DigiTimes (10/23) reports 32 Nvidia B300 GPUs seen on China Telecom-linked endpoints, raising enforcement questions ([DigiTimes](https://www.digitimes.com/news/a20261023VL220/nvidia-chips-security-blackwell-china-telecom.html)). BIS Affiliates Rule suspension ends Nov 9 and the rule returns Nov 10 unless BIS acts (Boston Report 10/22). No new rule found overnight. **Affects:** SMH, TXN, QLD (Nvidia weight).
- **AI/semis premarket:** NVDA +0.4%, AMD ~+1%, META -0.6%, CRWV +2% at ~6:00am after Thursday's selloff (Stocktwits 6:13am). **Affects:** QLD, SMH.
- **Telecoms:** T, VZ, TMUS down >3% premarket on a report that SpaceX is talking to tower firms about a wireless carrier; CCI +8.5%, AMT +5.6% ([Reuters via Investing.com 6:45am](https://www.investing.com/news/stock-market-news/wall-street-futures-dip-after-ai-rout-telecoms-slide-4968816)). **Affects:** SPYM slightly.
- **Tariffs, sanctions, other wars:** no new overnight item found in my searches (missing, not confirmed absent).

### What changed vs last night
- Nothing in the plan broke overnight. ELV, LMT, TXN still inside their ranges on last prints (ELV and TXN prints are thin/stale). IWM still below its 200-day (275.19 vs 277.06). R still above its pullback range. SMH holds its guard but was already dropped.
- Geopolitical risk is higher in tone (tanker claims, threat to US bases, strike planning reports) but the gate's price legs are not met.
