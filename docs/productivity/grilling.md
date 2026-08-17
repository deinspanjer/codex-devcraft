## What it does

`grilling` models a plan, decision, or idea as a design tree and drains the current **frontier**: decisions whose prerequisites are already settled.

In Codex Default or Plan mode it normally asks one decision per structured prompt, incorporates the answer, recomputes the frontier, and continues in the same logical turn. It asks you for decisions and discovers facts itself.

## When to reach for it

Type `$grilling`, or the agent reaches for it automatically when a real design decision needs stress-testing. Use [grill-me](https://aihero.dev/skills-grill-me) for the stateless wrapper and [grill-with-docs](https://aihero.dev/skills-grill-with-docs) when resolved terms and durable decisions belong in repository docs.

## The frontier

Each prompt offers mutually exclusive choices with the recommendation first, one consequence sentence per choice, and a free-form `Other` path for nuance. If structured prompts are unavailable, the fallback asks no more than three numbered decisions at once.

When the tree resolves, a cold inventory verifies design-shaping factual assumptions. Mechanical mismatches may proceed; design-changing evidence reopens the frontier.

## Common questions

**Why not show every current question in one message?**

An early answer can invalidate later questions. Successive prompts preserve the frontier while avoiding stale choices and index-heavy replies.

**Can I ask for a different pace or format?**

Yes. An explicit preference for batching, pace, or question style overrides the defaults.

## It's working if

- Five independent decisions arrive as successive structured prompts.
- Dependent questions are recomputed after each answer.
- The recommendation is selectable by label, not an index.
- Discoverable facts never become questions for you.
- The Markdown fallback never asks more than three decisions at once.

## Where it fits

`grilling` is the model-invoked interview primitive used by [grill-me](https://aihero.dev/skills-grill-me), [grill-with-docs](https://aihero.dev/skills-grill-with-docs), and designed flows. [ask-devcraft](https://aihero.dev/skills-ask-devcraft) decides when it is warranted.
