---
purpose: "The two Agent Skills: creating a spec, and keeping it accurate after a change."
concepts: [skills, create, update, judgment, agentskills]
owns:
  - skills/
---

# Skills

Two skills in the open [Agent Skills](https://agentskills.io) format. They hold the judgment a script
can't make, and defer to the repo's `doc/spec/README.md` for policy.

**`durablespec-create`** drafts the first spec with the people who own the system. It surveys the code,
existing docs and history (never opening secrets), drafts the purpose, architecture, areas with `owns:`
lines and decision records it has evidence for, then asks what the code can't tell it. Unanswered
questions go to `backlog.md`, not scattered through the documents. If `doc/spec/` already has content,
it hands over to `durablespec-update`.

**`durablespec-update`** runs before a commit. It reads the diff and what the session knows about why,
applies the one rule, and edits only the documents that own the change, usually none. It checks that
every changed path is owned by some design document, then runs the script.

Both are biased hard toward not writing. Needless edits are the failure the update skill exists to
prevent. A third skill, to reconcile opposing decisions made on two branches, waits until a real
conflict calls for it (see [backlog](../backlog.md)).
