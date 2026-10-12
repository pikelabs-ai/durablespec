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
