---
purpose: "Why design/architecture.md opens with a list of every diagram in the spec, and why check enforces it."
concepts: [diagrams, c4, architecture, hub, discoverability, check]
---

# ADR-0010: architecture.md is the hub for diagrams

**Status:** accepted, 2026-10-28.

**Context.** People who need to understand a system start with its architecture, and many read only the
overview and `architecture.md`. [ADR-0007](0007-c4-diagrams-in-mermaid.md) puts each diagram next to
the prose that explains it: System Context in the overview, Container in `architecture.md`, Component in
area documents. That keeps one copy of each, but readers can't tell what pictures exist, and Component
diagrams in area documents go unseen. With agents building quickly, not knowing what exists is the
problem diagrams are meant to solve. In one working spec all four diagrams sat in `architecture.md` but
began in its fourth section.

**Decision.** Diagrams stay where ADR-0007 puts them. `design/architecture.md` opens with a
`## Diagrams` section listing every diagram in the spec, its own included, each with one line on what it
shows and a link to the heading it sits under. `check` fails when a diagram isn't linked from
`architecture.md`. Rejected: moving diagrams into a dedicated file or folder (two places to change for
every architecture change, and they drift); a generated `DIAGRAMS.md` holding copies (every diagram
twice in each diff, and a file people don't think to open); a generated list of links in `INDEX.md`
(not where people look).

**Consequences.** One page shows what pictures exist, and an agent can't add a diagram without listing
it there. Each diagram needs its own heading so a link can land on it. Existing specs fail `check` after
upgrading until the list is added; the upgrade note says how. The list is written by the skills, not
generated, so its descriptions can go stale even while `check` passes.
