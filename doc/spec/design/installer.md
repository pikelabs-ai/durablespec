---
purpose: "install.py: adds or upgrades DurableSpec in a repository without touching anything else."
concepts: [installer, upgrade, symlink, windows, idempotent]
owns:
  - install.py
---

# Installer

`python3 install.py /path/to/repo [--dry-run]`, from a clone of this repo, or run for you by
`durablespec.py upgrade` from a fetched release. Safe to run again: it
upgrades its own files and touches nothing else.

- **Skills** are copied to `.agents/skills/`, which Codex, Gemini CLI, Copilot and others read. Claude
  Code reads only `.claude/skills/`, so the installer links each skill there. Where links fail (Windows
  without developer mode), it copies instead.
- **`doc/spec/durablespec.py`** is always replaced, because it is versioned.
- **`doc/spec/README.md`** is written only if missing, so local edits to the rules survive upgrades.
- **`AGENTS.md`** gets the marked block, added or replaced between its markers. **`CLAUDE.md`** gets an
  `@AGENTS.md` line if it lacks one.

- **It stays inside the repo.** Before writing anything it resolves every path it would write or delete;
  if a link sends one outside the repo, it stops and changes nothing. A link where a skill folder should
  be is replaced, never followed, and a `CLAUDE.md` that links to `AGENTS.md` is left alone.

- **Upgrade notes.** When an upgrade brings something it can't apply to an existing spec by itself
  (diagrams in 0.3.0), the `NEWS` list in `install.py` prints what to ask the agent for. It reads the
  repo's old version from its `durablespec.py` before replacing it.

Installing by copying, rather than through a package manager, is deliberate
([ADR-0002](../adr/0002-stdlib-python-install-by-copy.md)).
