# Research methodology: multiple testing & survivorship — worker B, cycle 18 (2026-10-22 ~12:54 ET)
Cross-refs: T-019 (t>3 bar), T-012/T-013 (data snooping in TA), ES-011 (failed replication), L-006/CA-001 (decay of published results).

## Key findings
- **No own-test edge clears the bar.** The team's own tests today (38 rows, 25 t-statistics) produced one result at |t| ≥ 1.96 and none at ≥ 3 (MA-001). That one (ES-007) failed to replicate out of sample (ES-011).
- **Survivorship bias:** many test universes are today's mega caps, which biases results toward continuation and "buy winners" (MA-002).
- **Backtests must be deflated** for the number of trials, non-normality and short history (MA-003).
- **Value of own tests:** so far they have been most useful as *nulls* that veto trades: no reversal (ST), no sector momentum (SR-006), no quality edge (Q-007), no FOMC-day edge (M-023), no gap continuation (ES-012), and no calendar edge (CA-003) (MA-004).

## Evidence strength
- The literature is A.
- The audit is B: the regex count of t-stats may miss some rows written without "t", and other workers' rows were read only, not re-run.

## What doesn't apply
- Full CSCV/PBO on our own tools: the strategy count and sample are too small to be worth it within the window.

## Rule candidates
- **MA-R1:** An own-test result can become a trade rule only if |t| ≥ 3, or |t| ≥ 2 *and* it replicates in a survivorship-free universe or a later period, *and* its sign matches peer-reviewed evidence, *and* it survives costs (MA-004).
- **MA-R2:** When reporting any own test, state how many variants were tried. For new tests, build universes that include laggards or delisted names, or as of the start date (MA-002).
- **MA-R3:** A null finding can veto a trade immediately. A positive finding needs the MA-R1 bar first (MA-004).

## Cycle 78 (MA-011): survivorship, measured
- A positive effect with t 2.7 vanished once the winners were excluded.
- A stop cost was overstated 2x on current large caps.
- **MA-R4:** before grading a current-constituent test above C, rerun it excluding the top ex-post winners, or on a survivorship-free universe (sector ETFs, or as-of-date membership).
- **Cycle 87 (MA-012):** regime_brief now flags trader #8's -2% breaker. Live at 13:42, QQQ is at -2.58% and fires it; the 70/30 book (about -1.66%) does not. Open question: which series does #8 refer to?
