# Codex setup — the config this kit assumes

**Maintained centrally by Steve Reid**, like `troubleshooting.md`. Teachers: don't edit
this file, your changes will be overwritten when an updated copy goes round.

Everything else in this folder tells the agent how to behave. This file is about how Codex
itself is set up, which is a different thing — a rule in `AGENTS.md` is a request the agent
can be configured to ignore. Four things need to be true before any of the rest works.

**Agent: check these at the end of setup, report what you found, and stop if item 1 or
item 2 is wrong.** Do not carry on and hope.

---

## 1. The agent asks before it changes anything

`AGENTS.md` says: propose before you move, rename, delete or rewrite an existing file.
That is the promise the whole trial rests on — a teacher trusts this because nothing
happens to their work without them saying yes.

It is only a promise. If Codex is set to approve its own edits and commands, the agent can
rewrite a file and tell the teacher afterwards, and the rule in `AGENTS.md` will not have
stopped it. The setting wins over the instruction.

**The mode used in this trial is `Auto`.** Not the fully automatic one above it.

**A mode name does not tell you what it actually stops, so check it rather than trusting
it.** `Auto` is a middle setting: on some builds it edits files inside the working folder
without asking and only pauses for things outside it. If that is how it behaves here, then
`Auto` does not enforce rule 2 and the mode below it is the one this trial needs.

**Agent: settle it live, at setup.** Propose a trivial change to an existing file in the
folder — a blank line at the end of `My Subject/README.md` will do — and see what happens.

- If Codex asks the teacher to approve it first, `Auto` is right. Say so and carry on.
- If the edit just happens, say so plainly, undo it, and tell the teacher that
  propose-before-change is not being enforced at this setting and which mode to drop to.
  Then tell Steve, so this file can be corrected for everyone.

Yes, it means more prompts in the first week. That is the trade, and it is the right way
round for teachers who are watching an agent work for the first time. A teacher who wants
to loosen it later, having seen what it does, can — it is their machine.

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

- the approval mode, and what the live check above actually did,
- the full path of the folder you are running in,
- one detail from `Context/meridan.md`, as proof it loaded,
- whether the curriculum plugin is there and responding.

If 1 or 2 is wrong, say so and stop. Getting those right takes a minute at the start and
saves a rewritten file the teacher did not agree to.
