---
name: Multi-seller OTD quote hunt
description: >-
  Use when the user wants inventory matching specific constraints and written
  out-the-door quotes from multiple local sellers or dealers before negotiating.
---
# Multi-seller OTD quote hunt

Goal: find matching units, then collect **comparable written out-the-door quotes** from several sellers without leaking the user’s phone or starting a call storm.

## Preconditions
- Product constraints are locked (trim, color, options, radius, must-haves).
- A **target OTD** and **walk-away** exist (run local paid-price discovery first when comps matter).
- User has explicitly approved **outbound contact** to sellers. No forms, emails, or DMs without that yes.

## Steps
1. **Inventory sweep.** Use the category’s best inventory tool or dealer sites. Record for each match: seller, stock # / VIN / SKU, distance, days on lot if shown, asking / “internet” price, link.
2. **Rank outreach.** Prefer: in-radius → exact constraints → longer days-on-lot (more room to discount) → written-quote friendly dealers. Cap the first wave (often 3–7) unless the user asks for wider.
3. **Contact channel rules (strict):**
   - Prefer **email or web forms that do not require a phone number**.
   - Never put the user’s real phone on a form unless they explicitly said to. If a form requires phone, pause and ask, or use an email-only path.
   - Never auto-SMS or auto-call sellers.
   - One clear ask: **best out-the-door price** for that exact unit (VIN/stock), itemized: vehicle/product, discounts/rebates, mandatory fees, optional add-ons (decline by default), tax/title if applicable, **OTD total**.
4. **Template the ask.** Same constraints and same OTD definition to every seller so quotes compare. State you want everything in writing; calls get “please email the breakdown.”
5. **Log a quote sheet.** Seller | unit ID | asking | itemized fees | OTD | expiry | source message link. Update as replies arrive.
6. **Human gate.** Drafts only until the user approves the first-wave send list and copy. After approval, send only what they approved.

## Failure modes to avoid
- Prefilling phone/email from connected accounts “because it’s convenient” without an ask.
- Mixing trade-in, financing rate, and sale price in the first ask (sale/OTD only unless the user said otherwise).
- Treating dealer add-ons as mandatory without challenging them in writing.
- Contacting sellers before inventory is deduped (same VIN on two sites = one outreach).

## Handoff
When ≥2 written OTDs exist (or the wave timed out), run competitive quote negotiation.
