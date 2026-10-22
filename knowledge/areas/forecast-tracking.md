# Forecast tracking & calibration — worker B, cycle 15 (2026-10-22 ~12:50 ET)
Cross-refs: BP-003/BP-R5 (LLM optimism and extrapolation), P-003/P-019 (market prices as priors), BR-003/PC-004 (P&L noise).
Tool: tools/forecast_log.py writes to forecasts/forecasts.csv. It has add, resolve and score commands, with flock. Outcomes can't be edited once resolved.

## Key findings
- **LLMs vs people:** LLMs forecast worse than superforecasters and about at public-crowd level (FT-001, FT-002).
- **Deviating from base rates is costly:** in near-efficient markets, deviating from the base rate without strong information *lowers* accuracy. Noise of sd 0.10 is enough to turn Brier skill negative (FT-003).
- **Limits of a 2-week log:** 30–50 forecasts can catch gross miscalibration but can't prove skill (FT-004).

## Evidence strength
- ForecastBench is A (ICLR, peer-reviewed). Halawi et al. is B (arXiv).
- The simulations are B: they are mechanical and depend on the assumed sd.

## What doesn't apply
- Superforecaster-style teaming and training: a single agent can't do this, though "tracking" (keeping score) can be copied.

## Rule candidates
- **FT-R1:** Every trade's rationale_id gets a forecast row before the order: a probability, a base rate, and a resolve date. The base rate comes from tools data, e.g. P(10-day up) ~0.6 for SPY/QQQ. With no row, there's no trade (BP-R1, FT-003).
- **FT-R2:** Start forecasts at the market-implied number (prediction-market, options or base rate) and move at most ±0.10 without new primary-source information (FT-002/003, BP-R5).
- **FT-R3:** Run a weekly score. If Brier skill is below 0 after 20 or more forecasts, cut satellite size in half for the rest of the window (FT-003/004).
