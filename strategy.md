# Strategy

Current version: v0.1 (2026-10-22), paper trading only.

## The daily loop
1. **After the close, around 4:30pm.** Write a market brief: indexes, rates, dollar, oil, gold, sectors, breadth, catalysts and earnings, and risks. Every figure has a source. The format follows the @tychozzz daily-report framework (see below).
2. **Evening, around 6:30pm.** From that brief, propose 0 to 5 candidates. Each one gets a thesis, its sources, a confidence score from 1 to 5, and a size on the $1,000 paper account. These are proposals only.
3. **Next morning, around 9:45am.** Re-check every proposal against fresh prices and news, and drop any that no longer hold. Run the survivors through the risk limits in `rules.md`. During paper trading, the ones that pass are logged as paper fills. When live, they go to Wuyue for approval before any order.
4. **Every Friday.** Compare results with SPY and QQQ.
5. **After 2026-11-05.** Review the paper results against SPY and QQQ, and ask Wuyue whether to go live.

## Why this shape
The structure comes mostly from FriesTrader, the open-source flow in the Xiaohongshu post by 抢走所有人的薯条 (about 2026-08-07, edited 2026-09-19).
- Research and trading are separate steps. Ideas formed after the close get re-verified the next morning, because news can change overnight.
- The risk rules are mechanical, and the model can't override them. The author argues that the value of using AI here is discipline, not better prediction.
- Everything is logged, and new users run paper trading first.
- The author says the approach can't be backtested, because a model reasoning over historical news tends to make things up. That's why live paper trading is the test.

The after-close brief follows the @tychozzz post (Nico投资有道, 2026-05-24, https://x.com/tychozzz/status/2058496485969576269). It's a 15-section daily US-market report with a hard rule: every figure is sourced, and anything unavailable is marked "no reliable data" instead of guessed.

## Deliberately not adopted
- **The 15-stock bet on semiconductors and oil** (诶哟哟, 2026-10-02, about +11.64% in one month on $5k). One month on a small account isn't evidence, and a commenter noted QQQ rose about 5% over the same stretch.
- **0DTE options** (存1500w🔪退休, 2026-10-09, +40% in a week on about $375). The risk is far too high, and the account has no options permission anyway.

## Changelog
- 2026-10-22: v0.1 drafted from the three Xiaohongshu posts and the X post Wuyue supplied. Wuyue approved paper trading through 2026-11-05.
