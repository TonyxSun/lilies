# Satellite options (what could fill the 30% satellite?) — Trader, cycle 03
Date: 2026-10-22 (round 3). Data: `backtests/2026-10-22-satellite-etfs/` (live ETF prices; Ken French CRSP to 2026-08).

## Bottom line
- **No candidate has convincing post-2009 evidence of beating SPY.** None of the live ETF records or unbiased CRSP long-only tilts has t ≥ 2 after 2009.
- The only positive live records — QQQ, SPMO, VUG, XLK — are all the same bet: US mega-cap growth/tech. About two-thirds of NDX's 2009–2026 price gain came from P/E expansion (12→38), per one (C-grade) estimate. That is hard to repeat from today's valuations.
- **Verdict: hold the index by default.** If Wuyue wants a satellite anyway, 30% QQQ is the cheapest and most honest one: one liquid ETF, ~0 turnover, no stock-picking. Treat it as an explicit growth bet, not an edge.

## Findings
- **SO-001 (A, data)** Unbiased CRSP long-only large-cap tilts minus market, %/yr (t-stat), for 1963–2008 → 2009–2026-08:

  | Tilt | 1963–2008 | 2009–2026 |
  |---|---|---|
  | Profitability | +1.0 (1.8) | +1.0 (1.2) |
  | Value | +3.2 (2.8) | +0.5 (0.2) |
  | Growth | −0.5 | +1.5 (1.6) |
  | Conservative investment | +2.0 (2.4) | +0.5 |
  | Low-variance quintile | +0.2 | −1.1 |
  | Momentum | +3.6 (3.6) | −0.4 |
  | Industry momentum (top 10 of 49) | +6.1 (4.5) | +0.9 (0.5) |

  Long-short factors over 2009–2026: HML −0.7, RMW +1.9 (t 1.0), CMA +0.2, UMD −0.8. Computed by us in `factor_check.py` from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
- **SO-002 (B, live data)** Live ETF returns vs SPY over each fund's life, to 2026-10-21 (CAGR difference, pts/yr, with t-stat):

  | ETF | From | vs SPY (t) | Max drawdown |
  |---|---|---|---|
  | QQQ | 1999 | +2.0 (1.4) | −83% |
  | QQQ | 2015-10 | +4.7 (1.9) | |
  | SPMO | 2015-11 | +3.7 (1.2) | |
  | VUG | 2004 | +1.4 | |
  | XLK | 1998 | +1.7 | −82% |
  | MTUM | 2013 | +0.9 (0.45) | |
  | IWF | 2000 | −0.2 | |
  | RSP (equal weight) | 2003 | −0.4 | |
  | QUAL | 2013 | −0.5 | |
  | SPHQ | 2006 | −1.1 | |
  | VLUE | 2013 | −1.2 | |
  | VTV | 2004 | −1.1 | |
  | IWD | 2000 | −0.2 | |
  | USMV | 2011 | −3.3 (−1.7) | |
  | SPLV | 2011 | −4.2 (−1.6) | |
  | SPDR sector momentum, top 3 of 9 | 2009 | −1.9 | |
  | SPDR sector momentum, top 3 of 9 | 2000 | +0.9 | |

  Source: `results_etf.csv`.
- **SO-003 (A)** "Smart Beta Mirage" (Huang et al., JFQA): smart-beta indexes' market-adjusted return drops from ~3%/yr on paper before ETF launch to ~0.5–1% after, explained by data mining in index construction. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/35CA1CEA091A485DDA960BB2D9930BC9/S0022109023000674a.pdf/smart_beta_mirage.pdf
- **SO-004 (B)** "The Performance of Exchange-Traded Funds" (J. Alternative Investments 2020), survivorship-bias-free US equity ETFs: ETFs collectively lagged the market by about as much as active funds; most factor ETFs failed to beat it. https://doi.org/10.3905/jai.2020.1.116
- **SO-005 (C)** Holdout Labs pre-registered audit (2026) of factor ETFs vs SPY: no fund shown to deliver. Methodology changes mattered:
  - MTUM: +3.1 pts/yr until its index switched in Nov 2020, −0.1 after.
  - QUAL: +1.7 under the original index, −0.8 after it moved to the sector-neutral index in Aug 2015.

  https://holdoutlabs.io/case-study/
- **SO-006 (A)** Fama & French, "The Value Premium" (RAPS 2021): value premiums were much lower in the second half of 1963–2019, but volatility is too high to reject equal expected premiums in both halves. The value drought is consistent with bad luck and with decay; it is not tradeable evidence either way. https://doi.org/10.1093/rapstu/raaa021
- **SO-007 (A/B)** Asness, Frazzini & Pedersen, "Quality minus Junk" (Review of Accounting Studies, 2019; sample to 2016): QMJ earns significant risk-adjusted returns in the US and in 23 of 24 countries. It is long-short, with negative market beta. Our long-only large-cap profitability tilt since 2009 is +1.0–1.8 pts/yr, not significant, and the QUAL ETF lagged. Quality is the most plausible factor but is not shown to deliver long-only after costs. https://link.springer.com/article/10.1007/s11142-018-9470-2
- **SO-008 (B/C)** Why QQQ won since 2009:
  - NDX revenue, EPS and free-cash-flow growth were about twice the S&P 500's over ~20 years (EPS 13× vs <3×; Nasdaq's own presentation, B, vendor).
  - Roughly two-thirds of the 2009–2026 price gain was P/E expansion from 12 to 38 (Value Seeker Substack, May 2026, C).
  - AQR ("Driving with the Rear-View Mirror") shows repeating a decade driven by multiple expansion would need record valuations (B).
  - Concentration predicts lower future returns at the industry level (Aalto thesis, C).
  - Repeatability: fundamentals partly earned it; the re-rating part isn't repeatable.

  Sources: https://indexes.nasdaqomx.com/docs/NDX%20Extended%20Presentation.pdf, https://valueseekerreport.substack.com/p/nasdaq-100-can-we-repeat-the-2009, https://www.aqr.com/-/media/AQR/Documents/Insights/White-Papers/Driving-with-the-Rear-View-Mirror.pdf
- **SO-009 (C, our test)** 70% SPY + 30% satellite since 2015-10, at ~9%/yr turnover:

  | Satellite | CAGR | vs SPY 14.6% | Max drawdown |
  |---|---|---|---|
  | QQQ | 16.0% | +1.5 | −32.0% |
  | SPMO | 15.7% | +1.1 | |
  | QUAL | 14.3% | −0.3 | |

  This compares with the round-2 70/30 stock-momentum satellite at 225%/yr turnover, whose apparent edge was survivorship.
- **SO-010 (logic)** The goal is to beat SPY *and* QQQ. Any mix of the two lands between them by construction. Beating QQQ needs something beyond QQQ (e.g. SPMO-like concentration), and nothing beyond QQQ has a significant live record.

## Proposed rules (satellite)
- Satellite = 30% QQQ, buy-and-hold; re-mix to 70/30 only at a month-end if more than 5 pts off target. **Changes** the round-2 #2–#4 (stock-momentum satellite). B. Needs Wuyue.
- No factor/smart-beta satellite (QUAL, USMV/SPLV, VLUE, MTUM, RSP, sector momentum): live records lag or match SPY, and post-launch decay is documented. **New.** A/B.
- The 10-stock momentum satellite becomes an optional paper-only experiment, so we learn without real money. **Changes.** C. Needs Wuyue.

## Round 5 — stress test on the bad years (2026-10-22, 1:24pm ET)
Data and code: backtests/2026-10-22-stress/ (README has the assumptions and biases; results_tables.md has the full tables). Yahoo via yfinance, fetched 13:21 ET. SPY and QQQ use Adj Close (total return). QQQ before 1999-03-10 = ^NDX price, no dividends, used only for warm-up. Costs 0.15%/side. **Sanity check, not proof.**

| Window | SPY | QQQ | 70/30 | 50/50 | QQQ wide stop (strict re-entry) | QQQ wide stop (literal re-entry) |
|---|---|---|---|---|---|---|
| Dot-com 2000-02: return / max DD | −37.5% / −47.5% | −73.3% / −83.0% | −49.8% / −61.4% | −57.3% / −68.9% | −28.0% / −41.8% | −31.9% / −47.1% |
| … years from peak to recovery | 6.6 | 14.9 | 12.5 | 13.1 | 6.8 | 10.0 |
| GFC 2007-09: return / max DD | −16.0% / −55.2% | +7.3% / −53.4% | −9.3% / −54.1% | −4.7% / −53.7% | +29.8% / −27.0% | +23.3% / −30.6% |
| Covid 2020: return / max DD | +18.3% / −33.7% | +48.4% / −28.6% | +26.8% / −32.0% | +32.7% / −30.8% | +44.1% / −21.0% | +43.8% / −25.0% |
| 2022: return / max DD | −18.2% / −24.5% | −32.6% / −34.8% | −22.7% / −27.5% | −25.6% / −29.7% | −9.0% / −13.8% | −19.3% / −24.3% |
| 1999→2026 CAGR / max DD | 8.7% / −55.2% | 11.1% / −83.0% | 9.6% / −61.4% | 10.2% / −68.9% | 6.6% / −44.3% | 11.6% / −49.5% |
| 3-yr windows beating SPY: all / start<2009 / start≥2009 | — | 77 / 51 / 94% | 78 / 52 / 95% | 78 / 52 / 95% | 39 / 67 / 20% | 64 / 64 / 65% |
| Worst 3-yr return | −39.6% | −76.6% | −51.8% | −59.8% | −28.9% | −40.3% |

Findings:
- **The 70/30 "beats SPY 78% of the time" is a post-2009 artefact.** For 3-yr windows starting before 2009 it is a coin flip (52%). In a dot-com replay $1,000 bottoms at ~$386 (vs ~$525 for SPY) and takes 12.5 years to get back, vs 6.6 for SPY. Over 1999–2026 it still ends ahead (9.6% vs 8.7% CAGR), so this is a risk statement, not a refutation. [C]
- **The wide stop on QQQ is a drawdown tool, not a return tool, and its result depends on an ambiguous re-entry rule.**
  - Strict "back above 200DMA" (must dip below first): 6.6% CAGR, below SPY. It sat in cash for 2 years in 2016–18, and has been in cash since its 2026-07-29 exit while QQQ (725.20) is above its 200DMA (675.27).
  - Literal re-entry: 11.6% vs 11.1% for QQQ buy-and-hold.
  - The 27 parameter neighbours span 7.9%–13.7% CAGR (median 11.4%), i.e. no robust return edge, but every one cut the max DD to between −37% and −66%.
  - After an estimated tax in a taxable account (ST 32%/LT 15%) the literal stop loses: 9.3% vs 10.5% for QQQ buy-and-hold.
  - It is also a market-timing switch, which conflicts with round-2 rule 6 (no timing). [C]
- **What a $1,000 account practically experiences:**
  - Dollar drawdowns in the worst window: SPY −$475 to −$552; 70/30 −$614 (dot-com); QQQ −$830.
  - The blends need ≤12 tiny rebalances a year (fewer with the 5-pt band); cost drag ≈0.01%/yr.
  - The wide stop makes 2–3 trades a year (≈$1.50 each at 0.15%), costs 0.3–0.5%/yr, and turns gains short-term.
  - Longest time underwater 1999–2026: SPY 6.6 yrs, 70/30 12.4, QQQ 14.9, stops 6.8 (strict) / 10.0 (literal).

### Proposed rules (round 5)
- Keep A1 (30% QQQ) only if Wuyue accepts, in writing, a dot-com-style case of −61% and ~12 years underwater. Otherwise drop to SPY only or a smaller tilt. **Changes existing (A1 → flag).** C.
- Do not adopt the wide stop / 200DMA re-entry on QQQ (or the index core) to raise returns: there is no robust edge, it is worse after tax, and it conflicts with rule 6. **Confirms existing (rule 6).** C.
