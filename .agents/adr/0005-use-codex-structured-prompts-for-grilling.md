---
status: accepted
---

# Use Codex structured prompts for grilling

A large Markdown questionnaire exposes decisions that may become stale as earlier answers reshape the design. Grilling therefore models the interview as a design tree and drains only the currently unblocked decision frontier through successive Codex structured prompts, normally one decision per prompt, recomputing the frontier after every answer.

Each prompt offers mutually exclusive choices with the recommendation first, a short consequence for each choice, and free-form nuance through `Other`. Codex discovers factual answers independently and asks the user only for decisions. When structured prompts are unavailable, the fallback is at most three compact numbered questions; an explicit user preference for batching or pace wins.

## Consequences

`grilling`, `grill-me`, and `grill-with-docs` share this interaction contract. `grill-with-docs` continues recording resolved terms in `CONTEXT.md` and only qualifying durable decisions as ADRs.
