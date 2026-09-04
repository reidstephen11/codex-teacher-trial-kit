# Codex Teacher Trial Kit

A self-installing scaffold for a voluntary teacher trial of agentic AI at Meridan State
College. Teachers receive it as a ZIP, point Codex at it, and say *"Open this and follow
the instructions inside."* The agent unpacks itself into the teacher's own OneDrive, reads
the school context and the boundaries, runs a short onboarding interview, and stops.

This repository is the **source of truth for the kit**. The thing teachers actually get is
a ZIP built from it with `./build-zip.sh`, which strips this README, `docs/` and the git
metadata — teachers get the kit, not the paperwork behind it.

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
| `Routines/onboarding-interview.md` | The short first-session interview. |
| `Routines/wrap-up.md` | End-of-session routine that drafts the log. |
| `Logs/` | Where session logs land. Empty by design. |
| `My Subject/` | The teacher's own space. Unstructured on purpose. |
| `docs/design-brief.md` | Why the trial is shaped this way; the decisions behind the kit. |
| `docs/session-reflection.md` | The cohort-wide reflection format. Unused; see the design brief. |
| `docs/Trial_Operations.md` | Trial-side operations: log collection, synthesis cadence, end-of-trial evaluation. Not in the ZIP. |
| `build-zip.sh` | Builds the teacher-facing ZIP. Not included in it. |

## Privacy position

Each teacher's folder lives in **their own OneDrive**. Nothing syncs anywhere else. Sending
a log is opt-in, session by session — the agent offers once at the end of a wrap-up and
never sends anything itself. No student names or identifying details go into any log.

`.gitignore` excludes `Logs/`, `My Subject/` and `my-profile.md` so that working material
cannot be committed by accident.

## Status

Design settled; trial runs to the end of the 2026 school year. Participation is by
expression of interest — volunteers, not a mandated cohort.

## Related

[`agent-starter-kit`](https://github.com/reidstephen11/agent-starter-kit) — the earlier,
agent-agnostic setup for curriculum QA and student feedback that this trial builds on.
