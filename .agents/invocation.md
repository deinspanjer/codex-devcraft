# Model-invoked vs user-invoked

Every `SKILL.md` in this repo is a skill. The one axis that splits them is **invocation** — who can reach it:

- **User-invoked** — reachable **only through explicit `$skill-name` invocation**. Set `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. The `description` is **human-facing**: a one-line summary for the skill picker. Strip trigger lists ("Use when the user says…").
- **Model-invoked** — reachable by **Codex or user**. The default: omit the `policy` block from `agents/openai.yaml`. The `description` is **model-facing** and keeps rich trigger phrasing ("Use when the user wants…, mentions…, asks for…") so auto-invocation fires. The test for whether a skill should stay model-invoked: _could Codex usefully reach for this autonomously?_ (Reuse is the reason to extract a skill, not the test.)

The policy excludes a user-invoked skill from Codex's implicit reach, so no other skill can fire it. A user-invoked skill may apply model-invoked skills, but it can never reach another user-invoked skill.

Every skill also carries an `agents/openai.yaml` beside its `SKILL.md`. It holds Codex UI metadata — `interface.display_name` and `interface.short_description` for the skill picker — and, for user-invoked skills, `policy.allow_implicit_invocation: false`.

Bucket `README.md`s and the top-level `README.md` group entries into **User-invoked** and **Model-invoked**.

## Dependencies between them

Dependencies are expressed as an explicit instruction to **apply the named skill** ("Apply the `grilling` skill"), not deep `../other-skill/FILE.md` cross-references. Shared reference docs live inside the skill that owns them; other skills reach that material by applying the owning skill, not by linking across folders.

This is about **operative** instructions — a skill's own steps telling Codex to apply another skill now. Router prose that names skills for a human to pick from (`ask-devcraft`, bucket `README.md`s) uses `$skill-name` labels.

A step that needs two skills names both explicitly: "Apply the `grilling` and `domain-modeling` skills."

This convention only holds when the named skill is **model-invoked**. A user-invoked skill can never be reached this way. When a step's precondition is a user-invoked skill such as `setup-devcraft`, tell the user to invoke `$setup-devcraft` explicitly.

## Passive vs active domain work

Merely _reading_ `CONTEXT.md` for vocabulary is a one-line prose pointer, not the `domain-modeling` skill. Only the active build/sharpen discipline (challenge terms, edge-case scenarios, write ADRs, update `CONTEXT.md` inline) is `domain-modeling`.
