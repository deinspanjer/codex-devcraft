# Codex Devcraft

Low-ceremony Codex skills for practical engineering: direct work when the answer is already clear, just enough workflow when judgment remains, and deeper design flows only when the work earns them.

These skills are small, adaptable, and composable. They preserve developer control and use proportional testing and review.

## Provenance

- Forked from [Matt Pocock's skills](https://github.com/mattpocock/skills) at `9c9f36ccd3995266cd675468af71639c8dde1ec5`, preserving its Git history, attribution, and MIT license.
- Engineering disciplines were also reviewed from [Peter's toolkit](https://aipurveyors.com/peterz/peters-toolkit) at `9e5fe76301e25c54f330442051b41b2b17cd3d39` and adapted manually. Peter's repository is provenance, not a runtime dependency.
- Future upstream changes are reviewed and imported selectively.

## Installation

### 1. Get the skills

```bash
codex plugin marketplace add deinspanjer/codex-devcraft
codex plugin add codex-devcraft@codex-devcraft
```

Start a new Codex task after installation so the bundled skills are available.

### 2. Run `$setup-devcraft`

In Codex, run it once per repo. It will:

- Ask you which issue tracker you want to use (GitHub, GitLab, local files, or a custom workflow)
- Ask you what labels you apply to tickets when you triage them (`$triage` uses labels)
- Ask you where you want to save any docs we create

### 3. You're ready to go

## Why These Skills Exist

Devcraft adapts the upstream collection to fix common Codex failure modes while adding lighter routes for already-clear and localized work.

### #1: Codex Didn't Do What I Want

> "No-one knows exactly what they want"
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**. The most common failure mode in software development is misalignment. You think the dev knows what you want. Then you see what they've built - and you realize it didn't understand you at all.

There is a communication gap between you and Codex. The fix is a **grilling session** that gets Codex to ask detailed questions about what you're building.

**The Fix** is to use:

- [`$grill-me`](./plugins/codex-devcraft/skills/grill-me/SKILL.md) - for non-code uses
- [`$grill-with-docs`](./plugins/codex-devcraft/skills/grill-with-docs/SKILL.md) - same as [`$grill-me`](./plugins/codex-devcraft/skills/grill-me/SKILL.md), but adds more goodies (see below)

Use these when a material design decision remains. Already-specified and localized changes belong on the direct or minimal routes instead.

### #2: Codex Is Way Too Verbose

> With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
>
> Eric Evans, [Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**The Problem**: At the start of a project, devs and the people they're building the software for (the domain experts) are usually speaking different languages.

Codex is usually dropped into a project and asked to figure out the jargon as it goes. So it uses 20 words where 1 will do.

**The Fix** is a shared language that helps Codex decode the project's jargon.

<details>
<summary>
Example
</summary>

Here's an upstream [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) example. Which one is easier to read?

- **BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
- **AFTER**: "There's a problem with the materialization cascade"

This concision pays off session after session.

</details>

This is built into [`$grill-with-docs`](./plugins/codex-devcraft/skills/grill-with-docs/SKILL.md), which builds shared language and records qualifying durable decisions in ADRs.

> [!TIP]
> A shared language has many other benefits than reducing verbosity:
>
> - **Variables, functions and files are named consistently**, using the shared language
> - As a result, the **codebase is easier for Codex to navigate**
> - Codex also **spends fewer tokens on thinking**, because it has access to a more concise language

### #3: The Code Doesn't Work

> "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that’s too big."
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**: You and Codex are aligned on what to build, but the result still does not work.

It's time to look at your feedback loops. Without feedback on how its code actually runs, Codex is flying blind.

**The Fix**: You need the usual tranche of feedback loops: static types, browser access, and automated tests.

For automated tests, a red-green loop provides tight feedback: Codex writes a failing behavioral test first, then the minimum implementation that passes it.

The **[`$tdd`](./plugins/codex-devcraft/skills/tdd/SKILL.md) skill** slots into any project. It encourages a red-green loop and gives Codex guidance on what makes good and bad tests.

For debugging, **[`$diagnosing-bugs`](./plugins/codex-devcraft/skills/diagnosing-bugs/SKILL.md)** wraps best practices into a disciplined loop, gated phase by phase.

### #4: We Built A Ball Of Mud

> "Invest in the design of the system _every day_."
>
> Kent Beck, [Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

> "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
>
> John Ousterhout, [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**The Problem**: Codex can radically speed up coding, but it can also accelerate software entropy. Codebases get complex faster than their design improves.

**The Fix** for this is a radical new approach to AI-powered development: caring about the design of the code.

This is built in to every layer of these skills:

- [`$to-spec`](./plugins/codex-devcraft/skills/to-spec/SKILL.md) records settled implementation and testing decisions for multi-session work

And crucially, [`$improve-codebase-architecture`](./plugins/codex-devcraft/skills/improve-codebase-architecture/SKILL.md) surveys a codebase for deepening opportunities and hands you the candidates. Run it periodically when architecture upkeep is the actual task. It is a survey, not a rescue: on a genuinely old codebase it will find real candidates, but it won't untangle the mud for you.

### Summary

Software engineering fundamentals matter more than ever. These skills condense them into repeatable practices while keeping ordinary work lightweight.

## Reference

These split on one axis — who can invoke them. **User-invoked** skills are reachable only when you type them (for example, `$grill-me`); their job is to orchestrate. **Model-invoked** skills can be invoked by you or reached for automatically by Codex when the task fits; they hold the reusable discipline. A user-invoked skill may apply model-invoked skills, but never another user-invoked one.

### Engineering

Skills for daily code work.

**User-invoked**

- **[ask-devcraft](./plugins/codex-devcraft/skills/ask-devcraft/SKILL.md)** — Choose the lightest workflow, grilling depth, and review coverage, then continue in the same context.
- **[direct-work](./plugins/codex-devcraft/skills/direct-work/SKILL.md)** — Execute a fully specified change directly with proportional verification.
- **[minimal-workflow](./plugins/codex-devcraft/skills/minimal-workflow/SKILL.md)** — Implement a localized change with the narrowest load-bearing check.
- **[grill-with-docs](./plugins/codex-devcraft/skills/grill-with-docs/SKILL.md)** — Grilling session that also builds your project's domain model, sharpening terminology and updating `CONTEXT.md` and ADRs inline.
- **[triage](./plugins/codex-devcraft/skills/triage/SKILL.md)** — Move issues through a state machine of triage roles.
- **[improve-codebase-architecture](./plugins/codex-devcraft/skills/improve-codebase-architecture/SKILL.md)** — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[setup-devcraft](./plugins/codex-devcraft/skills/setup-devcraft/SKILL.md)** — Configure this repo for tracker-dependent engineering skills (issue tracker, triage labels, domain doc layout). Run once per repo.
- **[to-spec](./plugins/codex-devcraft/skills/to-spec/SKILL.md)** — Turn the current conversation into a spec and publish it to the issue tracker. No interview — just synthesizes what you've already discussed.
- **[to-tickets](./plugins/codex-devcraft/skills/to-tickets/SKILL.md)** — Break any plan, spec, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges — written as text in a local file, or as native blocking links on a real tracker.
- **[implement](./plugins/codex-devcraft/skills/implement/SKILL.md)** — Build described work with TDD where meaningful, proportional checks, and review; commit only when requested.
- **[wayfinder](./plugins/codex-devcraft/skills/wayfinder/SKILL.md)** — Plan work larger than one Codex task can hold as a shared map of decision tickets, resolved one at a time.

**Model-invoked**

- **[prototype](./plugins/codex-devcraft/skills/prototype/SKILL.md)** — Build a throwaway prototype to answer a design question — a single shareable HTML file for state/logic questions, or several radically different UI variations toggleable from one route.
- **[diagnosing-bugs](./plugins/codex-devcraft/skills/diagnosing-bugs/SKILL.md)** — Disciplined diagnosis loop for hard bugs and performance regressions: build a feedback loop that goes red on this bug → minimise → hypothesise → instrument → fix → regression-test.
- **[research](./plugins/codex-devcraft/skills/research/SKILL.md)** — Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background subagent.
- **[tdd](./plugins/codex-devcraft/skills/tdd/SKILL.md)** — Test-driven development through an existing observable entry point, one red-green vertical slice at a time.
- **[domain-modeling](./plugins/codex-devcraft/skills/domain-modeling/SKILL.md)** — Actively build and sharpen a project's domain model — challenge terms against the glossary, stress-test with edge-case scenarios, and update `CONTEXT.md` and ADRs inline.
- **[codebase-design](./plugins/codex-devcraft/skills/codebase-design/SKILL.md)** — Shared discipline and vocabulary for designing deep modules: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface.
- **[code-review](./plugins/codex-devcraft/skills/code-review/SKILL.md)** — Evidence-backed review across correctness, safety, repository conformance, non-blocking design signals, specialized-review need, and readiness.
- **[resolving-merge-conflicts](./plugins/codex-devcraft/skills/resolving-merge-conflicts/SKILL.md)** — Work through an in-progress git merge or rebase conflict hunk by hunk, resolving by intent traced to each side's primary source, then finish the operation — never `--abort`.
- **[wizard](./plugins/codex-devcraft/skills/wizard/SKILL.md)** — Generate an interactive bash wizard that walks a human through steps only they can perform: provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover.

### Productivity

General workflow tools, not code-specific.

**User-invoked**

- **[grill-me](./plugins/codex-devcraft/skills/grill-me/SKILL.md)** — Get relentlessly interviewed about a plan or design until every branch of the design tree is resolved.
- **[handoff](./plugins/codex-devcraft/skills/handoff/SKILL.md)** — Compact the current conversation into a handoff document for another Codex task or a colleague.
- **[teach](./plugins/codex-devcraft/skills/teach/SKILL.md)** — Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.
- **[to-questionnaire](./plugins/codex-devcraft/skills/to-questionnaire/SKILL.md)** — Turn a decision you can't answer alone into a Markdown questionnaire for the one person who can — filled in async, or together over a meeting. It grills you about the send (who it's for, what you need back), not the subject.
- **[wait-what](./plugins/codex-devcraft/skills/wait-what/SKILL.md)** — Fire this the moment a message doesn't land. Codex re-pitches it with the missing context, in plain English, using your `CONTEXT.md` vocabulary.

**Model-invoked**

- **[grilling](./plugins/codex-devcraft/skills/grilling/SKILL.md)** — Drain the current decision frontier through successive structured prompts, recomputing after every answer. The reusable interview primitive behind `grill-me`, `grill-with-docs`, `triage`, `wayfinder` and `improve-codebase-architecture`.
- **[writing-for-agents](./plugins/codex-devcraft/skills/writing-for-agents/SKILL.md)** — Write Codex-facing documents: skills, `AGENTS.md`, and docs reached by context pointers.
