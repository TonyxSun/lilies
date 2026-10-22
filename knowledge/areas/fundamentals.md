# Fundamentals & earnings — warm digest (owner 牛马; refreshed 2026-10-22 12:35pm ET, pass 3: gaps filled 12:33pm ET)

## Key findings (evidence strength in brackets)
1. **Classic PEAD is dead in large caps [A].**
   - Bernard-Thomas reported +4.19% over 60 days (F-001).
   - Martineau finds no 60-day drift for non-microcaps since 2006 (F-003).
   - Pass 2 adds Subrahmanyam (2025): the EAR-based drift factor has t=1.43 once microcaps are excluded (F-005). The claimed post-2020 revival is a microcap artifact (F-004).
   - Practitioner data agrees: 42% of beats closed lower on the reaction day (F-018).
   - So **the earnings reaction is a filter, not an entry trigger.**
2. **Guidance and the reaction beat the EPS headline [A/B].**
   - Guidance cuts are punished more than beats are rewarded (F-017).
   - EAR is more informative than SUE (F-012), but by pass 2 it is mostly priced on day 0 (N-019).
3. **The earnings announcement premium survives only in the largest firms [A].**
   - Market-wide, it vanished after the 2004 8-K reform (F-028).
   - The top 500 announcers still earn about 0.30% per week of alpha (F-026, verified).
   - Per event, that's about +0.3% expected against a ±4.6% move, so the pre-earnings rule stays (FC-5). Options-implied moves price earnings risk roughly fairly in large caps (M-017).
4. **Quality and profitability are real as long-short factors, but long-only quality lagged cap-weight in 2023–25 [A factor / B index].**
   - Sources: F-007, F-008, F-013, F-014.
   - Junk avoidance is the useful part: profitless tech fell 57% in 2022 vs the Nasdaq-100's 32% (F-027).
5. **Analyst revisions [B].** Durable in the 1990s literature (F-010, F-011). Pass 2: the drift faded after 2002 and concentrates in low-priced firms (F-033). Vendor claims are marketing (F-023). Weak for >$10B names.
6. **Text-based fundamentals are the most LLM-suited edge [A, slow].**
   - Lazy Prices: 10-K/10-Q language changes predict 34–58 bp/month of underperformance, and up to 188 bp for risk-factor changes. There's no announcement reaction; returns accrue over 6–18 months, and it is not small-cap-only (F-030). Out-of-sample replication is thin (F-031, C).
   - Earnings-call tone predicts 60-day PEAD in older samples, but raw sentiment hurt after 2020 (F-032).
   - Long-only we can use only the *avoid changers* side, and over our 2-week window it is a **veto, not a return source.**
7. **Factors are real but smaller [A].** JKP find about 82% replicate, with about 47% decay after publication (F-022). McLean-Pontiff put decay at 58% (F-015). Price momentum is largely earnings momentum (F-029).

## What doesn't apply ($1k, long-only, daily, >$10B screen, ends 11/05)
- Short legs, which carry most of the drift.
- Microcap PEAD.
- 6–18 month text effects as return targets.
- Annual factor tilts.
- Nothing here gives a reliable 2-week edge over SPY. Fundamentals mainly tell us **what not to own.**

## Rule candidates
- **FC-1 (filter):** after earnings, a name stays eligible only if its day-1 reaction vs SPY is ≥0 *and* guidance was not cut. Never buy solely because of a beat. [F-003, F-005, F-012, F-017, F-018]
- **FC-2:** no buy within 5 trading days after a guidance cut or a day-1 reaction worse than −5% vs SPY. [F-017, N-001, N-011]
- **FC-3 junk veto:** require positive TTM gross profit and operating cash flow. [F-007, F-008, F-027]
- **FC-4:** haircut any backtest or paper return claim by ≥50%. [F-015, F-022]
- **FC-5:** no new single-name position in the 2 sessions before its earnings; holding SPY/QQQ through mega-cap earnings is fine. [F-019, F-026, F-028, M-014]
- **FC-6 (new, test; pass 3 made concrete):** before buying, fetch the latest 10-Q from EDGAR.
  - If Part II includes **Item 1A with new or changed risk text** vs the prior filing, skip the name. Omission or a "no material changes" note passes.
  - For a fresh 10-K, diff Item 1A against last year's and skip on a large change (new risk categories).
  - Log every skip and track it at +20d vs SPY.
  - Evidence: 10-Q risk updates predict lower 3-month returns (F-034). The IBM prototype extracts in under a second (F-035). [F-030, F-031, F-034, F-035]

## Pass 4: FC-6 live test on last night's 10-Qs (1:00pm ET)
- **TSLA:** incorporates by reference, so it passes.
- **IBM:** omits Item 1A, so it passes.
- **META:** reproduces the full Item 1A every quarter. Words are up 4.9%, about 130 sentences are new (some are page-number artifacts), and the similarity is 0.997. The new text includes AI-initiative risk (F-036).
- **FC-6 revised:** veto only when the Item 1A word count changes by more than 10% vs the prior 10-Q, or a new risk heading appears that names a current business line (it must be reviewed). Small reworded additions in full-reproduction filers pass but get logged. The threshold is untested, so use C-grade judgment and track it for 20 days.
- **Timing pitfall:** filingDate in submissions JSON is next-day for acceptances after 5:30pm (F-037). Use acceptanceDateTime or the index Accepted time.
