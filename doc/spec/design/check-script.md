---
purpose: "durablespec.py: the index builder and mechanical checks, identical in every repo."
concepts: [index, check, front-matter, owns, drift, ci]
owns:
  - template/durablespec.py
---

# Check script

`durablespec.py` lives at `doc/spec/durablespec.py` in each user repo and is the same file everywhere: it
has no settings. It finds the spec from its own location, and reads each document's front matter rather
than any configured folder. This came from the drift seen when an earlier index script was copied by
hand between repos and each copy hard-coded its own paths.

- **`index`** rewrites `INDEX.md`: one line per document, grouped by folder, built from front matter.
- **`check`** exits 1 if a document lacks front matter or a purpose, has unknown keys, has an `owns:`
  path that is missing or outside the repo, has a broken relative link, or shares an ADR number with
  another; if a diagram isn't listed in `design/architecture.md`
  ([ADR-0010](../adr/0010-architecture-is-the-diagram-hub.md)); if anything looks like a secret; or if
  `INDEX.md` is stale. It also prints notes, without failing, for design documents that
  own nothing and top-level folders no `owns:` covers, skipping folders git doesn't track, and
  text that may be an instruction to an AI or private detail ([security](security.md)). `--strict`
  turns those notes into failures.
- **`version`** prints the version, so a stale copy is easy to spot.
- **`upgrade`** finds the newest release tag with `git ls-remote`, shallow-clones it into a temporary
  folder, checks the tag is signed by a release key ([ADR-0011](../adr/0011-upgrades-run-only-signed-releases.md)),
  and runs that release's installer against this repo (`--dry-run` passes through). It refuses to
  run inside this repository. `DURABLESPEC_SOURCE` points it at an `https://` mirror
  ([ADR-0008](../adr/0008-upgrade-from-tagged-releases.md)).

Front matter is a small YAML subset parsed by hand, to stay within the standard library. It needs no AI,
so it runs where no agent is present: a git hook or CI.
