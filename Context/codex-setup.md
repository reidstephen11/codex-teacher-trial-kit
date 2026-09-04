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

**Required:** the mode where Codex asks for approval before editing files and before
running commands. Not the fully automatic one.

> **Exact setting on a Department machine:** `<Steve to fill in once, before orientation>`

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

**Required:** either the EDU Australian Curriculum plugin is installed and the teacher
knows to point at it as the source of truth, or official descriptor text gets saved into
`My Subject/` before any alignment work. If neither is true, the agent has nothing to quote
and will produce something fluent and wrong.

> **Plugin installed on the day:** `<yes / no — Steve to confirm>`

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

- whether the approval mode is the asking one, and what it is set to,
- the full path of the folder you are running in,
- one detail from `Context/meridan.md`, as proof it loaded,
- whether there is a curriculum source, or that there is not yet.

If 1 or 2 is wrong, say so and stop. Getting those right takes a minute at the start and
saves a rewritten file the teacher did not agree to.
