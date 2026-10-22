# Extended hours & after-close events — worker B, cycle 14 (2026-10-22 ~12:48 ET)
Cross-refs: E-004 (fractional mechanics), R-011 (stop orders), M-014 (AMC earnings calendar), OS-006 (MSFT implied move), ES-004.

## Key findings
- **Robinhood rules (EH-001):**
  - Extended hours run 7–9:30 AM and 4–8 PM ET, limit orders only.
  - Fractional shares can trade in extended hours only for eligible names (4–7:30 PM).
  - **Stops never execute outside regular hours.**
- **Stops don't help through earnings (EH-002).** Every big catalyst in our window is after the close, so a stop-loss fills at the next open, often well through the stop.
- **AH moves are mostly real (EH-003, EH-004).** The AH move is mostly the real repricing: 17 of 22 kept their sign, with a median of 0.88× by the next close. Buying the next open in the AH direction showed no edge. Post-close quotes are noisy and costs are 4–5× daytime.

## Evidence strength
- Robinhood mechanics are A (primary docs, fetched today).
- Barclay–Hendershott is A but uses 2000-era data; spreads are tighter now, but the direction still holds.
- The own test is C: n=22, one earnings season, and Yahoo's last-print data rather than quotes.

## What doesn't apply
- Overnight-return anomalies (night vs day returns): those are long-short and cost-heavy.
- Trading AH to "get ahead" of the move: limit-only, wide spreads and no edge (EH-004).

## Rule candidates
- **EH-R1:** Don't hold a position through an AMC/BMO earnings release unless its size passes the gap test: weight × implied move (e.g. MSFT ±5.3%, OS-006) × 2 ≤ the max single-event loss (~$15–20 on $1k). Don't rely on a stop (EH-001/002).
- **EH-R2:** No extended-hours or 24-hour-market orders. Trade only in regular hours, at least 15 minutes after the open, using limit orders (EH-003/004, E-004).
- **EH-R3:** After an AH earnings move in a holding, don't chase or fade at the open. Re-check the thesis by the close of day 1 (EH-004; cf. ES-007 drift evidence).
