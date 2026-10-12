---
purpose: "Why spec diagrams follow the C4 model and are drawn in Mermaid."
concepts: [diagrams, c4, mermaid, ascii, structurizr]
---

# ADR-0007: C4 diagrams, drawn in Mermaid

**Status:** accepted, 2026-10-12.

**Context.** Specs need pictures of the system, and until now the rules said nothing about them, so each
repo drew its own way, mostly in ASCII. The C4 model's levels line up with the spec's folders: System
Context with the purpose, Container with the architecture, Component with an area. Its advice that the
code level is rarely worth drawing matches the rule that the spec is not a mirror of the code. Architects
also already know the vocabulary.

**Decision.** Diagrams follow C4, Context and Container first, Component only where an area needs it,
never code level. They are drawn as Mermaid flowcharts in C4 style: name, type and purpose in each box,
labeled arrows, a subgraph for the boundary. Both skills draw them once there is enough to show, roughly
three or more parts or outside systems. This is guidance; `check` doesn't enforce it. Rejected:
ASCII (breaks when edited, and agents draw it badly); Mermaid's own C4 syntax (experimental, poor
layout); Structurizr DSL (the reference C4 tool, but it needs its own tooling).

**Consequences.** Diagrams render on GitHub and GitLab and diff as text. In a terminal or a raw file they
read as source, which is still legible. A diagram is one more thing that can go stale, so the update skill
treats it as part of its document, and the prose stops repeating what the diagram shows.
