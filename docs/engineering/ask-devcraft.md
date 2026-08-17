## What it does

`ask-devcraft` chooses the lightest workflow that fits the current work, whether grilling is warranted, how much review to run, and whether one specialized review is worth considering.

It starts from your stated scope and confidence, verifies repository facts itself, recommends once, asks for one confirmation, and continues in the same context. It does not turn every change into a ceremony.

## When to reach for it

You invoke this by typing `$ask-devcraft` — the agent won't reach for it on its own. Use it when you want one front door to the suite or are unsure whether work is direct, minimal, designed in one session, or broad enough for the full flow.

| Situation | Likely route |
| --- | --- |
| Outcome or method already specified | `direct-work` |
| Localized judgment, no material design decision | `minimal-workflow` |
| One material decision that fits this session | Single-session grilling |
| Broad, foggy, or multi-session work | Full flow |

## The lightest route

The router stops exploring when one route is clear. An explicit developer workflow choice wins after at most one evidence-based advisory. Direct, minimal, and single-session work use focused same-agent review; independent reviewers are reserved for the full flow or an explicit request.

## Common questions

**Will it tell me other skills are missing because they are user-invoked?**

No. It treats the repository manifest and skill tree as authority instead of assuming the model-visible skill list is exhaustive.

**Does choosing a route start the work?**

Yes. After one confirmation it continues in the same context. The recommendation is a decision point, not a handoff ritual.

## It's working if

- The recommendation names workflow, grilling, review coverage, additional review, and one reason.
- Facts come from repository inspection rather than questions to you.
- Already-clear work reaches implementation without a spec or grilling session.
- Your explicit workflow choice is honored after at most one concrete advisory.

## Where it fits

`ask-devcraft` is the standalone router over the entire set. Its most common destinations are [direct-work](https://aihero.dev/skills-direct-work), [minimal-workflow](https://aihero.dev/skills-minimal-workflow), and [grill-with-docs](https://aihero.dev/skills-grill-with-docs).
