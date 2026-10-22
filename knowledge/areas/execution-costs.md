# Execution & costs — ~$1k Robinhood cash account (Trader, cycle 01, 2026-10-22)

Plan: `cycles/01-execution-costs-plan.md`. Grades: A = peer-reviewed/replicated; B = solid data/regulator/primary docs; C = anecdote.
Note: we are paper trading now, but these rules make the paper results comparable to what real money would get.

## Bottom line
- Zero commission ≠ zero cost. Round-trip execution costs on identical market orders ranged ~0.07%–0.46% across brokers in a large controlled experiment. Use **limit orders**, trade liquid large caps, and avoid the open.
- Cash-account mechanics (T+1 settlement, good-faith/freeriding) matter more for us than the PDT rule, which never applied to cash accounts and has been replaced for margin accounts anyway.
- **Taxes are the biggest hidden drag vs the index**: short-term gains are taxed as ordinary income; a buy-and-hold SPY position defers tax. Retros should show an after-tax estimate.

## Findings
- [E-001] Controlled experiment, ~85,000 simultaneous identical market orders across 6 accounts at 5 brokers (Dec 2021–Jun 2022): mean round-trip cost 0.07%–0.46% excluding commissions; price improvement $0.03–$0.08/share (19%–47% of the NBBO spread); differences come from wholesalers giving different brokers different prices; PFOF level does not explain the variation (A). Schwarz, Barber, Huang, Jorion & Odean, J. Finance, Jul 2025. https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.13467
- [E-002] SEC order (Dec 17, 2020): Robinhood's unusually high PFOF rates contributed to inferior execution prices that cost customers $34.1M in aggregate *even after* commission savings (2015–2018 period); $65M penalty, no admission (B, regulator; historical, not current quality). https://www.sec.gov/newsroom/press-releases/2020-321
- [E-003] Market orders execute at the best available price but price is not guaranteed and can deviate from the quote; limit orders guarantee price, not execution; stop orders become market orders when triggered (B). SEC Investor Bulletin, updated 2026-08-18. https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14
- [E-004] Robinhood fractional shares: $1 minimum; dollar-based orders during market hours are converted to shares and executed immediately "at the best available price" (i.e., market-style); fractional orders are handled **Not Held** (Robinhood has time/price discretion); only NMS-listed stocks/ETFs; fractional orders can't be cancelled 9:20–9:30am ET; fractional shares aren't transferable (B, broker primary doc). https://robinhood.com/us/en/support/articles/fractional-shares/
- [E-005] Intraday spreads are U/reverse-J shaped: widest in the first 30 minutes after the open, narrowing through the day, rising slightly into the close (A, but NYSE data from 1989). McInish & Wood, J. Finance 1992. https://doi.org/10.1111/j.1540-6261.1992.tb04408.x
- [E-006] Closing auctions were ~9% of total US equity volume on a typical 2025 day, ~20% on rebalance/expiration days (B/C, vendor research). BMLL. https://www.bmlltech.com/news/market-insight/into-the-close-unpacking-u-s-closing-auction-dynamics-and-the-impact-of-the-russell-reconstitution . Implication: the close is the deepest liquidity point; it's also the price our rules use (closing-price signals).
- [E-007] Settlement is **T+1** since May 28, 2024 (a Monday sale settles Tuesday) for stocks and ETFs (B). SEC Investor Bulletin. https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin
- [E-008] Cash accounts (Reg T): you must pay for a purchase before selling it. Buying with unsettled sale proceeds is allowed, but selling that new security before the earlier sale settles is **freeriding** → broker may freeze the account for 90 days (trade only with fully paid cash) (B). SEC Investor Bulletin "Trading in Cash Accounts," updated 2026-08-07. https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/updated-9 . (Brokers also track "good faith violations"; commonly 3 in 12 months → 90-day restriction per broker policy — B/C, Fidelity FAQ via search, not opened.)
- [E-009] PDT: the old pattern-day-trader rules ($25k minimum) were margin-account rules. FINRA Regulatory Notice 26-10 (Apr 20, 2026) **replaced them entirely** with intraday margin standards for margin accounts, effective June 4, 2026, broker phase-in until Oct 20, 2027 (B, regulator). Irrelevant to our cash account. https://www.finra.org/rules-guidance/notices/26-10
- [E-010] Taxes: assets held ≤1 year → short-term gain, taxed as ordinary income; >1 year → long-term at 0/15/20% depending on income; net capital losses deductible up to $3,000/yr with carryforward (B). IRS Topic 409, reviewed 2026-09-24. https://www.irs.gov/taxtopics/tc409
- [E-011] Wash sale: loss disallowed if substantially identical securities are bought **within 30 days before or after** the loss sale (a 61-day window); the disallowed loss is added to the replacement's basis (deferred, not lost) in a taxable account; in an IRA it's permanently lost (B). IRS Pub 550. https://www.irs.gov/publications/p550 ; Investor.gov glossary https://www.investor.gov/introduction-investing/investing-basics/glossary/wash-sales
- [E-012] Trading costs explain most of the retail gap to the market (A). Barber & Odean 2000 (R-003).
- Our arithmetic on cost drag: at 0.3% assumed round trip (mid of E-001's range) and 100% annual turnover, cost ≈ 0.3%/yr; at 500% turnover (a position held ~10 weeks on average) ≈ 1.5%/yr — a big share of any plausible momentum edge after decay (T-018). Short-term tax at, e.g., a 24% bracket vs 15% LTCG on the same gain is a 9-point haircut on realized gains vs a deferred index holding.

## Proposed rules (execution & costs) — checked against current repo rules
| # | Rule (one line, mechanical) | Evidence | Status |
|---|---|---|---|
| E-R1 | Use limit orders only for whole-share trades: buy limit = ask + 0.1% (sell = bid − 0.1%), day order; if unfilled, re-evaluate next session rather than chasing. | E-001, E-003 | New |
| E-R2 | Fractional (dollar) orders only for stocks/ETFs with price > 10% of equity per share (i.e., when a whole share would break the 10% cap) and only in liquid names (avg daily dollar volume > $500M). | E-004 | New (threshold judgment) |
| E-R3 | No orders in the first 30 minutes (9:30–10:00am ET); morning re-verify runs at/after 10:00am ET. | E-005 | New |
| E-R4 | Signals are computed on official closes; when acting on a close-based exit, use the next session's limit order (or a limit-on-close if the broker supports it). | E-006, R-011 | New |
| E-R5 | Cash discipline: never sell a position bought with unsettled proceeds before those proceeds settle (T+1); track "settled cash" separately from "buying power" in the daily file. | E-007, E-008 | New |
| E-R6 | Paper P&L must deduct an assumed 0.30% round-trip cost per trade; retros report pre-tax and an estimated after-tax return (ST gains at an assumed marginal rate) vs SPY/QQQ buy-and-hold. | E-001, E-010, E-012 | New |
| E-R7 | Wash-sale rule clarified: no rebuy of a security sold at a loss within 30 calendar days **after**, and note any buys in the 30 days **before**, the loss sale (61-day window). | E-011 | Changes existing (clarifies "30-day wash-sale") |
| E-R8 | PDT is not a constraint (cash account; PDT replaced June 2026); the binding constraint is settled cash. | E-008, E-009 | New (documentation) |

## Round 2 (2026-10-22, cycle 02) — adversarial check + gaps
### New findings
- **E-013 (B)** "Retail limit orders", Review of Finance 30(2):459 (2026): retail limit orders are ~25.5% of orders; fill rate 65.2% vs 99.8% for marketable orders; unfilled shares cost ~15.9 bp of opportunity cost, but all-in implementation shortfall is still ~8 bp lower than marketable orders (via search synthesis; full text fetch timed out — numbers not checked in the paper). https://academic.oup.com/rof/article/30/2/459/8277182
- **E-014 (A)** Linnainmaa (JF 2010): individual investors' limit orders get picked off (adverse selection), which mechanically produces poor post-trade returns and apparent disposition/contrarian behaviour. Resting limit orders far from the market are not free. https://doi.org/10.1111/j.1540-6261.2010.01576.x
- **E-015 (A+C)** Rebalance frequency: Novy-Marx & Velikov 2016 (T-027) + our test — weekly rebalancing raised turnover ~2.5× (688%→1717%/yr) and cut CAGR (26.5%→21.3%); monthly with a hold buffer (top 10 in / rank >20 out) cut turnover to 418%/yr. For a $1k account where each trade is a fixed effort/approval, monthly + buffer is clearly better.

### Adversarial verdicts
| Rule | Counter-evidence | Verdict |
|---|---|---|
| E-R1 limit at ask+0.1% / bid−0.1% | E-013: passive limits miss ~1/3 fills; E-014: resting limits get picked off. Ours are *marketable* limits (cross the spread with a cap), so non-fill is rare and pick-off risk small | Confirm (B) |
| E-R2 fractional only when needed | No counter-evidence; at $1k many S&P 100 names need fractional to hit 10% | Confirm, merged |
| E-R3 no orders 9:30–10:00 | No counter-evidence; spreads widest at open (McInish-Wood) | Confirm (B) |
| E-R4 signal on close, act next session | Backtest built this way; works | Confirm (B) |
| E-R5 settled cash | Regulatory | Confirm (A) |
| E-R6 0.30% RT in paper P&L | Schwarz et al. range 0.07–0.46% | Confirm (B) |
| E-R7 61-day wash-sale window | IRS Pub 550 | Confirm (A) |
| E-R8 PDT not binding | Documentation only | Keep in file, not in final list |
