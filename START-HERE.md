# Start here

**If you are a teacher reading this:** you don't need to read any further. Open Codex,
point it at this folder (or the ZIP it came in) and say:

> Open this and follow the instructions inside.

That's it. The agent will read the rest of this file, set itself up in your OneDrive, and
then tell you what it did. Give it five minutes and answer its questions.

If something goes wrong, skip to **If the setup fails** at the bottom.

---

## Everything below this line is for the agent

You are being run by a teacher at Meridan State College who is part of a voluntary trial of
agentic AI. This may well be the first time they have watched an agent do anything. Your
conduct in the next ten minutes sets what they expect from the whole trial.

Your job right now is **installation and orientation**. Do not draft any teaching resource,
unit, lesson or feedback in this session, even if asked — say you'll do it first thing next
session, once the setup is finished.

### Step 1 — Work out where you are and say so

Before you touch anything, tell the teacher in two or three lines:

- what this folder is,
- where it currently sits on their machine,
- and that you are about to copy it into their OneDrive.

If the kit is still inside a ZIP, unpack it to a temporary location first.

### Step 2 — Agree an install location, then install

Propose a location inside the teacher's **own OneDrive**, so it syncs to their laptop and
backs itself up. On a Department-managed Mac or PC this is usually a path like:

- macOS — `~/Library/CloudStorage/OneDrive-DepartmentofEducation/Codex Trial/`
- Windows — `%USERPROFILE%\OneDrive - Department of Education\Codex Trial\`

Do not guess. Check that the OneDrive folder actually exists before proposing it, and if
you find more than one OneDrive folder, show the teacher the list and ask which is theirs.

Show the full path you intend to use and wait for a yes. If they'd rather it went
somewhere else, use their location — it is their machine.

Then copy the whole kit there. **Copy, don't move**, so the original download is still
intact if anything goes wrong. Verify afterwards that the files are actually at the
destination, and say so plainly if they are not.

From this point on, work in the installed copy, not the download.

### Step 3 — Report what you did

Tell them, in plain language and no more than about eight lines:

- the folder you created and where it is,
- what is in it, one line each,
- that `Context/boundaries.md` is the rules file and is worth two minutes of their time,
- that everything in the folder is theirs to change, including your own instructions in
  `AGENTS.md`,
- and what happens next (you're about to read the school context, then ask them some
  questions).

Do not use the words "installed successfully" and leave it there. They should be able to
find the folder in Finder or Explorer from what you just told them.

### Step 4 — Check how Codex itself is set up

Read `Context/codex-setup.md` and work through it. It is short. It matters because the
standing rules in `AGENTS.md` — propose before you change anything, in particular — are
requests to you, and a Codex configured to approve its own edits will override them
without either of you noticing.

Report the four lines that file asks for. If the approval mode is wrong, or you are running
from the download rather than the installed copy, say so and stop there. Do not continue
into the interview.

### Step 5 — Read the school context and reflect it back

Read `Context/meridan.md` in full. Then say back to the teacher, in three or four
sentences, what you now know about where they work — the College's own words, not a
paraphrase of them.

Keep it short. The point is that they see you are already contextualised, not that you
recite the file at them.

### Step 6 — Read the boundaries

Read `Context/boundaries.md` and `Context/exclusions.md`. Do not summarise these back at
length. Say one line: that you've read what can and can't go into the tool, and that you'll
stop them if they head towards a line.

### Step 7 — Run the onboarding interview

Follow `Routines/onboarding-interview.md` exactly. It is short and it matters — it is how
you find out what this particular teacher actually needs, rather than assuming.

### Step 8 — Stop and hand over

Finish by telling them:

- what exists now,
- that the next thing to do is **one real job they brought with them** — something that is
  genuinely annoying them today, not a demo,
- and that at the end of a working session they should say "wrap up" and you will draft the
  session log for them to correct.

Then stop. Do not start the real job in this session unless they ask you to.

### Rules for this session

- One question at a time. Wait for the answer.
- Short answers get written down as they were said. Do not inflate a one-line answer into
  three paragraphs of educational prose.
- Never write anything into `Context/meridan.md`, `Context/boundaries.md`,
  `Context/exclusions.md` or `Context/troubleshooting.md` during setup. Those are supplied.
- If a step fails, say which step and what the error was. Do not carry on as though it
  worked.

---

## If the setup fails

Nothing here is magic — it is a folder of text files. If the agent cannot install it:

1. Copy this whole folder into your OneDrive by hand, anywhere sensible.
2. Open Codex in that folder.
3. Say: *"Read AGENTS.md, then run the onboarding interview in Routines/."*

That gets you to the same place. If you're stuck, tell your agent you're stuck — it will try
to sort it out and only involve Steve if it can't.
