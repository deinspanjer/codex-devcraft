## What it does

`grill-me` runs a stateless `grilling` session. It inherits the design tree, successive structured prompts, fallback behavior, and factual-assumption inventory, but writes no repository artifact.

## When to reach for it

You invoke this by typing `$grill-me` — the agent won't reach for it on its own. Use it for a plan, decision, opinion, or piece of writing outside a repository. For repository work where terms and durable decisions should persist, use [grill-with-docs](https://aihero.dev/skills-grill-with-docs).

## Stateless by design

The resolved design remains in the conversation. If it must travel to another task, use [handoff](https://aihero.dev/skills-handoff); if it belongs in a project glossary or ADR, use `grill-with-docs` from the start.

## Common questions

**Will it jump straight into implementation?**

No. It closes the design tree, inventories factual assumptions, and waits for your confirmation before acting.

## It's working if

- The interview follows the `grilling` frontier rather than a fixed questionnaire.
- No `CONTEXT.md`, ADR, spec, or ticket is created.
- The agent waits for shared-understanding confirmation before action.

## Where it fits

`grill-me` is the stateless front door to [grilling](https://aihero.dev/skills-grilling). [ask-devcraft](https://aihero.dev/skills-ask-devcraft) routes repository implementation work separately.
