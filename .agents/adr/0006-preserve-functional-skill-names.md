---
status: accepted
---

# Preserve functional skill names while replacing upstream identity names

Skill names are a public interface: renaming every inherited skill would break saved prompts, wrappers, and user habits, while retaining upstream identity names would misrepresent ownership of the fork. Codex Devcraft therefore preserves functional names and renames only identity-specific entry points: `ask-matt` becomes `ask-devcraft`, and `setup-matt-pocock-skills` becomes `setup-devcraft`.

Behavior is reworked where Codex semantics require it or where Devcraft deliberately changes the workflow, including the new `direct-work` and `minimal-workflow` routes. Historical issue, commit, and provenance references remain upstream; current product instructions, metadata, source links, and public routing use Codex Devcraft names and locations.

## Considered options

- Rename every skill for a visibly distinct catalog. This would create duplicate concepts and needless migration work.
- Retain all upstream names. This would leave branded entry points that no longer describe the product.
- Preserve behavior-oriented names and replace only identity-oriented names. This keeps compatibility without obscuring the fork boundary.
