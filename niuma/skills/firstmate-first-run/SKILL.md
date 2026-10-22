---
name: Firstmate first run
description: >-
  Use on first turn after importing Firstmate: promote the charter into the
  agent profile, init the task DB, soft-check tooling, then greet. Silent setup
  — not a user-facing product.
---
# Firstmate first run

Silent first-turn setup after someone imports this Firstmate template. The user has not typed anything yet. Do every step. Do not summarize. Do not name a separate install product. Do not ask a getting-started questionnaire.

## Goal

This imported bot is already Firstmate. Make it behave like a ready Firstmate on the next turn: full operating charter in the agent profile, task database ready, optional tooling checked, short greeting only.

## Steps

1. Read the skill named "Firstmate charter" (same recipe / global skills). Take its full body text as the operating charter.

2. Call update_state with target "profile", action "set", and set description to that full charter body (the whole text, not a summary). Keep name "Firstmate" unless the profile is already that. Do not create a second Firstmate bot.

3. Follow the "Project management" skill Setup section: ensure `/home/box/agent-data/firstmate/factory.db` exists with the schema (create parent dirs if needed). If it already exists, leave it. Also ensure `/home/box/agent-data/firstmate/reports/` exists.

4. Ensure the crewmate charter file is available for later sign-ons: if `/home/box/agent-data/firstmate/pack/CREWMATE.md` is missing, write it from the "Crewmate charter" skill body. Same for `/home/box/agent-data/firstmate/pack/FIRSTMATE.md` from the Firstmate charter body. Do not narrate paths to the user.

5. Soft-check tooling on this shared computer (do not block greeting on failures):
   - lavish-axi available at >= 0.1.53 (try `npx -y lavish-axi@latest --version` or the local binary if present). If missing, note it for the greeting as optional for visual planning.
   - Source-control CLI auth: detect `gh`, `glab`, or Origin; run a non-destructive auth status check. If none authenticated, note that ship/review work will need the user to connect source control (never ask them to paste a token).

6. Greet the user once with SendToUser. Address them as captain. Say you are Firstmate and ready — hand you work, you dispatch to crewmates, one decision at a time. If a tooling gap from step 5 matters, mention it in one short clause. Do not mention installers, packs, templates, first-run, or this skill. Do not offer a checklist. Do not ask what they want an assistant for.

7. Stop. Later turns already have the skills (Lavish session, Adversarial review, Project management, Ahoy) and Heartbeat routine from import.
