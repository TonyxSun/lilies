---
name: Adversarial review
description: 'Use after a ship cloud agent pushes a branch, before any pull request.'
---
# Adversarial review

Review draft ship work on a pushed branch. Do not open a pull request until this pass is clean.

## Who runs it

A project crewmate starts a **fresh** subagent. Do not resume an old review subagent. The parent model is whatever the crewmate is running unless the captain asked for a specific one.

The subagent starts blank. The dispatch must include the repo, source control CLI, branch, base, and this entire prompt.

The subagent cannot see a cloud agent VM. It reads the branch through the source control CLI recorded for the project (`gh`, `glab`, or the recorded forge) or git, on the shared computer.

## Prompt

<Use this as the subagent task. Fill the context fields.>

Review the code changes and return structured findings with a risk assessment.

Context:

- branch: <branch>
- base: <default branch or merge base>
- review scope: branch changes between base and the pushed tip
- ignore patterns: none, unless the project listed some

Task:

- Read the relevant history and diff yourself.
- Focus findings on risks introduced by changed code, but inspect surrounding code, call sites, shared helpers, tests, and invariants when needed to understand root cause.
- Do NOT run tests during review.
- Analyze for bugs, risks, and code simplification opportunities.
- "Simplification" opportunities in this pass mean reducing code complexity through non-functional refactoring (e.g. deduplication, clearer control flow). They do NOT mean removing features, changing product behavior, or stripping intentional user-facing output; a component the intent does not require is reported through the dedicated Simplification section below, never as an "auto-fix" refactor.
- Treat security issues, performance regressions, breaking changes, and insufficient error handling as risks.
- Report a finding only when you can construct a concrete sequence that occurs during the change's intended usage, including rare but real sequences those callers actually perform. Do not report a finding whose only supporting path is a hypothetical unused execution that intended callers, the public API, or documented usage never take.
- Do a full review pass before returning. Do not stop after the first valid finding.

Rules:

- Anchor every finding to a specific file and one-indexed line number in the changed code when possible.
- Severity `error` must not merge. `warning` can be a follow-up. `info` is nice to have.
- Be concise and actionable. No generic advice like "add more tests".
- Only comment on things that genuinely matter.
- Do NOT report styling, formatting, linting, compilation, or type-checking issues.
- If the change is clean, return an empty findings array.
- For each finding, set action to one of:
  - `ask-user`: functional requirements, product behavior, or the author's deliberate intent. When in doubt, ask-user.
  - `auto-fix`: non-functional, not user-visible (correctness, error handling, security, performance, mechanical quality) that can be fixed without discussing intent.
  - `no-op`: informational.
- Classify by the remedy, not only by the topic. If the smallest honest remedy for a finding would add new durable state, a schema change, new background, retry, or persistence machinery, a new subsystem, or otherwise EXTEND the change beyond its stated intent rather than CORRECT what it already does, the action must be `ask-user` even when the defect itself looks mechanical. Say in the description that the remedy, not the defect, is what needs authorization.

Simplification (a dedicated pass over what the change introduced, in addition to the findings above):

- Enumerate every component the change introduced: a new branch, acceptance or matching path, fallback, alias, mode, flag, option, a second definition of a concept the code already defines once, or a parallel copy of a rule. Judge each one against the stated intent / change purpose. The stated purpose sets the required scope, not the implementation.
- For each component that is not strictly required to satisfy that intent, report a finding with severity `warning` and action `ask-user`. Name the component, state that no intent requirement needs it or which requirement it exceeds, and recommend removing it as the remedy. Do not recommend hardening, validating, or documenting a component the intent does not require.
- When a defect you reported above lives inside such a component, say so in that finding and name removal of the component as the smallest honest remedy, instead of prescribing a repair that keeps the component and hardens it.
- Report each unrequired component once. When a component is required but a strictly narrower form satisfies the intent, name the narrower form.

Risk assessment after all findings:

- `low` if well-bounded and straightforward
- `medium` if room to improve but safe to raise first
- `high` if it should not raise without explicit human approval

Return JSON:

```json
{
  "findings": [
    {
      "severity": "error|warning|info",
      "action": "ask-user|auto-fix|no-op",
      "file": "path",
      "line": 1,
      "description": "..."
    }
  ],
  "risk_level": "low|medium|high",
  "risk_rationale": "one sentence"
}
```

## Loop

- `auto-fix`: reply to the same cloud agent with the findings. Prefer the smallest correction. When a finding names removal of an unrequired component as the remedy, fix through removal rather than adding validation, fallbacks, or parallel machinery. Then a new fresh review subagent.
- `ask-user`: Firstmate takes one decision card to the captain. Do not raise.
- `error`: do not raise.
- Empty findings, or only `info` / already-answered `ask-user`: the crewmate may open the pull request.

Fix-forward. Do not revert the author's intentional first commit to silence a finding.

## Do not

- Do not open a pull request to make the branch visible for review
- Do not run this on scout tasks
