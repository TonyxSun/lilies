# Strategy

Current version: v0.3 (2026-10-23 12:37am ET): live since Fri 2026-10-23, Trader trades on its own within rules.md, with paper tests alongside.

## Objective
Make money by beating the index (set by Wuyue, 2026-10-22). "Beat the index" is defined (approved by Wuyue 2026-10-22 3:38pm ET): performance is judged on our cumulative return since 2026-10-22, after costs, against SPY, QQQ and a 70/30 SPY/QQQ blend over the same dates and cash flows. 2026-11-05 is a progress report; the keep-or-drop decision is Wuyue's year-end 2026 review (approved 2026-10-22 3:55pm ET), which replaces the 3-point trigger and the 3-month give-up rule. Medium-term strategies (weeks to months) are in scope; trades may change any day.

Every Friday after the close there's a retro. It shows our return against the better of SPY and QQQ that week (context only, since a 70/30 mix always lands between the two in any single week) and the cumulative comparison above, lists which trades helped and hurt and why, and proposes any rule changes for Wuyue to approve or reject.

The real-money shape (plan A, Wuyue 2026-10-22 4:16pm ET) is a core of about 60% split between QLD (2x Nasdaq-100) and SPYM, plus cash and about $100 bets such as dip buys and news trades, each with Wuyue's OK. Momentum stock picks stay paper-only; the X fast-news idea is a paper test. See `rules.md`.

## The daily loop
1. **After the close, around 4:30pm.** Write a market brief: indexes, rates, dollar, oil, gold, sectors, breadth, catalysts and earnings, and risks. Every figure has a source. The format follows the @tychozzz daily-report framework (see below).
2. **Evening, around 6:30pm.** From that brief, propose 0 to 5 candidates. Each one gets a thesis, its sources, a confidence score from 1 to 5, and a size on the $1,000 paper account. These are proposals only.
3. **Next morning, around 9:45am.** Re-check every proposal against fresh prices and news, and drop any that no longer hold. Run the survivors through the risk limits in `rules.md`. During paper trading, the ones that pass are logged as paper fills. When live, they go to Wuyue for approval before any order.
4. **Every Friday.** Run the retro against SPY and QQQ (see Objective).
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
- 2026-10-22 3:38pm ET: Wuyue approved HOT 1,2,3,10,14, the tradable test and the benchmark definition; declined the history squash.
- 2026-10-22: Objective set by Wuyue to beat SPY and QQQ, with a weekly Friday retro.
- 2026-10-22: v0.1 drafted from the three Xiaohongshu posts and the X post Wuyue supplied. Wuyue approved paper trading through 2026-11-05.

- 2026-10-22 4:16pm ET: Wuyue chose plan A for the Oct 23 live book: half the core in QLD, SPYM for the other half, real-money news trades allowed (v0.2).
- 2026-10-22 3:55pm ET: Wuyue approved making Nov 5 a progress report and using his year-end review instead of the 3-point trigger and the 3-month give-up rule.
- 2026-10-23 12:15-12:37am ET: Wuyue funded the account ($1,000, pending), gave Trader a standing authorization to trade within the rules and report after each fill (at most 4 daytime signals, score ≥ 6, bets ≤ ~40%), banned 2x/3x inverse funds, and told the bots to "recursively self-approve" research and rule improvements within the plan (v0.3). Step 3 of the daily loop now runs without a per-order OK.
- 2026-10-23 10:10am ET: after a duplicate QLD fill from two parallel pre-open runs, Trader added order locks and a re-read-orders-before-every-place rule.
