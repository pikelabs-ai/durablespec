---
purpose: "Known work on DurableSpec that isn't scheduled, and open questions."
concepts: [backlog, todo, open-questions]
---

# Backlog

- **Replay test.** Run past spec-touching and non-spec commits from a long-running repo through
  `durablespec-update`; record whether it would have written and where; compare with what happened. Put
  the results in the README as evidence.
- **Second model.** Run the replay with Codex or Gemini CLI reading the same skills from `.agents/skills/`.
- **Migrate the original repos** from the hand-copied index script and skill to the installed versions.
- **Reconcile skill,** for opposing decisions made on two branches. Wait until a real conflict calls for it.
- **A home for gotchas:** traps that aren't decisions or conventions ("this test is flaky because…").
  Decide whether they belong in `constitution/`, area documents, or a new place.
- **Retire the old OneSpec repository:** push the pointer README and archive it.
- **Fixes from the 0.3 blind re-create of a large monorepo** (2026-10-12):
  - The README's decision-record example has no front matter, but every document needs it and `check`
    fails without it. Show front matter in the example.
  - Length: a 19-module monorepo came out at about 12,000 words, against "about fifteen minutes". Say
    what to cut, or accept a longer read for large repos with the index as the entry point.
  - Say whether overlapping `owns:` (a parent folder in one area, subfolders in another) is allowed, and
    which wins.
  - Give stale existing documents their own heading in `backlog.md`, apart from open questions. Cover a
    README that exists but is wrong, not only a missing one.
  - When production runs older code than the branch, tell the create skill to find the deployed commit.
  - Diagram layout: put sources on the left and sinks on the right; about 12 boxes is the limit.
  - Say that dot-folders and `docs/` don't count as top-level code folders.
  - Large repos need parallel surveying; say how to make sure counts are measured, not copied from old
    documents.

## Open questions

- Should `check` read the repo's `.gitignore` before noting unowned top-level folders?
