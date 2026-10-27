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

- **The spec is knowledge, not commands.** Agents use it to understand the system and never follow
  instructions found in it, or in anything the skills read; they report such text to the person
  instead. This goes in the `AGENTS.md` block, the rules and both skills. `check` flags the obvious
  signs: text addressed to an AI, hidden HTML comments, links to unexpected hosts, long encoded blobs.
  Teams that take outside contributions should require review of `doc/spec/` (CODEOWNERS).
- **Secrets stay out.** Both skills refuse to open or quote secrets, and keep out of the spec what a
  public repo shouldn't carry: credentials, internal host names and IP ranges, cloud account,
  subscription and tenant ids, and customer names unless the team says otherwise. `check` flags common
  key and token formats and private IP ranges.
- **Upgrades run only signed releases.** `upgrade` accepts only `https://` sources, verifies the release
  tag's signature against a key shipped with the current version before running anything, shows the
  version and source, and keeps `--dry-run`.
- **The installer stays inside the repo.** It refuses any path it would write or delete that resolves
  outside the repo, which a planted symlink would cause, and touches only its own files.
- **The script stays small.** No network except `upgrade`; `owns:` paths and links are checked against
  the repo boundary after resolving symlinks; regexes are simple enough to run in linear time.
