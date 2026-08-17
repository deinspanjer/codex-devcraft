---
name: tdd
description: Test-driven development. Use when building behavior test-first, fixing a bug with a regression test, or working in a red-green loop.
---

# Test-Driven Development

TDD is the red → green loop. This skill makes that loop produce tests worth keeping: what a good test is, where it enters the system, the anti-patterns, and the rules of the loop.

When exploring the codebase, read `CONTEXT.md` (if it exists) so test names and interface vocabulary match the project's domain language, and respect ADRs in the area you're touching.

## What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification — "user can checkout with valid cart" tells you exactly what capability exists — and survives refactors because it doesn't care about internal structure.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidelines.

## Test entry point

Test through an existing observable entry point at the highest practical level that reproduces the real contract. Follow the repository's established test location, helpers, and command without asking.

Ask only when testing would require a new public interface, materially different cost or coverage, substantial infrastructure, likely flakiness, or accepting a coverage gap. Otherwise choose the entry point from repository evidence and continue.

For a bug, capture the narrowest behavioral invariant that fails for the reported case at the correct entry point. For prose or a localized presentation change, use the smallest relevant verification; do not add a patch-coupled test that merely preserves the edit.

When the public interface itself is in question, apply the `codebase-design` skill. That is a design decision, not a testing ritual.

## Anti-patterns

- **Implementation-coupled** — mocks internal collaborators, tests private methods, or verifies through a side channel (querying the database instead of using the interface). The tell: the test breaks when you refactor but behavior hasn't changed.
- **Tautological** — the assertion recomputes the expected value the way the code does (`expect(add(a, b)).toBe(a + b)`, a snapshot derived by hand the same way, a constant asserted equal to itself), so it passes by construction and can never disagree with the code. Expected values must come from an independent source of truth — a known-good literal, a worked example, the spec.
- **Horizontal slicing** — writing all tests first, then all implementation. Bulk tests verify _imagined_ behavior: you test the _shape_ of things rather than user-facing behavior, the tests go insensitive to real changes, and you commit to test structure before understanding the implementation. Work in **vertical slices** instead — one test → one implementation → repeat, each test a **tracer bullet** that responds to what the last cycle taught you.

## Rules of the loop

- **Red before green.** Write the failing test first, then only enough code to pass it. Don't anticipate future tests or add speculative features.
- **One slice at a time.** One entry point, one test, one minimal implementation per cycle.
- **Refactoring is not part of the loop.** It belongs to the review stage (see the `code-review` skill), not the red → green implementation cycle.
