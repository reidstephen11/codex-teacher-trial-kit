# Orientation day — run sheet

Stephen-side. Not part of the kit teachers receive; `docs/` is stripped from the ZIP.

The kit runs the session. Your job is not to present it — it is to be in the room while it
happens, and to collect the two things that cannot be recovered afterwards.

**The two that cannot be recovered:**

1. **`my-profile.md`, collected on the day.** It records, in each teacher's own words, what
   would make the trial worth their while and what they are sceptical about. The end-of-year
   evaluation is that baseline set against the same two questions in December. Ask in
   November and you get a reconstruction, not a baseline.
2. **Wrap-up practised while you are in the room.** The four-field log is the only
   standardised artefact in the trial. If the first time anyone runs it is alone on a
   Tuesday, some of them never will.

Everything else on the day can be fixed later.

---

## Before the day

- [ ] **Say in the invite email: bring one real job.** Something genuinely annoying them
      this week — a unit they haven't read, a task sheet that needs rewriting. Not a demo.
      If this is not in the email, nobody brings one and step 6 has nothing to work on.
- [ ] Codex installed on each machine, OneDrive signed in. An IT job, not a day-one job.
- [ ] EDU Curriculum plugin installed, and a named contact from that team who will answer
      quickly during the trial.
- [ ] Run the whole kit yourself, start to finish, on a machine like theirs. Not in a cloud
      workspace — the install writes into OneDrive and that is the part that breaks.
- [ ] Close the open decisions at the foot of `Trial_Operations.md`. Two of them bite on the
      day: where logs get sent, and whether profiles are collected at orientation.
- [ ] Decide how you will hold profiles, and be ready to say it in one sentence (below).

## In the room — about an hour

Stretch it if you have longer. The agent-led stretches are the ones to protect.

| | | |
|---|---|---|
| **0–5** | Framing | Yours. Two minutes, below. |
| **5–10** | ZIP out, unpacked, Codex opened in the folder | Watch for the folder mistake. |
| **10–25** | Agent installs, checks config, reflects the school context back | Agent-led. Float. |
| **25–35** | Onboarding interview | Agent-led. Stay out of it. |
| **35–50** | One real job | The point of the day. |
| **50–58** | Wrap-up, practised | Do not let this get squeezed. |
| **58–60** | Profiles, and what happens next | Yours. |

### 0–5 · Framing

Three things, briefly:

- Voluntary, runs to the end of the year, and stopping is a legitimate outcome.
- The agent writes the session log, they correct it. There is no reflection journal.
- The curriculum plugin is early-stage software they are helping to shape. A glitch is
  useful information, not a failure.

Then stop talking. The kit is better at the rest than a slide is.

### 5–10 · Getting Codex open in the right place

The one thing to watch. Codex reads `AGENTS.md` from the folder it is opened in, so a
teacher who opens it a level up, or leaves it pointed at the download, gets none of the
school context — and the agent will still answer, fluently, which is what makes it hard to
spot from across the room.

Unpack the ZIP first. Open Codex in the unpacked folder.

### 10–25 · Install and config

Agent-led. Two moments worth naming out loud when they happen:

- **A prompt while it copies into OneDrive.** That is Auto asking before it touches anything
  outside the folder. The boundary working, not a fault.
- **The two demonstrations in `Context/codex-setup.md`** — an in-folder edit that goes
  through without asking, an outside-folder request that stops. Let the agent do it. This is
  where the room learns what the tool will and won't do on its own, and it lands far better
  as a demonstration than as a warning.

Say the honest version once: inside their folder the agent can change things without asking,
it is instructed to propose first, and OneDrive version history is the undo. Show someone
where version history is if there is time.

### 25–35 · The interview

Agent-led, one question at a time. **Do not help.** A teacher hedging their scepticism
because their HOD is standing behind them produces a worse baseline than an awkward pause.
Be elsewhere in the room.

### 35–50 · One real job

Whatever they brought. If someone has nothing, the agent will have suggested a first job at
the end of the interview from their own answer about what eats their time — use that.

Resist improving their prompt. Watching what a teacher asks for unprompted is the most
useful thing you will see all day, and it is gone the moment you coach it.

### 50–58 · Wrap-up

Have everyone say **"wrap up"** at the same time, even those whose job is half-finished.
Especially those — a log that says the job was not finished is a good log.

They correct what the agent got wrong. Say plainly that the corrections are the valuable
part and that a log full of successes tells the trial nothing.

### 58–60 · Profiles and next steps

Ask for `Context/my-profile.md`. One sentence on why, and one on how you hold it — something
like: *"Their working copy stays theirs and stays on their machine; the copy I take today is
the baseline I put your December answers next to."*

Say it out loud rather than collecting quietly later. The kit's privacy position is that
nothing syncs anywhere, `my-profile.md` is gitignored by design, and a copy appearing on
your drive without being mentioned looks like the promise moved.

Then: how to send a log, that sending is optional every time, and that the agent is the
first line of support — tell it before emailing anyone.

## If someone gets stuck

Do not stall the room. `START-HERE.md` has a manual fallback at the bottom: copy the folder
into OneDrive by hand, open Codex there, and say *"Read AGENTS.md, then run the onboarding
interview in Routines/."* That reaches the same place.

Anything you fix twice in the room belongs in `Context/troubleshooting.md` that afternoon,
while you still remember the exact wording of the error.

## Afterwards

- [ ] Profiles filed as the baseline. Note anyone who did not hand one over.
- [ ] Whatever broke twice, written into `Context/troubleshooting.md` and sent round.
- [ ] Anything the config section got wrong, corrected in `Context/codex-setup.md` — it is
      centrally maintained, so one fix reaches everyone.
- [ ] First synthesis is week 3. From then, a teacher whose logs stop is a finding worth
      asking about at the time rather than guessing at in December.
