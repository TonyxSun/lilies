---
name: Submit YPF Uber Eats expense
description: >-
  Use when Wuyue gives a date (like 0821) and wants YPF meal expenses submitted
  from that day's Uber Eats orders into the MGC expense Google Form.
---
# Submit YPF Uber Eats expense

## Goal
For a given date `{mmdd}` (example: `0821` = August 21), collect **every** Uber Eats order from that calendar day, fill the MGC Expense Submission Form, attach all receipt PDFs, and submit. On-demand only — run when Wuyue names a date.

## Inputs
- `{mmdd}` — required date code (MMDD). Derive calendar `{month}/{day}` for the description (e.g. `0821` → `8/21`).
- `{portion_count}` — optional integer `xx` for how many 份. If unknown/unavailable, omit it.
- `{payer_name_and_zelle}` — value for "Name and Zelle 付款方式". Prefer prior form value / saved preference; if missing, ask once. Never hardcode phone numbers into skill text.

## Fixed destinations
- Form: `https://docs.google.com/forms/d/e/1FAIpQLScPEv3YZYaaKG7t-yww3A8PBebXy0arwMqohxu_K60P7DHnFg/viewform`
- Assumes signed-in Chrome for Google Forms (`tonysunwuyue@gmail.com`).
- Receipt folder: `/home/box/workspace/mgc_ypf_receipts/` (create if needed). Name files `{mmdd}_1.pdf`, `{mmdd}_2.pdf`, …; if form allows only one file (max 10 MB), merge/compress to `{mmdd}_all_compressed.pdf` under 10 MB.

## Form field mapping
On "Expense Report 1" (click **Next** from intro if needed):
1. **Ministry 事工:** `YPF 团契`
2. **Expense Category 支出分类:** `Food 食物`
3. **Expense 费用 ($):** sum of that day's Uber totals (USD)
4. **Description 具体内容:** `YPF {month}/{day} 饭食 {portion_count} 份` or without ` {portion_count} 份` if unknown
5. **Name and Zelle:** `{payer_name_and_zelle}`
6. **Receipt upload:** one PDF with every that-day receipt (merge + compress under 10 MB if needed)
7. **Required disclaimer:** check `我确认已经和部门负责人沟通过，并且得到了这项支出的批准。`

## Steps
1. Open the form; re-auth Google if signed out.
2. **Receipts via Gmail connector first** — search Uber Eats order emails for that date (e.g. `from:uber.com after:YYYY/MM/DD before:YYYY/MM/DD`, subjects like "Your … order with Uber Eats"); download each PDF attachment as `{mmdd}_{n}.pdf`. Use Uber Eats UI only if Gmail is missing a receipt.
3. Compute total and optional portion count; merge/compress for the single-file 10 MB upload limit.
4. Fill fields as mapped; check the disclaimer.
5. Confirm with the user before Submit (unless they already said to submit). After success, remind that the form asks to notify Qianshu on WeChat.

## Do not
- Do not invent orders/totals; do not embed secrets; do not prefer Uber scraping when Gmail has receipts; do not create a recurring auto-submit.

## Report back
Date, merchants + amounts, total, description, file attached, submitted yes/no.
