# Productivity

General workflow tools, not code-specific.

## User-invoked

Reachable only through explicit `$skill-name` invocation (`policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[grill-me](../../plugins/codex-devcraft/skills/grill-me/SKILL.md)** — Get relentlessly interviewed about a plan or design until every branch of the design tree is resolved.
- **[handoff](../../plugins/codex-devcraft/skills/handoff/SKILL.md)** — Compact the current conversation into a handoff document for another Codex task or a colleague.
- **[teach](../../plugins/codex-devcraft/skills/teach/SKILL.md)** — Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.
- **[to-questionnaire](../../plugins/codex-devcraft/skills/to-questionnaire/SKILL.md)** — Turn a decision you can't answer alone into a Markdown questionnaire for the one person who can — filled in async, or together over a meeting.
- **[wait-what](../../plugins/codex-devcraft/skills/wait-what/SKILL.md)** — Fire this the moment a message doesn't land. Codex re-pitches it with the missing context, in plain English, using your `CONTEXT.md` vocabulary.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[grilling](../../plugins/codex-devcraft/skills/grilling/SKILL.md)** — Drain the current decision frontier through successive structured prompts, recomputing after every answer.
- **[writing-for-agents](../../plugins/codex-devcraft/skills/writing-for-agents/SKILL.md)** — Write Codex-facing documents: skills, `AGENTS.md`, and docs reached by context pointers.
