---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you have not heard yet. A round drains its currently valid frontier; it does not dump the frontier into one message. After every answer, incorporate it and recompute the frontier before asking again. Never ask a question made stale by an earlier answer.

## Ask decisions

In Codex Default or Plan mode, when `request_user_input` is available, use it for one frontier decision at a time. Continue through successive calls in the same logical assistant turn until the currently valid frontier is drained or a required fact is still being investigated.

- Offer one to four mutually exclusive choices, subject to the tool's schema. Put the recommendation first and suffix its label with `(Recommended)`.
- Give each choice one short consequence sentence.
- Let the prompt's automatic free-form `Other` choice carry nuance.
- Do not number structured prompts or require the user to refer to an index.

If structured prompts are unavailable, ask at most three compact numbered Markdown questions at once, each with a recommendation. Recompute the frontier after the response.

An explicit user preference for question style, batching, or pace overrides these defaults.

Finding _facts_ is your job, never the user's. Inspect the environment instead of asking for discoverable facts. A fact still being investigated is an unsettled prerequisite: wait only on its downstream decisions and continue with the rest of the frontier. The _decisions_ are the user's: put each to them and wait.

## Close the tree

When the frontier is empty, perform a conversation-only cold inventory of every design-shaping factual assumption, including relevant dependents and negative claims. Verify anything not already evidenced. Mechanical mismatches may proceed; evidence that changes the design reopens the frontier. Create no mandatory spec, evidence file, or commit for this gate.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
