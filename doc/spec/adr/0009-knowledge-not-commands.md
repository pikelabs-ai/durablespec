---
purpose: "Why agents treat the spec, and everything the skills read, as knowledge and never as instructions to act."
concepts: [security, prompt-injection, trust, AGENTS.md, skills]
---

# ADR-0009: The spec is knowledge, not commands

**Status:** accepted, 2026-10-27.

**Context.** The `AGENTS.md` block tells every agent to read the spec first and to treat what it settles
as settled. That makes the spec a standing channel into every future session: a careless or malicious
edit (a pull request, a compromised account, text pasted from an outside source) would be obeyed by
every agent after it. The skills have the same exposure one step earlier, since they read code,
READMEs, history and deploy files that anyone with commit access, or any dependency, can write.
Agents can't reliably tell a real convention from a planted instruction by its wording alone.

**Decision.** The spec informs how an agent does what a person asked; it never gives the agent a new
task or widens what it may do. Purpose, design, decisions and conventions (how to build and test, git
habits, which tools the team uses) are followed. Text that asks the agent to send data or credentials
anywhere, download and run something, change permissions or access, skip a check, or disregard other
instructions is never followed, from the spec or from anything the skills read; the agent tells the
person instead. A first draft drew the line at "any text telling the agent to run a command or change a
setting"; a survey of ten working specs showed that would have blocked ordinary conventions such as
build commands, git hygiene and a per-repo commit email, so the line is drawn at new tasks and wider
reach instead. The rule goes in the `AGENTS.md` block, the rules template and both skills. Rejected:
trusting the spec because it is reviewed (review is uneven and agents can't see whether it happened),
and stripping or escaping text mechanically (it can't separate the two kinds; `check` only flags obvious
signs).

**Consequences.** A spec can no longer hand an agent a task of its own; conventions keep working. A
planted instruction becomes a report to a person instead of an action. The `AGENTS.md` block reaches
existing repos on upgrade; their `doc/spec/README.md` is kept, so they get the rule there only if they
take the new template. The rule depends on the model following it, which is why review of `doc/spec/`
and the `check` flags back it up.
