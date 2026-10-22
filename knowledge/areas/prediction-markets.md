# Prediction markets (Polymarket, Kalshi): warm digest
Owner: worker B. Updated 2026-10-22 12:30pm ET. Rows: P-001..P-012. Cold detail: INDEX.tsv, cycles/01-prediction-markets-plan.md, sources/pm_snapshot_2026-10-22.json, tools/pm_snapshot.py.

## Key findings
1. **Liquid macro markets are accurate and already priced.** Kalshi fed-funds forecasts are about as accurate as fed funds futures (MAE ~1 bp) and update quickly (P-001, A). Polymarket's resolved markets are well calibrated (30-day Brier ~0.045, slope ~0.95–0.98) (P-003, B). The odds are a fair read of consensus, not a source of edge.
2. **Favourite-longshot bias.** On Kalshi, contracts under 10c lose more than 60% after fees, while favourites are roughly fair (P-002, A). Treat low-probability tails, like "crash" or "recession this year", as overpriced.
3. **Thin markets drift and disagree.** Price shocks stay visible for weeks in thin markets (P-004, B). The two venues have traded ~3c apart (P-005, B). Today's snapshot has ladders that are incoherent or non-monotonic, e.g. S&P buckets summing to ~1.18 (P-009, B).
4. **What moves stocks is the surprise, not the level.** An unexpected 25 bp Fed move maps to roughly a 1% one-day index move (P-011, A, Bernanke–Kuttner). Election-odds swings feed into equities (P-006, A). The pre-FOMC drift has been gone since about 2016 (P-010, A).
5. **Current context (P-008, P-012; 2026-10-22 ~12:25pm ET):**
   - Oct 28 FOMC: hold 93.5%.
   - Dec FOMC: hike ~70–75% (both venues).
   - Recession by end-2026: 4–7.5%. That is a longshot, so discount it.
   - Midterms Nov 3: House D 92.5%, Senate D 68.5%.
   - Oct CPI (≈Nov 10–12) above 0.2% MoM: 59c.

## Evidence strength
- **A:** P-001, P-002, P-006, P-010, P-011.
- **B:** P-003, P-004, P-005, P-007, P-008, P-009, P-012. The calibration numbers come from a thesis or independent analysis, not peer review.
- Every snapshot number is a point-in-time read and goes stale within hours.

## What doesn't apply to our setup
- We can't trade event contracts: the account is long-only stocks and ETFs, no sign-ups. Their whole value here is as information.
- Arbitrage between the venues and longshot-selling strategies (P-002, P-005) can't be done in our account.
- A $1k account over a 2-week window gets only a few event days: FOMC Oct 28, midterms Nov 3, CPI just after the window. There's too little data to test a timing edge, so use odds for risk context only.

## Rule candidates (testable, one line each)
- **PM-R1:** Use PM/Kalshi odds only as a regime and risk input. Never treat the odds level as a buy signal, since it's already priced (P-001, P-003, P-011).
- **PM-R2:** Ignore or discount any contract priced under 10c, e.g. tail recession or crash odds (P-002).
- **PM-R3:** Use a market only if both venues agree within 5 pts and the ladder is monotonic with >$100k volume. Otherwise log it as noise (P-004, P-005, P-009).
- **PM-R4:** No "buy before FOMC" drift trades (P-010).
- **PM-R5:** Before an event day where the odds are under 85% (today: Senate control 68.5%; Dec FOMC ~72%), don't open a new full-size position the session before. Re-check the odds the next morning (P-006, P-011, P-012).

## Pass-2 counter-evidence (12:30pm ET)
- **Odds moves can lead stocks.** In 2024, a +1 pt move in Trump's odds predicted about +13 bp the next day on "Trump trade" assets. That's a Sharpe of 1.95 for a long-short strategy, but part of the move later reversed as noise (P-013, B, one event). It suggests a big overnight swing in midterm odds may carry into the next day's prices. It's untested for midterms, and we can't short, so the most it supports is "don't fight a large overnight odds swing in exposed names".
- **Polymarket volume is unreliable.** About 25% of historical volume, and ~20% in Oct 2025, looks like wash trading (P-014, B). PM-R3's >$100k volume floor is a minimum bar, not proof of liquidity. Prefer the Kalshi bid/ask spread.

## Daily pull (read-only)
`python3 tools/pm_snapshot.py` writes sources/pm_snapshot_<date>.json. The endpoints are listed in P-007. Kalshi rate-limits bursts (429), so the script sleeps 0.4s between calls.

## Pass-3 adjacent (12:30pm ET)
- **Midterm seasonality.** The S&P 500 rose in the 12 months after all 19 midterms since 1950. The 3-month record is less clean: it fell after 1978 and 2018 (P-015, B). Our window closes Nov 5, two days after the vote, so this is context only. Don't de-risk *because of* the midterms. The surprise case to watch is a Republican Senate hold (31.5%).

## Pass 4 (cycle 08, 2026-10-22 ~12:39 ET) — daily pipeline + calibration by category
**Pipeline:** `python3 tools/pm_regime.py` (fresh snapshot) or `--snapshot <json>`; writes `sources/pm_regime_<date>.md` = one paragraph + flags.
Mid = (bid+ask)/2 if spread ≤5c else last (ILLIQUID flag); DISAGREE if venues differ >5 pts; longshot <10c discounted; UNCERTAIN if top outcome <85%; EVENT-GUARD within 10 days of FOMC / midterms (Nov 3; triggers from Oct 24).
Live test 12:38 ET (P-019): Oct 28 FOMC hike 7%/8% (hold ~93%), Dec 9 hike ~76% (both venues) → **market prices a hiking cycle restarting in Dec**; recession 2026 4–7.5% (longshot); Oct CPI >0.2% MoM 59%; Senate D 68.5/67.5, House D 92.5/91.5. Venues agree within ~1.5 pts on every line.
**Calibration by category (P-016/P-017, grade B; P-018 C unverified):**
- Politics: underconfident (compressed toward 50%), slope ~1.5–1.8 at 1d–1mo, on both venues. Raw 68% ≈ ~80% after slope-only recalibration; treat political favourites as *more* likely than quoted.
- Finance/econ (Fed, CPI, indices): ~calibrated within a week; mildly compressed at 1w–1mo (1.42). Fed odds days before FOMC ≈ face value.
- Sports/crypto: near-calibrated short-horizon; all domains compress beyond 1 month (favourite–longshot).
- Weather short-horizon: over-extreme (irrelevant to us).
**Does not apply:** recalibrated odds still aren't a trading edge for equities (P-001: priced in); recalibration constants are in-sample to 2025.
**Rule candidates:**
- PM-R6: Read political favourites one notch stronger than quoted (68% ≈ 80%); read Fed/CPI odds at face value inside 1 week. (P-016, P-017)
- PM-R7: Run pm_regime.py once per trading day before the plan; act only on flags (EVENT-GUARD/DISAGREE), never on levels. (P-019, P-001)

## Addendum, cycle 53 (13:22 ET): live refresh during the selloff (P-020)
- Fed and recession odds were essentially unchanged between 12:38 and 13:21. Hike tails eased by 1-2 pts.
- An October hold is ~93%, and a December hike ~68-70%.
- **PM-R (context):** when equities fall hard but PM macro odds don't move, treat it as an equity-specific shock. It's no reason to change the core (consistent with DD-R1 and RR-R2).
- **Cycle 89 (P-021):** small/mid-cap catalyst contracts exist: Kalshi FDA decisions (SMMT ivonescimab 0.51-0.58, CMPS COMP360 dated ladder, NTLA, BBP-418) and M&A (VKTX about 0.12, GTLB). They are thin, wide and calendar-year dated: a base-rate cross-check only, not a timing signal.
