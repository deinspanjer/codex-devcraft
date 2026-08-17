## What it does

`minimal-workflow` handles a localized change that needs some implementation judgment but no material design decision. It traces the relevant flow, implements, leaves one narrow load-bearing check, and runs a focused review.

It skips grilling, specs, and tickets by default.

## When to reach for it

You invoke this by typing `$minimal-workflow` — the agent won't reach for it on its own. Use it for a small feature, bug fix, or refactor whose desired outcome is clear but whose exact code change is not. For a fully specified edit, use [direct-work](https://aihero.dev/skills-direct-work).

## One escalation

If implementation reveals a material design decision, the agent offers one escalation to single-session grilling. You may resolve the decision inline and remain minimal.

## Common questions

**Does minimal mean untested?**

No. It means the narrowest load-bearing behavioral or regression check, not the absence of verification.

## It's working if

- No spec or ticket appears for localized work.
- The agent traces the affected callers before choosing the smallest change.
- One existing observable entry point proves the behavior when a test is warranted.
- A real design decision is surfaced once rather than silently guessed or inflated into a full workflow.

## Where it fits

`minimal-workflow` sits between [direct-work](https://aihero.dev/skills-direct-work) and the single-session grilling flow. [ask-devcraft](https://aihero.dev/skills-ask-devcraft) chooses among them.
