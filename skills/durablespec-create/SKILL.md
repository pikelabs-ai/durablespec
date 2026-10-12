---
name: durablespec-create
description: Create doc/spec, the spec of record, for a repo that doesn't have one. Use when asked to "create the spec", "set up DurableSpec", or when doc/spec is missing or empty. Reads the code and history, drafts purpose, architecture, areas and the decisions it can see evidence for, then asks the people what the code can't tell it.
license: Apache-2.0
metadata:
  author: Pike Labs, Inc.
  version: "0.1.0"
---

# durablespec-create

Draft the first `doc/spec/` with the people who own the system. It's a conversation, not a form: the
code shows what was built, only people know why. Read `doc/spec/README.md` first; it holds the rules.
If `doc/spec/` already has content, stop and use `durablespec-update` instead.

## What to aim for

Short enough that a new engineer or tomorrow's agent reads it in minutes. Typically:

- `purpose/overview.md`: what the system is, who it is for, what problem it solves
- `purpose/glossary.md`: only terms a newcomer would trip on
- `constitution/conventions.md`: tech stack and the standing rules the code actually follows
- `design/architecture.md`: the parts, how they connect, where it runs
- `design/<area>.md`: one per major part, each with `owns:` naming its folders (a monorepo gets one
  spec, with each part as an area)
- `design/status.md`: what is built, what is in progress
- `adr/NNNN-*.md`: one per load-bearing decision you can see evidence for
- `backlog.md`: known work owed, if any surfaced

## Procedure

1. **Survey.** Read the README, build files, top-level layout, entry points, configuration, deployment
   files and recent `git log`. If the repo already has design documents elsewhere, read them: the spec
   should absorb what is still true so it stays current once code changes.

2. **Draft.** Write the documents above, each with front matter (`purpose:` quoted, `concepts:`, and
   `owns:` for design documents). Describe what and why, not a tour of the code. Write decision records
   only where the code or history shows a deliberate choice; mark them "recorded after the fact" and
   state the evidence. Don't invent reasons.

3. **Ask.** List the questions the code can't answer, and ask the people: who it's for, why the odd parts
   are odd, which decisions were deliberate, what is planned. Bring a product owner to the purpose
   section if possible. Fold the answers in.

4. **Finish.** Run `python3 doc/spec/durablespec.py index` and `python3 doc/spec/durablespec.py check`
   until check is clean. Report what was written and the questions still open.
