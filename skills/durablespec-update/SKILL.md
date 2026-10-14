---
name: durablespec-update
description: Keep doc/spec accurate after a change. Use before a commit, when wrapping up a session with uncommitted work, or when asked to "update the spec", "did the spec drift?" or "add the C4 diagrams to the spec". Reads the diff and the reasons behind it, updates only the spec documents that warrant it (usually none), rebuilds the index, and reports.
license: Apache-2.0
metadata:
  author: Pike Labs, Inc.
  version: "0.3.2"
---

# durablespec-update

Keep `doc/spec/` true to what changed. The policy is this repo's `doc/spec/README.md`; read it first if
unsure. The spec is an abstraction over the code, not a mirror. **Bias hard toward not writing.** Most
changes don't move the picture, and needless edits are the failure this skill exists to prevent.

When asked only to add diagrams to an existing spec, skip the diff: read `purpose/overview.md`,
`design/architecture.md` and the area documents, draw what is missing following the diagram guidance in
step 5, then run the index and check.

## Procedure

1. **Gather the change.** `git diff --staged --stat` and `git diff --staged`; if nothing is staged, use
   `git diff --stat` and `git diff`. Add what the session knows that the diff doesn't: why the change was
   made, what was decided, what was rejected.

2. **Apply the one rule to the change as a whole.** Would a reader tomorrow form a materially different
   picture of the system without a spec change? The default is no. Bug fixes, refactors, tests, renames
   and dependency bumps almost never qualify. New components, changed boundaries, new or reversed
   load-bearing decisions and new conventions usually do.

   Whatever the answer, always ask one more question, because the files a change touches rarely point
   at the architecture: **did it add, remove or reconnect a deployable part (an app, service, database,
   queue, container or job), a kind of user, or an outside system?** Look at compose, Terraform,
   Kubernetes, Dockerfiles, CI and build files in the diff as well as code. If so, the spec changes:
   `design/architecture.md` and its Container diagram, and for users and outside systems the overview's
   System Context diagram, whichever area owns the files.

3. **If yes, find the one document that owns each part of it** (table in `doc/spec/README.md`):
   - overall shape → `design/architecture.md`
   - inside one area → that area's document, found by matching changed paths against `owns:` lines
   - a load-bearing choice → a new `adr/NNNN-short-title.md`, next free number, in the format in
     `doc/spec/README.md`. Never edit a decided record; write a new one that says what it replaces, and
     change only the old one's status line to "replaced by ADR-NNNN".
   - a convention → `constitution/`; a term → `purpose/glossary.md`
   - build progress → `design/status.md`; deferred work → `backlog.md`

4. **Check coverage.** For each changed source path, find the design document whose `owns:` covers it.
   A path no document owns means an existing area grew (extend its `owns:`) or an area is missing (write
   a short new design document with `owns:`). An `owns:` entry pointing at a deleted path is drift: fix it.

5. **Edit minimally.** Touch only what warrants it, at the level of what and why, never restating the
   diff. Keep the existing voice. Diagrams are part of the document they sit in:
   - If the change adds, removes or reconnects something a diagram shows (a person, an outside system,
     a container, a component), update that diagram in the same edit.
   - If a document you are editing now describes three or more parts or outside systems and has no
     diagram, add one, following the diagram convention in `doc/spec/README.md`. The overview gets the
     System Context diagram and `architecture.md` the Container diagram.
   - If the spec lacks a C4 diagram that makes sense for this repo (Context, Container, or Component for
     a complex area), add it when you are in that document. Parts in other repos are single outside
     boxes.
   - Never add a diagram for its own sake, or redraw one that is still true.

   If that README predates diagrams, the essentials are: C4 levels (System Context in the overview,
   Container in `architecture.md`, Component only where an area needs it, never code level), drawn as a
   Mermaid `flowchart`; each box gives `<b>name</b><br/>[type]<br/>what it does`, every arrow is labeled,
   and a subgraph marks the system boundary.

   Then run `python3 doc/spec/durablespec.py index` and
   `python3 doc/spec/durablespec.py check`, and fix anything check reports.

6. **Report.** If the change alters something another repo relies on (an API, a message, a setting, a
   deployed part; `RELATED.md` lists related repos), say so, so the person can update that repo's spec.
   List each file changed with one line on why, or say plainly that no spec change was
   warranted and why. "Nothing needs to change" is a common, correct result. Teams that want a record of
   that decision put `[skip-spec]` in the commit message; it's a convention, nothing enforces it.
