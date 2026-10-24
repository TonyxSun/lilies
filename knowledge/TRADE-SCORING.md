# Trade scoring (Wuyue, Oct 22 2026, 4:20pm ET): rank every candidate, take only top scores, sit out the rest

Applies to every non-core trade (SMH, IWM, news trades, inverse news trades, anything new). The core (SPYM + QLD) is held, not scored daily, except its month-end QQQ 200-day switch.

Score each candidate (max 10; one shared rubric for both bots):
1. Evidence (0-3): our tested result. t >= 3 = 3; t ~2 = 2; t 1.5-2 or published study only = 1; none/negative = 0.
2. Edge after costs (0-1): tested excess return vs its benchmark after costs > 0 = 1.
3. Catalyst (0-2): dated, fresh (<= 2 days) and confirmed by a filing/release = 2; dated but partly priced = 1; none or stale = 0.
4. Setup (0-2): still inside the entry range and nothing overnight broke the case, above 200-day, no >3% open gap = 2; in range = 1; out of range or case broken = 0.
5. Risk and fit (0-2): bad-stretch loss <= 1% of account and adds no concentration = 2; one of the two = 1; neither, or earnings within 2 days = 0.

Rules:
- A 0 on both Evidence and Catalyst = skip. A 0 on Setup = skip.
- Take only candidates scoring >= 6, highest first, until the bet pool (~40% of account) or per-trade cap is used. Ties: lower correlation with the core wins.
- Below 6 = sit out; money stays in cash. Doing nothing is a valid result.
- Every evaluation posts a ranked table (name, five sub-scores, total, take/skip, one-line reason) with sources and times.

## Cut-loss rules (Wuyue, Oct 23 2026 12:15am ET: "have cut loss factors")
All stops are close-based (checked ~3:45pm ET) and start the trading day after the buy (never a same-day sell). Before the deposit settles, a hit stop still sells: one good-faith warning costs less than holding a falling position.
- QLD (2x QQQ core): sell on a close >=15% below average entry (~4% of the account at 26%); switch to QQQM at month end if QQQ closes below its 200-day average.
- SPYM (index core): no single-position stop; covered by the account limits below.
- Single stocks / news trades (e.g. ELV): the stated price stop (ELV close < 426) or 5 trading days, whichever first.
- SMH dip buy: close >12% below entry, or 50 trading days, or Dec 31.
- Account limits: account down >=2% in a day, no new buys the next day; account down >=8% from $1,000 (close <= $920), sell all bets and QLD and keep only SPYM plus cash until Wuyue reviews.

## Geopolitical gate (Wuyue, Oct 23 2026)
Pre-open: major overnight escalation AND futures down >=1.5% or Brent up >=5% => no bets, SPYM half of core only. Futures down >=3% => buy nothing. Overnight risk check: 牛马, ~10pm ET Sun-Thu (facts lane).

## Universe and intraday signals (Wuyue, Oct 23 2026 12:28am ET)
- Any asset class is allowed if it scores >= 6: stocks, sector ETFs, gold (GLD/IAU), oil (USO/BNO; note futures roll cost, keep holds short), bonds (TLT/IEF), plus the core. Still no -2x/-3x inverse funds.
- Intraday monitor every 30 min 10:00-15:30 ET; act on BIG signals only, max 4 per day (cut-loss hits and SPY/QQQ >=3% shocks exempt). Log in cycles/SIGNALS-<date>.md.

## Evidence bar (Oct 23 2026)
Adopted 10/23 (Wuyue's overnight research ask; Trader batch 2, backtests/2026-10-23-ai-edge-2/).
- **Count trials.** Every backtest lists its number of variants (N) in PREREGISTERED.md before data is pulled, and the team keeps a running total (~229 as of 10/23 ~1:20am ET). With that many tries, t ≈ 2 shows up by chance (AS-029, AS-030).
- **Pass bar:** out of sample (2013-2026), after costs at both 0.05% and 0.15% a side: t >= 3, or a deflated Sharpe > 0.95 given the total team trial count. It must also be cash-account feasible (hold >= 1 day, no same-day round trips). Results below the bar can score Evidence 1 at most.
- **No speed trades on headlines or filings.** Prices absorb public news in seconds to minutes, and the fast edge goes to paid feeds and co-located traders (AS-012, AS-013, AS-027, AS-028). Fresh news can only veto a trade or support a multi-day read.
- **Dip/reversal rules count only in stressed regimes** (VIX > its 1y 80th percentile, or > 25). Reversal profits are pay for providing liquidity and concentrate in high-VIX periods (AS-006). Our own test agrees in direction but stays below t 3 (AE-005). In calm regimes, dip rules score Evidence 0.
- **Trend/rotation rules are drawdown tools, not return engines.** Their return edge is weak once vol scaling is handled (AS-008, AS-009), and our own cross-asset rotation cut max drawdown (-36% vs -51%) with no excess return (AE-004). Use them for risk, never as a reason to expect beating SPY/QQQ.

## Fixed limits (Wuyue, Oct 23 2026 12:22pm ET)
~40% bet pool; score >= 6; t >= 3 test bar; all cut-loss rules incl. $920 account floor and no buys the day after a >=2% down day; max 4 signals/day; no 2x/3x inverse funds; no same-day sells except a hit stop. Changing ANY limit, tighter or looser, needs Wuyue's explicit yes first. "Recursively self-approve" does not cover limits.

## Settlement and good-faith violations (Wuyue via HCI, Oct 23 2026 12:26pm ET)
- Ledger: tools/settlement.csv. Each buy records what paid for it (settled cash, pending deposit, or proceeds from a sale on date X) and when that cash settles. Sales settle T+1 (next business day). Robinhood instant buying power is NOT settled cash.
- Before any sell, check the ledger. If the shares were paid for with unsettled cash, don't sell, unless a cut-loss rule is hit; then sell anyway, log it as a deliberate violation in tools/gfv-count.md, and tell Wuyue.
- Sell one thing and buy another the same day: mark the new position "no sell until <date>" in settlement.csv and the daily note.
- Rolling 12-month violation count in tools/gfv-count.md. At 1, warn Wuyue. At 2, pause any trade that could cause a third and ask him first.
- This does not change the fixed limits.

## Adaptive scoring (Wuyue, Oct 23 2026 5:24pm ET: "readapt frequently based on previous signals and new signals")
- Fixed (not adapted without Wuyue's yes): the take bar (total >= 6), the t >= 3 evidence bar for new trading rules, and every other fixed limit.
- Adapted by me: the sub-score definitions and weights above, and new signal factors.
- Every scored candidate (taken AND skipped) goes in tools/score-log.csv with all five sub-scores, ref price and time, and signal tags. The evening run fills 1/5/20-day returns and SPY over the same span.
- Daily (evening): note any sub-score or signal tag whose skipped names keep beating taken ones.
- Weekly (Friday retro): recalibrate. For each sub-score and tag, compare forward excess return vs SPY by score level. Change a weight or definition when the data points the same way for 2+ weeks or >= 15 outcomes (whichever first); max 2 changes a week; log each change here with date, before/after and the evidence; revert if it underperforms the old version over the next 2 weeks (shadow-score both).
- New signals (e.g. from 牛马's research or a fresh event type) enter as a tagged shadow factor: scored and logged but worth 0 points until its tracked outcomes earn it weight.

## Shortlist + deep research, and adaptive rubric (Wuyue, Oct 23 2026 5:24pm ET)
- The rubric is a SHORTLIST tool. Each evening, take the top ~10 scored candidates (any asset class; include near-misses scoring 4-5) and research each one individually, irrespective of its first score: fresh news and filings, price action/technicals (trend, 200-day, gaps, volume), options-implied move, earnings/event dates, correlation with the current book, and the bear case. Then re-score. The take bar stays >= 6 (fixed limit). Write the research per name in cycles/ORDER-PLAN-<date>.md.
- Score log: tools/score-log.csv. Every scored candidate (taken or skipped) gets a row: date, symbol, five sub-scores, first score, post-research score, take/skip, entry-reference price, then 1-day and 5-day returns and excess vs SPY filled in later.
- Re-tuning: the evening routine fills outcomes daily; the Friday retro checks which sub-scores and research factors predicted excess returns and may re-weight or redefine rubric components (or add a new factor from new signals). Guards: at most one rubric change per week, logged here with date, before/after and evidence; revert next week if the changed rubric's picks did worse. Rubric tweaks are allowed; the fixed limits (>= 6 bar, t >= 3 evidence bar, bet pool, stops, signal cap) are not changed without Wuyue's yes.
