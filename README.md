# DurableSpec

**One shared spec for your team and every AI it works with.**

A free, open-source spec that gives every engineer and every AI session the same context, draws and
maintains your C4 architecture diagrams, and builds a lasting product specification, in plain Markdown
next to your code.

- **Shared context across people and AI sessions.** What one person's session works out, every later
  session knows, whoever runs it. Nobody re-explains the system.
- **Architecture diagrams that maintain themselves.** C4 Context and Container diagrams in Mermaid,
  drawn from your code and redrawn in the commit that changes them.
- **A product spec that lasts.** Purpose, customers, business rules and the decisions behind the
  design: the context that isn't in the code, in plain language product owners can read and write.
- **Drift gets caught.** Each document names the code it describes, so a stale document is flagged.
- **Free and simple.** Plain Markdown, two Agent Skills and one Python script. Works with Claude Code,
  Codex, Copilot, Cursor and Gemini CLI.

Try it on any repository (you need git and Python 3.8+), then ask your agent to "create the spec":

```
git clone https://github.com/pikelabs-ai/durablespec.git
python3 durablespec/install.py /path/to/your/repo
```

![Four people on four days, each adding to one shared spec, so Thursday starts with everything Monday to Wednesday worked out.](docs/durablespec-hero.jpg)

> **Status: beta.** The practice is in daily use across nine repositories; the packaging is new. Every
> release is [tagged](https://github.com/pikelabs-ai/durablespec/tags).
> More at [pikelabs.ai/durablespec](https://pikelabs.ai/durablespec).

## Why

Every AI session starts from zero. You spend the first part of it re-explaining the system, the
customer, and what was decided last week, and when the session ends, what you worked out together
goes with it. With several people each running their own sessions, the loss multiplies: nobody's
agent knows what anyone else's agent learned.

DurableSpec fixes that with a small folder of plain-Markdown documents, `doc/spec/`, kept next to the
code. It records what the system is for, how it is shaped, and why it was built that way. Every
session, human or AI, starts by reading it, and the work that matters gets written back before the
session ends. The knowledge carries forward from one session to the next, and from one person to
the next.

**Continuity beyond the session** is the main point.

- **Working alone,** a new session starts at full speed. The agent reads a few pages instead of
  re-deriving the system from the code, so it uses little of its context window getting oriented
  and has more left for the actual work. What you decide today is waiting for tomorrow's session.
- **Working as a team,** the spec carries everyone's relevant work. When a colleague's session
  settled a design question yesterday, your session knows the answer today, without anyone
  writing a hand-off note or remembering to mention it.

## Not just for engineers

Some of the most valuable content in a spec is business context: who the customers are, what
problem the system solves for them, what a term means in this business, which constraints come
from contracts or regulation. Engineers often don't have that knowledge. Product owners and
business people do.

DurableSpec is written in plain language so they can read it and write in it, especially the
`purpose/` section, which is where that context lives. This matters more every year: a growing
share of the people building software with coding agents are business people, not career
engineers. The spec is how their knowledge reaches every session, including the ones they never
see.

## How a session goes

This is the habit that makes it work. It is not obvious, so here it is step by step.

**1. Start with the problem, and have the agent read the spec first.** For example:

> Today we're going to extend billing so it can handle Acme's invoices in euros and pounds.
> Before we start, read `doc/spec`, and also the storefront repo's `doc/spec` to see how the
> storefront uses billing. Then let's brainstorm. I was thinking we could store each amount in its
> original currency and convert only when reporting. Will that work, and what else would it
> affect?

The problem can be deeply technical or purely about the business, such as growing a system to
meet a new customer's needs. Either way, the agent starts from the recorded purpose, design and
past decisions, not from guesses. It reads the index and the few documents that matter, not the
whole codebase.

**2. Brainstorm.** Talk it through. Let the agent push back, raise consequences you hadn't
considered, and suggest alternatives. This is where the real thinking happens, and it goes better
when the agent knows why the system is the way it is.

**3. Update the spec.** Once you've settled on an approach, ask the agent to record it: a new
decision record for the choice and why, and changes to the design documents it affects. Do this
*before* building, while the reasons are fresh.

**4. Build it.** Now the agent builds, with the agreed design written down in front of it.

**5. Check the spec before you commit.** Ask the agent to update the spec (the `durablespec-update` skill). Usually
nothing more needs to change. Sometimes building taught you something the spec should know.

The next session, yours or a teammate's, starts at step 1 with everything this one learned.

## Getting started

You need git and Python 3.8 or later; nothing else is installed. Clone this repo once, then run the
installer against any repository:

```
git clone https://github.com/pikelabs-ai/durablespec.git
python3 durablespec/install.py /path/to/your/repo
```

It adds two [Agent Skills](https://agentskills.io), `durablespec-create` and `durablespec-update`, in
`.agents/skills/` (read by Codex, Gemini CLI, GitHub Copilot and others) with links in `.claude/skills/`
for Claude Code. It also adds `doc/spec/durablespec.py` (the mechanical checks), the rules in
`doc/spec/README.md` if you have none, a marked section in `AGENTS.md`, and an `@AGENTS.md` line in
`CLAUDE.md`. It never touches anything else, and running it again upgrades in place. Add `--dry-run` to see what
it would do first.

`main` is the latest code; to install a specific release, add `--branch` and a [release tag](https://github.com/pikelabs-ai/durablespec/tags)
to the clone (for example `--branch v0.3.3`). Later, upgrade from inside your repo with `python3 doc/spec/durablespec.py upgrade`
([Upgrading](#upgrading-and-stopping)).

Commit what it adds. On Windows, Git may check out the `.claude/skills/` links as plain text files;
running the installer again on that machine replaces them with copies.

Then ask your agent to **create the spec**. It works like a session in the previous section: a
conversation, not a form.

- **Existing code, no spec.** The agent reads the code and drafts the overview, the architecture,
  and the decisions it can see evidence for. Then it asks you what the code can't tell it: who the
  system is for, why the odd parts are odd, which decisions were deliberate. You correct the draft
  together. Bring a product owner for the purpose section if you can.
- **New project.** Start with the problem and brainstorm as above. As the design firms up, the
  agent records the purpose, the architecture and each decision as it is made.
- **A design already written elsewhere.** Point the agent at it. It turns the design into the
  overview, architecture and decision records, so the design stays current once code lands
  instead of becoming a document nobody reopens.

## The shape

```
doc/spec/
  README.md          the rules for this repo (the one rule, what goes where)
  INDEX.md           generated map: one line per document, read this first
  RELATED.md         optional: specs in other repos this one depends on
  backlog.md         known work you owe but haven't scheduled (changes freely)
  purpose/           why the system exists: overview, customers, glossary
  constitution/      how we build here: conventions, tech stack, standing rules
  design/            what we're building: architecture, one doc per area, status
  adr/               why this over that: numbered decision records, never edited
```

Everything else in `doc/` stays free-form. The rules apply only inside `doc/spec/`.

Each document starts with a few lines saying what it is for. The index is built from them, so an
agent can find the right document without opening every one:

```markdown
---
purpose: "How invoices are created, priced and sent; currency handling."
concepts: [invoice, pricing, currency, tax]
owns: [src/billing/invoice/, src/billing/currency/]
---
# Invoicing
```

A few conventions carry most of the weight:

- **Each design document names the code it governs** (`owns:`), so a changed file can be traced to
  the document that describes it, and a document pointing at deleted code gets caught.
- **Build status lives in one place,** `design/status.md`. Status notes scattered through design
  documents are the first thing to go stale.
- **Diagrams follow the C4 model, drawn in Mermaid** (see [Architecture that stays true](#architecture-that-stays-true)).
- **Decision records are never edited.** To change a decision, write a new record that replaces
  the old one. When you cite a record from another repo, name the repo: `billing ADR-0004`, never
  a bare number.

## Architecture that stays true

The spec draws your system with the [C4 model](https://c4model.com): a System Context diagram in the
overview (who uses it, what it talks to), a Container diagram in the architecture (the running parts and
how they connect), and Component diagrams for areas complex enough to need one. They are Mermaid, so
GitHub shows them as pictures and they live as plain text beside the code:

```mermaid
flowchart LR
  clerk["<b>Billing clerk</b><br/>[Person]<br/>Issues and corrects invoices"]
  subgraph billing["Billing (this system)"]
    app["<b>Web app</b><br/>[Container: React]<br/>Invoice screens"]
    api["<b>API</b><br/>[Container: Java]<br/>Prices and sends invoices"]
    db[("<b>Database</b><br/>[Container: PostgreSQL]<br/>Amounts in original currency")]
  end
  bank["<b>Bank</b><br/>[External system]<br/>Daily exchange rates"]
  clerk -- "uses" --> app
  app -- "JSON over HTTPS" --> api
  api -- "reads and writes" --> db
  api -- "fetches rates" --> bank
```

The agent draws them when it creates the spec. On every change, it checks whether an app, service,
database, user or outside system was added, removed or reconnected, even when the change only touched a
compose or Terraform file, and if so redraws the picture in the same commit. This repo's own
[architecture](doc/spec/design/architecture.md) is a worked example.

## The one rule

> Touch the spec only if a reader tomorrow would form a materially different picture of the
> system without the change.

The default is no. Bug fixes, refactors, renames, new tests and dependency updates almost never
qualify. New components, new connections between parts, reversed decisions, new customers'
requirements and new conventions usually do. The rule is as much about when not to write as when
to, and it is what keeps the spec short enough to read at the start of every session.

## What it is not

DurableSpec does not tell an AI how to plan, think, or break down work. Some spec tools walk the model
through a fixed sequence (specify, plan, task, implement). That kind of scaffolding gets in the
way as models improve.

DurableSpec manages **what the team knows**, not **how the work gets done**. Better models make that
more valuable, not less: no model, however capable, can recover a decision that was never written
down. And the better models get at writing, the more a project needs a rule about when *not* to
write.

The test for every feature in this project: *would it still be useful if models were ten times
smarter?*

## Day to day

**Agents read before they decide.** The section the installer adds to `AGENTS.md` tells every agent
to check the spec before settling any design question, and to answer from it rather than re-derive
it. Agents still forget mid-session; when one starts guessing, point it back at the spec.

**Agents write before you commit.** Ask the agent to update the spec. The `durablespec-update` skill
reads the change and the conversation behind it, applies the one rule, and either edits the one or
two documents that should move or tells you nothing needs to change. "Nothing needs to change" is the
common, correct answer. Put `[skip-spec]` in the commit message to record that.

**The mechanical checks need no AI.** `doc/spec/durablespec.py` checks that every document has its
opening lines, `INDEX.md` is current, every `owns:` path still exists, and no two decision records
share a number. Run it locally, in a git hook, or in CI.

```
python3 doc/spec/durablespec.py index     # rebuild INDEX.md
python3 doc/spec/durablespec.py check     # exit 1 on any problem
```

## Teams and branches

Because the spec is plain files in the repo, it branches and merges with the code. When two branches
both changed it, merge as usual, then run `check`: it catches clashing decision-record numbers and a
stale index. Where the two branches made *opposing* decisions, don't pick a winner in the merge; put
the conflict in front of the people who made them. A skill to help with this is planned.

## Large repos

A monorepo gets one spec, at the root, like any other repo. Each part is an area in `design/`,
and its `owns:` line names the part's folders, so a change anywhere still traces to the document
that describes it. Decision records share one sequence. Monorepos differ too much for a fixed
recipe: one holding several complex, high-throughput modules is a different thing from one that is
a plain REST application split into folders. Start with one spec for both; if a part later earns
its own, record that as a decision.

## Alongside other spec tools

Per-change spec tools (GitHub Spec Kit, OpenSpec, Kiro, or a team's own story specs) plan and record
individual changes. DurableSpec holds the standing picture those changes add up to. They don't
overlap; keep both. The spec always lives at `doc/spec/`, even in a repo that already has a `docs/`
folder, so every tool and agent finds it in the same place.

## Works with any agent

The rules are written for any reader, not for one product. The skills follow the open
[Agent Skills](https://agentskills.io) format, and the standing instruction lives in `AGENTS.md`,
which most coding agents read; Claude Code reads it through the `@AGENTS.md` line in `CLAUDE.md`.
Nothing is written twice.

## Upgrading, and stopping

From the repo you want to upgrade (repos on 0.3.2 or later; for older ones, run the installer once from a
fresh clone):

```
python3 doc/spec/durablespec.py upgrade            # add --dry-run to see what it would change
```

It finds the newest release with git, fetches it, and runs its installer against your repo, printing
anything new that it can't apply by itself. `python3 doc/spec/durablespec.py version` shows which
version a repo has. Running the installer from a fresh clone of this repo does the same thing.

To stop using DurableSpec, delete `doc/spec/`, the two skills, and the marked section of
`AGENTS.md`. Nothing else depends on it.

## Status

Beta. The practice has been in daily use since spring 2026 across nine repositories, from a
coding-agent harness to a production data service, with specs written before the code, alongside
it, and after it. The tooling around it is new.

More at [pikelabs.ai/durablespec](https://pikelabs.ai/durablespec).

## License

Apache License 2.0. Copyright 2026 Pike Labs, Inc.
