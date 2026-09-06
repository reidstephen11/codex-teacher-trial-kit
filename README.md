# Codex Teacher Trial Kit

A self-installing scaffold for a voluntary teacher trial of agentic AI at Meridan State
College. Teachers receive a ZIP and open the unpacked folder as a Codex project.
With Steve in the room, the agent helps copy it into Department OneDrive, hands over to
the installed project, checks setup, captures a short profile and helps with one real job.
Everyone practises wrap-up before leaving. Deidentified, non-sensitive student work is
permitted; original student writing stays unchanged and feedback is saved separately.

This repository is the **source of truth for the kit**. The thing teachers actually get is
a ZIP built with `./build-zip.sh [commit-or-tag]` (default: `HEAD`). The builder archives
an explicit list of supplied files from that Git commit, never the working directory.
Commit approved edits before building. The ZIP's archive comment records the commit SHA.
Profiles, setup state, teaching work, collected logs and maintainer documents are excluded,
even if accidentally tracked. GitHub remains the source of truth for shared kit changes.

Run `python3 -m unittest discover -s tests -v` to check packaging before distribution.

## Design principle

The trial manages itself using the tool being trialled. Reporting burden is what usually
kills teacher trials — nobody fills in the reflection journal. Here the agent drafts the
session log and the teacher corrects it, which produces evidence that would otherwise never
be collected.

The organising tension is **convergent plumbing, divergent practice**. The only thing
standardised is the shape of the log that comes out the end. Folder structure, subject
context and workflow are the teacher's to restructure, extend or ignore.

## Layout

| Path | What it is |
|---|---|
| `START-HERE.md` | The entry point. First half is for the teacher, the rest instructs the agent through install and orientation. |
| `AGENTS.md` | Standing instructions for the agent once the kit is installed. |
| `Context/meridan.md` | College vision, values and context — the school knowledge the agent starts with. |
| `Context/boundaries.md` | What can and can't go into the tool, in plain language. |
| `Context/exclusions.md` | Things the agent must not do or touch. |
| `Context/troubleshooting.md` | Common failures and how to get unstuck. |
| `Context/codex-setup.md` | The Codex configuration the kit assumes, and why. Checked at setup. |
| `Routines/onboarding-interview.md` | The short first-session interview. |
| `Routines/worklog.md` | The running record the agent keeps as it works. Teacher never writes in it. |
| `Routines/wrap-up.md` | End-of-session routine that drafts the log, read off the worklog. |
| `Logs/` | Where session logs land. Empty by design. |
| `My Subject/` | The teacher's own space. Unstructured on purpose. |
| `docs/design-brief.md` | Why the trial is shaped this way; the decisions behind the kit. |
| `docs/session-reflection.md` | The cohort-wide reflection format. Unused; see the design brief. |
| `docs/orientation-run-sheet.md` | What Steve does on orientation day, and what must be collected. Not in the ZIP. |
| `docs/Trial_Operations.md` | Trial-side operations: log collection, synthesis cadence, end-of-trial evaluation. Not in the ZIP. |
| `build-zip.sh` | Builds the teacher-facing ZIP. Not included in it. |

## Privacy position

Each teacher's folder lives in **their Department OneDrive**. The kit does not automatically
collect work or logs for Steve. AI processing is not promised to be offline. Sending
a log is opt-in, session by session — the agent offers once at the end of a wrap-up and
never sends anything itself. No student names or identifying details go into any log.

`.gitignore` excludes working logs, teaching files, profiles and setup state to reduce
accidental commits. Ignore rules do not remove material already tracked. The distribution
builder uses a separate allowlist.

## Status

Design settled; trial runs to the end of the 2026 school year. Participation is by
expression of interest — volunteers, not a mandated cohort.

## Related

[`agent-starter-kit`](https://github.com/reidstephen11/agent-starter-kit) — the earlier,
agent-agnostic setup for curriculum QA and student feedback that this trial builds on.
