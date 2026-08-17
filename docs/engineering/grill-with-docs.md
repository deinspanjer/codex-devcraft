## What it does

`grill-with-docs` runs `grilling` and `domain-modeling` together. The interview resolves a design tree while settled domain terms update `CONTEXT.md` and only qualifying durable decisions become ADRs.

The docs remain domain documentation, not a disguised spec or transcript.

## When to reach for it

You invoke this by typing `$grill-with-docs` — the agent won't reach for it on its own. Use it when a material repository design decision fits one session and its vocabulary or durable decisions should persist. For stateless thinking use [grill-me](https://aihero.dev/skills-grill-me); for localized implementation with no material design decision use [minimal-workflow](https://aihero.dev/skills-minimal-workflow).

## Prerequisites

Run it in the repository whose `CONTEXT.md` and ADRs it may update. Existing domain-doc layout and ADR rules remain authoritative.

## Two records, two bars

| What resolved | Where it goes |
| --- | --- |
| Stable domain term, meaning, relationship, or avoided synonym | `CONTEXT.md` |
| Durable decision that qualifies under the repository's ADR rules | ADR |
| Implementation detail, tentative idea, or ordinary answer | Conversation only |

## Common questions

**Does every answer become an ADR?**

No. An ADR is reserved for a qualifying durable decision. Writing unimplemented or tentative ideas as in-force architecture poisons later context.

## It's working if

- The interview uses successive structured prompts and recomputes dependent questions.
- `CONTEXT.md` remains a glossary rather than a plan.
- ADRs contain durable decisions, not every resolved choice.
- The factual-assumption inventory runs before implementation begins.

## Where it fits

`grill-with-docs` is the design step in the single-session and full flows. [ask-devcraft](https://aihero.dev/skills-ask-devcraft) skips it for direct and minimal work.
