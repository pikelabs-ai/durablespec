---
purpose: "What is built, what is being tested, and what comes next."
concepts: [status, version, field-tests, beta]
---

# Status

As of 2026-10-28. **Version 0.4.0, beta. The repository is public.**

**Built:** the two skills, the check script (index, check, version, upgrade), the installer, the rules template and
the `AGENTS.md` block. Since 0.3.0 the skills draw C4 diagrams in Mermaid
([ADR-0007](../adr/0007-c4-diagrams-in-mermaid.md)); since 0.3.1 the update skill always asks whether a
change added or removed a deployable part, user or outside system, and the `AGENTS.md` block asks for the
update before every commit; since 0.3.2 `durablespec.py upgrade` installs the newest tagged release
([ADR-0008](../adr/0008-upgrade-from-tagged-releases.md)); since 0.3.4 people in diagrams carry a figure.
Since 0.4.0 the installer stays inside the repo, agents treat the spec as knowledge, not commands
([ADR-0009](../adr/0009-knowledge-not-commands.md)), the update skill keeps secrets out, and
`architecture.md` opens with a list of every diagram ([ADR-0010](../adr/0010-architecture-is-the-diagram-hub.md)).
This repo uses its own spec, diagrams included.

**Field-tested** (v0.2 came from what these found): a new spec for a small Node app with no prior spec; a
draft central spec for a team's multi-module monorepo; and a spec written alongside a new infrastructure
repo. 0.4 was tried before release on an existing multi-service app with years of docs and no spec; it
found three bugs, since fixed. The practice itself has been in daily use since spring 2026.

**Not yet done from the pre-publication test plan:** replaying past commits through `durablespec-update` to
measure how often it writes and where; running that replay on a second agent and model; and migrating a
repo from the older hand-copied script and skill.

**Next:** the rest of the security hardening in [security](security.md), as 0.5: upgrades that run
only signed releases, and `check` flags for instruction-like text and secrets. Then messaging to match.

**After that:** feedback from the first team using it, and the replay test.
