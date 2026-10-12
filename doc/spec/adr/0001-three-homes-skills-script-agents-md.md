---
purpose: "Why DurableSpec ships as skills plus a script plus an AGENTS.md block, not a CLI tool."
concepts: [packaging, skills, script, AGENTS.md, cli]
---

# ADR-0001: Skills for judgment, a script for checks, AGENTS.md for standing behavior

**Status:** recorded after the fact, from the packaging evaluation of 2026-10-11.

**Context.** Before packaging, the question was "a tool or a skill?". The practice turned out to do three
different kinds of work: judgment (does this change touch the spec, and where), mechanical checks
(index, front matter, `owns:` paths, ADR numbers), and a standing rule (read the spec first) that must
apply in every session. Established spec tools ship a CLI whose main job is installing commands into
25 to 30 agent products.

**Decision.** Each kind of work goes where it fits. Judgment goes in Agent Skills, since only a model can
make those calls. Checks go in a plain script, since they are deterministic and must run in hooks and CI
where no agent is present. The standing rule goes in `AGENTS.md`, since skills load only on a matching
request. Rejected: a CLI tool as the primary interface, and putting the checks in a skill.

**Consequences.** No per-agent command formats to maintain. The weak spot is skill locations, which
differ between agents; the installer handles it (see [installer](../design/installer.md)). Skill quality
can vary by model, so portability has to be tested, not assumed.
