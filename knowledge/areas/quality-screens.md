# Quality / profitability screens from free data — warm digest (owner 牛马; new area, 2026-10-22 12:40pm ET)
Ids Q-. Tool: `tools/quality_screen.py` (read-only, SEC XBRL companyfacts, point-in-time via `--asof`).

## Findings
- **Free point-in-time fundamentals work** (Q-001, B). The companyfacts API returns a `filed` date for every fact, so a screen can be run as-of any decision date without look-ahead.
  - Pitfall: revenue tags change over time, so the tool picks the most recent tag.
  - Banks need different handling: no gross profit, and OCF can be negative by design.
- **Today's output** (Q-002): NVDA has GP/assets of 0.71 but accruals of +0.18, meaning net income is well ahead of cash flow. INTC lost money on a TTM basis but had positive OCF. AAPL is at 0.59, MSFT 0.30, TSLA 0.13.
- **The return evidence is weak out of sample.**
  - Gross profitability: long-short t=0.93 for 2016–26; S&P 500 long-only about +0.28%/yr (Q-004, B).
  - Accruals: decayed since about 2013 (Q-003, A).
  - Long-only quality indexes lagged (F-013, F-014).
  - The junk tail is real, though: profitless tech fell 57% in 2022 (F-027).

## Doesn't apply
- Quality as a 2-week alpha source.
- Long-short factor spreads.

## Rule candidates
- **Q-R1 (implements FC-3):** run `quality_screen.py <TICKER> --asof <decision date>` on every candidate. Veto any non-financial name with TTM GP ≤0 or OCF ≤0 (Q-001, F-027).
- **Q-R2:** if accruals exceed +0.10, the thesis must explain the NI/OCF gap (receivables or inventory build). It's a scrutiny flag, not a veto (Q-002, Q-003).
- **Q-R3:** never cite quality or profitability as the reason a name will beat SPY in 2 weeks (Q-004).

## Pass 3: run on today's reporters (12:44pm ET)
- **XBRL lands fast:** companyfacts had META, IBM and TSLA September-quarter data within hours of their 10-Qs. LRCX and PG are still on the June quarter because only their 8-Ks are filed.
- **All five pass FC-3.**
- **Gap:** an OCF-based veto misses capex-driven FCF turns. META's Q3 FCF was reportedly negative (Q-005).
- **Q-R4:** the TTM FCF check (OCF − PaymentsToAcquirePropertyPlantAndEquipment) is implemented in v1.1 as `fcf_flag`. It is a scrutiny flag, not a veto. AMZN is flagged: TTM FCF −$11.6B (Q-006).

## Pass 4: own point-in-time backtest (12:58pm ET; tools/quality_backtest.py; output in cycles/05-quality-backtest.txt)
- **Setup:** 19 as-of dates in 2022–26, about 59 large caps.
- **High GP/assets:** top-minus-bottom +0.28% over 10 days (t 0.7) and −1.15% over 63 days (t −1.0).
- **Low accruals:** −0.38% over 10 days (t −0.9).
- **Conclusion:** no edge (Q-007). This confirms Q-R3. Quality is used only as the FC-3 junk veto plus the Q-R2 and Q-R4 scrutiny flags.

## Pass 5: Piotroski and post-publication decay (1:36pm ET)
- **Piotroski F-score:**
  - The US spread weakened after 2000.
  - It isn't implementable after costs (2005–15 test).
  - The large-cap premium of about 0.30%/month comes from ex-US data.
  - Verdict: cold (Q-008, B).
- **McLean-Pontiff:** published anomalies decay about 35% after publication, and more in large, liquid stocks (Q-009, A).
- **Q-R5:** haircut any literature effect by at least 50% before comparing it with the 2.6–5.9% two-week noise (BR-001).
