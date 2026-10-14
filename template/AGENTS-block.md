<!-- durablespec:start -->
## Spec of record (DurableSpec)

`doc/spec/` describes what this system is for, how it is shaped, and why. Before deciding how anything
should work, read `doc/spec/INDEX.md`, open the documents it points to, and answer from them; don't
re-derive what the spec settles. **Before every commit, run the `durablespec-update` skill** (or follow
`doc/spec/README.md`), even when nobody asks: put it on your task list. Touch the spec only if a reader
tomorrow would form a materially different picture without the change. Usually nothing needs to change,
but a new or removed app, service, database, queue, user or outside system always does.
<!-- durablespec:end -->
