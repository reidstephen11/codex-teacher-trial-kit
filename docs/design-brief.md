# Codex Teacher Trial — Design Brief

**Author:** Stephen Reid, Head of Department – Innovation, Technology & Interactive Learning (ITIL), Meridan State College
**Status:** Design settled; ready for build
**Trial period:** To the end of the 2026 school year

---

## Context

Following a staff presentation on agentic AI at Meridan, a teacher trial of Codex is being scoped. Participation is by expression of interest — volunteers only, not a mandated cohort. This brief captures the design decisions reached and is intended as a handover document for build work in Claude Code.

---

## Core design principle

The trial manages itself using the tool being trialled.

Reporting burden is what usually kills teacher trials — nobody fills in the reflection journal. Here the agent writes the session log and the teacher corrects it, which produces data that would otherwise never be collected.

The organising tension is **convergent plumbing, divergent practice**. The whole point of the trial is that different teachers will approach this from different angles, so the scaffold must not prescribe a path. The only thing standardised is the shape of the log that comes out the end. Everything else — folder structure, subject context, workflow — is theirs to restructure, extend or ignore entirely.

---

## Delivery mechanism

The scaffold is emailed as a ZIP. Teachers download it and point Codex at the ZIP with a single instruction: open it and follow the instructions inside.

The ZIP is the installer, not just a bundle of files. The agent unpacks itself, sets up the folder structure in the teacher's own OneDrive, and introduces itself.

This is deliberate — teachers experience the agent doing real work before anyone explains what an agent is. The setup routine must finish by telling them what it just did and where things now live, so nobody is left with a working setup they don't understand.

**Privacy position:** each teacher's folder lives in their own OneDrive. Nothing syncs to Stephen's. Sharing is opt-in throughout.

---

## Scaffold contents

| Component | Purpose |
|---|---|
| School context file | Meridan vision and values, design principles, contextual information about the school, students, local area and employers. Mirrors Stephen's existing agent context. |
| Constraint boundary | What can and can't go into the tool, in plain language. |
| Subject folder | Empty and unstructured. Theirs. |
| Logs folder | Where session logs land. |
| Wrap-up skill | Run at the end of a working session. |
| Onboarding interview routine | Runs once at setup. |
| Shared troubleshooting file | Updated by Stephen as real issues emerge; every teacher's agent reads it. |

The constraint boundary sits in the folder so the compliance question is answered where the teacher is, rather than arriving in Stephen's inbox in week one.

The school context file is reusable beyond this trial — it becomes the school's context layer that other agent work can plug into later.

---

## Onboarding interview

As part of setup, the agent interviews the teacher to build its own understanding of their priorities. Three or four questions along these lines:

- What's eating your time?
- What would you like to try?
- What are you sceptical about?
- What would make this worth your while?

It writes their profile into the folder and works from it thereafter.

This does double duty. It solves the divergence problem without prescription — the agent elicits their path rather than assigning one, and everyone ends up with a different configuration built from their own words. And their answers become the day-one baseline, in their own language, to compare against at the end of the year.

---

## Session log

Deliberately short — four fields. Anything longer and correcting the agent's draft becomes work in itself.

1. What did you try
2. What happened
3. What surprised you
4. What you'd want next

The agent drafts it, the teacher reads it, fixes a line, and chooses whether to send it. Consistent shape across all teachers is what makes synthesis possible.

---

## Synthesis

An agent runs across the collected logs to produce a living "what we've learned" document that updates as logs arrive — so the trial generates value by week three rather than only at the end. At the close of the trial, the same corpus produces the evaluation report, built from evidence rather than Stephen's impressions of how it went.

Patterns worth surfacing:

- Where teachers got stuck
- Which tasks kept recurring
- What was abandoned after a single attempt

---

## Support behaviour

The default help path is the agent itself, not Stephen's inbox.

Bake into the config that when a teacher is stuck, the agent attempts to resolve it first, and only escalates by drafting a message to Stephen if it can't. Issues that reach Stephen then arrive already diagnosed rather than as "it's not working".

The shared troubleshooting file means one person's problem becomes everyone's fix. It also means Stephen's week-two inbox tells him something useful — whatever gets through is genuinely hard.

---

## Orientation day workflow

1. Email the ZIP; teachers download it and point Codex at it.
2. Agent unpacks, installs into OneDrive, and reports back what it did and where things now live.
3. Agent checks how Codex itself is configured against `Context/codex-setup.md` and reports back — approval mode, which folder it is running in, proof the context loaded, curriculum source. Approval mode is the one that cannot be left to chance: propose-before-change is an instruction in `AGENTS.md`, and a Codex set to approve its own edits overrides it silently. Confirm the exact setting names on a Department machine before the day and write them into that file, so every teacher gets the same version.
4. Agent reads the school context and reflects it back to them. This is the moment it lands, because it's already contextualised.
5. Agent runs the onboarding interview.
6. Teacher completes **one real task they brought with them** — a unit they haven't read, a set of feedback comments, whatever is genuinely annoying them. Not a demo task.
7. Run the wrap-up skill once, with Stephen in the room, so the loop isn't novel when they're working alone.

---

## EDU Plugins

A small team is mapping the Australian Curriculum into an agent plugin. Stephen has met them and briefly tested it; they want user experience and feedback from real teachers, he wants the networking and a genuinely useful tool. Going in on day one.

Framing on the day: early-stage software they are helping to shape, not a finished product. This reframes any glitch as useful data rather than a failure, and it's flattering to be asked to test something.

Worth securing a named contact from the team who will respond quickly during the trial window.

---

## Build status

Built 3 September 2026. Kit lives in `Codex Teacher Trial Kit/`, packaged as
`Codex-Teacher-Trial-Kit.zip`. Trial-side operations (log collection, synthesis cadence and
prompt, end-of-trial evaluation) are in `docs/Trial_Operations.md`, which stays in this
repository and out of the teacher ZIP.

- [x] School context file — `Context/meridan.md`, distilled from `Fable projects/Meridan Context`
- [x] Constraint boundary — `Context/boundaries.md`, green/amber/red in plain language
- [x] ZIP setup instructions the agent executes on first run — `START-HERE.md`
- [x] Onboarding interview routine — `Routines/onboarding-interview.md`
- [x] Wrap-up skill — `Routines/wrap-up.md`
- [x] Shared troubleshooting file starter — `Context/troubleshooting.md`
- [x] Codex configuration — `Context/codex-setup.md` (approval mode `Auto`; EDU plugin in
      on day one). The agent checks live at setup whether `Auto` actually stops an edit to
      an existing file — if it does not, drop a mode and correct this file for everyone.
- [x] Worklog routine — `Routines/worklog.md`, agent-maintained, read at wrap-up
- [x] Synthesis cadence and where logs land — `docs/Trial_Operations.md` (fortnightly from week 3,
      proposed; collection point still to decide)

Outstanding decisions are listed at the foot of `docs/Trial_Operations.md`.

### Note on the session log format

`session-reflection.md` in this folder specifies a five-section, half-page reflection with a
time-saved estimate, written for a leadership audience. The kit implements the four-field log
specified in this brief instead. The two are different instruments: the four-field log is the
per-session capture, and the reflection's concerns — time bought back, capability unlocked,
student experience — are better answered across the corpus at synthesis than guessed at
session by session. `session-reflection.md` is retained unused.
