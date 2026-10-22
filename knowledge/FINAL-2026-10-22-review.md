# FINAL review, 2026-10-22 research loop (promotion/demotion pass, 3:30pm ET)

## Inputs read
README.md, INDEX.md, INDEX.tsv (514 data rows; 165 A, 289 B, 60 C), 47 areas/*.md digests, cycles/* (A-final-summary.md, B-final-summary.md, ~100 plan/review files), proposals/trader-2026-10-22.md (Trader: technicals, sizing and risk, execution and costs; ranked index default 1st, 70/30 split 2nd, replacement stop 3rd).

## Validation
- `awk -F'\t' 'NF!=7'` on INDEX.tsv: 0 broken rows before and after this pass. No duplicate ids, no empty id/claim/grade fields. Nothing needed repair.

## Promoted to HOT (15 rules, see HOT.md)
1 index default (Trader #1); 2 70/30 core, momentum satellite paper-only (Trader #2/A1/A3, R5-1); 3 replacement stop (Trader #5, B's SL-R1); 4 no cash around macro days; 5 no market-timing switch; 6 evidence bar; 7 no gap-up buys, no PEAD; 8 earnings guard and sizing; 9 quality junk veto; 10 news sleeve paper-only, LATE veto only; 11 execution; 12 T+1 settlement; 13 costs and tax; 14 breakers on own book; 15 default no trade, slow rule changes.
INDEX.tsv tier column: the 80 ids cited in HOT.md are now `hot` (75 changed).

Citation note for rule 2 (momentum): the S&P 100 sanity backtest (T-026, R-021; grade C; today's S&P 100 members, 2014-2026, survivorship-biased) and the Ken French CRSP data (T-021, SO-001; grade A; long-only large-cap momentum -0.4%/yr vs market 2009-2026, 0.0%/yr 2014-2026) disagree. HOT follows the unbiased French data and keeps momentum paper-only.

## Demoted (tier hot -> warm) and why
- SL-002, SL-004, SL-006: superseded by SL-005/SL-008/SL-009 (robustness and survivorship-free reruns), which carry the stop rule now.
- PT-004, PC-007, PC-008: reconciliation notes between rules.md and Trader's proposals; their content is now inside HOT rules 2, 3, 5 and 11.
- US-007, US-008, US-011: Tradable v1 universe and v2-news sleeve specs. They are proposals pending Wuyue and do not change a decision while the core is index-only and the sleeve is paper-only; kept warm.

## Considered and left out of HOT (warm)
- VIX/VIX3M ladder (VX-001..007, MS-005): a risk gauge, not direction; single-source own tests; useful for satellites only, which are paper-only.
- Prediction markets (P-*): base-rate cross-check, thin and wide; not a trigger.
- Sector cap ≤3 per GICS (R-017/R-018): only matters if a stock satellite goes live.
- Stock > 200DMA screen and $10B cap in rules.md: Trader #11 says it adds nothing (T-026, C); Tradable v1 would replace $10B. Pending Wuyue; no change.
- Insider trades (IN-*, FP-017): cold; only opportunistic insider buys carry signal.

## Needs Wuyue's yes before rules.md changes (⚑)
HOT 1 (3-pt hold-the-index trigger), 2 (70/30 SPY/QQQ, accepting the dot-com drawdown), 3 (stop replacement), 10 (news sleeve paper-only), 14 (breaker defined on our own book). rules.md was not edited.
