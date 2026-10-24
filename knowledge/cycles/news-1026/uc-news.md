# Tradable v2-news check as of 2026-10-23 (SEC EDGAR live; market data from --market/--ohlcv). PAPER research, no orders.

## BAH Booz Allen Hamilton Holding Corp -> TRADABLE-NEWS (mechanical part); size bucket: large/mid (>= NYSE 40th pct); max weight 3%

| Check | Result | Value | Note |
|---|---|---|---|
| H1 listed NYSE/Nasdaq (no OTC) | PASS | NYSE | EDGAR exchange field |
| H2 price >= $5 | PASS | 78.31999969482422 | penny/lottery screen |
| H3 market cap >= $300M | info | $9,421M | info only in news profile; ~NYSE 5th pct ($256M, 2026-08) |
| H4 30d avg $ volume >= $2M | PASS | $126.6M | judgment C |
| H5 quoted spread <= 0.50% (re-check at order) | PASS | 0.05% | cost cap |
| H6 10-K/10-Q filed <= 150 days ago | PASS | 2026-10-23 (0d) | current SEC reporting |
| H7 no NT 10-K/10-Q late notice (12m) | PASS | none | late filer |
| H8 >= 8 quarters of reported revenue | info | 39 | info only in news profile; history; screens recent IPOs/SPACs |
| H8n >= 4 periodic filings (10-Q/10-K, ~12 months listed) | PASS | 46 filings since 2015-07-29 | news profile: relaxed history |
| H9 no 8-K Item 1.03 bankruptcy (12m) | PASS | none |  |
| I1 earnings release 8-K (Item 2.02) <= 135d | PASS | 0 | info sufficiency; WARN only |
| J0 no 'substantial doubt/going concern' text (400d) | PASS | 0 | WARN: read the filing; boilerplate is common |
| J1 max daily return 21d < 15% | PASS | 6.1% | MAX/lottery (Bali et al. 2011) |
| J2 63d realized vol < 60%/yr | PASS | 36% | high-variance junk |
| J3 no day with volume>=5x avg and abs(ret)>=10% in last 5 | PASS | 0.0 | herding (Barber et al. 2022): wait 20 sessions |

News sleeve (round 7): sleeve <= 10% of account, <= 3 names, 2-3% each. Before any buy: written thesis, DATED catalyst source (from 牛马), preset exit (stop or time limit). Every FLAG above must be answered by that catalyst source.

Manual info checklist (all required): read latest 10-K business + risk factors; latest earnings release or call transcript; >= 1 independent news/coverage item in 90 days; one-paragraph thesis + what would prove it wrong; next earnings date.

## BCPC BALCHEM CORP -> TRADABLE-NEWS (mechanical part); size bucket: large/mid (>= NYSE 40th pct); max weight 3%

| Check | Result | Value | Note |
|---|---|---|---|
| H1 listed NYSE/Nasdaq (no OTC) | PASS | Nasdaq | EDGAR exchange field |
| H2 price >= $5 | PASS | 177.0 | penny/lottery screen |
| H3 market cap >= $300M | info | $5,642M | info only in news profile; ~NYSE 5th pct ($256M, 2026-08) |
| H4 30d avg $ volume >= $2M | PASS | $48.8M | judgment C |
| H5 quoted spread <= 0.50% (re-check at order) | PASS | 0.26% | cost cap |
| H6 10-K/10-Q filed <= 150 days ago | PASS | 2026-10-23 (0d) | current SEC reporting |
| H7 no NT 10-K/10-Q late notice (12m) | PASS | none | late filer |
| H8 >= 8 quarters of reported revenue | info | 68 | info only in news profile; history; screens recent IPOs/SPACs |
| H8n >= 4 periodic filings (10-Q/10-K, ~12 months listed) | PASS | 76 filings since 2008-03-17 | news profile: relaxed history |
| H9 no 8-K Item 1.03 bankruptcy (12m) | PASS | none |  |
| I1 earnings release 8-K (Item 2.02) <= 135d | PASS | 0 | info sufficiency; WARN only |
| J0 no 'substantial doubt/going concern' text (400d) | PASS | 0 | WARN: read the filing; boilerplate is common |
| J1 max daily return 21d < 15% | PASS | 2.2% | MAX/lottery (Bali et al. 2011) |
| J2 63d realized vol < 60%/yr | PASS | 19% | high-variance junk |
| J3 no day with volume>=5x avg and abs(ret)>=10% in last 5 | PASS | 0.0 | herding (Barber et al. 2022): wait 20 sessions |

News sleeve (round 7): sleeve <= 10% of account, <= 3 names, 2-3% each. Before any buy: written thesis, DATED catalyst source (from 牛马), preset exit (stop or time limit). Every FLAG above must be answered by that catalyst source.

Manual info checklist (all required): read latest 10-K business + risk factors; latest earnings release or call transcript; >= 1 independent news/coverage item in 90 days; one-paragraph thesis + what would prove it wrong; next earnings date.

