# Morning execution (worker B), created 2026-10-22 13:13 ET, cycle 42

## Key findings
- **Overnight carries the return.** SPY and QQQ earn ~3-5bp per overnight (t 2.3-4.9) and ~0-3bp intraday (MX-001). This is consistent with N-003.
- **The 9:45 fill costs almost nothing.** Filling at ~9:45 the next morning instead of the decision-day close costs about one overnight, ≈--.03-0.05 on cd /workspace/lilies-knowledge && python3 /tmp/addrow.py <<'EOF'
[["MX-001","morning-execution","Own test (Yahoo daily OHLC, price-only, so ex-dividend drops fall overnight and understate it): SPY 1993+ averaged +3.3bp per overnight (t 4.59) vs +0.7bp intraday (t 0.71); 2015+ it was +3.0bp (t 2.29) vs +2.1bp (t 1.35). QQQ 1999+: +5.3bp overnight (t 4.92) vs -0.0bp intraday; 2015+: +4.7bp (t 2.99) vs +2.8bp. This matches Lou-Polk-Skouras (N-003). Buying a core position at the next morning's ~9:45 fill instead of the decision-day close gives up about one overnight, ≈3-5bp, or $0.03-0.05 on $1,000. The morning re-check is effectively free.","B","sources/morning_execution_2026-10-22.txt","warm"],
["MX-002","morning-execution","Own test (same data): gaps do not reliably continue or reverse. Open→close after a ≤-1% gap: SPY +10.4bp (n=382, t vs base 1.00); 2015+ +11.0bp (t 0.79); QQQ +16.4bp (n=553, t 1.57). After a ≥+1% gap, SPY 1993+ showed +19.2bp (t 2.12), but this fails out of sample (2015+ t 0.96; QQQ t 0.45), so it does not pass MA-R1. Open→10-day returns after gap-down days were not worse than base (SPY +0.86% vs +0.39%; QQQ +0.35% vs +0.49%).","B","sources/morning_execution_2026-10-22.txt","warm"],
["MX-003","morning-execution","Implication for the 9:45 re-check in strategy.md: an overnight gap in SPY or QQQ is not, by itself, a reason to cancel, resize or chase a planned core buy (MX-002). Re-check items should be thesis-level facts (news, earnings dates, rule limits), not the gap. For single stocks with big prior-day moves or news, Berkman et al. (N-024) find buying at the open is costly, which argues for limit orders or waiting past the open for satellites only.","B","MX-001/002; N-024","warm"]
]
EOF
cat > areas/morning-execution.md <<EOF
# Morning execution (worker B), created 2026-10-22 $(date +%H:%M) ET, cycle 42

## Key findings
- **Overnight carries the return.** SPY and QQQ earn ~3-5bp per overnight (t 2.3-4.9) and ~0-3bp intraday (MX-001). This is consistent with N-003.
- **The 9:45 fill costs almost nothing.** Filling at ~9:45 the next morning instead of the decision-day close costs about one overnight, ≈$0.03-0.05 on $1,000, so the re-verify step is worth keeping (MX-001).
- **Gaps don't predict.** SPY/QQQ gaps don't reliably continue or reverse intraday or over 10 days. The one t>2 cell (SPY gap-up 1993+) fails 2015+ and fails on QQQ (MX-002).

## Evidence strength
- Own long-sample tests (B).
- Price-only data, so dividends are booked overnight. The SPY yield is about 0.5bp/day, which doesn't change the sign.
- Daily OHLC only: the 9:30→9:45 slice isn't observed, and the open is used as a proxy for the 9:45 fill.

## What doesn't apply
- Intraday-momentum trading (Gao et al.), which needs intraday execution the loop doesn't do.
- Overnight-only holding strategies, which turn over daily and fail costs (L-016).

## Rule candidates
- **MX-R1:** At the 9:45 re-check, an index gap alone never cancels or resizes a planned SPY/QQQ buy. Re-check facts, not price (MX-002/003).
- **MX-R2:** For satellites after a big prior-day move or news, use a limit order or wait until after ~10:00; don't send a market order at the open (N-024, MX-003). Grade B/C.
- **MX-R3:** Don't add an "enter at the close" step to chase the overnight drift. It's worth ≈3-5bp, smaller than the value of the re-check (MX-001).
EOF
cat > cycles/42-review-B.md <<EOF
# Cycle 42 review (worker B): morning execution, $(date +%H:%M) ET
Done: sources/morning_execution_2026-10-22.txt; MX-001..003; areas/morning-execution.md; INDEX.md.
Learned: the strategy's next-morning fill costs ~3-5bp, which is negligible, and gap size shouldn't drive the re-check. This directly supports tomorrow's (Oct 23) first 9:45 step.
Next: cycle 43.
EOF
python3 /tmp/idxmd2.py '{"areas/morning-execution.md":"B cycle 42"}'; awk -F'\t' 'NF!=7' INDEX.tsv | wc -l; date +%H:%M,000, so the re-verify step is worth keeping (MX-001).
- **Gaps don't predict.** SPY/QQQ gaps don't reliably continue or reverse intraday or over 10 days. The one t>2 cell (SPY gap-up 1993+) fails 2015+ and fails on QQQ (MX-002).

## Evidence strength
- Own long-sample tests (B).
- Price-only data, so dividends are booked overnight. The SPY yield is about 0.5bp/day, which doesn't change the sign.
- Daily OHLC only: the 9:30→9:45 slice isn't observed, and the open is used as a proxy for the 9:45 fill.

## What doesn't apply
- Intraday-momentum trading (Gao et al.), which needs intraday execution the loop doesn't do.
- Overnight-only holding strategies, which turn over daily and fail costs (L-016).

## Rule candidates
- **MX-R1:** At the 9:45 re-check, an index gap alone never cancels or resizes a planned SPY/QQQ buy. Re-check facts, not price (MX-002/003).
- **MX-R2:** For satellites after a big prior-day move or news, use a limit order or wait until after ~10:00; don't send a market order at the open (N-024, MX-003). Grade B/C.
- **MX-R3:** Don't add an "enter at the close" step to chase the overnight drift. It's worth ≈3-5bp, smaller than the value of the re-check (MX-001).
