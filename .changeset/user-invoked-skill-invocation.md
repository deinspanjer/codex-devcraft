---
"codex-devcraft": patch
---

Stop skills from trying to reach user-invoked skills implicitly. Fix cross-skill references that violated the invariant in `.agents/invocation.md`, `to-spec`, `wayfinder`, `to-tickets`, `triage`, `code-review`, and `diagnosing-bugs`.

- `setup-devcraft` is user-invoked, so dependent skills tell the human to invoke `$setup-devcraft` instead of trying to apply it implicitly.
- `diagnosing-bugs`'s Phase 6 post-mortem hand off to `improve-codebase-architecture` (also user-invoked) the same way, from an autonomous, often-unattended bug-fixing flow with no human in the loop to catch the failed call. Removed the hand-off outright rather than softening it — it rarely fired in practice. Phase 6 is now "Cleanup" only; the mechanical checklist is untouched.
- Clarified in `.agents/invocation.md` that operative cross-skill instructions apply only to model-invoked skills.

Fixes #453.
