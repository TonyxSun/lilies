# Idle cash in a $1k Robinhood cash account: worker B, cycle 25 (2026-10-22 13:00 ET)
Cross-refs: E-007 (T+1), E-008 (freeriding), BP-R1 (default no trade), PC-001 (core-satellite).

## Key findings
- Sale proceeds in a cash account can't be reused until the next trading day, so every rotation costs a day out of the market (CS-001, A: Robinhood help page).
- T-bill parking earns about $0.47 on $300 over the window. That is trivial compared with the ~$1.35 expected drag of holding cash instead of SPY (CS-002).

## Evidence strength
- A for the platform rule. B for the arithmetic: the SPY expected return is a base rate, not a forecast, and the bill yield is as of Oct 20.

## What doesn't apply
- Robinhood Gold high-yield cash sweep: that is a subscription, and "no accounts or sign-ups" applies.
- Margin "instant settlement": margin is not allowed.

## Rule candidates
- **CS-R1:** Unallocated cash defaults to the SPY/QQQ core, not to bills, unless a buy is planned within 2 days. Cash drag vs the benchmark is the real cost (CS-002).
- **CS-R2:** Plan rotations as two-day operations: sell on day T, buy on T+1. Or fund new satellites from idle cash only, never by selling another position on the same day (CS-001, E-008).
- **CS-R3:** Never park cash in SGOV/BIL inside this 2-week window. The carry is worth less than $0.50 and it adds a settlement lock (CS-002).
