---
name: Local paid-price discovery
description: >-
  Use when negotiating a high-ticket local purchase (car, dealer appliance,
  furniture floor model) and you need what real buyers nearby actually paid
  before setting a target or contacting sellers.
---
# Local paid-price discovery

Goal: set a **walk-away / target out-the-door (OTD)** number from real recent transactions, not MSRP or dealer asking prices.

## When this applies
- Cars, dealer-sold goods, or any purchase where sticker price is theater and local comps matter.
- User has named make/model/trim/year (or equivalent SKU) and a geography.

## Steps
1. **Lock the exact product.** Year, make, model, trim, powertrain, and must-have options. Note nice-to-haves separately so comps stay comparable.
2. **Search real paid prices, not listings.** Prefer in this order:
   - Recent owner threads (Reddit, marque forums) that state **cash/OTD paid**, location, and date
   - Transaction aggregators / invoice tools when available for that category
   - Local classifieds sold posts (weaker signal)
   Skip dealer “internet price” pages as comps unless the buyer confirms they paid that.
3. **Normalize every data point.** For each usable report capture: date, metro/state, trim, options that move price, stated paid amount, whether tax/title/fees were included, and any dealer cash / rebate.
4. **Build a tight band.** Report typical paid, lowest credible paid, and sample size. Discard outliers without trim/option match. Convert to an **OTD target** and a hard **walk-away** (usually a bit above the best credible local paid, or at the user’s budget floor — ask only if those conflict).
5. **Deliver before outreach.** One short table + the recommended target and walk-away. Do not contact sellers until the user accepts the target band (or explicitly says to skip discovery).

## Do better than naive scrapes
- Prefer last 60–90 days; flag older comps.
- Same metro / state beats national averages for cars and dealer goods.
- Separate **sale price** from **OTD** (tax, doc fees, add-ons). Never mix them in one column.
- If security blocks or CAPTCHAs hit a source, switch sources — don’t thrash the same wall.
- Never invent a paid price. If comps are thin, say so and widen geography or age with labels.

## Handoff
Pass the accepted **target OTD** and **walk-away** into the multi-seller OTD quote skill (or equivalent outreach).
