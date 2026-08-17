# Phase boundaries

A **phase** is a chunk of work inside a session — the grilling, the implementation, the QA. The definition is fuzzy on purpose: a phase ends when you think *"ok, we're done with that"*.

The **phase boundary** is the gap between two phases, and it is the only place this decision belongs. Mid-phase there is no decision to make — continue, or split independent work into subagents. Compacting mid-phase makes Codex lose the thread.

## The five options

| Option       | What it does                                                    |
| ------------ | --------------------------------------------------------------- |
| **Continue** | Stay in the session. No context switch at all.                    |
| **New task** | Start a fresh Codex task with no inherited context.               |
| **`$handoff`** | Write a portable markdown file and seed a session anywhere with it. |
| **Subagent** | Send the task to its own context window and get a report back.     |
| **Compact** | Compress this context and continue from the summary.               |

## The tree

Work top to bottom at the boundary. The first **yes** wins.

**1. Can you continue in this session?** Two things make the answer yes: the next phase needs this phase as a **primary source**, or you have enough [smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone) left (~150k tokens) for the next phase to fit. Grilling → implementation is the standard yes: the implementation wants the reasoning verbatim, not a summary of it. Continue costs nothing and loses nothing, so rule it out before anything else.

**2. Is the context irrelevant to what comes next?** If the exploration, decisions, and dead ends are disposable, start a **new Codex task**. The old task remains available if needed.

The cost of getting this wrong is one-way. Clear a *relevant* context and you lose the **why** behind what you built, and no amount of reading the diff back gets it returned.

**3. Do you need to hand off?** `$handoff` is narrow. You need it only when you are:

- moving to a **new Codex task** that cannot inherit this context,
- moving to a **new directory** or repo,
- sending the work to a **colleague**,
- or forking a side task you found **mid-phase** without derailing what you're doing.

That list is the whole clause. What `$handoff` buys is **portability** — a file that travels. If nothing is travelling, you don't need it.

**4. Can the task be done AFK?** Is it scoped tightly enough to run without steering? Then send it to a **subagent** and leave this task untouched. Automated review is the standard case: the subagent reads the diff and reports.

**5. Otherwise, compact.** Relevant context, same Codex task, same directory, and you need to stay in the loop — this is where the tree lands often. State what the next phase is so the summary keeps what it needs.

Compaction is the **default, not the first reach**. It sits at the bottom because the four questions above are cheaper or more precise. Starting here can produce a summary that flattens a decision the next phase needs.

## Primary and secondary sources

Every move except **Continue** turns a **primary source** into a **secondary source** — the session as it happened, replaced by a summary of it. The trade is always the same shape:

| Source                            | Information | Noise | Room to move |
| --------------------------------- | ----------- | ----- | ------------ |
| Primary (Continue)                | Full        | Lots  | Little       |
| Secondary (compact, `$handoff`)    | Lossy       | Less  | Lots         |

This is why question 1 comes first. You only pay the lossiness when staying costs more than it saves.

## These are judgement calls

The questions are not objective — each has taste in it, and the same boundary can go two ways on two days. The value is in asking them **in order**, at the boundary rather than in the middle of the work.
