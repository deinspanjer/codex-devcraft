---
name: code-review
description: Review a branch, PR, diff, or work-in-progress change for correctness, safety, repository conformance, design signals, and readiness. Use for direct code review or workflow closeout.
---

# Code Review

Own finding admission. `ask-devcraft` may select review coverage, but this skill decides what is evidence-backed enough to report. An empty review is valid.

## Process

### 1. Pin the review surface

Use the scope the user named. Include committed, staged, and unstaged changes in that scope. If no range is named, inspect repository state: review the current branch from its default-branch merge base when it has branch changes, otherwise review worktree changes against `HEAD`. Ask only when the intended surface remains ambiguous.

Capture the diff once so every pass reviews the same bytes. Confirm the surface is non-empty before continuing.

### 2. Gather authority

Read repository instruction and standards files that govern the changed paths. Find the originating request, issue, spec, or acceptance criteria when available. Missing documentation never creates a standard, and missing requirements never justify inventing one.

### 3. Review behavior and evidence

Trace changed behavior through its callers and observable entry points. Run the smallest relevant checks needed to validate a suspected finding. Review tests for sensitivity to the behavior they claim to protect, not mere presence.

For direct, minimal, and single-session work, use a focused same-agent pass. Reserve independent review agents for a full multi-session flow or an explicit request. Verify any delegated claim yourself before admitting it; never recursively invoke `code-review`.

### 4. Admit findings

Admit only high-signal findings with evidence in the current change. Every finding names the concrete consequence, cites the relevant file and location, and recommends the smallest correction justified by the evidence.

Exclude:

- generic best practice and personal taste;
- speculative future needs;
- quotas or invented work;
- smells without a present consequence.

Documented repository standards remain enforceable even when a breach does not immediately break behavior. Under-documented repositories may justify broader smell discovery, but a smell is only a search lens and judgment call. A design signal becomes blocking only through independent correctness, safety, or documented-standard evidence, in which case report it on that axis instead.

Useful lenses include Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, and Refused Bequest. None implies a categorical remedy.

## Output axes

Report these sections separately:

1. **Correctness and safety** — behavioral defects, regressions, data loss, security failures, and unmet requirements.
2. **Repository conformance** — documented repository rules the change violates.
3. **Design signals (non-blocking)** — evidence-backed present design costs relevant to this change.
4. **Additional review recommended** — `none`, or one specialized review with a short risk-based reason.
5. **Readiness** — ready or not ready, based on blocking findings and verification gaps.

An empty first three sections is a valid clean review.

Recommend at most one specialized review when warranted:

- authentication, authorization, secrets, tenant boundaries, or untrusted input → **security**;
- new module/interface/persistence boundary or cross-cutting convention → **architecture**;
- schema, destructive operation, or data transformation → **migration/data**;
- performance-sensitive path → **performance**.

The developer decides whether to run it. Keep implementation-plan review separate from code review.
