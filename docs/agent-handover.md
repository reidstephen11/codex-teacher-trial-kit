# Agent handover — suitability review (3 September 2026)

**For the next agent working on this kit, not for teachers.** This file lives in `docs/`
so `./build-zip.sh` strips it from the ZIP. Do not copy it into `AGENTS.md`,
`START-HERE.md`, or anything a teacher will see unless a human asks you to.

A cloud agent evaluated this repo for: *getting teachers started with Codex and agentic
workflows for education*. The findings are below. Consider them before changing the kit.
Do not treat this file as a mandate — the teacher (Steve, who owns the trial) decides.

---

## Verdict to take as the starting point

The kit is **ready as a runtime constitution** for a facilitated first session: school
context, boundaries, exclusions, onboarding interview, wrap-up, agent-first support.

It is **not yet a standalone getting-started kit**. The missing work is the last mile
*before* the first useful job: how to open Codex in a folder, which Codex surface is
in scope, unpack the ZIP first, OneDrive signed in, no student files.

Do not "fix" that gap by adding lesson templates, prompt libraries, or a prescribed
workflow. The design principle is **convergent plumbing, divergent practice**. The only
standardised artefact is the four-field session log.

---

## Constraints you must not violate

Read `docs/design-brief.md` and `AGENTS.md` before editing teacher-facing files.

- Teachers receive a ZIP and one instruction. Do not add a reading list they have to
  finish before they can start.
- `My Subject/` stays empty and unstructured.
- Do not invent curriculum wording. Do not add fake descriptor codes as examples.
- Do not put student names, student work, or red-list material anywhere, including here.
- `docs/session-reflection.md` is **unused**. The live instrument is the four-field log
  in `Routines/wrap-up.md`. Do not wire the five-section leadership reflection into
  wrap-up.
- `Context/meridan.md`, `boundaries.md`, `exclusions.md` and `troubleshooting.md` are
  supplied centrally. Do not rewrite them as part of a getting-started pass unless Steve
  asked.

Predecessor kit, for literacy that was deliberately *not* copied in:  
https://github.com/reidstephen11/agent-starter-kit  
Useful there: glossary, which tools can read a local folder, "local ≠ private" (files
still leave the machine), Track A before any student data. Do not import Track B
(student-work feedback) into this trial kit.

---

## Gaps worth acting on (priority order)

### 1. Before-you-open-Codex sheet (highest value)

A **one-page** teacher-facing note, probably the top of `START-HERE.md` or a sibling
file that *does* go in the ZIP. Cover only:

- Which Codex surface is in scope (local on a Department Mac/PC). Cloud / browser
  Codex cannot honour the OneDrive install and is the wrong surface for this kit.
- Unpack the ZIP first; do not assume Codex can be pointed at a `.zip`.
- How to open Codex *in that folder* (File → Open Folder / equivalent). One or two
  sentences, not a tutorial.
- OneDrive signed in on that machine.
- No student files in the folder.

The existing "If the setup fails" section is the right tone. It is currently too far
down the page.

### 2. Reconcile session one

`START-HERE.md` forbids any teaching resource in the setup session.  
`docs/design-brief.md` (orientation day) wants one real job, with wrap-up practised
while Steve is in the room.

Those contradict. Pick one with Steve, then write the winner into the teacher-facing
page. Suggested default if he is in the room: setup *then* one real job. Suggested
default if they are working alone from email: setup only, and name the first job for
next time (onboarding already does this).

### 3. Three example first jobs — suggestions, not templates

After the interview, teachers who have never used an agent often cannot name a prompt.
Add three examples that do not prescribe a unit structure, e.g.:

- Drop a task sheet *they already wrote* into `My Subject/` and ask the agent to list
  problems, changing nothing.
- Save official curriculum text they need, then ask for alignment issues against that
  file only.
- Paste a week's planning notes and ask for a skeleton, not a script.

Put them in `Routines/onboarding-interview.md` under "Finish by naming the first job",
or in troubleshooting as "I don't know what to ask". Do not turn them into workflow
files.

### 4. Troubleshooting starters still missing

`Context/troubleshooting.md` covers OneDrive path, sync lag, invented curriculum codes,
unwanted rewrites, output too long, boundary refusals. Add (as starters, before the
trial, if Steve agrees):

- Codex is not installed / will not open a folder
- Agent did not read `START-HERE.md` (paste-the-fallback already exists; make it a
  known issue)
- Cloud or web Codex vs local
- Department proxy / sign-in failures (only if someone has actually seen them — do not
  invent)

### 5. `Trial_Operations.md` is cited and not in this repo

`docs/design-brief.md` marks synthesis cadence as done and points at
`Trial_Operations.md`. It is not here. Either add it, or stop claiming it is in this
repository. Outstanding decisions listed at its foot cannot be actioned from this clone.

---

## What is already strong — do not "improve" these

- One-sentence teacher entry in `START-HERE.md`
- School context in College language (`Context/meridan.md`)
- Green / amber / red boundaries; wellbeing material stops
- Pedagogical exclusions with replacements
- Propose-before-change; teacher decides, agent recommends
- Four-field wrap-up, share-optional, agent never sends
- Agent as first-line support; diagnosed escalation to Steve only if stuck
- `my-profile.md` created at onboarding, gitignored, verbatim scepticism

Length is not quality. A plan is a skeleton, not a script.

---

## What the evaluating agent could not check

- Live Codex on a Department image (OneDrive paths, ZIP-as-folder, Files-On-Demand)
- The EDU Australian Curriculum plugin named in the design brief — not in this kit
- `Context/my-profile.md` — absent by design
- `Trial_Operations.md` — missing from this clone

Prove the OneDrive install on a machine like the teachers', not in a cloud workspace.

---

## If you change teacher-facing files

Propose first if you are rewriting an existing file. Creating a new file is fine.
Keep Australian English. Keep the ZIP small. After any kit-file change, confirm
`./build-zip.sh` still excludes `docs/`, `README.md`, git metadata, and working
material (`Logs/` contents, `My Subject/` contents, `my-profile.md`).
