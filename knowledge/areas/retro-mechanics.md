# Retro mechanics (worker B), created 2026-10-22 13:14 ET, cycle 43

## Key findings
- **No benchmark dividends in the window.** Neither SPY nor QQQ goes ex-dividend between Oct 22 and Nov 5, so price return equals total return for the retro (RM-001).
- **The calculation spec.** Same start mark for us and the benchmarks; idle cash earns 0%; fill prices from the paper log; report excess vs SPY, QQQ and the 50/50 blend, together with the process score (RM-002, OE-R1/R4).
- **Costs.** Commission --. The SEC fee is 0.60 per cd /workspace/lilies-knowledge && python3 - <<'EOF'
import csv,fcntl
with open('INDEX.tsv','r+',newline='') as f:
    fcntl.flock(f,fcntl.LOCK_EX); rows=list(csv.reader(f,delimiter='\t'))
    for r in rows:
        if r[0]=='RM-003': r[3]=r[3].replace('(cents on a $1,000 account; current rates not verified this cycle)','(the SEC fee is ≈$0.02 per $1,000 sold, see RM-004; FINRA TAF not verified)'); r[5]=r[5].replace('Robinhood fee schedule not re-fetched (unverified rates)','RM-004; FINRA TAF unverified')
    f.seek(0); f.truncate(); csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows); fcntl.flock(f,fcntl.LOCK_UN)
EOF
python3 /tmp/addrow.py <<'EOF'
[["RM-004","retro-mechanics","SEC Section 31 fee advisory (Feb 27 2026): $20.60 per $1M of covered sales from April 4 2026 ($0.00 before that). The rate stays until 60 days after the FY2027 appropriation is enacted; whether that has happened was not checked. On a $1,000 sale it is ≈$0.02, immaterial to the retro.","A","https://www.sec.gov/rules-regulations/fee-rate-advisories/2026-2","cold"]
]
EOF
cat > areas/retro-mechanics.md <<EOF
# Retro mechanics (worker B), created 2026-10-22 $(date +%H:%M) ET, cycle 43

## Key findings
- **No benchmark dividends in the window.** Neither SPY nor QQQ goes ex-dividend between Oct 22 and Nov 5, so price return equals total return for the retro (RM-001).
- **The calculation spec.** Same start mark for us and the benchmarks; idle cash earns 0%; fill prices from the paper log; report excess vs SPY, QQQ and the 50/50 blend, together with the process score (RM-002, OE-R1/R4).
- **Costs.** Commission $0. The SEC fee is $20.60 per $1M of sales, ≈$0.02 per $1,000 (RM-004 A). The real cost is the spread, so paper fills need a stated haircut (RM-003 C).

## Evidence strength
- RM-001 B (Yahoo events).
- RM-004 A (SEC).
- RM-002 is a design spec.
- The RM-003 haircut is judgment.

## What doesn't apply
- Money-weighted return (no external flows).
- Benchmark dividend reinvestment (none in the window).

## Rule candidates
- **RM-R1:** The benchmark start is the same timestamp as ours (Oct 22 close), not the first fill. Deployment delay counts against us.
- **RM-R2:** Apply a fixed paper-fill haircut (5bp per side on ETFs, 10-20bp on single stocks), stated in the retro.
- **RM-R3:** Every retro reports the process score next to excess return. The result alone can't show skill (OE-002).
EOF
cat > cycles/43-review-B.md <<EOF
# Cycle 43 review (worker B): retro mechanics, $(date +%H:%M) ET
Done: RM-001..004; areas/retro-mechanics.md; INDEX.md. RM-003 was revised after verifying the SEC rate.
Useful for: the first Friday retro (Oct 23). The spec is ready to hand to the trader.
Next: cycle 44.
EOF
python3 /tmp/idxmd2.py '{"areas/retro-mechanics.md":"B cycle 43"}'; awk -F'\t' 'NF!=7' INDEX.tsv | wc -l; date +%H:%MM of sales, ≈--.02 per cd /workspace/lilies-knowledge && python3 - <<'EOF'
import csv,fcntl
with open('INDEX.tsv','r+',newline='') as f:
    fcntl.flock(f,fcntl.LOCK_EX); rows=list(csv.reader(f,delimiter='\t'))
    for r in rows:
        if r[0]=='RM-003': r[3]=r[3].replace('(cents on a $1,000 account; current rates not verified this cycle)','(the SEC fee is ≈$0.02 per $1,000 sold, see RM-004; FINRA TAF not verified)'); r[5]=r[5].replace('Robinhood fee schedule not re-fetched (unverified rates)','RM-004; FINRA TAF unverified')
    f.seek(0); f.truncate(); csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows); fcntl.flock(f,fcntl.LOCK_UN)
EOF
python3 /tmp/addrow.py <<'EOF'
[["RM-004","retro-mechanics","SEC Section 31 fee advisory (Feb 27 2026): $20.60 per $1M of covered sales from April 4 2026 ($0.00 before that). The rate stays until 60 days after the FY2027 appropriation is enacted; whether that has happened was not checked. On a $1,000 sale it is ≈$0.02, immaterial to the retro.","A","https://www.sec.gov/rules-regulations/fee-rate-advisories/2026-2","cold"]
]
EOF
cat > areas/retro-mechanics.md <<EOF
# Retro mechanics (worker B), created 2026-10-22 $(date +%H:%M) ET, cycle 43

## Key findings
- **No benchmark dividends in the window.** Neither SPY nor QQQ goes ex-dividend between Oct 22 and Nov 5, so price return equals total return for the retro (RM-001).
- **The calculation spec.** Same start mark for us and the benchmarks; idle cash earns 0%; fill prices from the paper log; report excess vs SPY, QQQ and the 50/50 blend, together with the process score (RM-002, OE-R1/R4).
- **Costs.** Commission $0. The SEC fee is $20.60 per $1M of sales, ≈$0.02 per $1,000 (RM-004 A). The real cost is the spread, so paper fills need a stated haircut (RM-003 C).

## Evidence strength
- RM-001 B (Yahoo events).
- RM-004 A (SEC).
- RM-002 is a design spec.
- The RM-003 haircut is judgment.

## What doesn't apply
- Money-weighted return (no external flows).
- Benchmark dividend reinvestment (none in the window).

## Rule candidates
- **RM-R1:** The benchmark start is the same timestamp as ours (Oct 22 close), not the first fill. Deployment delay counts against us.
- **RM-R2:** Apply a fixed paper-fill haircut (5bp per side on ETFs, 10-20bp on single stocks), stated in the retro.
- **RM-R3:** Every retro reports the process score next to excess return. The result alone can't show skill (OE-002).
EOF
cat > cycles/43-review-B.md <<EOF
# Cycle 43 review (worker B): retro mechanics, $(date +%H:%M) ET
Done: RM-001..004; areas/retro-mechanics.md; INDEX.md. RM-003 was revised after verifying the SEC rate.
Useful for: the first Friday retro (Oct 23). The spec is ready to hand to the trader.
Next: cycle 44.
EOF
python3 /tmp/idxmd2.py '{"areas/retro-mechanics.md":"B cycle 43"}'; awk -F'\t' 'NF!=7' INDEX.tsv | wc -l; date +%H:%M,000 (RM-004 A). The real cost is the spread, so paper fills need a stated haircut (RM-003 C).

## Evidence strength
- RM-001 B (Yahoo events).
- RM-004 A (SEC).
- RM-002 is a design spec.
- The RM-003 haircut is judgment.

## What doesn't apply
- Money-weighted return (no external flows).
- Benchmark dividend reinvestment (none in the window).

## Rule candidates
- **RM-R1:** The benchmark start is the same timestamp as ours (Oct 22 close), not the first fill. Deployment delay counts against us.
- **RM-R2:** Apply a fixed paper-fill haircut (5bp per side on ETFs, 10-20bp on single stocks), stated in the retro.
- **RM-R3:** Every retro reports the process score next to excess return. The result alone can't show skill (OE-002).
