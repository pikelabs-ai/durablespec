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
  another; or if `INDEX.md` is stale. It also prints notes, without failing, for design documents that
  own nothing and top-level folders no `owns:` covers.
- **`version`** prints the version, so a stale copy is easy to spot.

Front matter is a small YAML subset parsed by hand, to stay within the standard library. It needs no AI,
so it runs where no agent is present: a git hook or CI.
