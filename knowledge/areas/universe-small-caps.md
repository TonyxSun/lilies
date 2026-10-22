# Universe: big AND small caps — tradable definition v1 (Trader, round 6, 2026-10-22)

**Steer** (Wuyue, 1:26pm ET): widen the universe to big and small caps. A stock is tradable if we can find enough information to make an informed decision. The "$10B market cap" screen is to be replaced.

**Bottom line (honest):**
- Before 2009, stock-picking signals were much larger in small caps.
- In unbiased CRSP data for 2009-01..2026-08, no long-only small-cap signal beats the market significantly (all t < 1).
- The size premium is negative: −1.2%/yr, t −0.4.
- The robust part is what to **exclude**: small, high-variance, lottery, penny, newly listed and herding names. These lag the market in both periods.
- So widening the universe adds choice, risk and cost. It does not add a proven return.
- The index (SPY/QQQ) stays the default and the yardstick. Data and scripts: `backtests/2026-10-22-size/`.

## 1. Where are edges larger? Evidence

### 1a. Ken French portfolios, split at 2009 (own computation, grade B)

Full tables are in `backtests/2026-10-22-size/README.md`. Units are annual %, t in brackets, shown as pre-2009 → post-2009.

**Long-short spreads are 1.5–20× larger in the smallest NYSE quintile pre-2009:**

| Signal | Small (ME1) | Big (ME5) |
|---|---|---|
| Momentum | 18.98 (t 8.3) | 9.18 |
| Value | 10.71 | 2.61 |
| Investment | 7.36 | 3.62 |
| Low variance | 14.27 | 0.71 |

Post-2009 momentum is ~0 in every size bucket. The only spreads still positive post-2009 are small-cap value 6.08 (t 1.54), investment 4.37 (1.46) and low variance 10.97 (1.79). None is significant.

**Long-only legs vs the VW market** (what a long-only account can capture):
- Small winners: +11.24 (t 5.2) → −1.89 (t −0.6).
- Small value: +7.58 → +2.47 (t 0.6).
- Small low-variance: +5.78 → +1.95 (t 0.7).
- **Small high-variance: −8.49 (t −2.5) → −9.02 (t −1.5).** This is the most stable sign in the data.

**Size premium (VW):**
- Q1−Q5: +3.34%/yr (t 1.46) → −1.22%/yr (t −0.37).
- D1−D10: +3.88 → −2.20.

### 1b. Literature (opened)

- **Asness, Frazzini, Israel, Moskowitz & Pedersen (2018), "Size matters, if you control your junk"**, JFE 129(3):479–509, https://doi.org/10.1016/j.jfineco.2018.05.006. The size premium is weak alone and reappears once you control for quality/junk. **[B]** Implication: small caps are only interesting with a quality screen.
- **Novy-Marx & Velikov (2016), "A Taxonomy of Anomalies and Their Trading Costs"**, RFS 29(1):104–147, https://doi.org/10.1093/rfs/hhv063 (WP https://www.nber.org/system/files/working_papers/w20721/w20721.pdf). **[A for direction]**
  - Low-turnover anomalies (value, profitability, investment) survive costs even in small/micro caps.
  - High-turnover ones do not. Their microcap high-frequency combo goes from 1.77%/mo gross to −0.66%/mo net.
  - Example: Val-MomProf micro/small/large gross 1.67/1.42/1.09%/mo, net 1.27/1.14/0.83.
  - Microcaps are ~60% of firms but ~3% of market cap.
  - A buy/hold spread around a rank threshold is the most effective cost mitigant.
- **Bali, Cakici & Whitelaw (2011), "Maxing out"**, JFE 99(2):427–446, https://doi.org/10.1016/j.jfineco.2010.08.014. Stocks with the highest max daily return in the past month underperform; the low-minus-high MAX decile difference is over 1%/mo. **[A]**
- **Kumar (2009), "Who gambles in the stock market?"**, JF, https://doi.org/10.1111/j.1540-6261.2009.01483.x. Lottery-type stocks (low price, high idiosyncratic volatility, high skewness) underperform. **[B]**
- **Barber, Huang, Odean & Schwarz (2022), "Attention-induced trading and returns: evidence from Robinhood users"**, JF 77(6):3141–3190, https://onlinelibrary.wiley.com/doi/10.1111/jofi.13183. **[B]**
  - Stocks with the most intense Robinhood herding average −4.7% over the next 20 days.
  - Extreme user surges average −19.6%.
  - Robinhood's Top Movers list only includes stocks with market cap above $300M.
- **Loughran & Ritter (1995), "The New Issues Puzzle"**, JF 50(1):23–51, https://doi.org/10.1111/j.1540-6261.1995.tb05166.x. **[B]** (old sample, still standard)
  - IPOs averaged 5%/yr over five years vs 12% for size-matched non-issuers.
  - Seasoned equity offerings (SEOs) averaged 7% vs 15%.
- **Kausar, Taffler & Tan (2009)**, JAR 47(1):213–239, https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1475-679X.2008.00317.x. There is negative drift after first-time going-concern opinions. A later revisit (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2747774) finds the drift fades once you match on financial characteristics. **[B as an exclusion; weak as a short signal]**
- **S&P DJI Indexology blog (2025-07-30), "Quality by design: a deep dive into the S&P SmallCap 600"**, https://www.indexologyblog.com/2025/07/30/quality-by-design-a-deep-dive-into-the-sp-smallcap-600/. **[B/C, vendor research]**
  - The S&P 600 beat the Russell 2000 by ~1.6%/yr since 1994 with lower volatility.
  - Most of the gap (~75%) is attributed to the quality effect of its earnings screen: positive as-reported earnings over the trailing four quarters.
  - So **a profitability gate matters in small caps**.
- **SEC "Penny Stock Rules"** (archived sec.gov/answers/penny.htm, https://web.archive.org/web/20170301041030/http:/www.sec.gov/answers/penny.htm): "a penny stock generally refers to a security issued by a very small company that trades at less than $5 per share." **[A as a convention]**
- **SEC Financial Reporting Manual Topic 1, §1330** (https://www.sec.gov/about/divisions-offices/division-corporation-finance/financial-reporting-manual/frm-topic-1). **[A]**
  - 10-K deadline: 60/75/90 days after fiscal year-end (large accelerated / accelerated / non-accelerated filers).
  - 10-Q deadline: 40/40/45 days after quarter-end.
  - A Form 12b-25 (NT 10-K / NT 10-Q) extension gives up to 15/5 days.

### 1c. Costs at our size (Robinhood read-only quotes, one snapshot ~1:28pm ET, grade C)

At $1,000 an order is tens of dollars, so market impact is nil. The cost is the **quoted spread** (you pay about half on each side).

Snapshot (`spread_snapshot.csv`):

| Market cap | Quoted spread |
|---|---|
| ≥ $10B | 0.01–0.06% |
| $1–6B | 0.11–0.46% |
| $300–700M | 0.24–0.58% |
| < $100M | 0.7–5.5% |

Sub-$100M names have ADV of $0.03–0.4M. Price below $1 and odd statuses also appear there.

Implication: a 0.5% spread cap is roughly where the round-trip cost becomes 2–3× our 0.30% round-trip assumption. Novy-Marx & Velikov say only low-turnover strategies survive there, so **small-cap holdings must be low-turnover** (hold months, not days).

## 2. Mechanical "Tradable v1" definition (replaces "market cap > $10B")

Checker: `python3 tools/universe_check.py SYM ... --market mkt.csv [--ohlcv px.csv]`.
- It uses SEC EDGAR live, plus market data from Robinhood MCP read-only.
- It prints PASS/FAIL/WARN per line, the size bucket and the max weight.
- 牛马's bulk `tools/universe_screen.py` placeholders (TRADER-TBD) can take these constants. Difference to note: they use ADV ≥ $5M; I propose $2M plus the spread cap.

Hard rules (all must PASS):

| # | Rule | Threshold | Why | Grade |
|---|---|---|---|---|
| H1 | Listed common stock on NYSE or Nasdaq; no OTC. NYSE American is excluded for v1. | EDGAR `exchange` field | Listing standards plus SEC reporting; OTC is where penny stocks are generally quoted (SEC). | B |
| H2 | Price ≥ $5 | $5 | SEC penny-stock convention; Kumar's lottery stocks are low-priced. | B (convention); exact level C |
| H3 | Market cap ≥ $300M | ≈ NYSE 5th percentile ($256M, 2026-08) | Spreads blow out below ~$100–300M in our snapshot. Microcaps are ~60% of names but ~3% of cap, where anomaly costs are highest. Robinhood's own Top-Movers cutoff is also $300M. | C |
| H4 | 30-day average dollar volume ≥ $2M | $2M | Protects against stale or gappy quotes. At $1k we are never the volume problem. | C |
| H5 | Quoted spread ≤ 0.50%, re-checked at order time; use limit orders | 0.50% | Keeps the round-trip cost ≤ ~0.5%. | C |
| H6 | Latest 10-K/10-Q filed ≤ 150 days ago | 150 days | Covers the longest normal gap (Q3 10-Q at day 45 → 10-K at day 90 ≈ 137 days). | A (deadlines) / C (buffer) |
| H7 | No NT 10-K / NT 10-Q in the last 12 months | | A late-filing notice is a red flag. | C |
| H8 | ≥ 8 quarters of reported revenue (XBRL) | 8 | Two years of history. It also mechanically excludes IPOs, SPACs and direct listings < ~2 years old (Loughran-Ritter). | B (direction) / C (8) |
| H9 | No bankruptcy 8-K (Item 1.03) in 12 months | | | B |
| P1 | Profitability gate for names < $3.66B (NYSE 40th percentile): positive sum of the last 4 quarters' net income, or positive operating profitability (fundamentals area) | | S&P 600 quality effect; Asness et al. "control your junk". | B |
| J1 | Max daily return over the last 21 sessions < 15% | 15% | MAX effect (Bali et al.). | A (effect) / C (15%) |
| J2 | 63-day realized volatility < 60%/yr | 60% | Small high-variance stocks lag the market by 8–9%/yr in both periods (own Ken French test). | B (effect) / C (60%) |
| J3 | No session in the last 5 with volume ≥ 5× its 30-day average AND abs(return) ≥ 10%; else wait 20 sessions | | Robinhood herding is followed by −4.7% over 20 days (Barber et al.). | B (effect) / C (proxy) |
| W | WARN (read before buying): a "substantial doubt / going concern" text hit in the last 400 days; no earnings-release 8-K (Item 2.02) in the last 135 days | | Going concern often appears as risk-factor boilerplate, so a person must read it. | B/C |

Notes:
- **P1** is not yet automated in `universe_check.py` (Robinhood has no income statement). Check it from EDGAR companyfacts or the fundamentals/quality-screens agents' output.
- The `universe_check.py` demo on 10 names: PLAB, IIIN, CALM, LWAY and UFPT pass the mechanical part. CLFD fails on spread 0.58% and vol 64%. SIGA fails on price $3.14. NTIC, HBIO and CRMT fail cap, ADV and spread (CRMT also MAX/vol). This is NOT a recommendation of any of them.

**Information-sufficiency checklist** (manual; all required before the first buy; logged in the trade rationale):
1. Read the latest 10-K business section and risk factors, and the latest 10-Q MD&A.
2. Read the latest earnings release (8-K Item 2.02) or call transcript.
3. Find at least one independent source (news or analyst) from the last 90 days. Robinhood `get_equity_analyst_ratings` returned **no coverage for PLAB ($1.65B), SIGA or NTIC**, so analyst coverage cannot be a hard rule; news or transcripts must do.
4. Know the next earnings date (Robinhood `get_earnings_calendar` / `get_earnings_results`).
5. Write one paragraph covering the thesis, what would prove it wrong, and why this beats just holding SPY/QQQ.

If any item cannot be done, the stock is not tradable. That is Wuyue's own definition.

## 3. Size and risk adjustments (all judgment, grade C unless noted)

**Max weight per name, by NYSE breakpoint** (update yearly from Ken French ME_Breakpoints):

| Size bucket | Market cap (2026-08) | Max weight |
|---|---|---|
| ≥ NYSE 40th percentile | ≥ $3.66B | 10% (existing) |
| Small, 20th–40th percentile | $1.19–3.66B | 7% |
| Micro band, < 20th percentile | $300M–1.19B | 5% |

Rationale: small-quintile VW volatility is 21.8% vs 14.8% for big, about 1.5× (own computation). Single names are worse.

**Other limits:**
- **Combined names < $3.66B ≤ 20%** of the stock sleeve.
- ≤ 2 names per Robinhood `industry`, with the existing sector cap (3 per sector) kept.
- Small caps are buy-and-hold; minimum intended holding period is 3 months (Novy-Marx & Velikov: only low-turnover survives costs).
- Earnings window: no new buy within 2 trading days before earnings (existing rule, applied to all sizes).
- Size the micro band at half weight into the first earnings report after purchase. This is judgment; there is no direct source.
- Limit orders only, at or inside the mid, for names with spread > 0.10%. This follows the execution-costs area.

**Benchmark honesty:** scoring stays vs SPY and QQQ. IWM (Russell 2000) and IJR (S&P 600) are shown as context only: `python3 tools/scorecard.py --ledger L --context IWM,IJR`. Beating IWM while losing to SPY is a loss.

## 4. Robinhood MCP read-only: what it gives and what it lacks

Checked 2026-10-22.

**What it gives:**
- `get_equity_fundamentals`: market_cap, shares_outstanding, float, average_volume / average_volume_2_weeks / average_volume_30_days, OHLC and volume, 52-week high/low, pe_ratio, pb_ratio, dividend yield, sector, industry, description, CEO, num_employees, year_founded, financial_status_indicator plus description.
- `get_equity_quotes`: bid/ask (spread) and last trade.
- `get_equity_historicals`: OHLCV, from which MAX, volatility and herding can be computed.
- `get_earnings_results` (8 quarters of EPS estimate vs actual, report dates) and `get_earnings_calendar`.
- `get_equity_analyst_ratings`: often null for small caps.
- `search`.

**What it lacks** (fill from SEC EDGAR: `company_tickers_exchange.json`, `data.sec.gov/submissions`, `companyfacts`, full-text search):
- revenue and financial statements;
- audit or going-concern status;
- filing dates and late notices;
- listing exchange;
- IPO date;
- transcripts.

`get_equity_tradability` needs an account number, so it was **not called**. It is off-limits under the read-only/market-data constraint.

EDGAR requires a User-Agent with a contact email. Set `LILIES_SEC_UA`; it returns 403 otherwise.

## Proposed rules

1. ⚑ **Replace "market cap > $10B" with Tradable v1** (H1–H9, P1, J1–J3, WARN read, and the information checklist). Keep the 200DMA part as is, pending rule 11's review. [B/C | changes existing]
2. ⚑ **Size-bucket weight caps**: 10% / 7% / 5%, with names < $3.66B combined ≤ 20% of the stock sleeve, ≤ 2 per industry, small caps held ≥ 3 months. [C | new]
3. **Junk exclusions** apply at every size: penny, MAX, high volatility, herding, recent IPO, late filer, bankruptcy. [A/B effect, C thresholds | new]
4. **Score vs SPY/QQQ only.** IWM/IJR are context, not the bar. [confirms existing]
5. **Default stays the index.** No evidence since 2009 that small-cap picking beats it; the wider universe is optional, not a mandate. [B | confirms A1/A3]


## Appendix (News/Fundamentals agent 牛马, 2026-10-22 ~1:45pm ET): evidence for Trader to fold in. Append-only, no definition changes.
- **Quality pass rate falls with size** (UV-002, B): mega 67%, large 57%, mid 45%, small 34%. Filters are GP/A≥0.10, accruals≤0.10, dilution≤5%, NI>0, SEC frames FY2025. On your NYSE buckets the 1043 passes split 629 / 232 / 182. Supports applying the junk veto harder below $3.66B.
- **P1 (positive trailing-4Q earnings < $3.66B) isn't implemented in `universe_check.check()`.** My screen enforces FY2025 NI>0 and latest-quarter NI>0 as a proxy. You may want a P1 row in the code.
- **H5 spread:** daily-range estimators (Corwin-Schultz, Abdi-Ranaldo) are volatility-biased, putting AAPL at 0.5–2% (UV-006). Your live-quote approach (US-005) is the only usable one. My screen leaves H5 n/a, so every survivor shows "INCOMPLETE".
- **UC.check on my 45 top quality names** (UV-003): J2 is the most frequent hard fail (LRCX, AMAT, RNG, LZ, all >60% 63d vol). H7 caught PNRG with 3 NT filings. No H8 or H9 fails in that set.
- **Coverage gaps:** SEC frames have no 20-F/40-F filers (foreign private issuers), so they fall out of any SEC-based small-cap screen. Also, the Nasdaq screener's volume field is today's partial-day volume, so use 30d ADV from bars.
- **Cycle 91 (US-012, A):** lockup expiries average about -1.5% over 3 days (3x larger if VC-backed; Field & Hanka 2001). For ~1-year-old IPO names, check the 424B4 unlock date before entry. Today's live reads: AVEX LATE; ALMR and EROC negative.
- **Cycle 94 (US-013, B):** recent IPOs (2025-26 smid): median vol 68% (3.2x IWM); P(≤-20% within 10 sessions) is 7.2%; median 10d excess return -0.65%. Size at about 1/3 of a normal satellite weight.
