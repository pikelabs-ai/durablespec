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
  - Say whether overlapping `owns:` (a parent folder in one area, subfolders in another) is allowed, and
    which wins.
  - Give stale existing documents their own heading in `backlog.md`, apart from open questions. Cover a
    README that exists but is wrong, not only a missing one.
  - When production runs older code than the branch, tell the create skill to find the deployed commit.
  - Diagram layout: put sources on the left and sinks on the right; about 12 boxes is the limit.
  - Say that dot-folders and `docs/` don't count as top-level code folders.
  - Large repos need parallel surveying; say how to make sure counts are measured, not copied from old
    documents.

- **The update skill misses architecture changes** (reported by an engineer on a team using it, 2026-10-14: it
  only updates the architecture when reminded). Three likely causes, three fixes:
  - **It often doesn't run.** `AGENTS.md` asks for it before committing, but agents commit without
    loading it; the reminder is what triggers it. Firmer wording in the `AGENTS.md` block, and see the
    commit hook below.
  - **Ownership routes around the architecture.** `architecture.md` owns no code, so a new container
    shows up as an edit to a compose or Terraform file owned by a deployment area, and only that area's
    document gets updated. Add a question the skill must always answer, whatever owns the files: did
    this add, remove or reconnect a deployable part, a user or an outside system? If so,
    `architecture.md` and its Container diagram change too (and the overview's Context diagram for
    users and outside systems).
  - **The bias toward no change** lets a new service inside a larger change through. The same
    question fixes this.
  - **A mechanical nudge in `check`:** when deployment files (compose, Terraform, Dockerfiles, CI, build
    files) change and the spec doesn't, print a reminder. Works even when the skill never ran.
- **An optional commit hook that forces the decision.** A git `commit-msg` hook, installed through a
  committed hooks folder (`core.hooksPath`), rejects a commit that changes code but neither changes
  `doc/spec/` nor says `[skip-spec]`, with a message telling the agent to run `durablespec-update`.
  It works for every agent and for people, needs no AI, and turns "remember to run it" into an
  explicit yes or no on every commit. Opt-in in the installer, since some teams will find it strict.

## Open questions

- Should `check` read the repo's `.gitignore` before noting unowned top-level folders?
