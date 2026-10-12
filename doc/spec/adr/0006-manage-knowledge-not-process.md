---
purpose: "Why DurableSpec manages what the team knows and never prescribes how the work gets done."
concepts: [scope, workflow, scaffolding, future-models]
---

# ADR-0006: Manage knowledge, not process

**Status:** recorded after the fact, from the README and the competitive comparison of 2026-10-11.

**Context.** Other spec tools walk the model through a fixed sequence: specify, plan, task, implement.
That scaffolding helps today's models and gets in the way as models improve.

**Decision.** DurableSpec records what the team knows (purpose, design, decisions) and never tells an
agent how to plan or break down work. Every feature must pass one test: would it still be useful if
models were ten times smarter? Rejected: a plan/task workflow, and per-change proposals.

**Consequences.** DurableSpec sits alongside per-change tools rather than competing with them. It grows
more valuable as models improve: no model can recover a decision nobody wrote down, and better writers
need a firmer rule about when not to write.
