# News & catalysts — warm digest (owner 牛马; refreshed 2026-10-22 12:38pm ET, pass 2: counter-evidence applied)

## Key findings
1. **No speed edge.** Large caps price news within milliseconds to seconds (N-017, N-019). A bot that reads news at 4:30pm or 9:45am can only win by *interpreting* better over days, never by being first.
2. **Drift after real news, reversal after no-news moves.** Chan (2003): stocks with public news keep drifting (mostly bad news, mostly small and illiquid stocks); big moves without news revert (N-001, N-020). LLM headline signals predict 1–2 day drift, but the long leg is weak (8 bp/day vs 26 bp on the short leg) and the edge has decayed as LLM use spread (N-002). **Pass 2:** Jiang, Li & Wang (2021) confirm this with intraday news timestamps. News-driven returns continue for days; non-news returns reverse. The edge is about 1.4–2.1%/month net, but it's long-short (N-021, A).
3. **Bad news keeps going, but only for severe primary-source events.** Pass 2 (verified): after generic negative GPT-4-scored headlines, *large caps* drift +0.06% (slight reversion) while small caps drift −0.70% (N-029). Positive news drifts positively at all sizes, smaller in large caps. Lopez-Lira's Sharpe kept decaying, reaching 1.22 in Jan–May 2024. So NC-1 applies only to severe events (N-030). Restatements (8-K Item 4.02) average -2.0% vs SPY over 20 days (N-011). The same pattern shows up in Chan's bad-news drift and in the guidance-cut penalty (F-017).
4. **Attention and crowd buying are a negative signal (pass 2 nuance: the surge is the signal; aggregate retail order flow actually predicts slightly positively, N-026).** Retail buys attention-grabbing stocks, which then underperform (N-007). Robinhood herding stocks lose about 3.5% over 5 days and about 5% over a month (N-008). We are literally on Robinhood: trending "everyone's buying" names are fade candidates, not entries.
5. **Media sentiment at the market level is noise.** It reverses within a week (N-004). Firm-level negative words carry about 3 bp of next-day information, which costs erase (N-005).
6. **Timing (pass 2: overnight claim downgraded).** The claim that momentum accrues overnight (N-003) is contested: 2026 RFS evidence and Lachance (2023) find it weak or attenuating (N-025). Don't build on it. What survives is Berkman et al. (2012): high-attention stocks get bid up at the open by retail and give it back intraday (N-024, A). **Never buy a news or attention name in the first 15 minutes, and prefer limit orders** (flag for Trader).
6b. **Base rates (pass 2):** in FINSABER (2004–24, S&P 500 including delisted names), buy-and-hold significantly beats LLM trading agents, which have no CAPM alpha (N-022, A). Robinhood customers earned about 3.7%/yr vs the S&P's 16.8% in 2020–25 (N-027, B, unverified detail). A 2-week LLM contest shows huge luck dispersion (N-028, C). **The prior for an LLM news trader beating SPY in 2 weeks is below 50%.**
7. **Event types (large caps):**

| Event | Day-0 | Post-event drift for a long-only buyer | Use |
|---|---|---|---|
| Earnings with a positive reaction | priced in seconds | small or none in large caps (F-003) | only with guidance not cut |
| Guidance cut / restatement / bad 8-K | priced fast | continues negative (N-011, F-017) | exit or avoid ≥5 days |
| Analyst up- or downgrade | priced (partly before the timestamp) | ~none (N-015) | ignore for entries |
| S&P 500 addition | big after-hours gap | unverified; mostly in the gap (N-009, N-010) | don't chase the open |
| M&A target | jump toward the offer | capped upside, deal-break tail (N-014) | avoid |
| Buyback announcement | small | none in 2003–12 (N-016) | ignore |
| No-news big move or retail herding | — | reversal (N-001, N-008) | avoid buying |

## Daily news-triage pipeline (for the 4:30pm brief), v0
1. **Collect** (4:15pm ET). Sources: SEC EDGAR 8-K RSS and full-text search for the watchlist and holdings (free, ≤10 req/s, declared User-Agent; N-013); company IR press releases; Finnhub free company-news (60/min); X `search_news` for context; a Reuters or AP headline pass. Record `first_seen_at` (ET) and the publisher timestamp for each item.
2. **Dedupe.** Key = ticker + event type + date. Cluster near-duplicates by normalized title similarity and keep the earliest primary source (the filing or press release beats a news recap; N-005 shows morning recaps add nothing).
3. **Classify.** Event type from a fixed taxonomy (earnings, guidance, 8-K item, M&A, analyst, index, legal or regulatory, product, macro, no-news move), direction, and whether the source is primary. Have the LLM score sentiment on an anonymized copy (company name replaced) to cut the distraction effect (N-006).
4. **Measure the reaction.** Record the stock's move vs SPY from the last close before publication to the next close, plus volume relative to its 20-day average. If the move is large and there's no news item, flag it as a "no-news move" (N-001).
5. **Decay log.** For every classified event, log the abnormal return vs SPY at +1, +5 and +20 trading days in `news_events.tsv`. That gives us our own decay curves by event type within weeks, which is the real test.
6. **Avoid look-ahead.** Only use items with a publisher timestamp before the decision time. Never let the model "recall" what happened after a date. Use prices only from the decision timestamp or earlier. Mark anything else "no reliable data."
7. **Output.** At most 5 items into the brief, ranked by: primary source, event type with known drift (the table above), and relevance to holdings or candidates. Each gets a one-line "why it should beat SPY," or else "avoid / exit."

## Pipeline v1 additions (pass 3, 2026-10-22)
**Event-log schema** (`news_events.tsv`, one row per deduped event):
`event_id | ticker | event_type | direction(+/-/0) | severity(1-3) | primary_source_url | t_published_ET | t_first_seen_ET | t_decision_ET | close_before | ret_d1_vs_SPY | relvol_d1 | ar_d5 | ar_d20 | used_in_decision(Y/N)`

- **Dedupe key:** `ticker + event_type + trading_date(t_published)`. Within a key, keep the earliest primary source: EDGAR first, then company IR, then a wire, then any recap.
- **Timestamp rules:**
  - For EDGAR, use the filing-index "Accepted" time (ET). The submissions-JSON `acceptanceDateTime` disagreed with it by 8h on one of two IBM filings checked (N-033).
  - X news stories carry only `updated_at` and can be rewritten after the fact, so they're **discovery only**. Every fact must be confirmed at a primary URL timestamped before `t_decision` (N-032).
  - If `t_published > t_decision`, the item is excluded.
- **Severity 3** (triggers NC-1): guidance cut, 8-K 4.02, going-concern, SEC/DOJ action, CEO/CFO exit without a successor.
  - Severity 2: earnings, M&A, index change.
  - Severity 1: everything else, logged but never acted on alone.
- **Budget:** EDGAR ≤10 req/s with a declared User-Agent. Finnhub free tier 60/min. X reads are rate-limited (30/min, 1000/day observed on 2026-10-22).

## What doesn't apply
- Short-side drift (most of the academic edge), and speed trading.
- Microcap news drift, which our $10B screen excludes.

## Rule candidates
- **NC-1:** Never open a long on a stock with a guidance cut, restatement (8-K 4.02), or similar *severe* primary-source bad news in the last 5 trading days. Generic negative headlines in >$10B names don't count (N-029, N-030). [N-001, N-011, F-017]
- **NC-2:** Don't buy a stock whose ≥1-day move of more than 2 SD has no identifiable news, or that is trending on retail or Robinhood lists. [N-001, N-007, N-008, N-020]
- **NC-3:** News alone is never a buy signal in large caps. The thesis must state an edge beyond "good news" (it's already priced in seconds). [N-017, N-019, N-002]
- **NC-4:** Every news item in a decision carries a publisher timestamp earlier than the decision time. Sentiment is scored on anonymized text. [N-006]
- **NC-6 (pass 2):** default to SPY/QQQ when no candidate clears NC-1..NC-3 plus FC-1..FC-3; an empty slate is a valid output. [N-022, N-027]
- **NC-5:** Log the +1, +5 and +20 day abnormal return of every triaged event, and review by event type at each Friday retro. [N-002, F-015]

## Pipeline v1: implemented and live-tested (2026-10-22, 12:34pm ET)
- **Tool:** `tools/news_triage.py TICKERS [--days N] [--decision "YYYY-MM-DD HH:MM"] [--headlines x.json]`. It's read-only and uses only free sources:
  - EDGAR submissions plus the filing-index Accepted time
  - Yahoo chart daily bars (unofficial endpoint, approximate)
  - optional X headlines, used for discovery only
- **Look-ahead guards:**
  - Events accepted after the decision time are dropped.
  - Day-1 reactions are used only after the close, unless the run is live, in which case they're marked `(intraday)`.
- **Live test** on IBM, TSLA, META, LRCX and PG: all five earnings 8-Ks were found, timestamped to the minute (N-035). Intraday moves vs SPY:

  | Ticker | Move vs SPY |
  |---|---|
  | META | −6.0% |
  | LRCX | −9.1% |
  | PG | +7.4% |
  | IBM | +0.6% |
  | TSLA | −0.6% |

  The X summaries agree in direction (N-036). The output is in cycles/05-triage-test-2026-10-22.tsv.
- **Fixes found while testing (N-038):**
  - Collapse each multi-item 8-K into one event.
  - A no-news-move flag needs a headline check, because EDGAR misses news that isn't in a filing.
- **New rule NC-7:** an earnings reaction is judged on the guidance, capex and FCF lines, not the headline beat. Example: LRCX had a record quarter with in-line guidance and fell 9% (N-037, C, anecdotal). Use the tool output only to apply NC-1, NC-2 and FC-1; never as a buy signal.
- **One-command brief** (`tools/daily_brief.py TICKERS`): runs triage plus the quality screen and prints a veto/flag table. It was tested on 7 names (N-039), and the output is in cycles/05-daily-brief-2026-10-22.md.

## Pass 5: own test of 8-K severity in large caps (1:30pm ET; tools/severe_8k_test.py; output in cycles/06-severe-8k-test.txt)
- **Severity-3 items are rare:** in five years across 80 names, there were no 4.02 filings, four 1.05 filings (−1.2% on day 1), and six standalone 2.06 filings (−2.3% over the next 10 days, t −2.0) (N-040, C).
- **High-frequency items are noise:** 5.02 (n=873) and 1.01 (n=265) have mean |day-1| moves of about 1.4–1.5% and no drift (N-041, B).
- **Calibration:** the severity map in news_triage.py stands. Treat 5.02 at severity 2 as context only. Note that the NC-1 veto will rarely fire on large caps; its main job is to stop us buying into a standalone impairment or restructuring.
