# Sector rotation & business cycle — warm digest (owner 牛马; new area, 2026-10-22 12:37pm ET)
Ids SR-.

## Findings
- **Business-cycle rotation is a myth, even with perfect foresight [A].** Best case is about 2.3%/yr (0.16%/month) before costs from 1948 to 2022, and it disappears after costs or mistiming. Simply holding the market except in early recession matches it (SR-001).
- **Industry momentum is real but weakened [A/B].** Long-short returns fell from +7.9%/yr (Sharpe 1.83) to +5.3%/yr (Sharpe 0.96) after 2000, with a −35% drawdown (SR-002, SR-003). US momentum broadly kinked down after 2002 (SR-005).
- **Sector ETFs vs SPY [B]:** in a pre-registered test, 24 of 24 rotation states had no edge at 10–60 days. The median sector beats SPY only 42–49% of the time over 60 days, because of mega-cap concentration (SR-004). Top-3 sector momentum returned about 10.5% vs SPY's 12.8% in 2010–24.

## Doesn't apply
- Long-short industry momentum.
- Monthly rotation across 11 ETFs on a $1k book over 2 weeks.

## Rule candidates
- **SR-R1:** No sector-rotation trades. Don't swap SPY/QQQ for sector ETFs on cycle narratives or relative-strength (RRG) states (SR-001, SR-004).
- **SR-R2:** A sector ETF is allowed only as a deliberate, logged bet against the base rate (≤45% chance of beating SPY over 60 days). Never use one as a "safer" substitute for SPY (SR-004).

## Pass 3: own test (12:40pm ET; tools/sector_mom_test.py)
- **Test:** the 9 SPDR sectors, 1999–2026, in about 690 non-overlapping 10-day windows. Hold the top 3 sectors by trailing 21-, 63- or 252-day return.
- **Results vs SPY over the next 10 days:**

  | Lookback | Excess vs SPY | t-stat |
  |---|---|---|
  | 21 days | −0.06% | −0.8 |
  | 63 days | −0.12% | −1.8 |
  | 252 days | +0.05% | +0.8 |

  No subperiod is significantly positive (SR-006, B).
- **This confirms SR-R1:** don't rotate sectors on momentum within the project window.

## Pass 4 (10/22, about 2:15pm ET): valuation-based rotation and timing
- SR-007 (A): Goyal-Welch-Zafirov (RFS 2024) retested 46 equity-premium predictors, including valuation ratios, through 2021. More than a third lose significance even in-sample, and half of the survivors fail out-of-sample.
- SR-008 (A): Asness et al. (JPM 2017). Timing factors by their value spread adds no Sharpe to a diversified portfolio (0.98 to 0.91).
- SR-009 (B, own test, tools/sector_value_test.py; cycles/09-sector-value-test.txt): buying the 3 cheapest SPDR sectors by trailing 3y/5y return earned +0.05% and +0.02% vs SPY over 10 days (t 0.64 and 0.30), and +0.19% and +0.45% over 63 days (t ≤0.87). Cheap minus rich is about 0.
- **SR-R3:** no valuation-based market timing or sector tilt in the window. "Cheap" or "expensive" sectors or indexes aren't a 2-week signal (this joins SR-001 and SR-006).
