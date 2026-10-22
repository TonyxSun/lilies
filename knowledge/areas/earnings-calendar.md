# Earnings calendar for the window (worker B), created 2026-10-22 13:17 ET, cycle 47

## Key findings
- **Verified calendar.** From the Nasdaq calendar API (ER-001): MSFT/GOOGL Oct 28 amc, AMZN/INTC/SNDK Oct 29 amc, AAPL Nov 2 amc, AMD Nov 3 amc, STX Oct 27 amc, WDC today amc. NVDA, META and TSLA are not in the window.
- **The A3 sleeve has a hard block.** If formed at the Oct 30 close, AMD is blocked by the earnings rule, and four other top-10 names will have just reported (ER-002).
- **About $15.9T of megacaps report** after the close between Oct 28 and Nov 2 (ER-003).

## Evidence strength
- B: an exchange-operator feed, but dates may be estimates.
- Re-pull on the morning of each event (OS-R4).

## What doesn't apply
- Trading the prints (RT-R1/R2, ES rows).

## Rule candidates
- **ER-R1:** Re-pull this calendar at each 9:45 re-check, and drop any proposal on a name reporting within 2 trading days (enforces rules.md).
- **ER-R2:** Don't form the A3 sleeve at the Oct 30 close. Defer it to after Nov 4 or skip it within this paper window, because one top-10 name is blocked and four are post-earnings.
- **ER-R3:** The EVENT-GUARD dates are confirmed as Oct 27 (V/STX), Oct 28 (FOMC plus MSFT/GOOGL), Oct 29 (AMZN plus GDP/PCE), Nov 2 (AAPL) and Nov 3 (AMD plus the midterms).
- **Cycle 83 (ER-004, A):** AMD (Nov 3 AMC), MSFT and GOOGL (Oct 28) are confirmed by company releases. AMZN (Oct 29) and AAPL (Nov 2) are confirmed via a secondary source citing the IR releases.
- **Cycle 84:** AMZN (ir.aboutamazon.com) and AAPL (investor.apple.com) are now primary-confirmed too.
- **Cycle 85 (ER-005, A):** BEA confirms GDP Q3 advance plus September PCE on Thu Oct 29 at 8:30 ET.
- **Cycle 86:** BLS jobs (Nov 6) and CPI (Nov 10) both fall after the window, per search of the bls.gov schedule; the direct fetch was blocked. No BLS event-guard day inside the window.
