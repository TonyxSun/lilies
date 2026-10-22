# Rates regime (worker B), created 2026-10-22 13:12 ET, cycle 41

## Key findings
- **The stock-bond correlation is positive.** SPY/TLT is +0.39 over 60 days and +0.31 over 250 days, against a 2003-2026 median of -0.28. This matches the inflation regime in Campbell-Sunderam-Viceira, so bonds are not a reliable hedge right now (RR-001 A, RR-002 B).
- **Yield moves don't time equities.** The 20-day change in the 10y does not predict SPY or QQQ over the next 10 days (t -1.23 / -0.23, non-monotonic) (RR-003 B).
- **The level is extreme but not a signal.** The 10y closed at 5.15% yesterday and was ~4.98% live today. It has closed ≥5% on only 22 days since 2008 (RR-004).

## Evidence strength
- RR-001: published (A).
- RR-002/003: own long-sample tests (B). RR-003 is a null.

## What doesn't apply
- Bond duration trades and rate futures (not allowed in the mandate).
- TLT is an allowed ETF, but adding it as a "hedge" would add tracking error against two equity benchmarks while its hedging value is currently weak (RR-002).

## Rule candidates
- **RR-R1:** Don't add TLT, other long bonds or cash as a crash hedge. In the current positive-correlation regime they hedge poorly, and they create benchmark tracking error (RR-001/002, OE-R3).
- **RR-R2:** Don't rotate between SPY and QQQ on yield moves (RR-003, OE-006).
- **RR-R3:** Treat yields ≥5% as a volatility input (EVENT-GUARD context and VX sizing), not a directional signal (RR-003/004).
- **Cycle 62 (RR-005):** the 10y fell to ~4.96% intraday on Oct 22, from the 5.15% Oct 21 close. That's a flight-to-safety move, and the RR-R3 flag is off intraday. Still no rotation (RR-R2).
