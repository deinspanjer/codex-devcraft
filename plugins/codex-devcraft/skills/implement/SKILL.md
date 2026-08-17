---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
---

Implement the work described by the user, a spec, or a ticket. Resolve the exact work item before editing and preserve the user's stated scope.

Apply the `tdd` skill where meaningful. Use the repository's existing test entry point at the highest practical level that reproduces the real contract.

Run the narrowest useful checks while working and the repository's proportional final checks at the end.

Once done, apply the `code-review` skill for the coverage already selected by the workflow. Commit only when the user explicitly requests it.
