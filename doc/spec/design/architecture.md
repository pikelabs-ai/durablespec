---
purpose: "The parts of DurableSpec, what each does, and how they reach a user's repository."
concepts: [architecture, skills, script, installer, rules, AGENTS.md]
---

# Architecture

DurableSpec does three kinds of work, and each lives where it fits
([ADR-0001](../adr/0001-three-homes-skills-script-agents-md.md)):

| Work | Example | Home |
|---|---|---|
| Judgment | Should this change touch the spec? Which document owns it? | Two Agent Skills ([skills](skills.md)) |
| Mechanical checks | Index current? `owns:` paths exist? ADR numbers unique? | One stdlib script ([check script](check-script.md)) |
| Standing behavior | Read the spec before deciding anything | A block in `AGENTS.md` ([rules](rules.md)) |

```mermaid
flowchart LR
  subgraph src["DurableSpec repository (this repo)"]
    inst["<b>install.py</b><br/>[Container: Python]<br/>Adds or upgrades DurableSpec in a repo"]
  end
  subgraph repo["A team's repository"]
    block["<b>AGENTS.md block</b><br/>[Container: Markdown]<br/>Standing rule: read the spec first"]
    skills["<b>durablespec-create, durablespec-update</b><br/>[Container: Agent Skills]<br/>Judgment: what to write, and where"]
    spec[("<b>doc/spec</b><br/>[Container: Markdown]<br/>Purpose, design, decisions, rules, INDEX.md")]
    script["<b>durablespec.py</b><br/>[Container: Python]<br/>Builds the index, checks for drift"]
  end
  agent["<b>AI coding agent</b><br/>[External system]"]
  ci["<b>Git hook or CI</b><br/>[External system]"]
  inst -- "copies skills, script, rules and block" --> repo
  agent -- "always reads" --> block
  block -- "points to" --> spec
  agent -- "loads on request" --> skills
  skills -- "read and edit" --> spec
  skills -- "run" --> script
  script -- "indexes and checks" --> spec
  ci -- "runs check" --> script
```

The [installer](installer.md) puts these in a user's repository:

```
user's repo
  .agents/skills/durablespec-{create,update}/   copied from skills/
  .claude/skills/durablespec-*                  links to the above, for Claude Code
  doc/spec/durablespec.py                       copied from template/, always replaced
  doc/spec/README.md                            copied from template/, only if missing
  AGENTS.md                                     marked block from template/AGENTS-block.md
  CLAUDE.md                                     an "@AGENTS.md" line
```

After that, DurableSpec has no runtime presence. The user's agent reads `AGENTS.md`, loads a skill when a
request matches, and the script runs locally, in a git hook or in CI. Nothing calls home.

The repository README is the public introduction; its image is `doc/durablespec-hero.jpg`. The product page and the
comparison with other spec tools are on [pikelabs.ai](https://pikelabs.ai/durablespec), maintained in a
separate website repository.
