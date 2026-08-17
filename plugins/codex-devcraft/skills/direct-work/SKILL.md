---
name: direct-work
description: Execute a fully specified change directly with proportional verification.
---

# Direct Work

Use the developer's stated outcome or method as the scope. Inspect the relevant code and callers, then make the smallest root-cause change that satisfies it.

Fill reasonable, reversible local details without asking. Ask only when a missing decision changes the outcome, authority, safety, or an irreversible effect. An explicit workflow choice wins after at most one concrete evidence-based advisory.

Reuse repository patterns, the standard library, platform features, and installed dependencies before adding code or structure.

Verify proportionally through an existing observable test entry point. For bugs, check the narrowest behavioral invariant that captures the failure. For prose or localized presentation changes, use the smallest relevant verification instead of a patch-coupled test.

Finish with a focused same-agent review for correctness, safety, and repository conformance. Recommend a specialized review only when the current risk surface warrants it. Do not create a spec, tickets, workflow artifacts, or a commit unless the developer asks.
