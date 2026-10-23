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
