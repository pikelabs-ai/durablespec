---
purpose: "Known work on DurableSpec that isn't scheduled, and open questions."
concepts: [backlog, todo, open-questions]
---

# Backlog

- **Security settings on GitHub** (done by hand, not in code): private vulnerability reporting on the
  repository, branch protection on `main`, and 2FA required for the `pikelabs-ai` organization. PyPI
  trusted publishing and build attestations when the package comes.
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
  - Say whether overlapping `owns:` (a parent folder in one area, subfolders in another) is allowed, and
    which wins.
  - Give stale existing documents their own heading in `backlog.md`, apart from open questions. Cover a
    README that exists but is wrong, not only a missing one.
  - When production runs older code than the branch, tell the create skill to find the deployed commit.
  - Diagram layout: put sources on the left and sinks on the right; about 12 boxes is the limit.
  - Say that dot-folders and `docs/` don't count as top-level code folders.
  - Large repos need parallel surveying; say how to make sure counts are measured, not copied from old
    documents.

- **The update skill often doesn't run** unless someone asks (reported by an engineer on a team using
  it, 2026-10-14). 0.3.1 made the `AGENTS.md` block firmer and added an always-asked architecture
  question to the skill. Not done, and not urgent: people should ask for the update as part of their
  work. Options if it stays a problem:
  - **A mechanical nudge in `check`:** when deployment files (compose, Terraform, Dockerfiles, CI, build
    files) change and the spec doesn't, print a reminder.
  - **An optional commit hook that forces the decision.** A git `commit-msg` hook, installed through a
    committed hooks folder (`core.hooksPath`), rejects a commit that changes code but neither changes
    `doc/spec/` nor says `[skip-spec]`, with a message telling the agent to run `durablespec-update`.
    It works for every agent and for people, needs no AI, and turns "remember to run it" into an
    explicit yes or no on every commit. Opt-in in the installer, since some teams will find it strict.
- **The picture of a system that spans several repos** (an app, its infrastructure, a shared library).
  Deliberately not solved: each repo draws its own part and shows other repos as single boxes, and
  people keep related specs in step. An idea if it is needed later: each repo declares what it provides
  to and uses from other repos, and a script generates the whole-system diagram and reports mismatches.
- **One-line install, when outside teams start using it.** Install is two commands today, and adoption
  is held back by the message, not by install friction, so this waits.
  - **First, a Python package** (the step [ADR-0002](adr/0002-stdlib-python-install-by-copy.md) put off):
    publish to PyPI with a `durablespec` command (`install`, `upgrade`, `version`), so
    `uvx durablespec install .` works with nothing installed beforehand, and `pipx install durablespec`
    gives a lasting command. Covers Mac, Linux and Windows.
  - **Then a Homebrew tap,** `pikelabs-ai/homebrew-tap`, as a thin wrapper:
    `brew install pikelabs-ai/tap/durablespec`. Mac and Linux only; each release updates the formula's
    version and checksum, ideally automatically. Homebrew's main catalog only once the project is well
    known.

## Open questions

None right now.
