---
name: minimal-workflow
description: Implement a localized change with the narrowest load-bearing check.
---

# Minimal Workflow

Use when localized implementation judgment remains but no material design decision does. Skip grilling, specs, and tickets.

Trace the relevant flow and callers, reuse repository patterns, and implement the smallest coherent change. Use TDD where meaningful, through an existing observable test entry point at the highest practical level that reproduces the real contract.

Leave the narrowest load-bearing behavioral or regression check. Do not add patch-coupled tests for prose or localized presentation changes.

If implementation exposes a material design decision, offer one escalation to a single-session grilling flow. The developer may instead resolve it inline and stay minimal.

Finish with a focused same-agent review for correctness, safety, and repository conformance. Recommend a specialized review only for a current risk surface. Do not create workflow artifacts or a commit unless the developer asks.
