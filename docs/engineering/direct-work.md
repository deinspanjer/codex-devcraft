## What it does

`direct-work` executes a change whose outcome or method is already specified. It fills reversible local details, implements the smallest root-cause change, and verifies proportionally.

It deliberately creates no spec, tickets, workflow artifacts, or commit unless you ask.

## When to reach for it

You invoke this by typing `$direct-work` — the agent won't reach for it on its own. Use it when you have already said what should change or how to change it. For localized work that still needs implementation judgment, use [minimal-workflow](https://aihero.dev/skills-minimal-workflow).

## Proportional verification

The check matches the risk: an existing behavioral test entry point for code, the narrowest regression invariant for a bug, or a focused lint/render/manual check for prose and localized presentation.

## Common questions

**Will it challenge my chosen workflow?**

At most once, and only with concrete evidence. It then follows your choice unless safety, missing authority, or irreversible harm requires a stop.

## It's working if

- The agent starts from your scope instead of reopening design.
- The diff is the smallest coherent root-cause change.
- Verification is strong enough for the risk without producing patch-coupled tests.

## Where it fits

`direct-work` is the shortest implementation route. [ask-devcraft](https://aihero.dev/skills-ask-devcraft) recommends it when the outcome or method is already clear.
