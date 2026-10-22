# Fund flows and positioning (warm digest)
Owner: 牛马 (worker B) · last refreshed 2026-10-22 (pass 1) · INDEX ids FP-xxx

## Bottom line
Most famous flow/positioning anomalies have decayed (index inclusion, buyback drift) or live mainly in small caps and short legs (insider buying, retail flow). What survives for a long-only large-cap book is mostly **avoidance**: skip crowded shorts (high days-to-cover) and ETFs/stocks riding record inflows; treat genuine opportunistic insider *buying* as a tie-breaker, not a thesis.

## Key findings
| Finding | Grade | Ids |
|---|---|---|
| Opportunistic insider trades earn ~82 bps/mo VW abnormal; routine insiders ~0. | A | FP-001 |
| Insider signal concentrated in small firms; purchases matter, sales mostly don't. | A (+C recent) | FP-002 |
| Days-to-cover predicts low returns: low-minus-high DTC 1.19%/mo EW, 0.67%/mo VW (1988–2012). | A | FP-003 |
| S&P 500 inclusion effect fell from ~7.4% (1990s) to ~0.8% (2010s). | A | FP-004 |
| Buyback-announcement drift gone after 2003. | A | FP-005 |
| ETF flows reflect non-fundamental demand; high-inflow ETFs underperform after. | A | FP-006 |
| Retail order imbalance predicts next-week returns ~10 bps/week, weaker since 2016, esp. large caps. | A (contested) | FP-007 |
| 13F "best ideas"/cloning: ~3–4%/yr excess in working papers, 45-day lag costs ~1.5%/yr. | B | FP-008 |
| CFTC COT for S&P futures: weak, unreliable after reporting lag. | B | FP-009 |

## Free data we can pull (tested 2026-10-22, see `tools/fp_check.py`)
- FINRA short interest with days-to-cover (POST api.finra.org, twice-monthly, ~2-week lag; latest settle 2026-09-30).
- SEC EDGAR submissions JSON + Form 4 XML (transaction code P = open-market buy). Needs a "name email" User-Agent.
- CFTC COT via Socrata (publicreporting.cftc.gov/resource/gpe5-46if.json).
- FINRA daily short *volume* is not short interest (FP-011).

## What doesn't apply to us
Short legs, small-cap insider effects, index-inclusion and buyback event trades, COT timing.

## Rule candidates
1. **Skip any candidate in the top decile of days-to-cover (≈ DTC > 7–10 in large caps; threshold to calibrate).** (FP-003, FP-010)
2. **Don't buy an ETF or theme in the week it posts record inflows; flows mean-revert.** (FP-006)
3. **Count only opportunistic open-market insider purchases (Form 4 code P, not routine) as a +1 tie-breaker; ignore insider sales.** (FP-001, FP-002)
4. **Ignore buyback announcements and S&P inclusion news as buy reasons.** (FP-004, FP-005)

## Pass-2 update (2026-10-22 12:30pm ET; FP-012..FP-016)
- **Days-to-cover is weaker than it looked.** Large-cap short-interest predictability has faded, and high short interest in large caps has even been linked to *higher* returns (FP-014, C). Rule 1 is downgraded to a skip filter for extreme cases only (DTC >10). It is not a ranking factor.
- **Aggregate short interest works as a market regime signal** (FP-015, A). It is too slow (monthly) to matter inside our 2-week window. File it as context only.
- **The insider-buy effect is front-loaded.** The 2-day return is about +1.13% after SOX (FP-012, B). S&P 500 insider buys beat the index over 1 week and 1–3 months but lag it at 6–12 months (FP-013, C, unverified newsletter). This fits our short window. Act within 1–5 days of the filing, or not at all.
- **Flow-chasing is mixed.** Sector-ETF flows predict about 1 month of positive returns, then a reversal (FP-016, C). Rule 2 stays as "don't add in the record-flow week".

## Open questions (pass 3)
- Options-flow (unusual call volume) as a read-only signal: see S-005. Only non-public open-buy volume has an edge.

## Cycle 06 (12:36pm ET): insiders and 13F in depth (FP-017..FP-020)
- **Opportunistic vs routine insiders.** An insider who trades in the same calendar month every year is routine, and those trades carry about zero signal. Opportunistic trades earn 82 bp/month value-weighted (FP-017, A). Check: does the insider have a ≥3-year history of trading in the same month? If so, ignore the trade.
- **Cluster buys** (≥2 insiders) earn about 2× single buys: 3.8% vs 2.0% over 21 days (FP-018, B). The effect is mostly in small caps.
- **13F copying doesn't work after the 45-day lag.** A 2012–2025 test with costs and out-of-sample checks found 0 of 4 strategies with significant alpha (FP-019, B). Ignore "what hedge funds bought" lists.
- **In practice, large-cap insider buys are rare.** One day of EDGAR Form 4s (Oct 21) had no S&P 500 open-market buys (FP-020).
  - Tool: `tools/insider_scan.py <yyyymmdd…>` scans the EDGAR daily index for P-code buys and flags clusters.
  - openinsider.com timed out from the box.

### Updated rule candidates
- **FP-R3 (revised):** An insider purchase counts as a +1 tie-breaker only if all three hold:
  - It's an open-market buy (code P), not a grant or option exercise.
  - The insider is opportunistic, i.e. not trading in the same month as in prior years.
  - It's ≥$100k, or the CEO/CFO is buying, or it's a cluster of ≥2 insiders within 30 days.
  - Act within 5 trading days of the filing (FP-012, FP-017, FP-018).
- **FP-R5:** Never buy because a 13F shows a fund bought it (FP-019).

## Addendum, cycle 23 (2026-10-22): index events in the window
- No S&P 500 change was found effective Oct 22-Nov 5. Recent changes: VYLR on Oct 1 and TWLO on Oct 6. The Dec quarterly rebalance and NDX reconstitution fall outside the window (FP-021). An unscheduled add would still fall under FP-004 (don't trade inclusion announcements).
