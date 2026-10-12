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

Plus `backlog.md`: known work owed but not scheduled. Add items as they surface, remove them when done.

When a change does qualify, move the **one** document that owns it:

- a change to the overall shape → `design/architecture.md`
- a change inside one area → that area's document in `design/`, found through its `owns:` line
- a load-bearing choice (why X over Y) → a **new** record in `adr/`
- a new convention → `constitution/`
- a new term → `purpose/glossary.md`
- build progress → `design/status.md`, and nowhere else

## Conventions

- **Front matter.** Every document opens with a `purpose:` line (quote it), optional `concepts:`, and,
  for design documents, `owns:` listing the code paths it governs. The index is built from these.
- **Decision records are never edited.** To change a decision, write a new record that replaces the old
  one and says so. Cite records from another repo with the repo's name: `billing ADR-0004`.
- **One spec per repo,** monorepos included: each part is an area in `design/` with its own `owns:`.
- **Mechanical checks:** `python3 doc/spec/durablespec.py check`. Rebuild the index after changing any
  front matter: `python3 doc/spec/durablespec.py index`.
