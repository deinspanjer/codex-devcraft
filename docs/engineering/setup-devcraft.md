## What it does

`setup-devcraft` records one repository's issue tracker, triage label vocabulary, and domain-doc layout under `docs/agents/`.

It is prompt-driven and proposes what repository inspection supports before writing. The configuration stays in the repository; it does not modify personal agent instructions.

## When to reach for it

You invoke this by typing `$setup-devcraft` — the agent won't reach for it on its own. Run it once before tracker-dependent flows such as [triage](https://aihero.dev/skills-triage), [to-spec](https://aihero.dev/skills-to-spec), or [to-tickets](https://aihero.dev/skills-to-tickets).

## Prerequisites

Run it from the repository it should configure. It writes `docs/agents/issue-tracker.md`, `docs/agents/domain.md`, optional triage-label mapping, and a small pointer block in the repository instruction file you approve.

## Repository-local configuration

| Decision | Default |
| --- | --- |
| Issue tracker | Match the repository remote; GitHub, GitLab, local Markdown, and custom workflows are supported. |
| Triage labels | Keep the five canonical roles when `triage` is installed. |
| Domain docs | One root `CONTEXT.md` and `docs/adr/`; offer multi-context only for a real monorepo. |

## Common questions

**Does it create labels in my tracker?**

No. It records how Devcraft's roles map to labels that already exist.

**Do I rerun it after every skill update?**

No. Rerun it when the repository changes tracker or document layout, or when the checked-in configuration no longer matches the skills reading it.

## It's working if

- Tracker-dependent skills stop guessing where work lives.
- The instruction file points to inspectable repository-local Markdown.
- No personal or global instruction file changes.

## Where it fits

`setup-devcraft` is run-once setup for tracker-dependent engineering skills. [ask-devcraft](https://aihero.dev/skills-ask-devcraft) routes the rest of the set.
