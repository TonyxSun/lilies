# Whole-share execution on $1,000 (worker B), created 2026-10-22 13:19 ET, cycle 49

## Key findings
- **SPY/QQQ can't form the A1 split in whole shares on $1,000.** SPY is $763 and QQQ $707 (WS-001).
- **1 VOO + 1 QQQM = $992.30** gives 71/29, 99.2% invested, in whole shares with ordinary limit orders and the same indexes as the benchmarks (WS-001).
- **Fractional SPY/QQQ orders are Not-Held, market-price executions in RTH.** Fractional limit support during RTH is unverified (WS-002).
- **Only $7.70 of slack.** If prices rise ~0.8% before the fill, the pair doesn't fit. The fallback is 7 SPYM + 1 QQQM (68/32, 92% invested) (WS-003).

## Evidence strength
- B: live prices and Robinhood help pages.
- The fractional-limit point is unverified.

## What doesn't apply
- Tax-lot or wash-sale issues of VOO vs SPY (paper account).

## Rule candidates
- **WS-R1:** Implement A1 as 1 VOO + 1 QQQM (whole shares, limit orders), not fractional SPY/QQQ. Same indexes, near-full investment, and it avoids Not-Held fractional market orders.
- **WS-R2:** Re-check that the pair fits in cash at 9:45. If VOO + QQQM > ~$998, use 7 SPYM + 1 QQQM.
- **WS-R3:** Score the retro against SPY/QQQ as mandated. VOO/QQQM tracking difference is noise (PC-006).

## Cycle 50: tracking check (WS-004)
- VOO+QQQM vs SPY/QQQ 70/30: 10-day difference SD ~5.6bp, mean ~0.
- The only large deviation was a one-day close-print artifact (2025-04-09) that reversed the next day.
- The proxies are fine for scoring against SPY/QQQ.

## Cycle 60: spreads (WS-005)
- Quoted spreads are about 1bp on VOO and QQQM, roughly $0.04 total on the pair.
- Watch out: CBOE CDN files can be stale (hours old). Check the timestamp before trusting a quote.

## Cycle 63: fractional orders are market-only (WS-006)
- Through the agentic interface, fractional and dollar-based orders are type=market, regular hours only. No limits, no stops.
- **WS-R4:**
  - Satellites priced above ~$100 must be fractional market orders. Enter after ~10:00 ET (MX-R2's timing half still applies) and paper-fill with the RM-003 haircut.
  - Satellite stops on fractional positions are checked at the 9:45 re-check and executed as market sells. They don't rest as stop orders.
- Open question for Wuyue: should the paper ledger mirror these broker constraints? Recommended: yes.
