---
purpose: "Standing rules for working on DurableSpec itself."
concepts: [conventions, stdlib, dogfooding, versioning, plain-language]
---

# Conventions

- **Python 3.8+, standard library only.** No packages, no build step, nothing to install beyond git
  and Python ([ADR-0002](../adr/0002-stdlib-python-install-by-copy.md)).
- **Plain markdown everywhere else.** Skills follow the [Agent Skills](https://agentskills.io) format;
  the standing instruction is a marked block in `AGENTS.md`. Nothing is written per agent product.
- **Plain language.** The rules, skills and README are read by product owners as well as engineers.
  Short sentences, no coined jargon.
- **Every feature passes one test:** would it still be useful if models were ten times smarter?
- **Versions move together.** `VERSION` in `template/durablespec.py` and `metadata.version` in both
  skills are bumped together.
- **This repo uses its own spec, by link.** `doc/spec/README.md` and `doc/spec/durablespec.py` are
  symlinks to `template/`, and `.agents/skills` and `.claude/skills` link to `skills/`, so this repo
  always runs what it ships. Don't run the installer on this repo.
- **The public repo carries no client or partner material.** Field-test findings are described by the
  kind of repo, not its owner. Internal notes live in `internal/`, which is not committed.
- **Apache 2.0, copyright Pike Labs, Inc.** New files carry no other attribution.
