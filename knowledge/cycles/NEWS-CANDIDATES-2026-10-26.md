# NEWS CANDIDATES for Mon 2026-10-26 (LOTF-RESEARCH-1023)
Written 2026-10-23 ~4:45pm ET by 牛马 (research executor). Facts and evidence only: no scores, no sizing, no orders. Trader scores with TRADE-SCORING.md and owns execution.
Closes: Yahoo daily bars via yfinance, pulled 4:39-4:41pm ET 10/23. Full brief: /workspace/lilies-daily/2026-10-23.md, section "Research: 2026-10-23 收盘研究".

## Pass bar (same as 10/23, written before screening)
(1) dated primary-source catalyst (press release / 8-K) <= 3 sessions old; (2) tools/universe_check.py TRADABLE (v1) or TRADABLE-NEWS (`--profile news`); (3) close above the 200-day (rules.md single-stock rule);
(4) attention read not LATE (HOT 10); (5) no earnings within the next 2 trading days; (6) no gap-chase at the open (HOT 7/11: 10:00am-3:30pm ET marketable limits). Evidence bar: t >= 3 OOS after costs or Evidence <= 1 (TRADE-SCORING.md).

## Base rate (read first)
No single-stock candidate below has a tested edge. Large-cap post-earnings drift is null (NS-001, ES-011); EARLY-attention earnings names returned -0.19% vs IWM, t -1.08, n=1,135 (CC-007).
Geopolitical-risk spikes into SPY/QQQ/GLD/USO: 72 OOS cells, t -1.72..1.89, null (AE-007). VIX 19.45 is below its 1-yr 80th pct (19.54), so dip rules score Evidence 0.

## Market context (10/23 close)
SPY 759.97 (-0.52%), QQQ 704.40 (-0.01%), IWM 275.75 (-0.33%, below 200-day 278.23), SMH 527.20 (+0.74%), RSP -0.77%. VIX/VIX3M 19.45/20.48 = 0.9497 (< 0.95).
10y 5.00%, 2y 4.69% (Treasury CSV 10/23). WTI $103.17 (+3.72%); Brent settled $116.72 (+3.1%) per CNBC/WSJ 3:16pm ET (Yahoo BZ=F 111.48 inconsistent: 暂无可靠数据). Gold $4,011.20 (-1.21%).

## Today's reporters: pre-registered read (tools/read_preregistered.py on cycles/09-catalyst-calendar-2026-10-23_30.tsv, run 4:40pm ET 10/23; 1 session)
| Ticker | 8-K (EDGAR accepted, ET) | Direction from EX-99.1 | Day ret | $vol max / EARLY cap / LATE line ($M) | Pre-reg read | attention_timing.py (4:42pm ET) | Outcome |
|---|---|---|---|---|---|---|---|
| BAH | 0001628280-26-066971, 6:48am 10/23 | Positive: FY27 adj EPS guide raised to $6.50-6.70 (prior $6.00-6.35); revenue guide $11.3-11.6B (prior $11.2-11.7B); Q2 revenue -3.9% y/y; book-to-bill 1.5x | -0.3% | 279.4 / 350.0 / 583.3 | EARLY | LATE (relvol 2.1x, X "Booz Allen" pace 3.5x, StockTwits 32.6x on a tiny base) | SKIP (LATE) |
| BCPC | 0000009326-26-000032, 7:21am 10/23 | Positive: record Q3; sales $290.7M +8.6%; adj EPS $1.57 vs $1.35; no numeric guidance | +2.2% | 108.5 / 132.3 / 220.6 | EARLY | LATE (relvol 2.2x, X pace 3.7x; x_attention 4.29x vs weekday median; vs the pre-registered 25.8/day baseline the pace is 3.3x, under the frozen 5x line) | SKIP (LATE) |
| ALV | 0001193125-26-429404, 6:12am 10/23 | Negative: Q3 EPS $2.13 -6.8%, organic sales -1.1%; FY26 guide ~0% organic | -3.5% | 250.6 / 258.3 / 430.5 | EARLY | not run | SKIP (negative news; below 200-day 118.48) |
| GNTX | 0000355811-26-000060, 8:00am 10/23 | Negative: revenue ~$35M below its own forecast (customer issues, delayed launches) | -5.0% | 90.7 / 175.1 / 291.9 | EARLY | not run | SKIP (negative news; below 200-day 23.19) |
| RITM | n/a | not read | +8.2% | 148.2 / 191.7 / 319.5 | MID | n/a | no entry (MID) |
| FLG | n/a | not read | -9.3% | 251.6 / 207.4 / 345.7 | MID | n/a | no entry (MID) |
AXP (mega, before open 10/23): beat and raised FY26 profit outlook, 3,500 job cuts (X summary, not verified); close 313.22, -3.68%. Not assessed as a candidate.
EDGAR: https://www.sec.gov/Archives/edgar/data/1443646/000162828026066971/ , https://www.sec.gov/Archives/edgar/data/9326/000000932626000032/ , https://www.sec.gov/Archives/edgar/data/1034670/000119312526429404/ , https://www.sec.gov/Archives/edgar/data/355811/000035581126000060/

## Candidates carried to Mon 10/26 (facts only)
| # | Idea | Tested evidence | Catalyst (dated) | 10/23 close / 200-day | Entry range / stop facts | Overlap | Tradable / attention |
|---|---|---|---|---|---|---|---|
| 1 | TXN long | none tested (CC-007, NS-001) | Q3 beat + Q4 guide above est., release 10/21 after close (stale by Mon: 3 sessions) | 284.69 (+1.86%) / 256.76 | 10/22 range >= 276.59; idea stop close < 272.01 | semis on top of QLD | TRADABLE (v1, cycles/news-1026/uc-v1.md); X normal (0.82x, pace 0.55x) |
| 2 | LMT long | none tested (ES-011, NS-001) | beat-and-raise release 10/22 ~7:00am ET (3 sessions Mon) | 604.18 (+2.42%) / 566.29; 5-day +9.4% | above 10/22 range 577.50-601; idea stop close < 551.51 | low; ITA -1.10% | TRADABLE (v1); X 10/22 4.28x (SPIKE flag), 10/23 pace 1.26x; attention_timing QUIET |
| 3 | IWM year-end tilt | PB-003 t 1.97, +1.53% after costs vs 70/30 (below bar) | calendar only | 275.75 / 278.23 (below) | only after a close above the 200-day | low | ETF |
| 4 | BNO / XLE oil leg | AE-007 null; OIL-003 (SPY flat after Brent near-high regimes) | US-Iran escalation, Brent settle $116.72 (+3.1%, CNBC/WSJ 10/23); no filing | BNO 70.99 / 48.78; XLE 69.33 / 58.18 | none tested; roll cost; two-sided weekend gap | hedges core oil risk | ETF |
| 5 | GLD | AE-004, AE-007 (no excess) | none | 366.61 / 414.21 (below) | none | low | ETF |
| 6 | SH (1x inverse) | AG-009 t -3.3 (PSQ after inversion lost), VX-002 | none dated; VIX/VIX3M 0.9497 | 32.66 (+0.62%) | n/a | hedges core | ETF; 2x/3x inverse not allowed |
| 7 | ELV (held) | none tested | 10/21 release + 8-K (stale) | 439.95 (-1.20%) / 371.14 | hold rule: close < 426 or exit by 10/30 close | held 10% | TRADABLE (v1) |
| - | Cash | | | | default (HOT 15) | | |

Earnings within 2 trading days (tools/earnings_calendar.py, Nasdaq calendar, 4:43pm ET): none for TXN, LMT, ELV, BAH, BCPC, XOM, CVX in 10/26-10/29. KO 10/27 BMO, V 10/27 AMC, GEV 10/28 BMO, MSFT/GOOGL/KLAC/NOW 10/28 AMC, AMZN 10/29 AMC. FOMC 10/28 2:00pm; GDP+PCE 10/29 8:30am.

## Files
cycles/news-1026/: market.csv (yfinance 4:41pm ET; spread column = 10/22 regular-hours snapshot because after-hours quotes were unusable), ohlcv.csv, uc-news.md, uc-v1.md, x_counts_2026-10-23.json (x.get_posts_counts_recent, 4:41pm ET), x_attention.txt, attention_timing.txt.

## Missing / not run
Yahoo Brent (BZ=F) inconsistent: 暂无可靠数据. Live spreads: re-check at order time. tools/smallcap_catalysts.py (unscheduled 8-Ks) not run. CNN Fear & Greed, put/call, credit spreads: 暂无可靠数据.
