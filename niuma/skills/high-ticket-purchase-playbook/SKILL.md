---
name: High-ticket purchase playbook
description: >-
  Use when the user wants an end-to-end high-ticket local purchase (especially a
  car) handled like a modern agent buy: comps, multi-dealer written OTD quotes,
  then competitive negotiation with human gates.
---
# High-ticket purchase playbook

Orchestrates a Clawd-style (but stricter) buy for cars and other dealer / multi-seller high-ticket goods.

## Sequence
1. Run [Local paid-price discovery](sand-workflow:local-paid-price-discovery) → user accepts target OTD + walk-away.
2. Run [Multi-seller OTD quote hunt](sand-workflow:multi-seller-otd-quote-hunt) → written comparable quotes (no phone leak, no unsolicited outreach).
3. Run [Competitive quote negotiation](sand-workflow:competitive-quote-negotiation) → bidding loop with approve-before-send on every consequential reply.
4. **Human close:** credit app, e-sign, deposit, pickup. Agent stops at the paperwork wall.

## Hard upgrades vs early “agent bought a car” demos
- Explicit yes before any seller contact or form submit.
- Never auto-fill the user’s phone onto dealer forms.
- Email/writing preferred; voice negotiation is the user’s job.
- OTD means itemized all-in — challenge add-ons in writing.
- One negotiation variable at a time (price before trade/APR).
- Wrong-thread / wrong-recipient check before every send.
- No credit apps, signatures, or payments by the agent.
- Quote sheet + kill the email-watch routine when the deal ends.

## Scope
Goods and local dealer purchases. Travel and pure e-commerce checkouts stay on their own skills.
