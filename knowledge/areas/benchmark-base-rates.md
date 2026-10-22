# Benchmark base rates: can a $1k book beat SPY *and* QQQ in 2 weeks? (owner 牛马; new area, item e; 12:38pm ET)
Tool: `tools/baserate_test.py`, read-only (Yahoo adjusted close; 44 current megacaps; 125 non-overlapping 10-day windows, 2021–26).

| Book | P(beat SPY) | P(beat SPY & QQQ) | sd vs SPY | 5th pct |
|---|---|---|---|---|
| 1 stock | 48% | 21% | 5.9% | −8.2% |
| 3 stocks EW | 52% | 25% | 3.4% | −4.9% |
| 5 stocks EW | 53% | 26% | 2.6% | −3.7% |
| 10 stocks EW | 54% | 27% | 1.8% | −2.6% |

- **QQQ vs SPY over 10 days:** QQQ is ahead 53% of the time; mean +0.10%, sd 1.76% (BR-002).
- **Survivorship bias:** this universe is today's winners, so the means are biased upward (BR-001).

## What follows
- A SPY/QQQ blend can't beat both benchmarks; it always lands between them. Beating both takes active deviation, and the base odds are about 1 in 4 per window (BR-002).
- The noise (sd 2.6–5.9%) swamps every documented edge here: the PEAD spread is about +1.1% over 10 days, and quality and sector effects are about zero (BR-003, ES-007, Q-004, SR-001).

## Rule candidates
- **BR-R1:** report every proposed position with its expected excess *and* the sd of its excess vs SPY. Never present a 2-week pick as "likely to beat," because no rule in this knowledge base lifts P(beat) meaningfully above 50–55%.
- **BR-R2:** if the goal really means beating both indexes, the core is QQQ-like (it ties QQQ and beats SPY 53% of the time). Active sleeves are small, low-correlation deviations. Trader owns the sizing.
