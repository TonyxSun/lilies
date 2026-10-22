# Oil-shock regime — worker B, cycle 20 (2026-10-22 ~12:56 ET)
Cross-refs: FH-001 (Fed already hiking), P-019 (Dec hike ~76%), DD-001/002 (today's down day), M-015 (regime snapshot), SR-006 (sector rotation null).

## Key findings
- **Today's tape:** Brent is about $112 (futures; spot $115 on Oct 20), on its second spike of 2026 after the $138 April peak. Today's tape is risk-off: QQQ -2.6%, SMH -5.6%, VIX 18.8, and the 10y yield down 16 bp to 4.99% (OIL-001).
- **Why oil is moving matters.** Geopolitical "precautionary" spikes are the equity-negative kind (OIL-002, A).
- **History is weak and depends on the definition.** Near oil highs, SPY's 10- and 63-day returns ran below base, and chasing energy (XLE) underperformed. In "oil rebounding off a crash" regimes, the opposite held (OIL-003, C).
- **Today fits neither regime cleanly.** Use oil as an input for inflation, the Fed and volatility, not for direction (OIL-004).

## Evidence strength
- Kilian–Park is A.
- The own test is C: overlapping samples, a handful of independent episodes, and results sensitive to the definition.

## What doesn't apply
- Oil futures, energy leverage and inverse ETFs: these are outside the mandate or spirit (LE-R1).
- "Buy energy because oil is up": the own test and SR-006 both say no.

## Rule candidates
- **OIL-R1:** Don't add energy (XLE or oil names) as a satellite because oil is spiking. History shows energy lagging after oil highs, and sector momentum has no 2-week edge (OIL-003, SR-006).
- **OIL-R2:** Treat a Brent move of more than 5% in a day, or a new 3-month high, as an EVENT-GUARD trigger. No new satellite entries that day; the core holds (OIL-002, DD-R1).
- **OIL-R3:** Oil is the main live upside risk to the Dec hike odds. Re-run tools/pm_regime.py on any day Brent moves more than 5%, and act only on its flags (OIL-004, PM-R7).
