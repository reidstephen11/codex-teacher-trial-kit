# Codex setup — the config this kit assumes

**Maintained centrally by Steve Reid**, like `troubleshooting.md`. Teachers: don't edit
this file, your changes will be overwritten when an updated copy goes round.

Everything else in this folder tells the agent how to behave. This file is about how Codex
itself is set up, which is a different thing — and the gap between the two is the point.
Some of what `AGENTS.md` asks for is not enforced by any setting. Four things to establish
before the rest of the kit means anything.

**Agent: work through these at the end of setup and report what you found.** If item 2 is
wrong, stop there — do not carry on and hope.

---

## 1. Know what `Auto` actually protects

**The trial runs in `Auto`.** What that means, plainly:

- **Outside this folder, nothing happens without the teacher's say-so.** Auto stops and
  asks. That boundary is real, and it is the protection worth having.
- **Inside this folder, the agent can create, edit and overwrite files without asking.**

`AGENTS.md` rule 2 — propose before you move, rename, delete or rewrite an existing file —
is therefore an **instruction, not a lock**. Auto will not stop an agent that ignores it.
Follow the rule anyway; it is the difference between a teacher trusting this and not. But
do not tell a teacher that the setting is what keeps their work safe, because it is not.

**Agent: show them this at setup, don't describe it.** They should watch it happen once,
deliberately, in the first ten minutes rather than discovering it on a file that mattered.

1. Add a blank line to the end of `My Subject/README.md`. It goes through without a prompt.
   Say so, and undo it.
2. Then try to touch something outside the folder — reading the parent directory is enough.
   Codex will stop and ask. Say so, and decline it.

Then say, in two lines: inside this folder you can change things without asking, and you
are instructed to propose first; outside it, they get asked every time.

**Three things follow from that, and they matter more than the setting does.**

- **The recovery path is OneDrive version history**, not the approval prompt. If the agent
  overwrites something it shouldn't have: right-click the file, Version History, restore.
  It is in `Context/troubleshooting.md`. Tell them at setup, before they need it.
- **The supplied files stay supplied.** Never write into `Context/meridan.md`,
  `boundaries.md`, `exclusions.md`, `codex-setup.md` or `troubleshooting.md`. Auto would let
  you. Don't.
- **"No student files in this folder" is now load-bearing.** Anything in here is reachable
  and editable without a prompt. That is the reason for the rule, not an abstract one.

**During setup itself, expect to be asked.** Copying the kit from the download into OneDrive
crosses outside whatever folder Codex started in, so Auto will stop and ask. That prompt is
the boundary working, not a failure — say yes and carry on, and say to the teacher that this
is exactly the behaviour described above.

A teacher who wants tighter control can say so and work in a read-only mode, approving each
step. It is their machine. Most will not want to, and Auto is the right default for the
trial — but they should know which one they are in.

## 2. Codex is open in the installed folder

Codex reads `AGENTS.md` from the folder it is opened in. Open it one level up, or leave it
pointed at the original download instead of the installed copy in OneDrive, and the agent
gets none of this: no school context, no boundaries, no routines. It will still answer, and
it will sound fine, which is what makes this worth checking rather than assuming.

**Required:** Codex open in the installed kit folder in the teacher's own OneDrive — the
folder that contains `AGENTS.md` — and not in the download.

## 3. The context actually loaded

Config being right is not proof the files were read.

**Agent: prove it.** Say one specific thing that could only have come from
`Context/meridan.md` — not "I've read the school context", an actual detail. If you cannot,
say so plainly and check where you are running from.

## 4. Curriculum text has a source

`AGENTS.md` rule 4: curriculum wording is quoted from official text, never recalled. That
rule needs something to quote from.

**The EDU Australian Curriculum plugin is installed for this trial.** It is the source of
truth for curriculum wording — point at it, quote from it, and say when a descriptor came
from it.

It is early-stage software the teachers are helping to shape, so treat a glitch as useful
information rather than a failure, and say when it looks wrong instead of smoothing over it.

Where the plugin does not cover something, the fallback stands: official descriptor text
saved into `My Subject/` before any alignment work. Never write curriculum wording from
memory in the gap — you will produce something fluent and wrong that passes a quick read.

---

## Model

Use the strongest reasoning model available on the account for planning, alignment and
review work. Faster models are fine for small edits and tidying.

This is a preference, not a boundary — nothing in the kit breaks if it is wrong, and it is
the teacher's to change.

## What does not belong in the folder

No student files. Not to test something, not "just for a minute". The folder syncs to
OneDrive and the agent reads what is in it. See `Context/boundaries.md`.

---

## Agent: what to report

At the end of setup, four lines, no more:

- what the two checks in item 1 actually did — the in-folder edit and the outside-folder stop,
- the full path of the folder you are running in,
- one detail from `Context/meridan.md`, as proof it loaded,
- whether the curriculum plugin is there and responding.

If item 2 is wrong — you are running from the download, or a folder that has no
`AGENTS.md` — say so and stop. Everything else in this folder is void until that is fixed.
