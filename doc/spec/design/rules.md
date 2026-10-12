---
purpose: "The rules every user repo gets: the one rule, where things go, and the standing AGENTS.md instruction."
concepts: [one-rule, layout, front-matter, adr-format, AGENTS.md, credit]
owns:
  - template/README.md
  - template/AGENTS-block.md
---

# Rules

`template/README.md` becomes `doc/spec/README.md` in each user repo. It is the policy the skills defer
to, so it is the most important text in the project. It holds:

- **The one rule:** touch the spec only if a reader tomorrow would form a materially different picture
  without the change. The default is no.
- **Where things go:** `purpose/`, `constitution/`, `design/`, `adr/`, plus `backlog.md`.
- **Conventions:** front matter (`purpose`, `concepts`, `owns`), the decision-record format, never
  editing a decided record, build status only in `design/status.md`, length guidance, one spec per repo
  ([ADR-0003](../adr/0003-one-spec-per-repo.md)), always at `doc/spec/`
  ([ADR-0004](../adr/0004-folder-stays-doc-spec.md)), and C4 diagrams in Mermaid
  ([ADR-0007](../adr/0007-c4-diagrams-in-mermaid.md)).
- **A credit line** pointing back to this repository, so anyone who opens a spec can find where it came
  from without the tool's name in the path.

The installer writes it only when a repo has none, so a team can adapt its copy. Changes here reach
existing repos only if their owners take them.

`template/AGENTS-block.md` is the standing instruction: read `doc/spec/INDEX.md` before deciding, and
run `durablespec-update` before committing. It sits between `durablespec:start` and `durablespec:end`
markers so the installer can replace it without touching the rest of `AGENTS.md`.
