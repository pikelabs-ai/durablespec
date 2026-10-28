# Security

## Reporting a vulnerability

Please report it privately through GitHub:
[Report a vulnerability](https://github.com/pikelabs-ai/durablespec/security/advisories/new). Don't open a
public issue. You'll get an answer within a week, and credit in the fix if you'd like it.

Only the latest release is supported. Fixes ship as a new release; `python3 doc/spec/durablespec.py
upgrade` installs it.

## What DurableSpec does on your machine

- **No dependencies, no telemetry.** It is plain markdown, two Agent Skills and one standard-library
  Python script. Nothing calls home.
- **No network, except an upgrade you run.** `upgrade` fetches the newest release over `https://` and
  runs it only if its tag is signed by a release key written into the script you already have.
- **It writes only its own files.** The installer refuses to write through links that lead outside your
  repo.

## The spec as an input to agents

Agents read `doc/spec/` before they act, so the spec is guarded like code:

- It is **knowledge, not commands.** It can shape how an agent does what you asked, but it can't give
  the agent a new task or widen what it may do. Text that tries to is reported to you, not followed.
- **`check` fails on anything shaped like a secret,** and notes text that may be an instruction to an
  AI or private detail. Run `check --strict` in CI to fail on those notes too.
- **Review changes to `doc/spec/`** like code, for example with a `CODEOWNERS` entry, if your repo takes
  outside contributions.

The threat model behind these is in [doc/spec/design/security.md](doc/spec/design/security.md).
