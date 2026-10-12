---
purpose: "What doc/spec is, the one rule about when to write, and where each kind of knowledge goes."
concepts: [spec, rules, navigation]
---

# doc/spec: the spec of record

This folder is **an abstraction over the code, not a mirror of it.** It records what the system is for,
how it is shaped, and why it was built this way. The code stays the authority on *how*. Every person and
every AI session reads it first, so it must stay short enough to read.

Start with [INDEX.md](INDEX.md): one line per document, generated from each document's front matter.

## The one rule

**Touch the spec only if a reader tomorrow would form a materially different picture of the system
without the change.** The default answer is no. Bug fixes, refactors, tests, renames and dependency bumps
almost never qualify. New components, changed boundaries, reversed or new load-bearing decisions, new
conventions and a new customer's requirements usually do.

## Where things go

| Folder | Answers | Holds |
|---|---|---|
| `purpose/` | Why does this exist? | overview, customers, glossary |
| `constitution/` | How do we build here? | conventions, tech stack, standing rules |
| `design/` | What are we building? | `architecture.md`, one document per area, `status.md` |
| `adr/` | Why this over that? | numbered decision records, never edited |

Plus `backlog.md`: known work owed but not scheduled, and open questions nobody has answered yet. Add
items as they surface, remove them when done. Open questions live here, not scattered through the
other documents.

When a change does qualify, move the **one** document that owns it:

- a change to the overall shape → `design/architecture.md`
- a change inside one area → that area's document in `design/`, found through its `owns:` line
- a load-bearing choice (why X over Y) → a **new** record in `adr/`
- a new convention → `constitution/`
- a new term → `purpose/glossary.md`
- build progress → `design/status.md`, and nowhere else

## Conventions

- **Front matter.** Every document opens with:
  ```
  ---
  purpose: "One line: what this document is for. Don't repeat the title."
  concepts: [a, few, search, words]
  owns:                      # design documents only
    - src/billing/
  ---
  ```
  The index is built from these lines. Quote the purpose.
- **`owns:` names the main code an area governs:** folders where the code is grouped by area, file
  paths or globs (`src/routes/readings*.js`) where it isn't. Skip shared plumbing such as layouts and
  styles. `architecture.md` and `status.md` usually own nothing. A design for work not built yet owns
  nothing until the code exists.
- **Decision records** are named `adr/NNNN-short-title.md`, four digits from `0001`, and look like this:
  ```
  # ADR-0007: Store amounts in their original currency
  **Status:** accepted, 2026-10-12.   (or: replaced by ADR-0012; or: recorded after the fact, from <evidence>)
  **Context.** What forced a choice.
  **Decision.** What was chosen, and what was rejected.
  **Consequences.** What follows, good and bad.
  ```
  **Never edit a decided record.** To change a decision, write a new one that says
  `**Replaces:** ADR-0007`, and change only the old one's status line to `replaced by ADR-0012`. Cite
  records from another repo with the repo's name: `billing ADR-0004`.
- **`design/status.md`** opens with "As of <date>" and says what is built, in progress and next.
  Describing behavior belongs in the area documents ("off by default", "retries three times");
  whether something is built, deployed or waiting belongs in `status.md`.
- **The spec describes the code on its own branch.** Where production runs something older or
  different, say so in `status.md`.
- **Short means short.** Roughly: overview one page, architecture up to three, each area one or two,
  each decision record half a page. The whole spec should read in about fifteen minutes; link to
  longer documents instead of copying them.
- **One spec per repo,** monorepos included: each part is an area in `design/` with its own `owns:`.
- **Mechanical checks:** `python3 doc/spec/durablespec.py check`. Rebuild the index after changing any
  front matter: `python3 doc/spec/durablespec.py index`.
