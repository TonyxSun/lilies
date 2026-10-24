# ORDER PLAN: Mon 2026-10-26 (evening sizing, Trader, written ~6:40pm ET Fri 10/23)
Plan only, no orders placed tonight. Standing approval (10/23 12:35am ET) covers placing these on Monday inside the fixed limits; Wuyue is told after.
Inputs: cycles/NEWS-CANDIDATES-2026-10-26.md (牛马 facts, ~4:45pm ET), TRADE-SCORING.md, Notion Condensed rules (read 6:33pm ET), Robinhood read-only (6:31pm ET), technicals/implied moves in cycles/research-1026/tech.csv (yfinance, pulled 6:32pm ET), news via Reuters/CNBC/WSJ 10/23 evening.

## 0. Account (Robinhood, read-only, 6:31pm ET 10/23)
- Account value $999.87; cash $47.36; buying power $47.36; **$1,000 deposit still pending**. Settled cash: $0 (all holdings and cash came from the pending deposit; see tools/settlement.csv).
- Positions: QLD 6 sh avg 86.49; SPYM 3.725703 sh avg 89.56; ELV 0.227357 sh avg 439.84.
- Breakers: book -0.24% on 10/23 (no -2% day), far above the $920 floor. GFV count 0. Signals used Mon: 0/4.

## 1. Ranked shortlist (first score, then post-research score; Evid/Edge/Cat/Setup/Risk)
| Rank | Idea | Evid | Edge | Cat | Setup | Risk | First | Research | Call | One-line reason |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IWM year-end tilt | 1 | 1 | 0 | 0 | 2 | 4 | 4 | SKIP | Below 200-day; PB-003 t 1.97 is capped at Evidence 1 by the 10/23 bar |
| 2 | BCPC long | 0 | 0 | 2 | 0 | 2 | 4 | 4 | SKIP | LATE attention veto; news trades paper-only (HOT 10) |
| 3 | XLE oil leg | 0 | 0 | 1 | 1 | 2 | 4 | 4 | SKIP | Real oil shock, but no tested edge (AE-007) and already at a record high |
| 4 | BNO oil leg | 0 | 0 | 1 | 1 | 2 | 4 | 4 | SKIP | Same read; +19% in 20 days, roll cost, two-way weekend gap |
| 5 | LMT long | 0 | 0 | 1 | 0 | 2 | 3 | 3 | SKIP | Above its entry range; beat-and-raise mostly priced |
| 6 | TXN long | 0 | 0 | 0 | 2 | 1 | 3 | 3 | SKIP | Catalyst stale by Mon (Evid 0 + Cat 0 = skip); semis overlap QLD |
| 7 | SH 1x hedge | 0 | 0 | 0 | 1 | 2 | 3 | 3 | SKIP | No dated bearish catalyst; tested inverse triggers lost (AG-009 t -3.3) |
| 8 | BAH long | 0 | 0 | 2 | 0 | 1 | 3 | 3 | SKIP | LATE attention veto; below its 252-day high by 22% after a long slide |
| 9 | GLD | 0 | 0 | 0 | 0 | 2 | 2 | 2 | SKIP | Below 200-day; no tested edge |
| 10 | TLT (my idea) | 0 | 0 | 0 | 0 | 2 | 2 | 2 | SKIP | Below 200-day; FOMC 10/28 is a coin flip, no edge |
| 11 | SMH dip | 0 | 0 | 0 | 1 | 0 | 1 | 1 | SKIP | VIX 19.45 under its 1y 80th pct (19.54), so dip rule scores Evidence 0 |
| - | ELV (held) | | | | | | | | HOLD | Not re-scored; hold rule: stop close < 426 or exit by Fri 10/30 close |
Nothing reaches 6, so no new bets. Cash stays cash (HOT 15).

## 2. Research per name
- **IWM.** Close 275.75 vs 200-day 277.17 (Yahoo adj) / 278.23 (牛马's figure), 50-day 286.09, -2.2% over 20 days, relvol 0.80. Implied move to 10/30 ±2.4% (ATM straddle 6.57). Corr with SPY 0.74 over 60 days, so it adds little diversification. Bear case: small caps are rate-sensitive with the 10-year near 5%. Only a close above the 200-day reopens it; recheck daily through 10/30.
- **BCPC.** Record Q3 (8-K 10/23 7:21am ET, sales +8.6%, adj EPS $1.57 vs $1.35), +2.2% day, relvol 2.2x, X pace 3.7x so attention_timing calls it LATE. Implied move to 11/20 ±14% (thin chain, wide AH quote 173.55/180.45). Low corr with the book (0.05 vs SPY). Bear case: no guidance, momentum already chased. Vetoed by the LATE rule and paper-only rule.
- **XLE.** Brent settled $116.72 (+3.1%, highest since 4/29) and WTI $103.27 after Houthi attacks in Saudi Arabia and Iran's threats to Gulf targets (Reuters, CNBC, WSJ 10/23). S&P energy hit a record. XLE 69.33 at a 252-day high, +11.8% in 20 days, far above its 200-day 57.58; corr -0.33 with QQQ, so it would hedge the core's oil risk. Bear case: one de-escalation headline over the weekend gaps it down; AE-007 found no tested edge after geopolitical spikes. No options read pulled (yfinance chain error).
- **BNO.** Same story, more extreme: +19% in 20 days, 70.99 vs 200-day 48.78, ATR 2.6%, futures roll cost, AH spread 70.70/72.00. Corr -0.56 with QQQ. Same skip.
- **LMT.** Q3 release 10/22: sales +11% to $20.7B, EPS $7.97 vs $7.52 est., record $292B backlog, second straight guide raise (IR release). 10/23: price-target raises (UBS 692, Citi 706, RBC 600, Barclays 560 per Yahoo/The Fly) and a 10-year F-35 framework that is not yet a contract. Close 604.18, above the 577.50-601 entry range, +9.4% in 5 days, 200-day 560.99, still 10% below its 252-day high. No options read (chain error). Bear case: large-cap drift is null (NS-001, ES-011) and ITA fell 1.1% on 10/23. Setup 0 = skip.
- **TXN.** Beat and Q4 guide above estimates (10/21, three sessions old Monday). Close 284.69 above 200-day 255.34 and 50-day 272.40, relvol 1.09. Implied move to 10/30 ±5.2%. Corr 0.53 with QQQ, stacking on QLD into MSFT/GOOGL (10/28). Bear case: analog semis still 14% below their 252-day high and Thursday's AI selloff can return.
- **SH.** 32.66 (+0.62%), below its 200-day. A weekend hedge is tempting with Iran risk, but no dated bearish catalyst, VIX/VIX3M 0.9497 (no inversion), and our tested inverse triggers lost to cash. Not rule-backed.
- **BAH.** FY27 adj EPS guide raised to $6.50-6.70 (8-K 10/23 6:48am ET) but revenue -3.9% y/y; stock -0.3% on the day, above 200-day 75.98, relvol 2.1x and StockTwits 32.6x, so LATE. Implied move to 11/20 ±9.3%. Skip.
- **GLD.** 366.61, below 200-day 414.21 and down 6.8% in 20 days as yields and the dollar rose; gold did not act as a war hedge this week. Skip.
- **TLT.** 81.34, below 200-day 83.31; 10-year ~4.99-5.00%. Oil-driven inflation fear versus the AI-capex growth scare pull in opposite directions into FOMC 10/28. Implied move to 10/30 ±1.4%. No edge.
- **SMH.** 527.20 after a -6% Thursday and +0.74% Friday; below its 50-day 575, above 200-day 515. VIX is just under the stressed threshold, so the dip rule doesn't count. Implied move to 10/30 ±5.0%, corr 0.87 with QQQ. Skip.

## 3. Take list for Mon 10/26
**No new buys.** Nothing scored >= 6, and buying power is only $47.36 anyway.

## 4. Core fixes and exits due
| # | Ticker | Action | Condition | Order type | Window (ET) | Latest Robinhood quote |
|---|---|---|---|---|---|---|
| 1 | QLD | Sell 3 sh (trim duplicate, back to 3 sh) | Only if get_portfolio shows pending_deposits = 0 (deposit cleared). If still pending, hold and re-check each day; selling earlier is a good-faith violation for a non-stop reason | Limit, day, whole shares, at live bid - 0.1% | 10:00-15:30 | 4:00pm last 86.1365; AH last 86.45 (6:29pm); AH bid/ask 86.41/86.80 (6:30pm) |
| 2 | QLD | Stop | Close <= 73.52 (-15% from 86.49), checked 3:45pm from Mon | Limit at bid | 15:45 | as above |
| 3 | ELV | Stop / time exit | Close < 426, or exit by Fri 10/30 close | Market (fractional) | 15:45 check | 4:00pm last 439.75; AH bid/ask 430.00/439.95 (5:23pm, wide) |
| 4 | SPYM | Hold (core, no stop) | | | | 4:00pm last 89.44; AH bid/ask 89.57/89.61 (6:31pm) |
| 5 | QLD -> QQQM | Month-end switch check | Only if QQQ closes below its 200-day at month end (first check Fri 10/30). Now QQQ 704.40 vs 200-day ~676.10 (Yahoo adj), so no switch | | | QQQ AH 705.28 (6:31pm) |
QLD trim proceeds settle T+1 and stay cash; no reinvestment until a candidate scores >= 6 (or the core plan is revisited).

## 5. Monday pre-open gates (9:15am run)
- Geopolitical gate: major weekend escalation AND futures down >= 1.5% or Brent up >= 5% => no bets (none planned) and core stays as is. Futures down >= 3% => buy nothing.
- Earnings guard: MSFT/GOOGL report 10/28 after the close; no new positions in them Mon/Tue. FOMC 10/28 2:00pm.
- Re-read 牛马's ~10pm overnight checks (Sun night) before the pre-open run.
