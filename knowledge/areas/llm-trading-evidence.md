# LLM and agent trading evidence (warm digest)
Owner: 牛马 (worker B) · last refreshed 2026-10-22 (pass 1) · INDEX ids L-xxx

## Bottom line
LLMs are good at *reading* fresh news and filings, and bad at *timing* and at honest backtests. Every rigorous long-horizon test so far finds LLM trading agents do not beat buy-and-hold; the only robust edge (news drift) is small on the long side, concentrated in small caps, and decaying as LLMs spread.

## Key findings
| Finding | Grade | Ids |
|---|---|---|
| GPT-4 headline scores predict 1–2 day drift (post-cutoff Oct 2021–May 2024). Long-short 34 bps/day pre-cost, but the **long leg is only ~8 bps/day**; most alpha is in shorting bad news and small caps. Returns decline as LLM adoption rises. | A | L-001, L-002 |
| FINSABER (KDD 2026), 20 yrs × 100+ symbols: buy-and-hold significantly beats FinMem/FinAgent once survivorship and window-picking are removed; no significant alpha (p>0.34). Agents are too cautious in bull markets, too aggressive in bear markets. | A | L-003, L-004 |
| Memorization: GPT-4o recalls pre-cutoff S&P 500 levels to 0.6% MAPE; post-cutoff it has no skill. "Pretend it's date X" prompts don't stop it. Any LLM backtest on pre-cutoff data is invalid. | A | L-006 |
| Look-ahead + "distraction" (company knowledge biases sentiment). Anonymizing company names helped, esp. large caps. | A | L-005 |
| Live record: AIEQ (AI stock picker since 2017) 9.60%/yr vs S&P 500 14.73%/yr through 2025-09-30; 5y 8.71% vs 16.47%. | A (fund filing) | L-011, L-012 |
| Live contests: Alpha Arena S1 (crypto perps) 4/6 frontier models lost 42–59%, fees from over-trading dominated; S1.5 (US equities, 2 weeks) winner +12%. Too short and leveraged to generalize. | B/C | L-007, L-008 |
| Live benchmarks: StockBench (Mar–Jun 2025, Dow 20) agents beat a +0.4% B&H by ~1–1.5 pts; LiveTradeBench (50 days) best +6.25%, no index comparison; general benchmark scores and reasoning models don't predict trading skill. | B | L-009, L-010 |
| Financial-statement analysis: GPT-4 beats median analysts on earnings direction (60% vs 53%), but sample is mostly pre-cutoff and VW results favor a simple ANN. | B | L-013 |
| TradingAgents' +26.6% AAPL backtest failed independent reproduction (−25.4%), alleged news leakage. | B | L-014 |

## What doesn't apply to us
- Short legs and market-maker-cost strategies (L-001 short leg, long-short spreads): we are long-only, cash, retail costs.
- Small-cap drift: our screen is >$10B market cap, where news drift is weakest.
- Crypto/perp contests (L-007): leverage-driven.

## Rule candidates (testable, one line each)
1. **Never trust an LLM backtest or "what would have happened" over dates before the model's training cutoff; evaluate only live paper results.** (L-006, L-005, L-014)
2. **Default to holding SPY/QQQ; an LLM-proposed stock must justify why it beats the index, and the Friday retro measures that.** (L-003, L-011)
3. **Use the LLM to read/classify fresh news and filings, not to time the market; keep exits mechanical (stops, rules), never discretionary.** (L-001, L-004)
4. **Trade rarely: cap turnover (e.g. ≤ 3 new positions/week) since over-trading fees dominated live-agent losses.** (L-007)
5. **Strip company names when asking the model to score a headline's sentiment for large caps.** (L-005)

## Pass-2 update (2026-10-22 12:30pm ET; L-015..L-022)
**Counter-evidence check on the "LLMs read news well" claim:**
- **The edge decays fast.** The Lopez-Lira & Tang news-strategy Sharpe fell from 6.54 (2021Q4) to 1.22 (Jan–May 2024) as LLM use spread (L-015, A).
- **Costs kill it.** At 20 bp per trade, the daily-rebalanced strategy's Sharpe goes from 2.97 to −0.39 (L-016, A). This strengthens rule 4 (cap turnover) and argues against daily LLM news trading for our account.
- **It isn't purely a micro-cap effect,** since the result survives excluding sub-$5 and small stocks, pre-cost (L-017, A). The search-summary claim that large caps show no drift is UNVERIFIED.
- **Supportive but weak:**
  - GPT-4 with live web search gave ratings correlated with subsequent surprises and returns (L-018, B, short 2023 window).
  - LLM embeddings beat bag-of-words for return prediction (L-021, B, working paper).
- **Look-ahead bias exists, but it's task-dependent.** Point-in-time ChronoGPT matches Llama 3.1 on news→next-day returns, so leakage is small for *that* task (L-019, A). It doesn't excuse narrative or company-knowledge backtests (L-006 still stands).
- **No credible AI-ETF record beats SPY over multiple years** (L-020, C; L-011/012, A).
- **LLMs misread filings.** GPT-4 with retrieval got only 19% of FinanceBench filing questions right, and ~85% when given the right pages (L-022, B).

**Net:** rules 1–5 stand. Add:

6. **Every number an LLM extracts from a filing or article must be checked against the source page, with the page quoted in the trade note, before it can justify a trade.** (L-022)
7. **No daily LLM-news rebalancing. LLM news reads may only veto or approve entries on the weekly cadence.** (L-015, L-016)

## Open questions (pass 3)
- Has a long-only large-cap subset of the news strategy been tested after costs? Still unanswered.

## Pass-3 adjacent: live LLM arenas (12:30pm ET)
- **nof1 Alpha Arena S1** (live money, crypto perps, 2 weeks): only 2 of 6 LLMs were profitable, and four lost 42–59%.
- **S1.5** (US equities): the winner made +12.11%, with no same-window benchmark published (L-023, C).
- **Takeaway:** two-week, leveraged, single-run results are mostly luck. That supports B2 (index default) and B3 (low turnover). Don't read a good two weeks for our own agent as skill.
