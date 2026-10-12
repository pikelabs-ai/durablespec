---
purpose: "Why the folder is doc/spec and not doc/durablespec."
concepts: [folder, naming, doc/spec, credit, marketing]
---

# ADR-0004: The folder stays doc/spec

**Status:** accepted, 2026-10-12.

**Context.** Naming the folder `doc/durablespec` would make DurableSpec visible in every repo that uses
it, the way an `openspec/` folder advertises OpenSpec, and would avoid clashing with an existing
`doc/spec`.

**Decision.** Keep `doc/spec`. The spec belongs to the team, not the tool: it is plain markdown about
their system and stays useful if they stop using DurableSpec, while a folder named after a dropped tool
looks like leftover junk. "The spec" is also what people say. Credit comes instead from a line in each
spec's README and the `AGENTS.md` block heading. Rejected: `doc/durablespec`.

**Consequences.** Less passive visibility. Clashes are rare and already handled: the create skill
stops if `doc/spec/` holds other documents.
