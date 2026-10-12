#!/usr/bin/env python3
"""Install or upgrade DurableSpec in a repository. Python 3.8+, stdlib only.

    python3 install.py /path/to/repo [--dry-run]

Safe to run again: it upgrades its own files and never touches anything else.

  .agents/skills/durablespec-create/, durablespec-update/   the skills (read by Codex, Gemini CLI, Copilot ...)
  .claude/skills/durablespec-*                              links to the same skills, for Claude Code
  doc/spec/durablespec.py                                   index and check (always replaced: it is versioned)
  doc/spec/README.md                                        the rules, only if the repo has none
  AGENTS.md                                                 a marked block, added or replaced; the rest untouched
  CLAUDE.md                                                 an "@AGENTS.md" line, if not already there
"""
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = ["durablespec-create", "durablespec-update"]
START, END = "<!-- durablespec:start -->", "<!-- durablespec:end -->"


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in argv
    if len(args) != 1 or not os.path.isdir(args[0]):
        print(__doc__)
        return 2
    repo = os.path.abspath(args[0])
    actions = []

    def do(message, fn=None):
        actions.append(message)
        if fn and not dry:
            fn()

    for skill in SKILLS:
        src = os.path.join(HERE, "skills", skill)
        dst = os.path.join(repo, ".agents", "skills", skill)

        def copy_skill(src=src, dst=dst):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        do(("upgrade " if os.path.exists(dst) else "add ") + os.path.relpath(dst, repo), copy_skill)

        link = os.path.join(repo, ".claude", "skills", skill)
        target = os.path.join("..", "..", ".agents", "skills", skill)
        if os.path.islink(link) and os.readlink(link) == target:
            continue

        def make_link(link=link, target=target, dst=dst):
            os.makedirs(os.path.dirname(link), exist_ok=True)
            if os.path.islink(link) or os.path.isfile(link):
                os.remove(link)
            elif os.path.isdir(link):
                shutil.rmtree(link)
            try:
                os.symlink(target, link)
            except OSError:  # e.g. Windows without symlink rights: fall back to a copy
                shutil.copytree(dst, link)
        kind = "replace copy at " if os.path.isdir(link) and not os.path.islink(link) else "link "
        do(kind + os.path.relpath(link, repo) + " -> " + target, make_link)

    spec = os.path.join(repo, "doc", "spec")
    tool = os.path.join(spec, "durablespec.py")
    do(("upgrade " if os.path.exists(tool) else "add ") + "doc/spec/durablespec.py",
       lambda: (os.makedirs(spec, exist_ok=True),
                shutil.copy2(os.path.join(HERE, "template", "durablespec.py"), tool)))
    readme = os.path.join(spec, "README.md")
    if os.path.exists(readme):
        actions.append("keep doc/spec/README.md (already present)")
    else:
        do("add doc/spec/README.md (the rules)",
           lambda: shutil.copy2(os.path.join(HERE, "template", "README.md"), readme))

    with open(os.path.join(HERE, "template", "AGENTS-block.md"), encoding="utf-8") as fh:
        block = fh.read().strip()
    agents = os.path.join(repo, "AGENTS.md")
    text = open(agents, encoding="utf-8").read() if os.path.exists(agents) else ""
    if START in text and END in text:
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
        verb = "keep" if new == text else "update"
    else:
        new = (text.rstrip() + "\n\n" if text.strip() else "") + block + "\n"
        verb = "add to" if text else "create"
    if new != text:
        do(verb + " AGENTS.md (DurableSpec block)", lambda: open(agents, "w", encoding="utf-8").write(new))
    else:
        actions.append("keep AGENTS.md (block current)")

    claude = os.path.join(repo, "CLAUDE.md")
    ctext = open(claude, encoding="utf-8").read() if os.path.exists(claude) else ""
    if "@AGENTS.md" in ctext:
        actions.append("keep CLAUDE.md (already imports AGENTS.md)")
    else:
        newc = "@AGENTS.md\n" + ("\n" + ctext if ctext else "")
        do(("add @AGENTS.md to the top of " if ctext else "create ") + "CLAUDE.md",
           lambda: open(claude, "w", encoding="utf-8").write(newc))

    print(("Would do" if dry else "Done") + " in " + repo + ":")
    for a in actions:
        print("  " + a)
    if os.path.isdir(os.path.join(repo, "docs")):
        print("Note: this repo also has docs/. DurableSpec always uses doc/spec/ so every agent finds it in "
              "the same place; docs/ is left as it is.")
    if not dry:
        print("Commit: AGENTS.md, CLAUDE.md, .agents/skills/, .claude/skills/ and doc/spec/.")
        print("Next: ask your agent to create the spec (durablespec-create), or, if doc/spec already has "
              "documents, run: python3 doc/spec/durablespec.py index && python3 doc/spec/durablespec.py check")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
