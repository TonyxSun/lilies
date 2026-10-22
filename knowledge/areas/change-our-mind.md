# What would change our mind: evidence that would justify moving beyond SPY/QQQ (owner 牛马, 10/22 about 2:20pm ET)
Status quo: the core is SPY/QQQ. Active picks are small, sd-labelled deviations (BR-001/002, OE-001..006). Every item below is a specific, checkable trigger. None of them is a trade instruction; Trader owns sizing, and Wuyue owns the objective.

| # | Evidence that would change our mind | What it would justify | Where we are now | Ids |
|---|---|---|---|---|
| 1 | **Objective change.** Wuyue defines success as beating the better of SPY/QQQ, or as excess over a 50/50 blend, rather than beating both. | Active deviation sized to a stated tracking error. Under the current target, any SPY/QQQ mix beats both 0% of the time. | Open question | OE-004, OE-005, BR-001 |
| 2 | **Our own forward log.** At least 20 mechanically pre-registered EARLY reads (catalyst_calendar.py criteria fixed before the event) with mean 10-day excess vs IWM above +1% after measured spread, t ≥ 2, and LATE reads at or below 0 | A real news sleeve (Trader's 2-3% sizes, 10% cap) | 0 logged events; the 10/22 run had 0 clean EARLY positives | NS-R1, NS-004, S-002, OE-002 |
| 3 | **Post-2016 drift in our cap range.** A peer-reviewed or own cost-adjusted test showing ≥5-day drift above the NYSE 20th percentile after 2016 | PEAD-style holds beyond day 1 | Martineau and Chordia say no; own tests (ES-011) say no | NS-001, NS-002, ES-011 |
| 4 | **Underreaction class.** A catalyst type with ≤1% day-1 reaction to a ≥25% beat plus raised guidance (IRDM-type) that drifts more than 2× round-trip cost over 10 sessions in at least 15 own cases | A targeted "ignored good news" rule | Anecdotal (IRDM 10/20) | NS-013, UV-008 |
| 5 | **Short-horizon quality.** The junk veto showing t ≥ 2 at 10-63 days in mid/small caps, not only at 12 months | Quality as an alpha tilt, not just a veto | Null at 10-63 days in large caps; +9-10% at 12 months | Q-007, UV-009, UV-010 |
| 6 | **Regime break.** Trend and credit breaking together (S&P below its 200-DMA and HY OAS widening by more than about 150bp in a month) | Defensive deviation: cut equity beta. This moves beyond SPY/QQQ toward cash or T-bills | Not triggered | M-003, M-008 |
| 7 | **Opportunistic insider cluster.** At least 2 non-routine insiders buying ≥$100k each within 30 days, in a sleeve name passing the news profile, with an EARLY read | A watch-list entry for Trader | NPB has a CEO-only buy, above the current price, with bad news | NS-007, IN-001, NS-014 |
| 8 | **A valuation or macro predictor that survives Goyal-Welch-Zafirov out-of-sample** at 1-month or shorter horizons | Market timing or a sector tilt | Nothing survives; own sector test null (t ≤ 0.87) | SR-007, SR-008, SR-009, M-019 |
| 9 | **Costs.** Live measured quoted spreads at or below 0.2% plus our own fill-slippage log for sleeve names | Lower hurdles; more of the evidence would clear costs | First live spreads logged 10/22 (cycles/09-*) | NS-018+, UC H5 |
| 10 | **Index-add or FDA pre-event setups.** Own evidence of a pre-announcement run-up we can capture (announcement-to-effective drift, net of the day-1 reversal) | A pre-event sleeve trade | Literature: priced by day 1, then reversal | NS-005, NS-006 |

Note 10/22, 2:30pm ET: our own backtest of the CC-003 EARLY read was null (CC-007; EARLY-up -0.19% over 10 sessions vs IWM, t -1.08). The news-sleeve trigger therefore rests on the forward paper log alone.

Rule CM-R1: a trigger counts only if (a) its criteria were written down before the data arrived, (b) it holds after measured costs, and (c) it is logged in INDEX.tsv with a source. Backtests alone move an item at most to "warm".
