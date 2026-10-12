<!-- durablespec:start -->
## Spec of record (DurableSpec)

`doc/spec/` describes what this system is for, how it is shaped, and why. Before deciding how anything
should work, read `doc/spec/INDEX.md`, open the documents it points to, and answer from them; don't
re-derive what the spec settles. Before committing, use the `durablespec-update` skill (or follow
`doc/spec/README.md`): touch the spec only if a reader tomorrow would form a materially different picture
without the change. Usually nothing needs to change.
<!-- durablespec:end -->

## Working on DurableSpec itself

This repo ships DurableSpec and uses it. `doc/spec/README.md` and `doc/spec/durablespec.py` are links into
`template/`, and the skills are linked from `skills/`, so a change to the template changes this repo's own
rules too. Don't run `install.py` on this repo.
