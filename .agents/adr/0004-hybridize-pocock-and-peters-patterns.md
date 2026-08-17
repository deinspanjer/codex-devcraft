---
status: accepted
---

# Hybridize Pocock workflows with selected Peters engineering patterns

Matt Pocock's skill collection provides the base catalog, invocation split, and domain-document workflow. Peter's toolkit provides useful engineering disciplines around explicit developer control, proportional ceremony, test entry points, implementation review, and bounded workflow escalation. We chose to preserve the Pocock substrate and manually adapt selected Peters patterns instead of adopting either collection wholesale.

Peter's repository is reviewed provenance at commit `9e5fe76301e25c54f330442051b41b2b17cd3d39`, not a runtime dependency, Git submodule, or remote to merge. The first release adds direct and minimal routes while retaining the deeper single-session and multi-session flows for work that earns them.

## Considered options

- Keep the upstream workflows unchanged. This preserves familiarity but keeps more ceremony than ordinary Codex work needs.
- Adopt Peter's toolkit as the governing workflow or dependency. This would replace useful upstream concepts and couple the fork to another system.
- Selectively adapt the patterns that strengthen Codex behavior. This preserves a coherent base while making each divergence explicit and locally owned.
