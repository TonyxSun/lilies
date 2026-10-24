# X fast news: paper experiment (pre-registered)

Owner: 牛马 (X watch, logger, pre-registration). Trader owns scoring (`tools/xfast_score.py`), sizing and exits.
**PAPER ONLY.** No orders, no posts. Nothing here changes rules.md.
Pre-registered 2026-10-22 at about 3:50pm ET, **before any non-dry-run data**. INDEX row: XF-001.
Any change to the parameters below needs a new dated plan row (XF-00n). Data logged before that change keeps the old rules.

## Why
Wuyue (10/22): "if you are a fast reactor to news (ie. x) i believe you should be able to take advantage of things."
CC-007 found no edge at **daily** granularity **after official releases** (3,585 earnings 8-Ks). That test does not cover catching a story on X *before* the newswire or 8-K. S-025 also left the X leg untested. This experiment tests that gap forward, on paper.

PASS_BAR: variant=delay30m horizon=1d bench=BLEND7030 min_n=40 min_t=2.0 min_median=0 kind=catalyst
PASS_BAR: variant=delay30m horizon=1d bench=BLEND7030 min_n=40 min_t=2.0 min_median=0 kind=trend
PASS_BAR: variant=delay30m horizon=1d bench=BLEND7030 min_n=40 min_t=2.0 min_median=0 kind=sentiment

## Test 1: X-first catalysts (kind=catalyst)
**Hypothesis:** for a bullish catalyst on a small or mid cap first seen on X, with no newswire or 8-K yet, buying at the ask beats the benchmark after costs.

- **Universe.** NYSE/Nasdaq, market cap $300M–$10B (Nasdaq screener). It must pass Trader's `universe_check.py --profile news` at first-seen time, using a live Nasdaq bid/ask for H5.
- **Catalyst keywords.** These are regexes in `CAT` in `tools/xfast_log.py`; the first match wins.
  - Bullish: `fda_approval`, `acquisition` (merger, definitive agreement, to acquire, takeover), `contract` (award, wins or secures a contract or order), `guidance_raise`, `buyback`.
  - Bearish (secondary): `fda_crl`, `offering` (public, priced, registered direct, ATM, dilution, private placement).
  - Mixed: `ceo_change`. Logged but not scored.
- **Accounts that count.**
  - *wire_list:* @DeItaone, @FirstSquawk, @LiveSquawk, @financialjuice, @StockMKTNewz, @unusual_whales, @Benzinga, @eWhispers, @BioStocks. All were verified via X lookup on 10/22.
  - *Any verified account* posting a cashtag, recorded as account_class `company_handle` or `verified_other`. Unverified accounts are not searched.
  - Wire posts without a cashtag are matched only on an exact normalized company name from the sleeve universe.
  - Results are reported by account_class. The primary test pools all classes.
- **Spam filter.** Drop posts with more than 3 cashtags. Drop crypto, token, WhatsApp, Telegram and similar words (the `SPAM` regex).
- **Dedupe.** Log only the first post per (ticker, catalyst) in 7 calendar days.
- **"Fast" definition.**
  - first_seen = the time the routine fetched the post (the mtime of the saved X response).
  - The post must be ≤ 20 min old at first_seen.
  - first_seen must fall 9:40am–3:50pm ET on a trading day.
- **X-first.**
  - At first_seen, look for any 8-K/6-K accepted on EDGAR in the prior 48h (`acceptanceDateTime`, UTC converted to ET).
  - Also look for a newswire or news headline for the ticker in the prior 24h (Yahoo Finance news, `providerPublishTime`). A headline that matches the catalyst wins.
  - If either exists, the event is the **wire-first control group** and goes to `candidates_rejected.csv`.
  - For X-first events, `followups.csv` re-checks 2–30h later for a wire or 8-K that came *after* first_seen. That is the confirmed X lead.
- **Entry and costs (scored by Trader's scorer).**
  - Entry is at the first bar ≥ first_seen + 30 min, the approval-delay assumption (primary). A no-delay variant is also scored.
  - Entry is confined to 10:00–15:30 ET.
  - Cost per side = max(observed half-spread, 0.15%). My earlier "ask + 0.1%" reference is kept in `entry_ref_ask_plus10bp` for information. The scorer's cost model is the one used.
- **Horizons:** +1h, +1 trading-day close, +5 trading-day close.
- **Benchmarks:** IWM, QQQ and the 70/30 SPY/QQQ blend (BLEND7030) over the same window.
- **Pass bar (primary).** Variant delay30m, horizon 1d, vs BLEND7030.
  - It needs n ≥ 40 scored X-first bullish events.
  - Mean excess > 0 with t ≥ 2.0, and median excess > 0 (check the median by hand from the scorer table).
  - It's evaluated after about 4 weeks (around 2026-11-19), or as soon as n ≥ 40 after that.
- **Otherwise drop it.** If n < 40 after 4 weeks, report "insufficient", extend once by 4 weeks, then drop.
- **Secondary (not pass criteria):** the other horizons, IWM and QQQ, the no-delay variant, the wire-first control (`--events xfast/candidates_rejected.csv`), and bearish rows (do they fall?).

## Test 2: X trends and sentiment swings (kind=trend | sentiment)
**Hypothesis:** a trend or sentiment swing on X leads the direction of IWM, QQQ, a sector ETF or the named ticker at +1h, +1d and +5d, after costs.

- **Mention rate (velocity).** Counts come from `get_posts_counts_recent` at hourly granularity over the last 7 days.
  - Current = this hour's count scaled to 60 min if at least 20 min have elapsed, otherwise the last full hour.
  - Baseline = median of the same ET hour on up to 5 prior weekdays. This removes the time-of-day bias noted in S-024.
  - `mention_rate_vs_usual` = current / baseline.
  - **Trending bar: ≥ 3.0×.**
- **Scopes and targets (frozen):**

| Scope / name | X query (core) | target_type | target |
|---|---|---|---|
| market | "stock market", stocks, SPY, QQQ, IWM, "S&P 500", Nasdaq | index | SPY |
| semis_ai | semiconductor(s), semis, "chip stocks", SMH, "AI stocks" | sector_etf | SMH |
| biotech | biotech, XBI, "FDA approval" | sector_etf | XBI |
| small_caps | "small caps", "small-cap", "Russell 2000", IWM | index | IWM |
| rates_fed | FOMC, Powell, "rate cut/hike", "treasury yields", "10-year yield" | index | QQQ |
| energy_oil | "oil prices", "crude oil", OPEC, XLE, "energy stocks" | sector_etf | XLE |
| regional_banks | "regional banks", "bank stocks", KRE, "bank failure" | sector_etf | KRE |
| ticker (catalyst follow-up) | company name or "TICKER stock/shares" | stock | ticker (attention note only, no scored row) |

- **Direction.** Take up to 25 verified posts from the last 60 min (relevancy sort). Tag each post bullish or bearish with a fixed lexicon (`LEX_BULL` / `LEX_BEAR`). This is crude, grade C.
  - The direction is bullish or bearish only if at least 8 posts are tagged and |bull − bear| / (bull + bear) ≥ 0.30. Otherwise it's mixed, which isn't logged.
- **Rows.**
  - `kind=trend`: a scope crosses 3× and its sample has a direction.
  - `kind=sentiment`: the hourly market sample (the :40 run) has a direction while not trending.
  - Dedupe: one row per (target, kind, direction, day).
- **Scoring (Trader).** Did the target move in the called direction at 1h, 1d and 5d after costs?
  - Bullish rows are scored as longs vs the benchmarks.
  - Bearish rows are hypothetical shorts, i.e. "being in cash beat holding". The scorer keeps them out of its main long-only summary, so they're reported separately.
- **Pass bar.** Same as test 1: n ≥ 40 directional rows, t ≥ 2 on the signed after-cost return, and median > 0, after about 4 weeks. Primary horizon is 1d.

## Known conflicts with Trader's scorer (README wins; noted here)
1. **Pass bar per kind (resolved 2026-10-22 3:56pm ET).** Trader added `kind=` to PASS_BAR, so catalyst, trend and sentiment each have their own line above and are judged separately.
2. **Ineligible rows stay out of events.csv.** The scorer has no eligibility filter, so `events.csv` holds only pre-registered test rows. Untradable, wire-first, stale and off-hours candidates go to `candidates_rejected.csv`, which has the same columns. Dry runs go to `events_dryrun.csv`.
3. **Velocity column name.** Velocity is written as `mention_rate_vs_usual`, the README's name, not "velocity". `mention_count` and `baseline_count` sit next to it.
4. **wire_time is append-only.** It holds a wire or 8-K seen *before* first_seen. It's blank when the event was X-first at log time, so the scorer's lead-time stat only covers the control group. Wire times found *after* first_seen are in `followups.csv` (what=wire_recheck).
5. **Benchmark.** BLEND7030 is supported by the scorer (confirmed 3:50pm ET 10/22: 0.7×SPY + 0.3×QQQ return over the same window).

## events.csv schema (xfast/events.csv; also candidates_rejected.csv and events_dryrun.csv)
Append-only. Written with Python `csv` under `fcntl.flock`. One header row. Times are ISO-8601 with ET offset (e.g. `2026-10-22T15:47:53-04:00`).

| Column | Meaning |
|---|---|
| event_id | `TICKER-catalyst-postid` or `kind-scope-YYYYmmddHHMM` |
| logged_at_et | when the logger wrote the row |
| kind | catalyst / trend / sentiment |
| direction | bullish / bearish / mixed |
| target_type | stock / sector_etf / index |
| target | instrument scored (ticker, SMH, XBI, XLE, KRE, SPY, QQQ, IWM) |
| ticker | stock ticker (catalyst rows), blank for trend/sentiment |
| catalyst | fda_approval, fda_crl, acquisition, contract, guidance_raise, buyback, ceo_change, offering |
| matched_text | keyword that matched (catalyst) or scope name (trend/sentiment) |
| first_seen | fetch time of the X response (ET) |
| post_time_et | post created_at (ET) |
| lag_min | first_seen − post_time, minutes |
| wire_time | earliest wire/8-K known at log time (blank if X-first) |
| wire_source / wire_title | 8-K or publisher; headline |
| wire_before_first_seen | y / none_found |
| edgar_8k_time_et / newswire_time_et | the two raw checks |
| x_first | y if no wire/8-K before first_seen |
| post_id / post_url / account / account_class / verified_type / followers | X provenance; account_class is wire_list / company_handle / verified_other / other |
| last / bid / ask / quote_time / spread_pct | Nasdaq quote of target at first_seen (`spread_pct` fraction) |
| entry_ref_ask_plus10bp | ask × 1.001 (reference only) |
| mcap_usd | Nasdaq screener market cap |
| passes_news / uc_verdict / uc_fail / uc_flags | `universe_check --profile news` result (y/n/incomplete) |
| mention_count / baseline_count / mention_rate_vs_usual / trending | trend/sentiment rows only (blank on catalyst rows) |
| sent_bull / sent_bear / evidence_urls | lexicon tallies and up to 5 post URLs used |
| iwm_bid … spy_ask | benchmark quotes at log time |
| primary_eligible / reject_reason | y in events.csv; reasons in the rejected file |
| dry_run | y/n |
| notes | ticker match method + first 200 chars of the post |

`xfast/followups.csv` has the columns `logged_at_et,event_id,what,target,bid,ask,last,quote_time,wire_time,wire_source,wire_title,notes`. `what` is one of:
- `quote_t30`: Nasdaq bid/ask about 25–45 min after first_seen, for the approval-delay entry.
- `quote_t60`: the same, about 55–75 min after.
- `wire_recheck`: the later check for a wire or 8-K.

## Runbook: the 10-minute routine (9:40am–3:50pm ET, trading days)
Working dir `/workspace/lilies-knowledge`. Read the X guide skill once per session. X tools are free; on a 429, wait for the reset and retry once.
1. `python3 tools/xfast_log.py plan` prints JSON with `calls[]`, each holding `call_id`, `tool` and `arguments`. Skip the run if `budget_left_today` < 8.
2. Make each call with `CallDynamicTool(namespace="x", toolName=<tool>, arguments=<arguments>, write_to_file=true)`. Pass the arguments verbatim; they include since_id/start_time. Record each `call_id=<saved path>`. A normal run has:
   - `cat_wire`: search_posts_all from the 9 wire accounts with catalyst words.
   - `cat_pos`: search_posts_all for verified posts with cashtags and bullish catalyst phrases.
   - `cat_neg`: search_posts_all for verified posts with cashtags and offering/CRL phrases.
   - `cnt_market`: get_posts_counts_recent, hourly, 7 days.
   - Two `cnt_<theme>` counts, rotating so each theme comes up every 30 min.
   - `smp_market`: the hourly market sentiment sample, only on the run at or after :40.
3. `python3 tools/xfast_log.py ingest cat_wire=PATH cat_pos=PATH ... ` appends rows and prints a summary plus a `FOLLOWUPS [...]` JSON line.
4. If FOLLOWUPS isn't empty (≤ 2 calls: `cnt_tk_<TICKER>` attention counts for new events, `smp_<theme>` samples for trending themes), make those calls the same way and run `ingest` again with just those pairs.
5. Don't trade, post or message. When there's a new primary event, the routine may mention it in its run summary as "paper event logged".

**Budget.** Steady state is 6 calls per run, plus 1 hourly sample, plus 0–2 follow-ups. That's about 6–9 per run, and 38 runs × about 7.5 ≈ 280 a day, with a hard cap of `RUN_CAP=10` per run and `DAILY_CAP=400` per day in the logger. The user-wide limit is 1000 a day (resets 8pm ET) and 30 a minute, shared with other agents. The logger records `x_left_user_today` from each response.

## Dry run 2026-10-22, about 3:48pm ET (events_dryrun.csv)
- 7 X calls; the pipeline worked end to end (plan → X → ingest → quotes, news profile, EDGAR, newswire → csv).
- LNN, acquisition of Setorial (verified post 3:29pm ET): wire-first, because Business Wire was out at 2:52pm ET. It's also NOT TRADABLE on H5, with a spread of 0.70% at 3:48pm ET.
- NRIM, shareholder approval to acquire PBCO: wire-first (8-K 3:25pm ET), and the post was stale (24.6 min old).
- Market 1.15×, small caps 0.83×, rates/Fed 1.09× (none trending). The market sentiment sample was mixed (bull 1 vs bear 5, under the 8-post minimum).
- No primary events. Expected for a 3:48pm ET single pass.
- Fix after the dry run: the logger now prefers a headline that matches the catalyst over an earlier, unrelated 8-K for wire_time. The LNN dry-run row still shows the 6:45am ET earnings 8-K; re-checked, the matching headline is Business Wire at 2:52pm ET.
- Scorer check at 3:50pm ET: `xfast_score.py` mapped every column (event_id, target, ticker, kind, mention_rate_vs_usual, first_seen, wire_time, bid, ask, direction). The empty events.csv parsed, and the 2 dry-run rows came back `pending` (entry 10/23 10:00 ET). PASS_BAR was read with BLEND7030.


Note (2026-10-22 3:56pm ET): each kind is judged on its own line above. Bearish rows on SMH, XBI, XLE or KRE are left without an `instrument` on purpose: there's no 1x inverse fund for them, and -2x/-3x funds aren't allowed, so the scorer marks them not tradable. Bearish rows on SPY, QQQ or IWM are scored as SH, PSQ or RWM.
