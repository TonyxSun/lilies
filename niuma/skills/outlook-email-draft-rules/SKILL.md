---
name: Outlook email draft rules
description: >-
  Use this when drafting or sending email from Wuyue’s Outlook
  (sunwuyue@live.com / LIVE.COM), especially replies in an existing thread.
---
# Outlook email draft rules (Wuyue)

## Threading
- `DraftExternalMessage` with `mailbox: outlook` creates a **new** email only. It cannot set `replyToMessageId`. Real in-thread replies only work via Gmail’s draft card (`replyToMessageId`).
- If the living thread is on Outlook and the user wants a **reply**:
  1. Say so in chat before offering a card: you cannot attach it to the thread from here.
  2. Put the finished body in chat (or a plain code block) for them to paste after **Reply** in Outlook on the right message.
  3. Do **not** open an Outlook draft card framed as a reply (Subject `Re:` alone does not thread).
- New outbound (no prior thread) may use the Outlook draft card.

## Line breaks
- Outlook draft-card sends have sometimes arrived as one run-on paragraph. Put real blank lines between paragraphs in the body string.
- Prefer short paragraphs over “Hi X, sentence. Thanks,” on one line.
- After they send an Outlook card, if it was a multi-paragraph body, spot-check Sent Items once for missing newlines; if broken, say so and offer a corrected paste for them to resend via Reply if needed.

## Checklist before any email draft card
1. Mailbox = Outlook or Gmail?
2. New message or reply? If Outlook + reply → no card; paste for user.
3. Body has blank lines between paragraphs?
4. From address = real account address (`sunwuyue@live.com` for Outlook).
