---
status: accepted
---

# Fork the upstream collection as Codex Devcraft

The upstream skill collection remains the foundation, but its product identity and distribution are not Codex-specific. We chose a public Codex-specific fork that preserves the upstream Git history, attribution, and MIT license while giving Codex Devcraft its own interaction model, release history, and selectively imported upstream changes.

This supersedes ADR-0002's decision to defer a native Codex plugin. The fork resolves Codex's single-skill-path constraint by placing every promoted skill under `plugins/codex-devcraft/skills/`, leaving non-promoted work outside the plugin, and distributing the result through the repository-backed Codex marketplace.

## Considered options

- Continue contributing only to the upstream collection. This would preserve one source but would not provide a Codex-specific product boundary.
- Duplicate promoted skills into a generated plugin directory. This would create a sync process and a second source of truth.
- Fork and restructure the promoted set around the native Codex plugin boundary. This makes the fork responsible for its divergence while keeping provenance intact.

## Consequences

Codex Devcraft owns its public skill behavior and release decisions. Upstream changes are reviewed and imported manually rather than merged automatically, and the promoted plugin directory is the canonical source for shipped skills.
