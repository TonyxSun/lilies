# Rules in force

Last changed: 2026-10-23 ~12:35am ET (Wuyue's standing trading authorization, "recursively self-approve", no 2x/3x inverse funds) and 10:10am ET (Trader's order-lock process rule). Earlier: 2026-10-22 4:16pm ET (Wuyue chose plan A: live from Fri Oct 23, half the core in QLD, real-money news trades allowed). Earlier: 3:55pm (year-end review), 3:38pm (HOT 1, 2, 3, 10, 14, tradable test, benchmark; history squash declined).

## Set by Wuyue
- ~~No order is placed without Wuyue's explicit OK. No autonomous trading limit has been granted. (2026-10-22)~~ Superseded 2026-10-23 12:35-12:36am ET: Trader may place trades on its own within these rules and reports after each fill. This covers the morning plan, daytime signals (at most 4 a day, any asset scoring 6 or more on TRADE-SCORING.md, including GLD, USO/BNO and TLT) and stop-loss sells. Bets (everything outside the index core) stay at or under about 40% of the account.
- "Recursively self-approve" (Wuyue, 2026-10-23 12:37am ET): the bots may adopt their own research and rule improvements within the plan without asking him first. Trader owns trading decisions. The hard limits stay: cut-loss rules, bets ≤ about 40% of the account, no 2x/3x inverse funds, never force-push the repo.
- Any doubt resolves toward the index or cash; geopolitical risk and loss-cutting are factored into every plan (Wuyue, 2026-10-23 12:15am ET).
- Every number needs a source and a date. Never invent data. (2026-10-22)
- ~~Paper trading first, through 2026-11-05.~~ Superseded 2026-10-22 4:16pm ET: live trading may start Fri 2026-10-23 with about $1,000 once Wuyue funds the account; the $1,000 paper account and the X fast-news paper test continue alongside. (2026-10-22)
- Before any submit or confirm step, send Wuyue a screenshot and wait for his OK. (standing rule)

## Goal and benchmark (approved 2026-10-22 3:38pm ET)
- **Beat the index, defined.** Performance is judged on our cumulative return since 2026-10-22, after costs, against SPY, QQQ and a 70/30 SPY/QQQ blend over the same dates and cash flows. Each Friday retro also shows us against the better of SPY and QQQ that week, as context only. The retro explains which trades helped or hurt and proposes rule changes for Wuyue to approve.
  Why: a 70/30 mix always lands between SPY and QQQ in any single week, so one noisy week shouldn't decide; the running total is the fair test. (Wuyue's question 8)
- **Index is the default.** Every pick is scored against SPY and QQQ. On 2026-11-05 we post a progress report against SPY, QQQ and the 70/30 blend, not a switch decision. The keep-or-drop decision is Wuyue's year-end 2026 review, which replaces the 3-point trigger and Trader's 3-month give-up rule (approved by Wuyue 2026-10-22 3:55pm ET).
  Why: buy-and-hold beat LLM trading agents, most active funds lag, and a random stock book beats both SPY and QQQ over 10 days only 21-27% of the time. (HOT 1; N-022, PC-001, PC-002, R-014, R-001, BR-001, BR-002)

## Account
- Only the Robinhood agentic cash account is used. Wuyue's default Robinhood account is never touched.
- 2026-10-22 (Robinhood query): value $0, no positions, no options permission. So stocks and ETFs only.

## Portfolio shape (approved 2026-10-22 3:38pm ET; live book changed 4:16pm ET)
- **Live book from 2026-10-23 (plan A, Wuyue 4:16pm ET).** Core about 60%: QLD (2x Nasdaq-100) about half, SPYM (S&P 500) about half. The rest is cash plus up to about $100 per bet (dip buys and news trades), each within an entry range and with a close-based stop. This replaces the 1 VOO + 1 QQQM shape below for real money; the 70/30 SPY/QQQ blend stays a benchmark.
  Why: Wuyue wants aggressive bets that try to beat SPY/QQQ (3:45pm ET); in Trader's tests only leverage on QQQ beat QQQ, which is a beta bet, not an edge (backtests/2026-10-22-aggressive).
- **Core = 70% SPY-type / 30% QQQ-type.** On $1,000 that is 1 VOO + 1 QQQM in whole shares, bought and held. The 30% QQQ slice is a declared growth bet, not a proven edge, and Wuyue accepts its dot-com-style drawdown risk (in a 2000 replay $1,000 fell to about $386 and took about 12.5 years to recover).
  Why: QQQ beat SPY by about 4.7 pts/yr since 2015 (t 1.9), but it beat SPY in only ~52% of 3-year windows starting before 2009. (HOT 2; SO-002, SO-010, SO-011, WS-001, WS-005)
- **Momentum stock picks are paper-only**: at most 10% of the paper account, scored against QQQ. They move to real money only with Wuyue's yes after a live paper record beats QQQ after costs.
  Why: the good-looking backtest uses today's S&P 100 members (survivorship-biased); unbiased Ken French data show no long-only large-cap momentum edge since 2009. (HOT 2; T-021, SO-001, T-023, T-026, R-021)
- **News trades may use real money** (Wuyue chose plan A, 2026-10-22 4:16pm ET, overriding the earlier paper-only rule for this sleeve), at about $100 per trade, each with Wuyue's OK. ~~Paper-only until it has a pre-registered live record.~~ Inside it: a LATE attention spike is a veto (never buy after the crowd has piled in); being EARLY is not a buy signal on its own; check the lockup date for names listed about a year; every trade needs a dated filing or news source.
  Why: buying after a Robinhood herding spike averaged -4.7% over the next 20 days, and our own test of buying early on 3,585 earnings releases returned -0.19% vs IWM over 10 days (t -1.08), about the size of the spread. (HOT 10; S-002, NS-004, CC-007, S-022, US-012; proposals N5)

## Which stocks are tradable (approved 2026-10-22 3:38pm ET; replaces the old $10B market-cap minimum)
Checked with `tools/universe_check.py` (thresholds copied from proposals/trader-2026-10-22.md rounds 6 and 7).
- **Default test (Tradable v1, round 6):** listed on NYSE or Nasdaq (no OTC); price ≥ $5; market cap ≥ $300M; 30-day average dollar volume ≥ $2M; quoted spread ≤ 0.5% at order time; a 10-K or 10-Q filed ≤ 150 days ago; no NT (late-filing) or bankruptcy filing in the last 12 months; ≥ 8 quarters of reported revenue; positive trailing-4-quarter earnings if market cap < $3.66B; exclude names with a max daily return ≥ 15% (21 days), 63-day volatility > 60%/yr, or a herding spike in the last 5 days (wait 20 sessions). The manual 5-item information checklist must also be done (latest 10-K/10-Q read, latest earnings release, one independent source from the last 90 days, next earnings date known, a one-paragraph thesis); if any item can't be done, the stock isn't tradable.
- **News mode (Tradable v2-news, round 7; `universe_check.py --profile news`):** keeps NYSE/Nasdaq, price ≥ $5, ADV ≥ $2M, spread ≤ 0.5%, a 10-K/10-Q within 150 days and no bankruptcy 8-K as hard rules; needs ≥ 4 periodic filings (~12 months listed) instead of 8 quarters; drops the $300M floor and the profit gate. Hype checks (max return, volatility, herding) and late-filing notices become flags that need a dated catalyst source, not rejections.
- Still applies on top: price above its 200-day moving average for single stocks (not for the index core).
  Why: what lets a $30-100 order fill near the quoted price is listing, price, volume and spread, not size; since 2009 small-cap picking has shown no reliable edge, so the value is in excluding junk. (HOT 9, proposals R6-1/N1; UV-009, UV-010, US-002)

## Mechanical risk limits
These are applied as written. A strong story never overrides them. Wuyue can change them.

- At most 10% of the account in any one stock, and at most 12 positions. The SPY/QQQ index core (VOO, QQQM) is exempt from the 10% cap.
  Why: the cap limits single-stock blow-ups; a broad index fund isn't a single-stock risk. (HOT 2; proposals round-2 #7)
- Cash only. No margin, no shorting, no options. Leveraged long ETFs bought with cash are allowed (QLD in the core per plan A). Inverse funds: 1x only (SH, PSQ). No 2x/3x inverse funds (QID, SQQQ, etc.) — fixed limit, Wuyue 2026-10-23 just after midnight ET (logged as 12:22pm in an earlier edit, likely 12:22am); supersedes the 2026-10-22 3:55pm allowance. TRADE-SCORING.md is the source of truth for limits.
- **Stops (replace the old 2× ATR / -8% stop):** no stop on the index core (if one is ever mandatory, a -8% trailing stop). Single stocks exit at the next session if the close is below max(0.80 × highest close since entry, highest close − 5 × ATR14).
  Why: the 2× ATR stop cost -0.28 to -0.34% per 14-session window on the index and was the most harmful rule we tested; tight stops cut the momentum backtest by ~15 pts/yr. (HOT 3; SL-001, SL-005, SL-009, R-015, SL-007, SL-008, R-007)
- **Loss breakers, measured on our own account** (total account value, close vs prior close; not QQQ or SPY): a -2% day means no new buys that day; -8% from the equity high means no new buys plus a review with Wuyue. No forced selling.
  Why: the day after a -2% book day averaged +0.20%, so the breaker should delay buying, not force sales. (HOT 14; R-016, PT-007, PT-008)
- Never add to a losing position.
- Wash sale: after selling at a loss, don't buy the same stock back for 30 days.
- No new position within 2 trading days before earnings.
- **Order safety (Trader, 2026-10-23 10:10am ET, after a duplicate QLD fill):** only one run may place a given day's plan (lock file); re-read the day's orders on the symbol right before every place, cancel or re-price; a unique reference id per order line. No same-day sells except stops; never sell a position bought with unsettled funds for a non-stop reason (good-faith violation).
- **Cut-loss on the live book (Trader, 2026-10-23):** close-based, checked at 3:45pm ET from 2026-10-26. QLD exits on a close ≤ 15% below its average cost; single-stock bets use their own preset stop plus a time exit; account close ≤ $920 means sell the bets and QLD; a -2% account day means no new buys the next day.
