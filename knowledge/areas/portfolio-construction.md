# Portfolio construction for a $1k, 2-week contest: warm digest
Owner: worker B. Updated 2026-10-22 12:38pm ET. Rows: PC-001..PC-006. Trader owns sizing; this is evidence input only. Tools: tools/te_check.py (data: sources/te_check_2026-10-22.txt).

## Key findings
1. **Most professional stock pickers lose to the index.** 67% of active large-cap funds trailed the S&P 500 in H1 2026 (PC-001, A).
2. **Stock returns are dominated by a few big winners,** so concentrated portfolios usually lag. Only 42.6% of stocks beat T-bills over their lifetimes. Even 25-stock portfolios trail the market more than half the time (PC-002, A).
3. **Over two weeks, a single stock vs SPY is a coin flip with fat tails.** Using today's mega caps: standard deviation 5.5%, 10th/90th percentiles −5.1%/+6.5%, and the stock beat SPY in 51% of windows (PC-004, B, survivorship-biased in their favour).
4. **Equal weight is a separate bet, not a "smarter" S&P.** RSP trailed SPY by about 31 pts over 2023–25 and is about even in 2026 YTD (PC-003, B).
5. **If you deviate from the index, deviate deliberately.** High active share beats closet indexing (PC-005, B), but core-satellite structures don't show a robust edge.
6. **Which S&P 500 ETF to use doesn't matter for us.** Fee differences are negligible over 2 weeks. Holding SPY as the core gives zero tracking error to the main benchmark (PC-006, B).

## Evidence strength
- **A:** PC-001, PC-002.
- **B:** PC-003..PC-006.

## What doesn't apply to our setup
- Multi-decade compounding and fee arguments matter little over 2 weeks.
- Tax considerations don't apply (paper account).

## Rule candidates (note to Trader; sizing is the Trader's call)
- **PC-R1:** Use a core-satellite setup. The core is SPY, or SPY+QQQ to match both benchmarks. The satellite is at most ~30% total, with each pick ≤10–15%. The expected contest outcome is then about the index, with bounded noise (PC-002, PC-004).
- **PC-R2:** A satellite position needs a thesis that is genuinely different from the index (high active share). Don't hold a basket of mega caps that mimics QQQ (PC-005).
- **PC-R3:** Report results vs both SPY and QQQ total return every day. Count beating them only over the full window, since 2-week single-name noise has σ≈5.5% (PC-004).

## Addendum, cycle 55 (13:23 ET): reconciliation with the trader (satellite-options.md, proposals A1/A3/#5/#7/#9) (PC-007)
- **Agreement:** index default; 30% QQQ only as a declared growth bet; momentum sleeve paper-only.
- **Implementation changes, all from today's B evidence:**
  1. Execute as 1 VOO + 1 QQQM in whole shares (WS-R1).
  2. Use the #5 stop, or exempt the core (SL-R1).
  3. Extend the cap exemption to the QQQ leg (PT-004).
  4. Defer A3 past the earnings cluster (ER-R2).
  5. No bond hedge (RR-R1).
  6. Present the result as "between the benchmarks by construction" (OE-004).
- **Open for Wuyue:** items 2 and 3 are rules.md changes and need his OK.

## Cycle 74: reconciliation with trader rounds 5-6 (PC-008)
- **Agreement:**
  - #5 is a stock-level stop only, so the core has no stop (= SL-R1).
  - No 200DMA timing on the core.
  - No small-cap edge.
- **Conflict: R6-2 / #9 limit-only vs fractional market-only (WS-006).** In a $1,000 account, any name priced above its dollar cap must be fractional, and so can't take a limit order. Wuyue/Trader to choose:
  - (a) restrict to names where a whole share fits the cap; or
  - (b) allow fractional market orders after 10:00 ET with a 0.30% round-trip haircut.
- **Herding wait:** 20 sessions for small/retail names, 5 for mega caps (S-002, S-020).
- **Paper costs:** 0.30% round trip on single stocks (#14), ≈10bp on ETFs.
- **Cycle 75 (PC-009):** 76-91% of small and mid caps fit their dollar cap with whole shares, so R6-2's limit-only rule is workable. The fractional/market-only issue is mostly a $10B+ problem (about 50% of names).
- **Cycle 82 (PC-010):** use a tiered paper cost by cap. The flat 0.30% round trip is too low for small caps under $1B.
