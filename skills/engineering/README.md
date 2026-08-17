# Engineering

Skills for daily code work.

## User-invoked

Reachable only through explicit `$skill-name` invocation (`policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[ask-devcraft](../../plugins/codex-devcraft/skills/ask-devcraft/SKILL.md)** — Choose the lightest workflow, grilling depth, and review coverage, then continue in the same context.
- **[direct-work](../../plugins/codex-devcraft/skills/direct-work/SKILL.md)** — Execute a fully specified change directly with proportional verification.
- **[minimal-workflow](../../plugins/codex-devcraft/skills/minimal-workflow/SKILL.md)** — Implement a localized change with the narrowest load-bearing check.
- **[grill-with-docs](../../plugins/codex-devcraft/skills/grill-with-docs/SKILL.md)** — Grilling session that also builds your project's domain model, sharpening terminology and updating `CONTEXT.md` and ADRs inline.
- **[triage](../../plugins/codex-devcraft/skills/triage/SKILL.md)** — Move issues through a state machine of triage roles.
- **[improve-codebase-architecture](../../plugins/codex-devcraft/skills/improve-codebase-architecture/SKILL.md)** — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[setup-devcraft](../../plugins/codex-devcraft/skills/setup-devcraft/SKILL.md)** — Configure this repo for the engineering skills (issue tracker, triage labels, domain doc layout). Run once per repo.
- **[to-spec](../../plugins/codex-devcraft/skills/to-spec/SKILL.md)** — Turn the current conversation into a spec and publish it to the issue tracker.
- **[to-tickets](../../plugins/codex-devcraft/skills/to-tickets/SKILL.md)** — Break any plan, spec, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges — text in a local file, or native blocking links on a real tracker.
- **[implement](../../plugins/codex-devcraft/skills/implement/SKILL.md)** — Build described work with TDD where meaningful, proportional checks, and review; commit only when requested.
- **[wayfinder](../../plugins/codex-devcraft/skills/wayfinder/SKILL.md)** — Plan work larger than one Codex task can hold as a shared map of decision tickets, resolved one at a time.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[prototype](../../plugins/codex-devcraft/skills/prototype/SKILL.md)** — Build a throwaway prototype to answer a design question: a single shareable HTML file for state/logic, or several toggleable UI variations.

- **[diagnosing-bugs](../../plugins/codex-devcraft/skills/diagnosing-bugs/SKILL.md)** — Disciplined diagnosis loop for hard bugs and performance regressions: build a feedback loop that goes red on this bug → minimise → hypothesise → instrument → fix → regression-test.
- **[research](../../plugins/codex-devcraft/skills/research/SKILL.md)** — Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background subagent.
- **[tdd](../../plugins/codex-devcraft/skills/tdd/SKILL.md)** — Test-driven development through an existing observable entry point, one red-green vertical slice at a time.
- **[domain-modeling](../../plugins/codex-devcraft/skills/domain-modeling/SKILL.md)** — Actively build and sharpen a project's domain model — challenge terms, stress-test with scenarios, update `CONTEXT.md` and ADRs inline.
- **[codebase-design](../../plugins/codex-devcraft/skills/codebase-design/SKILL.md)** — Shared discipline and vocabulary for designing deep modules: small interfaces, clean seams, testable through the interface.
- **[code-review](../../plugins/codex-devcraft/skills/code-review/SKILL.md)** — Evidence-backed review across correctness, safety, repository conformance, non-blocking design signals, specialized-review need, and readiness.
- **[resolving-merge-conflicts](../../plugins/codex-devcraft/skills/resolving-merge-conflicts/SKILL.md)** — Work through an in-progress git merge or rebase conflict hunk by hunk, resolving by intent traced to each side's primary source, then finish the operation — never `--abort`.
- **[wizard](../../plugins/codex-devcraft/skills/wizard/SKILL.md)** — Generate an interactive bash wizard that walks a human through steps only they can perform: provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover.
