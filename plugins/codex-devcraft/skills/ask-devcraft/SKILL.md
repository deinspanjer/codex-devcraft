---
name: ask-devcraft
description: Choose the lightest Devcraft workflow, grilling depth, and review coverage for the current situation.
---

# Ask Devcraft

Choose the lightest route that fits, then continue in the same context. Start with the developer's stated scope and confidence. Inspect repository facts yourself when they matter; ask the developer only for decisions.

## Select the route

An explicit workflow choice wins. You may give one concrete, evidence-based advisory, then honor the choice unless safety, missing authority, or irreversible harm requires a stop.

Stop exploring as soon as one route is clear:

| Route | Use when | Default execution |
| --- | --- | --- |
| **`direct-work`** | The outcome or method is already specified. | Work directly, fill reversible local details, and verify proportionally. |
| **`minimal-workflow`** | Localized implementation judgment remains, but no material design decision does. | Skip grilling, specs, and tickets; implement and run the narrowest load-bearing check. |
| **Single-session flow** | A material design decision remains and fits one session. | Run grilling, then implement in the same context with TDD where meaningful. |
| **Full flow** | The effort is broad, foggy, or spans sessions. | Keep the existing `grill-with-docs → to-spec → to-tickets → implement → code-review` flow. |

Consider the developer's intent, change complexity, documentation maturity, and current risk surfaces. Do not manufacture process because a repository is under-documented.

## Recommend once

Give this compact recommendation:

```text
Workflow: <route>
Grilling: <none | single-session | full-flow>
Review coverage: <focused same-agent | independent full-flow>
Additional review: <none | security | architecture | migration/data | performance>
Reason: <one short evidence-based sentence>
```

Ask for one confirmation. After confirmation, continue in this context using the confirmed route. User-invoked skills cannot invoke one another, so apply `direct-work` or `minimal-workflow` directly. For a single-session design, apply the `grilling` skill and, when domain language or durable decisions are in play, also apply `domain-modeling`.

If minimal work exposes a material design decision, offer one escalation to single-session grilling. The developer may instead resolve it inline and stay minimal.

## Review coverage

- Direct, minimal, and single-session work use focused same-agent review.
- Full multi-session work may use independent review agents.
- Recommend at most one specialized review when the current change has a matching risk surface: security for auth, secrets, tenant boundaries, or untrusted input; architecture for a new module/interface/persistence boundary or cross-cutting convention; migration/data for schema, destructive operations, or transformations; performance for performance-sensitive paths.
- The developer decides whether to run the specialized review.

## Existing on-ramps

- **Incoming reports** → `$triage`, then `$implement` once agent-ready. Tickets created by `$to-tickets` skip triage.
- **A hard bug or regression** → `$diagnosing-bugs`, then the lightest implementation route supported by the diagnosis.
- **A huge effort whose path is still foggy** → `$wayfinder`, then `$to-spec`, `$to-tickets`, and `$implement` when the map clears.
- **A runnable design question** → `$prototype`, then return the answer to the selected route.

## Supporting skills

- `$tdd` supplies the red-green discipline when behavior warrants it.
- `$code-review` can review any requested change directly; this router selects its coverage, while the review skill owns finding admission.
- `$domain-modeling` owns project terminology and qualifying ADRs; `$codebase-design` owns deep-module vocabulary.
- `$improve-codebase-architecture` surveys codebase-wide deepening opportunities.

## Phase boundaries

At a boundary between phases, read [PHASE-BOUNDARIES.md](PHASE-BOUNDARIES.md) and take the first fitting option: continue, clear, hand off, delegate, or compact. Continue is the default when the next phase needs the current reasoning and the context still fits.

## Standalone skills

- `$grill-me` — stateless grilling outside a working directory.
- `$grill-with-docs` — grilling with `CONTEXT.md` and qualifying ADR updates.
- `$handoff` — portable context for a new Codex task, directory, colleague, or side task.
- `$research` — primary-source investigation captured in the repo.
- `$to-questionnaire` — collect decisions from someone else.
- `$resolving-merge-conflicts` — resolve an active merge or rebase by intent.
- `$wizard` — guide steps only a human can perform.
- `$wait-what` — re-pitch a message that did not land.
- `$teach` — stateful multi-session learning.
- `$writing-for-agents` — write documents agents consume.

## Precondition

Run `$setup-devcraft` before the first tracker-dependent engineering flow. Custom issue trackers are supported.
