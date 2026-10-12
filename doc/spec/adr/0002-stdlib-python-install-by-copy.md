---
purpose: "Why everything is stdlib Python and installed by copying, not a package."
concepts: [stdlib, dependencies, pypi, npm, install]
---

# ADR-0002: Standard-library Python, installed by copying

**Status:** recorded after the fact, from the packaging evaluation of 2026-10-11.

**Context.** Spec Kit needs Python with uv; OpenSpec needs Node and npm. Inside companies, a new package
or runtime may need approval, which slows adoption. Readers judging the project also benefit from being
able to read all of it.

**Decision.** The script and installer use only the Python 3.8+ standard library. Users clone this repo
and run `install.py`, which copies files into their repo. Rejected for now: publishing to PyPI or npm.
It stays a small later step if companies ask for a versioned package.

**Consequences.** Nothing to install beyond git and Python, and the whole project reads end to end.
Upgrades mean pulling and re-running the installer; `durablespec.py version` shows which version a repo
has. Front matter is parsed by hand, so it supports only a small YAML subset.
