---
purpose: "Why upgrade refuses any release whose tag isn't signed by a key shipped inside durablespec.py."
concepts: [security, upgrade, signing, ssh, tags, releases, supply-chain]
---

# ADR-0011: Upgrades run only signed releases

**Status:** accepted, 2026-10-28. Builds on [ADR-0008](0008-upgrade-from-tagged-releases.md).

**Context.** `upgrade` downloads the newest release and runs its installer, which writes into the
repo and runs with the developer's permissions. Until now it trusted whatever the source served: anyone
who could push a tag to the GitHub repository, take over the account, or point `DURABLESPEC_SOURCE`
somewhere else could run code on every machine that upgraded. Tags can also be moved after release.

**Decision.** Release tags are signed with an SSH key, and the public half of each release key is
written into `durablespec.py` itself (`RELEASE_KEYS`). `upgrade` fetches the tag, checks with
`git verify-tag` that one of those keys signed it and that the fetched files are the signed commit, and
runs nothing otherwise. Sources must be `https://`; a company mirror keeps the signed tags, so it
verifies the same way. A new or replacement key ships in a release signed by a key already listed.
Rejected: trusting GitHub's "Verified" badge (it is GitHub's word, fetched from the same place as the
code); GPG (more setup for the same guarantee); a checksum list published alongside releases (it would
sit next to the code it vouches for); a flag to skip the check (an attacker's instructions would just
include it).

**Consequences.** Taking over the repository or a tag is no longer enough to run code through
`upgrade`; an attacker also needs the signing key, which lives on the maintainer's machine behind a
passphrase. Protection starts with the first upgrade *from* a version that has the check (0.5.0):
repos on 0.4.0 or older run the old upgrade once. Verifying needs `ssh-keygen`, which ships with git
on Windows and with macOS and Linux. Losing the key without a successor in a release means users
reinstall by hand once.
