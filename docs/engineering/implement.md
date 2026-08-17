## What it does

`implement` builds work described by the user, a spec, or a ticket. It resolves the exact work item, uses TDD where meaningful, runs proportional checks, and closes with the selected code-review coverage.

It never commits automatically. A commit is a separate developer-authorized action.

## When to reach for it

You invoke this by typing `$implement` — the agent won't reach for it on its own. Use it when a spec or ticket is already the authority for the change. For fully specified conversational work use [direct-work](https://aihero.dev/skills-direct-work); for localized judgment without a spec use [minimal-workflow](https://aihero.dev/skills-minimal-workflow).

## Prerequisites

Provide the work item or keep its full context in the current conversation. Tracker-backed tickets require the repository configuration written by [setup-devcraft](https://aihero.dev/skills-setup-devcraft).

## Build, verify, review

The test entry point is an existing observable path at the highest practical level that reproduces the real contract. TDD is used where an independent behavioral assertion is meaningful; prose and localized presentation changes receive the smallest relevant verification instead.

## Common questions

**Does it commit when finished?**

No. It reports the implementation and verification state. It commits only when you explicitly ask.

**Does it always force TDD?**

No. It uses TDD where meaningful and avoids tests that merely preserve an intentional edit.

## It's working if

- The exact ticket or request is resolved before editing.
- Checks stay narrow while working and are proportional at closeout.
- Review covers the selected workflow risk without inventing findings.
- The working tree remains uncommitted unless you requested a commit.

## Where it fits

`implement` is the build step in designed flows and can also stand alone for a ready work item. [tdd](https://aihero.dev/skills-tdd) supplies the red-green discipline; [code-review](https://aihero.dev/skills-code-review) owns finding admission; [ask-devcraft](https://aihero.dev/skills-ask-devcraft) routes lighter work around it.
