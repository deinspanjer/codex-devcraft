## What it does

`handoff` compacts the conversation you are in into a **handoff document** — one Markdown file, written to your OS's temporary directory rather than the workspace, that a fresh Codex task or colleague can read.

What it buys is **portability**, not compression. You need a file only when work must travel to a new Codex task, a different directory, a colleague, or a side task. If nothing is travelling, stay in the current task or compact its context.

## When to reach for it

You invoke this by typing `$handoff`; Codex will not reach for it implicitly. Pass a note about what the destination task is for, and the document is written for it.

Four situations are the whole trigger:

| Situation | Why a file |
| --- | --- |
| Moving to a new Codex task | The new task cannot see the old [context](https://www.aihero.dev/ai-coding-dictionary/context) |
| Moving to a different directory or repo | A prototype directory is the common case |
| Sending the work to a colleague | They need something they can read |
| Forking a side task found mid-phase | You keep working; a second Codex task takes the fork |

For anything else — same task and directory, moving from [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling) to implementation — continue or compact within Codex. [ask-devcraft](https://aihero.dev/skills-ask-devcraft) carries the phase-boundary decision.

## Branching is the use people skip

The fork case is worth knowing. You **stay in the current task** and hand a copy of the accumulated context to a second Codex task working in parallel.

That is what the detour through [prototype](https://aihero.dev/skills-prototype) uses. You are deep in a design conversation, you hit a question that only running code will settle, and you do not want to spend the thread you built on finding out. Hand off to a prototype session, get the answer, hand the answer back, and reference it from the original thread. Two crossings, one live conversation, nothing re-explained.

Continuing preserves the conversation as a primary source. Compacting preserves intent inside the task. `$handoff` preserves the work's ability to move elsewhere.

## What travels, and what doesn't

The document carries the live thread — what's in flight, why, and what's next — plus a **suggested skills** section naming what the receiving Codex task should apply. Secrets are redacted before it is written.

What it deliberately does not carry is anything already written down. Specs, plans, ADRs, issues, commits and diffs are referenced by path or URL, never copied. That keeps the file small, and it keeps the settled detail in one place instead of two that drift.

## Common questions

**Handoff or compact?**
Compact unless something is travelling. Staying on the same task is not a handoff. `$handoff`'s advantage is the file you can carry to a new Codex task, directory, or person.

**What is the difference between compacting and handoff?**
Compacting keeps the summarized intent inside the current task. `$handoff` writes a portable file for somewhere else. Both turn a **[primary source](https://www.aihero.dev/ai-coding-dictionary/primary-source)** into a **[secondary source](https://www.aihero.dev/ai-coding-dictionary/secondary-source)**; continuing is the only lossless option.

**Where did my handoff file go?**
The temp directory. Ask Codex for the exact path before moving on. Temp is deliberate: a handoff is a transit document, not an artifact you maintain.

**My handoff vanished between sessions.**
Codex tasks may not share the same temporary storage, and `/private/tmp` disappears on reboot. If the destination task is not starting soon, copy the file somewhere durable. The same applies to files the document points at.

**How do I hand it to the next Codex task?**
Open the destination task and say: `Read <path>, then continue.` Point at the file rather than pasting its contents into a shell command, where backticks and substitutions can be mangled.

**Is this the same as forking a Codex task?**
No. A fork inherits the task context; this skill produces a targeted summary in a file. Use a fork when it reaches the destination. Use `$handoff` when the work must cross a directory or person boundary.

**When does something belong in `AGENTS.md` instead?**
Ask whether it remains true next month. `AGENTS.md` is standing project context loaded into every task. A handoff is about one piece of work in flight and is dead once that work lands.

**It captures the what, not the why.**
A fair criticism. Tell the skill what the destination task is for, so it keeps the reasoning that bears on that outcome. Read the document before handing it over and downgrade unverified beliefs; the receiving Codex task may otherwise treat them as facts.

**Why does Codex not invoke it automatically?**
Handoff is a destination choice that belongs to the user. Its `agents/openai.yaml` sets `policy.allow_implicit_invocation: false`, so it runs only when you type `$handoff`.

## It's working if

- The document is a small fraction of the conversation, and the specs, issues and diffs appear in it as paths and URLs rather than as copied text.
- You can read it cold, without the original session open, and know what to do next.
- The receiving Codex task starts working instead of asking you to re-explain the setup.
- In the fork case, your original session is still sitting there untouched when you come back to it.
- The suggested-skills section names the skill you'd have reached for yourself.
- Nothing in it is a key, a token, or a password.

## Where it fits

`handoff` is a narrow standalone at the seam between Codex tasks. Its closest neighbour is [prototype](https://aihero.dev/skills-prototype), because a prototype often lives in another directory. At a phase boundary, [ask-devcraft](https://aihero.dev/skills-ask-devcraft) helps choose between continuing, handing off, delegating, or compacting.
