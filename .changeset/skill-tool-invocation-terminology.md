---
"codex-devcraft": patch
---

Standardize cross-skill invocation on explicit "apply the named skill" instructions across `code-review`, `diagnosing-bugs`, `grill-with-docs`, `grill-me`, `improve-codebase-architecture`, `tdd`, `to-spec`, `to-tickets`, `triage`, and `wayfinder`.

- Operative steps now say "Apply the `grilling` skill" so Codex treats the name as an instruction rather than incidental prose.
- A step needing more than one skill names each one explicitly, such as "Apply the `grilling` and `domain-modeling` skills."
- Documents the convention in `.agents/invocation.md` for future skills to follow.
