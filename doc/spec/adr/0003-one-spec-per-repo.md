---
purpose: "Why every repo, monorepos included, gets one spec at the root."
concepts: [monorepo, one-spec, areas, owns]
---

# ADR-0003: One spec per repo, monorepos included

**Status:** accepted, 2026-10-11.

**Context.** Monorepos raised the question of a spec per module, or nested specs. Monorepos differ too
much for a fixed recipe: several complex, high-throughput modules are a different thing from a plain
REST application split into folders.

**Decision.** One spec at the root of every repo. Each part of a monorepo is an area in `design/` whose
`owns:` names its folders; decision records share one sequence. If a part later earns its own spec,
the team records that as a decision. Rejected: nested specs per module by default.

**Consequences.** One index, one place to look, and changed code still traces to its document. A large
monorepo needs judgment in grouping modules into five to twelve areas, which the create skill guides.
