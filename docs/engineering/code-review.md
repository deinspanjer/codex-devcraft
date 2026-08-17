## What it does

`code-review` reviews a requested branch, PR, diff, or work-in-progress surface and admits only evidence-backed findings. It reports correctness and safety, repository conformance, non-blocking design signals, one optional specialized review, and readiness as separate axes.

An empty review is valid. Smells are search lenses, not issue quotas or automatic remedies.

## When to reach for it

Type `$code-review`, or the agent reaches for it automatically when you ask for a code review or a workflow reaches closeout. It works directly without [ask-devcraft](https://aihero.dev/skills-ask-devcraft); the router selects coverage when present, while this skill owns finding admission.

## Pin the surface

The review includes committed, staged, and unstaged changes in the requested scope and captures the diff once so every pass sees the same bytes. With no range, it reviews a changed branch from its default-branch merge base; if the branch has no changes, it reviews the current worktree against `HEAD`.

## Finding admission

Every admitted finding has a concrete present consequence, a file and location, and the smallest evidence-justified correction. Generic best practice, taste, speculative future needs, and smells without a present consequence stay out.

| Axis | What belongs |
| --- | --- |
| Correctness and safety | Behavioral defects, regressions, data loss, security failures, unmet requirements |
| Repository conformance | Violations of documented rules governing the changed paths |
| Design signals | Present, evidence-backed design costs; always non-blocking on their own |
| Additional review | At most one of security, architecture, migration/data, or performance |
| Readiness | Ready or not ready based on blockers and verification gaps |

## Common questions

**Does it require parallel subagents?**

No. Direct, minimal, and single-session work use focused same-agent review. Independent reviewers are reserved for the full multi-session flow or an explicit request.

**Can a smell block readiness?**

Not by itself. It blocks only when independent correctness, safety, or documented-standard evidence exists, and then it is reported on that axis.

**Does it review implementation plans?**

No. Implementation-plan review remains a separate discipline.

## It's working if

- The diff includes uncommitted work when that work is in scope.
- Every finding is evidence-backed and location-specific.
- Design signals remain visually separate and non-blocking.
- A clean change can produce zero findings.
- Specialized review is recommended only for a current risk surface and remains the developer's choice.

## Where it fits

`code-review` closes [implement](https://aihero.dev/skills-implement), [minimal-workflow](https://aihero.dev/skills-minimal-workflow), and direct work, and also stands alone for any requested diff. [ask-devcraft](https://aihero.dev/skills-ask-devcraft) selects coverage but does not admit findings.
