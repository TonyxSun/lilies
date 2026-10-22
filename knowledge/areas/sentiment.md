# Sentiment: warm digest
Owner: worker B. Updated 2026-10-22 12:30pm ET. Rows: S-001..S-010. Tool: tools/sent_check.py (CBOE put/call, VIX, StockTwits). X counts come from the x MCP tool get_posts_counts_recent.

## Key findings
1. **Twitter-mood market timing doesn't hold up.** Bollen et al.'s 87% accuracy claim failed replication and showed signs of data snooping (S-001, A).
2. **Retail attention spikes come before *negative* returns.**
   - Robinhood herding events average about −4.7% over the next month, and bigger surges see bigger reversals (S-002, A).
   - A Google search spike gives about 2 weeks of price pressure, then reverses (S-003, A).
   - Bullish StockTwits posts are followed by about −1.9% over 5 days (S-007, A).
3. **Crowd stock-picking stopped working once it got popular.** WallStreetBets due-diligence posts predicted +2.33% a month before the GameStop squeeze and nothing after it (S-006, A).
4. **Sentiment matters most for speculative stocks.** High market-wide sentiment predicts that small, young, unprofitable, volatile names will underperform (S-008, A, Baker–Wurgler). Our large-cap, trend-filtered universe is mostly protected.
5. **Survey and put/call contrarian signals are weak.** Extreme AAII pessimism has been followed by above-average 6–12 month returns, but the academic support is marginal and it doesn't beat buy-and-hold risk-adjusted (S-004, B). Put/call has real stock-level predictability only in *non-public* open-buy volume. Public aggregate put/call evidence is mixed (S-005, A).
6. **Reachable data** (S-009):
   - Works: CBOE put/call JSON, VIX CSV, StockTwits (last 30 messages), tradestie WSB, X counts.
   - Blocked: Reddit, AAII, Google Trends.
   - Context on Oct 21: equity put/call 0.52 (low, i.e. complacent), VIX 16.68.

## Evidence strength
- **A:** S-001, S-002, S-003, S-005, S-006, S-007, S-008.
- **B:** S-004, S-009.
- **C:** S-010 (a single attention snapshot).
- Most return effects are pre-cost and strongest in small caps. The 20 bp cost result in L-016 suggests short-horizon sentiment edges die after costs.

## What doesn't apply to our setup
- We can't short, so negative-attention findings are avoid/exit filters only.
- Intraday StockTwits predictability (Renault, 30-minute SPY) doesn't fit daily cadence.
- 6–12 month AAII horizons are longer than our 2-week window.

## Rule candidates (one line each)
- **S-R1:** Never buy a name *because* it's trending. If X/StockTwits mentions are ≥2× their 7-day median, or it's a top Robinhood/WSB name, skip new entries for 5 trading days (S-002, S-003, S-007, S-010).
- **S-R2:** Don't use social-mood or Twitter-sentiment indices for market timing (S-001, S-006).
- **S-R3:** Sentiment readings (AAII, put/call, VIX) are context only. When they're extremely fearful (e.g. VIX >30), it's OK to deploy cash per plan. Never sell an index position on fear alone (S-004, S-005).
- **S-R4:** Stay out of speculative small, unprofitable, meme names entirely. High sentiment makes their forward returns worse (S-008, S-006).

## Pass-2 counter-evidence (12:30pm ET)
- **The Robinhood *aggregate* portfolio earned positive alpha in 2018–2020** (S-011, A, Welch). The harm is concentrated in *surge* events (S-002), not in popular large caps generally. So S-R1 targets spikes only. Being popular is not a reason to exclude a large cap.
- **Google search volume barely predicts returns in large caps** (S-012, B). It predicts volume and volatility. In our universe, an attention spike is a risk flag that justifies smaller size or waiting, not an alpha signal.

## Pass-3 adjacent: options-implied sentiment (12:30pm ET)
- **Option skew carries information.** A steep put skew predicts underperformance of about 10.9% a year for ≥6 months (S-013, A, Xing–Zhang–Zhao). The call-vs-put implied-vol spread earns about 50 bp a week, but that edge has decayed (Cremers–Weinbaum).
- **We can't use it yet.** No free per-stock implied-vol feed is verified. Candidate rule S-R5 (warm, untested): skip names whose 25-delta put skew is in the top decile of our universe.
- **"Unusual options activity" alerts aren't the same signal.** They are public and after the fact. Only non-public open-buy volume has shown an edge (S-005).

## Pass 4 (cycle 09, 2026-10-22 ~12:40 ET) — X attention pipeline + Twitter-volume evidence
**Pipeline (S-014):** call x `get_posts_counts_recent` (query "`<TICKER> -is:retweet`", granularity=day; 1 read/ticker of 1,000/day), save JSON like `sources/x_counts_2026-10-22.json`, run `python3 tools/x_attention.py <json>`. Metric = last complete weekday / median prior weekdays, plus today's pace (partial count × 24/h elapsed UTC; rough — intraday distribution is uneven). SPIKE ≥2x, elevated ≥1.5x.
Live today: NVDA 1.26x (pace 0.90x), AAPL 0.65x, MSFT 0.91x — all normal. Ambiguous tickers unusable (S-015: SPY ≈ "spy").
**Evidence:** volume tracks trading volume/volatility, not direction (S-018, B); retail-attention price pressure reverses next day (S-016, B); Twitter-mood-predicts-DJIA did not replicate (S-017, A).
**Does not apply:** we can't trade intraday overshoots; mega caps show weaker effects than small caps (S-016 driven by small stocks).
**Rule candidates:**
- S-R5: A held/candidate ticker with X SPIKE (≥2x weekday median) → no new buy that day or next (reversal risk); never a buy trigger. (S-016, S-002, S-007)
- S-R6: Ignore social "mood"/sentiment indices as directional signals. (S-017, S-018)

## Addendum, cycle 54 (worker B, 13:22 ET): live X attention during the selloff (S-019)
- Attention was normal (0.85-1.06x) on the AI-hardware names and indexes. Only META was elevated (1.5x, post-earnings).
- This is a price shock without a retail attention spike, so S-R1 is not triggered and there's no attention-based veto or signal today.

## Cycle 73: Wikipedia attention test (S-020)
- Mega-cap attention spikes show no reliable forward effect once ex-post winners are excluded (t -0.74).
- **S-R1 stays as a discipline rule:** don't chase a spike. It is labeled precautionary for mega caps, with evidence only for retail/small names (S-002).
- Pipeline note: Wikimedia pageviews are a free, long-history attention series. They could back-test any X-attention idea before it is used.
- **Cycles 90-91 (S-021 B, S-022 B hot):** new tools/attention_timing.py (StockTwits public plus X counts plus Yahoo) labels small/mid news names EARLY / BUILDING / LATE / NEGATIVE. In a volume-proxy backtest (150 current smid names, 2,405 earnings events) EARLY shows no 10-day edge after MA-R4 exclusion (-0.38%, t -0.6). LATE has a worse median (-2.3%, hit rate 34%, n=35). So use it as a veto, not a trigger. Trap: the Nasdaq screener download shows the PRIOR day's % change.
- **Cycle 92:** S-022 replication (seed 7). The LATE hint flips sign (+2.5%), so attention timing has no replicated drift edge on a volume proxy. Keep the LATE veto on the literature only (S-002/N-024).
- **Cycle 95 (S-023):** EARLY now requires an 8-K/6-K; no-news moves get flagged (Chan 2003). Today's genuine EARLY is WDFC (earnings, low attention). CALM was downgraded (no filing).
- **Cycle 97 (S-024):** hourly X pace shows WDFC attention began around 12pm ET (~5x baseline) while the daily ratio read 0.9x, so EARLY calls need a trailing-2h hourly pace check. BHVN has plateaued at ~80/h since the 7am news. TODO: add hourly pace to attention_timing.py.
- **Cycle 99 (S-025):** tool v3 adds hourly X pace. WDFC flips EARLY->LATE. Reconciled with CC-007: on independent samples, no edge for EARLY or LATE. Final: LATE veto + no-filing flag only.
