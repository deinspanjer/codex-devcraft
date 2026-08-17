## What it does

`tdd` builds behavior in red-green vertical slices: one failing behavioral test, the minimum implementation that passes, then the next slice.

It chooses an existing observable test entry point from repository evidence. It asks only when testing requires a new public interface, materially different cost or coverage, substantial infrastructure, likely flakiness, or an accepted coverage gap.

## When to reach for it

Type `$tdd`, or the agent reaches for it automatically when behavior should be built test-first or a bug needs a regression test. Skip it for prose, localized presentation, or work with no independent behavioral assertion.

## The test entry point

Use the highest practical existing entry point that reproduces the real contract and follow repository test patterns. For a bug, capture the narrowest invariant that fails for the reported case. Tests observe public behavior rather than internal call shape.

## Common questions

**Why didn't it ask me to choose a seam?**

Choosing an established test location is normally a repository fact, not a product decision. It asks only when the choice changes interface, cost, coverage, infrastructure, flakiness, or the accepted gap.

**Is this red-green-refactor?**

The implementation loop is red-green. Refactoring and broader design observations belong in review.

## It's working if

- One test fails for the intended reason before implementation changes.
- Each cycle is a vertical slice through an observable entry point.
- Expected values come from a spec, worked example, or known literal rather than reimplementing the algorithm.
- Internal refactors do not break behavior tests.
- Mocks appear only at system boundaries.

## Where it fits

`tdd` is the model-invoked testing discipline used by [implement](https://aihero.dev/skills-implement) and meaningful slices of [minimal-workflow](https://aihero.dev/skills-minimal-workflow). [ask-devcraft](https://aihero.dev/skills-ask-devcraft) decides when a workflow needs it.
