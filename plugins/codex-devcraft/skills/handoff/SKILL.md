---
name: handoff
description: Compact the current conversation into a handoff document for another Codex task or a colleague.
---

Write a handoff document summarising the current conversation so a fresh Codex task or colleague can continue the work. Save it to the user's OS temporary directory, not the current workspace.

Include a "suggested skills" section naming which skills the receiving Codex task should apply.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
