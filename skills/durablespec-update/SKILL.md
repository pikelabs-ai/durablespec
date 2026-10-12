---
name: durablespec-update
description: Keep doc/spec accurate after a change. Use before a commit, when wrapping up a session with uncommitted work, or when asked to "update the spec" or "did the spec drift?". Reads the diff and the reasons behind it, updates only the spec documents that warrant it (usually none), rebuilds the index, and reports.
license: Apache-2.0
metadata:
  author: Pike Labs, Inc.
  version: "0.1.0"
---

# durablespec-update

Keep `doc/spec/` true to what changed. The policy is this repo's `doc/spec/README.md`; read it first if
unsure. The spec is an abstraction over the code, not a mirror. **Bias hard toward not writing.** Most
changes don't move the picture, and needless edits are the failure this skill exists to prevent.

## Procedure

1. **Gather the change.** `git diff --staged --stat` and `git diff --staged`; if nothing is staged, use
   `git diff --stat` and `git diff`. Add what the session knows that the diff doesn't: why the change was
   made, what was decided, what was rejected.

2. **Apply the one rule to the change as a whole.** Would a reader tomorrow form a materially different
   picture of the system without a spec change? The default is no. Bug fixes, refactors, tests, renames
   and dependency bumps almost never qualify. New components, changed boundaries, new or reversed
   load-bearing decisions and new conventions usually do.

3. **If yes, find the one document that owns each part of it** (table in `doc/spec/README.md`):
   - overall shape → `design/architecture.md`
   - inside one area → that area's document, found by matching changed paths against `owns:` lines
   - a load-bearing choice → a new `adr/NNNN-short-title.md`, next free number. Never edit a decided
     record; write a new one that replaces it and names the one it replaces.
   - a convention → `constitution/`; a term → `purpose/glossary.md`
   - build progress → `design/status.md`; deferred work → `backlog.md`

4. **Check coverage.** For each changed source path, find the design document whose `owns:` covers it.
   A path no document owns means an existing area grew (extend its `owns:`) or an area is missing (write
   a short new design document with `owns:`). An `owns:` entry pointing at a deleted path is drift: fix it.

5. **Edit minimally.** Touch only what warrants it, at the level of what and why, never restating the
   diff. Keep the existing voice. Then run `python3 doc/spec/durablespec.py index` and
   `python3 doc/spec/durablespec.py check`, and fix anything check reports.

6. **Report.** List each file changed with one line on why, or say plainly that no spec change was
   warranted and why. "Nothing needs to change" is a common, correct result. Suggest `[skip-spec]` in the
   commit message when nothing changed, so the decision is recorded.
