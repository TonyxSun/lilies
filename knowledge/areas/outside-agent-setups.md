# Outside LLM / agentic trading setups: what they do, live evidence, how they failed, adopt/reject
Area created 2026-10-22 ~4:20pm ET (LOTF-PREOPEN-1023, Part A). Research only.
Rule used: a backtest without costs or with possible pre-cutoff data counts as ~zero evidence (L-005, L-006, L-019).
Evidence grades: A = live money or broker-paper post-cutoff with costs; B = contamination-controlled backtest with costs; C = in-sample / no costs / single run.

## Pass bar (set before reading)
"Adopt" only a practice that (a) has live or post-cutoff evidence after costs, or (b) is a pure risk/process control that costs nothing if wrong.
"Reject" anything whose only support is an in-sample backtest or a leaderboard over < 3 months.

## Summary table
| Setup | What it does | Out-of-sample / live evidence | How it failed | Grade | Adopt / reject for us |
|---|---|---|---|---|---|
| nof1 Alpha Arena S1 (Oct 18-Nov 3 2025) | 6 frontier LLMs, $10k real each, autonomous crypto-perp trading, same prompt | Live real money. 4 of 6 lost 42-59%; win rates 25-30% (L-007, L-023) | Over-trading: fees dominated early PnL; leverage; no regime control | A (n=6, 2 weeks) | Adopt: a trade budget and a turnover cap. Reject: any leverage-on-autopilot |
| Alpha Arena S1.5 (Nov 19-Dec 3 2025) | Same idea, US-equity perps (TSLA, NVDA, MSFT, AMZN, GOOGL, PLTR, NDX), several modes | Live. Winner Grok 4.20 +12.11% aggregate (L-008); only 6 of 32 runs profitable, the 32 accounts together $320k -> $237k (-25.9%) per amicobot.it reconstruction dated 2026-10-01; no Season 2 as of 2026-10-21 (alphaarena.ai) | Winner-picking from a 2-week, 32-run tournament; most runs lost | A (but 2 weeks) | Reject: "pick the model that won". Adopt: judge by the median run, not the best |
| TradingAgents (arXiv 2412.20138) | Multi-agent LLM "firm": analysts, bull/bear debate, trader, risk manager | Paper: +26.62% AAPL Jan-Mar 2024. Independent GitHub repro: -25.44% same window, alleged 2025 news leaking into the 2024 backtest (L-014) | Look-ahead/leakage; 3-month, 3-stock test; no costs | C | Adopt: the bull-vs-bear adversarial step (we already run one). Reject: its returns |
| FinMem / FinAgent | LLM agent with layered memory and reflection, timing single stocks | FINSABER (KDD 2026, 2004-2024, 100+ symbols, bias-controlled): buy-and-hold beats both; no significant alpha, p > 0.34 (L-003). Too conservative in bulls, too aggressive in bears (L-004) | Original gains came from short, cherry-picked windows; collapse when the window widens | B (negative) | Reject LLM market-timing of single stocks. Adopt: regime/trend filter + risk rules over more LLM reasoning (L-004) |
| FinGPT / FinGPT-Forecaster | Open-source finance-tuned LLMs (Llama-2-7B LoRA), weekly up/down forecasts from news + financials | No credible live or post-cutoff trading record. Independent benchmark: 47-53% direction accuracy, bullish bias, worse in downturns (arXiv 2507.08015, Jul 2025). Look-ahead pilot is 2 assets x 1 month (Research Square rs-10217060). Users report non-reproducible outputs (GitHub discussion #190) | Coin-flip direction; sampling randomness; undated sources | C | Reject as a signal source |
| CLQT benchmark (arXiv 2606.29771, revised Sep 2026) | Point-in-time gate, institutional cost model, committee vs autonomous scaffold, plus a 4-week live broker-paper track (Jun 15-Jul 10 2026, 18 days) | Net of costs, structured agents beat defensive baselines but "do not cleanly beat the index"; autonomous mode markedly worse; about half SPY's drawdown at the same Sharpe; agents' allocations don't follow their own stated analysis (gap +0.30 backtest, +0.23 live) | No index-beating; stated-vs-done gap | A/B (good design, short live) | Adopt: committee-with-constraints over autonomous agent; audit "did the trade match the stated thesis"; cost model in every test. Expect lower drawdown, not alpha |
| "When Agents Trade" / AMA (arXiv 2510.11695, WWW 2026) | 2-month live multi-market agent arena | Live: agent architecture and risk controls mattered more than which LLM was used | Short window; little index-relative significance | A (short) | Adopt: invest in process/risk rules, not model shopping |
| StockBench (arXiv 2510.02209) | 20 Dow stocks, daily decisions, Mar-Jun 2025 | Post-cutoff backtest: equal-weight B&H +0.4%; best agent +1.9% (L-009) | Tiny edges inside noise over 4 months | B | Neutral: shows agents can avoid disasters, not beat the market |
| LiveTradeBench (arXiv 2511.03628) | 21 LLMs, 50 live days Aug-Oct 2025 | Best +6.25% in a rising market; benchmark/reasoning scores didn't predict trading results (L-010) | Bull-market beta passed off as skill | A (short) | Adopt: always compare to SPY/QQQ over the same window |
| Lopez-Lira & Tang (JFE 2026) | GPT scores of overnight headlines -> next-day long-short | Post-cutoff: Sharpe 2.97 pre-cost but -0.39 at 20 bps costs; Sharpe decayed 6.54 -> 1.22 (2021Q4 -> 2024) as adoption rose (L-001, L-015, L-016) | Costs + crowding | B | Reject daily news-scoring for a retail account. Adopt: costs first, and expect decay |
| AIEQ ETF (IBM Watson, live since 2017-10) | AI stock-picker ETF | Live real money: 9.60%/yr vs S&P 14.73% since inception to 2025-09-30 (L-011, L-012) | Underperformed for 8 years | A | Base rate: the longest live AI-picker record loses to the index |
| Nathan Smith ChatGPT micro-cap (Jun 27-Dec 26 2025) | ChatGPT given daily closes, full control of a $100 real micro-cap portfolio, weekly Deep Research | Live real money: $100 -> $82.88 vs $111.68 in the S&P 500; max drawdown -50.33%; annualized alpha -34% (Substack, Week 26 post dated 2025-12-29; 40-page report 2026-01-26) | Concentration; repeated re-entry into losers; one outlier (ATYR) drove results; confident reasoning while losing | A (single run) | Adopt: our "never add to a loser" and no-re-entry rule; position caps. Reject: micro-caps |
| Retail "I gave ChatGPT $1,000" tests (blogs, 2025-26) | Ad-hoc prompting, small real accounts | About +1.40% vs +3.68% for the S&P over ~40 days; a 9-month run 5.8% vs 14% (blog posts, unverified) | Lag the index; frequent narrative-driven trades | C (unverified) | Base rate only |
| LiveOption (2026 study) | LLM overlays on options | LLM overlays underperform buy-and-hold after costs | Costs, short window | B | Irrelevant now (no options permission); reinforces "no" |

## What we adopt (process, cheap if wrong)
1. Judge by the median run and by index-relative results after costs, never by the leaderboard winner (Alpha Arena S1/S1.5, LiveTradeBench).
2. A constrained committee with hard rules beats an autonomous agent (CLQT, AMA). That is our current Trader/research split + rules.md: keep it.
3. Turnover and fee budget: S1 losses were dominated by fees from over-trading (L-007). Keep the small trade count; log costs on every paper trade.
4. Thesis-vs-trade audit: CLQT finds that agents don't do what they say (+0.23 live gap). Add a weekly check: did each trade match its written entry condition and stop?
5. Point-in-time discipline: TradingAgents' leaked backtest and the memorization results (L-006) mean any of our own backtests of LLM judgments before the model's cutoff are void.
6. No re-entry into a stopped-out loser; position caps (Smith experiment).
7. Expect lower drawdown, not alpha, from structured agents (CLQT). If Wuyue's goal is to beat SPY/QQQ, the agent layer is not the engine of that; exposure choice is.

## What we reject
- Picking or switching models because one won a short contest.
- LLM market-timing of single stocks (FINSABER null, L-003).
- Daily LLM news-scoring at retail costs (L-016).
- Leverage on autopilot (Alpha Arena S1).
- Any published LLM trading return without costs and without a post-cutoff window.

## Honest null
No outside setup with real money and >= 3 months of history beats the S&P 500 or QQQ after costs. The best evidence (CLQT, live, Sep 2026) says
structured agents roughly match index Sharpe with lower drawdown. That supports our process, not a return edge.
