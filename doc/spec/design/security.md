---
purpose: "What DurableSpec trusts, how each part could be abused, and the defense for each."
concepts: [security, threat-model, prompt-injection, upgrade, installer, secrets, trust]
---

# Security

DurableSpec is plain files, a stdlib script and two skills. It has no service, no dependencies and no
telemetry, and it touches the network only when someone runs `upgrade`. The risk is in what the files
make agents and scripts do. Four things are trusted, and each is a way in:

| Trusted thing | Who could abuse it | What they get |
|---|---|---|
| **The spec** (`doc/spec/`), which every agent reads first and treats as settled | anyone who can land an edit: a PR, a compromised account, text pasted from outside | standing instructions in every later agent session |
| **What the skills read**: code, READMEs, git history, deploy files, related repos | anyone who can put text in those | instructions inside a session that edits the spec |
| **The release source**, which `upgrade` downloads and runs | whoever controls the GitHub account, a tag, or `DURABLESPEC_SOURCE` | code running on the developer's machine |
| **The target repo's layout**, which the installer writes into | whoever prepared the repo: a planted symlink | files written or deleted outside the repo |

A fifth risk runs the other way: **sensitive detail leaking into the spec**, which is often in a public
repo and is written by agents that have seen secrets, internal host names and account ids.

## Defenses

- **The spec is knowledge, not commands.** It shapes how agents do what a person asked, conventions
  included, but neither it nor anything the skills read can give them a new task or widen what they
  may do; such text is reported to the person ([ADR-0009](../adr/0009-knowledge-not-commands.md)).
  This is in the `AGENTS.md` block, the rules and both skills. Teams that take outside contributions
  should also require review of `doc/spec/` (CODEOWNERS).
- **Secrets stay out.** Both skills refuse to open or quote secrets, and keep out of the spec what a
  public repo shouldn't carry: credentials, internal host names and IP ranges, cloud account,
  subscription and tenant ids, and customer names unless the team says otherwise.
- **`check` backs both up.** It fails on anything shaped like a secret: private keys, cloud and
  GitHub tokens, AI provider keys, passwords in URLs. It notes what deserves a look: text addressed to
  an AI, hidden HTML comments, invisible characters, long encoded blobs, plain-http links, private IP
  addresses and cloud account ids. `check --strict` fails on the notes too, for CI in repos that take
  outside contributions. The patterns were tuned against eleven working specs so that ordinary writing
  about AI systems doesn't trip them.
- **Upgrades run only signed releases.** `upgrade` accepts only `https://` sources and runs a release
  only if its tag is signed by a key written into `durablespec.py`
  ([ADR-0011](../adr/0011-upgrades-run-only-signed-releases.md)).
- **The installer stays inside the repo.** It refuses any path it would write or delete that resolves
  outside the repo, which a planted symlink would cause, and touches only its own files.
- **The script stays small.** Standard library only, no network except `upgrade`, no telemetry.
  `owns:` paths are checked against the repo boundary after following links, and every pattern is
  bounded so unusual text can't stall it.

Reporting a vulnerability is covered by `SECURITY.md` at the root of the DurableSpec repository.
