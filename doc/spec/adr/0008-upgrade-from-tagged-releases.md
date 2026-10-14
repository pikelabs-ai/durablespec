---
purpose: "Why upgrades fetch tagged releases with git, from a command in the repo's own script."
concepts: [upgrade, releases, tags, git, network, packaging]
---

# ADR-0008: Upgrade from tagged releases, through the repo's own script

**Status:** accepted, 2026-10-14.

**Context.** Upgrading meant cloning or pulling this repo and running the installer by hand, so repos
stayed on old versions. Tools such as Claude Code and Codex self-update with a global command, which
needs a package installed on every machine ([ADR-0002](0002-stdlib-python-install-by-copy.md) put that
off).

**Decision.** `doc/spec/durablespec.py`, already in every repo, gets an `upgrade` command. It finds the
newest `vX.Y.Z` tag with `git ls-remote`, shallow-clones that tag into a temporary folder, and runs its
installer. It never installs from an untagged branch. It is named `upgrade`, not `update`, so it can't be
confused with the `durablespec-update` skill. `DURABLESPEC_SOURCE` allows a company mirror. Rejected: a
PyPI or npm package with a global command (for now), and downloading archives (git is already present
and avoids unpacking archives by hand).

**Consequences.** Releases must be tagged. The command downloads and runs code, so it shows the source
and version first and supports `--dry-run`. It needs network access to the source; offline teams use a
mirror or the manual installer.
