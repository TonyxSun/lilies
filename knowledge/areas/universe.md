# Universe: broad-cap fundamentals screen (News/Fundamentals agent) — 2026-10-22

**Tradability is defined by Trader. I don't define it here.** It lives in `proposals/trader-2026-10-22.md` round 6 (R6-1 "Tradable v1") and `tools/universe_check.py`.
**⚑ It is still PENDING Wuyue's yes.** Small-cap and size-premium evidence is in `areas/universe-small-caps.md` (Trader). This file covers only the fundamentals screen and the candidates it finds.

## Method (tools/universe_screen.py, read-only, no orders)
1. Universe: SEC `company_tickers_exchange.json`, then common stock only, from the Nasdaq screener JSON (price, mcap, sector).
2. Tradability pre-filter: `import universe_check as UC`, using `UC.THRESH` (exchanges, price_min, mcap_min). No thresholds are copied.
   - There's one loose pre-filter on today's partial dollar volume, set to 0.25×`UC.THRESH['adv_min']`. It only saves fetches.
3. Fundamentals come from SEC XBRL **frames**: FY2025 revenue/GP/NI/OCF/capex/diluted shares, latest Assets (CY2026Q2I or Q1I), and Q2/Q1 2026 NI. A recent-filing check follows.
4. Quality filters (mine), applied to non-financials:
   - GP/Assets ≥ 0.10
   - accruals (NI−OCF)/A ≤ 0.10
   - dilution ≤ +5%
   - NI FY25 > 0 and latest quarter NI > 0
   - Composite score ranked within each size bucket.
5. Top 10 per bucket get Trader's full **`UC.check()`**:
   - `UC.edgar()` from live EDGAR, covering filing age, NT filings, 1.03, revenue quarters and going concern.
   - Market dict: 30-day ADV, MAX-21d, 63d vol and herding, from Yahoo daily bars via `UC.ohlcv_stats`.
   - A name with any hard FAIL is dropped, and the next name is pulled in.
   - **H5 spread is left n/a on purpose.** Daily-range estimators (Corwin-Schultz, Abdi-Ranaldo) are volatility-biased and put AAPL at 0.5–2%. A live quote is needed at order time (see Trader's US-005 snapshot). Every survivor's verdict is therefore "INCOMPLETE (n/a rows unchecked)" = passes all hard checks except the spread.

## Sample run, 2026-10-22, ~1:38pm ET (cycles/07-universe-screen-2026-10-22*.tsv)
| stage | mega ≥$200B | large ≥$10B | mid ≥$2B | small ≥$300M | micro | total |
|---|---|---|---|---|---|---|
| listed common | 71 | 783 | 1050 | 1297 | 1839 | 5040 |
| UC price/mcap + prefilter | 70 | 779 | 1031 | 1046 | 0 | 2926 |
| SEC frames fundamentals present | 56 | 610 | 867 | 824 | 0 | 2357 |
| recent filing | 55 | 600 | 856 | 798 | 0 | 2309 |
| quality pass | 37 | 343 | 388 | 275 | 0 | 1043 |
| UC.check on top names: hard FAIL / survivors | 3/10 | 0/10 | 1/10 | 2/10 | – | 5 FAIL / 40 |

- **Quality pass rate falls with size:** mega 67%, large 57%, mid 45%, small 34% (of names with fundamentals present).
- **Same 1043 passes on Trader's NYSE-breakpoint buckets:** large/mid (≥$3.66B) 629, small ($1.19–3.66B) 232, micro band (<$1.19B) 182.
- **Rejected by UC.check:**
  - J2 63d vol >60%: LRCX, AMAT, RNG, LZ
  - H7 NT filings: PNRG (NT 10-Q 2026-05-14, NT 10-K 2026-04-01, NT 10-Q 2025-11-14)
- **Caveats:**
  - 20-F/40-F filers are missing from the frames.
  - GP/A is meaningless for insurers and banks. UNH's 1.28 is suspect, and CACC/WRLD are financials, ranked only on accruals and dilution.
  - Today's-volume pre-filter is partial-day.
  - Point-in-time quality was null in my own backtest (Q-007), so this screen is a **junk veto and idea list, not an alpha signal** (FC-3).

## Candidates passing UC hard checks (top by composite, with notes; sources dated)
Earnings dates come from the Nasdaq calendar (tools/earnings_calendar.py). ES-R5 applies: a hold through the print is a coin flip, so size down.

| bucket (mine / Trader) | name | why it screens | note (source, date) | earnings in window |
|---|---|---|---|---|
| mega / L | META, AAPL, GOOGL, NVDA, WMT, KLAC, ABBV, NFLX, ANET | high GP/A, low accruals, buybacks | already SPY/QQQ heavyweights. Owning them is a tilt, not diversification (BR-001) | AAPL 11/2 AMC, GOOGL 10/28, KLAC 10/28, ABBV 10/30 BMO, ANET 11/3 |
| large / L | ADBE | GP/A 0.94, dilution −5%, FCFy 0.099, P/E ~15 | Wells Fargo cut to Underweight, PT $225, on Oct 12: organic NNARR −40% in Q3 (invezz 2026-10-12). Up ~6% intraday on Oct 22 (stockanalysis 2026-10-22). Value vs. structural-decline debate | none (Dec) |
| large / L | TPR | FY26 revenue $8.0B (+14%), op margin 23.4% | RJ PT cut to $140 (Oct 16), UBS to $200 (Oct 20). Macro/luxury worry (SA 2026-10-05). ~$115 vs. $165 52w high | 11/5 |
| mid / L | DBX | dilution −15.6% (buybacks), FCFy 0.113 | Q2 revenue +0.9%, new $900M buyback, FY26 uFCF ≥$1.07B. Consensus Sell, PT $31.8 vs. $36.6 (stockanalysis 2026-10-21; businesswire 2026-10-15) | 11/5 AMC |
| mid / L | BBWI | FCFy 0.21 | Q3 sales guided −2.5% to −5% on weak traffic. FY EPS raised to $2.60–2.80 with ~$80M tariff refunds. +20.8% over 1 month (Reuters 2026-08-26; stocktitan 2026-10-20) | none (Nov 20s) |
| mid / S | CARG, PGNY, YETI, DV, CRUS, CHE, FTDR, CACC(fin) | quality plus buybacks | not researched individually | most report 10/27–11/6 |
| small / micro | NRDS | GP/A 1.68, FCFy 0.195, cap $0.67B, ADV30 $6.8M | Q2 revenue +6%, NI $4.3M (−48%). Q3 guide +17% YoY. Organic-search pressure (SEC 8-K ex99 2026-08-06; businesswire 2026-10-15) | 11/5 |
| small / S | CMPR | FCFy 0.106 | FY28 EBITDA target ≥$615M (marketbeat 2026-10-03) | 10/28 AMC |
| small / S/micro | SAM, WRLD(fin), GCO, UPWK, CXM, TCMD, KFRC, ZD | quality plus buybacks | SAM reports today AMC. Small names likely hit US-005 spreads of 0.24–0.58% at $300–700M, so H5 is the binding check | various |

**Read:**
- Large/mid names fully pass the mechanical test.
- Small names pass all hard checks, but H5 spread at order is the likely binding constraint.
- Most candidates report inside the Oct 22–Nov 5 window, so ES-R4/R5 apply before any entry.
- Several cheap-on-FCF names (ADBE, DBX, TPR, BBWI) carry sell-side downgrades or demand declines. Quality screens pick "cheap and profitable," which is often "cheap for a reason."

## Testable rules (proposals only)
- **UV-R1:** a single name enters the idea list only if it passes `UC.check` hard rows **and** my quality filters (junk veto). It needs a live spread ≤ `UC.THRESH['spread_max']` at order time.
- **UV-R2:** for a name whose earnings fall in the hold window, apply ES-R5 (size down) and ES-R4 (no dip-buy for 10 sessions after a drop >5%).
- **UV-R3:** rerun weekly. Log counts per bucket so drift in pass rates is visible.

## NC-1 triage of the shortlist (cycle 08, ~1:50pm ET; cycles/08-shortlist-triage.tsv)
I ran 30 non-mega names over 45 days of EDGAR 8-Ks/10-Qs.
- **0 severity-3 veto events.**
- Severity-2 items worth reading before any entry:
  - WRLD 8-K 5.02 (9/21), −7.6% vs SPY on day 1
  - DPZ earnings (10/13), −4.75%
  - HALO 5.02 (9/30), −3.3%
  - BBWI 5.02 (9/23)
  - ADBE 5.02 (9/8): CEO/CFO transition
- CMPR had a +5.7% no-news move (NC-2: avoid chasing). (UV-007)

## Earnings-reaction size by bucket (cycle 08; cycles/08-earn-move-hist.tsv; UV-008, B)
Method: last 8 Item 2.02 8-Ks per name, reaction session from the EDGAR Accepted time, close-to-close excess vs SPY.

Mean |move| by bucket:
- mega: 4.4% (AAPL 2.6%, ABBV 2.2%, ANET 8.6%)
- large: 6.8% (DECK 12.5%, CART 8.5%)
- mid: 6.8% (PGNY 12.4%, DV 10.0%)
- small: 11.4% (TCMD 20.5%, NRDS 17.9%, UPWK 14.3%, KFRC 14.1%)

**Rule UV-R5 (proposal):** before holding any non-mega name through an in-window print, size it so that position × historical mean |move| ≤ ~0.5% of the book. At $1k that is about $45 in an 11%-mover.
This complements Trader's R6-2 caps, and is Trader's call to adopt.

## Junk-veto backtest (tools/junk_veto_test.py; cycles/08-junk-veto-test.txt)
- Setup: SEC frames for FY2018/19/21/22/23/24, same quality filters as the screen. Buy May 1 of Y+1, hold 12 months (Yahoo weekly adjclose). Non-financials only. Survivorship biases the spread downward.
- Pass minus fail, 12-month spread: large+ +9.4% (t 2.33), mid +10.4% (t 2.85), small +9.0% (t 2.57). Pass beats fail in 5 of 6 years in each bucket (UV-009, B).
- Left tail, P(12-month return < -50%): pass 2.4/3.9/7.2% vs fail 18.5/16.2/21.3% (large+/mid/small). Upside tails are similar, so the veto mainly cuts blow-ups (UV-010, B).
- At 10-63 days in large caps the veto shows nothing (Q-007). Its value is at 12 months and as tail-risk control, not as a 2-week alpha source.
- **UV-R4:** apply the quality veto as risk control. In the news sleeve, a veto failure is a blow-up flag rather than an exclusion (Wuyue's steer), with sizing left to Trader.
- News sleeve: see areas/news-smallcaps.md.
