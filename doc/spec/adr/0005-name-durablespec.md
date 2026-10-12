---
purpose: "Why OneSpec was renamed DurableSpec."
concepts: [name, rename, onespec, openspec, marketing]
---

# ADR-0005: Rename OneSpec to DurableSpec

**Status:** accepted, 2026-10-11.

**Context.** The project was published as OneSpec. An early reader confused it with OpenSpec, which
differs by one letter and has far more traffic. A name that is mistaken for the market leader loses
the marketing battle before it starts.

**Decision.** Rename to DurableSpec. The name has to refer to specification or to durable memory, and
this one says both: "spec" is the word buyers search for, and "durable" is the difference, since the
spec outlives the change, the session and the engineer. It was free on PyPI, npm and GitHub. Rejected:
SpecMem and Cairn (used by several agent-memory projects), Throughline (no reference to specs or
memory), and LivingSpec, AnchorSpec, SpecLedger and MemSpec (taken).

**Consequences.** The repository, skills (`durablespec-create`, `durablespec-update`), script and web page
were renamed. The old OneSpec repository is to point here and be archived.
