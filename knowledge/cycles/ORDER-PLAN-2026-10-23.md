# ORDER PLAN: Fri 2026-10-23 (final evening sizing, Trader, written ~6:45pm ET Thu 10/22)
**PLAN ONLY. No orders placed.** Every order needs Wuyue's explicit OK plus a Robinhood order-review screenshot first. Re-checked pre-open ~9:15am ET Fri with premarket prices.
Earlier draft (4:10pm + 4:16pm decision + 4:40pm update) kept at cycles/ORDER-PLAN-2026-10-23.draft-1641.md. Inputs: cycles/NEWS-CANDIDATES-2026-10-23.md (牛马 facts, ~4:50pm ET), TRADE-SCORING.md, Notion Condensed rules (read 6:42pm ET).

## 0. Account (Robinhood MCP, read-only, 6:40pm ET 10/22)
- Total value $0, cash $0, buying power $0, unsettled $0, pending deposits $0, no positions. **Still unfunded.**
- Sizes below assume $1,000. At 10:00am ET Fri re-read settled buying power and scale every line pro rata. If it is still $0, nothing is placed.

## 1. Ranked scores (final, Trader; 牛马's scores were reference, I agree with all of them)
| Rank | Idea | Evid | Edge | Cat | Setup | Risk | Total | Call | Reason |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ELV long | 0 | 0 | 2 | 2 | 2 | 6 | TAKE | Beat + FY26 raise (release/8-K 10/21), muted reaction, above 200-day (370.77); stop 426 on $100 = ~0.4% of account; no tested edge |
| 2 | SMH dip buy (after -6% day) | 2 | 1 | 1 | 2 | 0 | 6 | TAKE | Tested t 2.02, +2.03% vs QQQ over 50 days after costs; adds semis to a QQQ-heavy core and 12% stop on 10% = 1.2% risk |
| 3 | LMT long | 0 | 0 | 1 | 2 | 2 | 5 | SKIP | Real beat-and-raise 10/22, but the +7% day already priced most of it; large-cap drift null |
| 4 | TXN long | 0 | 0 | 2 | 2 | 1 | 5 | SKIP | Beat + guide above, but semi beta stacked on the QQQ-heavy core |
| 5 | IWM year-end tilt | 2 | 1 | 0 | 0 | 2 | 5 | SKIP | Setup 0: closed 276.67, below its 200-day (277.06 adj); recheck daily through 10/30 |
| 6 | R pullback | 0 | 0 | 1 | 0 | 2 | 3 | SKIP | Setup 0: above the <=258 pullback range |
| 7 | PSQ / SH | 0 | 0 | 0 | 1 | 2 | 3 | SKIP | No dated bearish catalyst; tested triggers lost vs cash |
Tie-break ELV vs SMH: ELV has lower correlation with the core, so ELV first.

## 2. Latest Robinhood quotes (get_equity_quotes, pulled 6:40pm ET 10/22)
| Ticker | Last regular (3:59pm ET) | After-hours last (time ET) | AH bid / ask (time ET) | 10/21 close |
|---|---|---|---|---|
| QLD | 86.24 | 86.17 (6:40pm) | 86.14 / 86.17 (6:40pm) | 91.46 |
| SPYM | 89.92 | 89.99 (6:33pm) | 89.97 / 90.13 (6:39pm) | 90.99 |
| ELV | 445.45 | 445.28 (4:08pm) | 436.60 / 447.88 (6:34pm, wide) | 434.13 |
| SMH | 523.16 | 522.92 (6:38pm) | 522.50 / 523.36 (6:38pm) | 556.70 |
| IWM (skip) | 276.69 | 276.83 (6:33pm) | 276.92 / 276.98 (6:40pm) | 276.48 |
| LMT (skip) | 590.205 | 588.39 (6:39pm) | 587.52 / 589.86 (6:35pm) | 551.51 |
| TXN (skip) | 279.50 | 278.42 (6:04pm) | 277.79 / 279.75 (6:40pm) | 284.65 |
| R (skip) | 265.89 | 265.53 (4:00pm) | 260.35 / 269.00 (6:32pm) | 240.31 |
| QQQ (ref) | 704.59 | 704.26 (6:38pm) | 704.20 / 704.28 (6:40pm) | 725.20 |

## 3. Take list for Fri 10/23 (sized at $1,000; window 10:00am-3:30pm ET, regular hours only)
| # | Ticker | Side | Size | Order type | Condition / limit | Window (ET) | Stop / exit |
|---|---|---|---|---|---|---|---|
| 1 | QLD (core) | Buy | 3 shares (~$259, ~26%) | Limit, day, whole shares | <= live ask + 0.1% | 10:00-15:30 | No price stop; 30%-from-high review; month-end switch to QQQM if QQQ closes below its 200-day (first check Fri 10/30) |
| 2 | SPYM (core) | Buy | 3 shares (~$270, ~27%) | Limit, day, whole shares | <= live ask + 0.1% | 10:00-15:30 | Core, no stop |
| 3 | SPYM (core top-up) | Buy | ~$65 (~6.5%) | Market, dollar/fractional | Only after #2 fills; spread <= $0.02 | 10:00-15:30 | Core, no stop |
| 4 | ELV | Buy | $100 (10%) | Market, dollar/fractional | Fresh quote 431.67-455; skip if outside or if it opens >3% gap | 10:00-15:30 | Close < 426 -> sell at 3:45pm check; hard stop max(0.8x high close, high - 5xATR14) |
| 5 | SMH | Buy | $100 (10%) | Market, dollar/fractional | Only if live >= 507.65 (0.97 x 523.35 official close; recompute from RH official close Fri) | 15:25-15:30 | Exit ~50 trading days (~Jan 5) or Dec 31, or close >12% below entry |
**Totals if all fill:** core ~$594 (~59%) + bets $200 (20%) = ~$794; **cash ~$206 (~21%)**. Bet pool ~40% is only half used because just two ideas scored >= 6.

## 4. Core fixes and exits due
- None due: no positions yet. No month-end QLD switch check until 10/30. VIX/VIX3M closed 0.946 (Yahoo, 4:37pm ET per 牛马); recheck pre-open (>= 0.95 is not a no-buy trigger per VX-002, context only).
- Own-account -2% day / -8% from high breakers: not applicable until funded.
- No -2x/-3x inverse funds. Every order: review_equity_order -> screenshot -> Wuyue OK -> place.

## 5. Change vs what's already in the chat
None. Same as the 4:40pm update (QLD 3 sh + SPYM ~$335 + ELV $100 + SMH $100, ~$200 cash). Open item: account still $0; funding needed before 10:00am ET Fri.

## Update 1:20am ET Oct 23 (Trader decision)
- SMH $100 dip buy: DROPPED. New evidence bar (t >= 3, TRADE-SCORING.md "Evidence bar") and AE-R5 (dip buys only scored when VIX > 1-yr 80th pct or > 25). SMH dip test was t 2.02; VIX closed 19.03 (75.8th pct, line 19.54). The $100 stays cash.
- ELV news trade: re-score at 9:18am against the new bar; keep only if it still scores >= 6.
- Core (QLD 3 sh, SPYM ~$335) unchanged. Overnight tests AE-001..AE-007: 0 passes (backtests/2026-10-23-ai-edge*, areas/ai-edge.md).
