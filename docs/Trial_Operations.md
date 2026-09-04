# Codex Teacher Trial — operations

Stephen-side. Not part of the kit teachers receive.

Covers the last open item from the design brief: where collected logs land, and the
synthesis cadence. Everything here is a proposal until you decide otherwise.

---

## Where logs land

Teachers' logs live in their own OneDrive and stay there. Sending is opt-in, session by
session; the agent offers once at the end of each wrap-up and does not send anything itself.

**Proposed collection point:** a Teams channel in a trial team, one thread per teacher, or a
shared mailbox folder if Teams is more friction than it's worth. Either way the teacher
pastes or attaches the log; the point is that the act of sending is theirs and visible to
them.

Keep a mirror at:

```
IT/AI work/Codex trial/Collected logs/<teacher>/YYYY-MM-DD.md
```

One folder per teacher, filename by date. That layout is what the synthesis agent reads, and
it makes "who has stopped sending" visible at a glance — which is itself a finding worth
having in week four.

**Why not auto-collect.** The brief's privacy position is that nothing syncs to your folder.
Automating collection would break that, and it would also remove the moment where a teacher
reads what the agent wrote and decides whether it's true. That decision is the quality
control on the whole dataset.

## Synthesis cadence

**Proposed: fortnightly during term, running from week 3.**

Weekly is too fast — with ten volunteers running at their own pace there won't be enough new
material to justify re-reading the corpus, and a document that changes little looks like a
trial that isn't going anywhere. Monthly is too slow to hit the brief's "value by week
three".

Fortnightly gives roughly five updates a term and lets a pattern show up twice before it
gets written down as a pattern.

Run it from `Collected logs/`, output to `What we're learning.md`, and send the link — not
the document — so everyone reads the current version.

## Synthesis prompt

Point an agent at the collected logs with this:

> Read every log in `Collected logs/`, including ones you have read before, and rewrite
> `What we're learning.md` from scratch. Do not edit the previous version — rebuild it, so
> patterns that have faded drop out.
>
> These are real logs from ten volunteer teachers in a trial of agentic AI. They were drafted
> by each teacher's agent and corrected by the teacher, so the corrections are the most
> reliable part.
>
> Surface:
> - **Where teachers got stuck** — same obstacle, more than one person. Name the obstacle
>   concretely.
> - **Tasks that keep recurring** — what people actually use it for, as against what we
>   expected them to use it for.
> - **What was abandoned after one attempt.** This is the most valuable pattern and the
>   easiest to miss, because nobody writes a log saying "I gave up". Look for a task that
>   appears once in someone's logs and never again.
> - **Where it fell over** — errors, unusable output, anything that would have gone out wrong
>   if the teacher hadn't caught it.
>
> Rules:
> - No teacher names and no student names. Refer to "one teacher", "three teachers".
> - Count. "Four of ten" beats "several".
> - Quote the teachers' own words where a line is better than a summary of it.
> - A pattern with one instance is an anecdote — say so, or leave it out.
> - Say what the logs do not show. Silence in the corpus is a finding: if nobody has
>   mentioned assessment, that is worth a line.
> - Plain Australian English, half a page to a page. No preamble, no closing summary, no
>   recommendations unless the logs support one.

## End of trial

Same corpus, different job: the evaluation report is built from the logs rather than from
impressions. Two comparisons make it worth reading —

1. **Baseline against outcome.** Every teacher's `my-profile.md` records, in their own words,
   what would make the trial worth their while and what they were sceptical about. Ask them
   the same two questions at the end and put the answers side by side. That is the strongest
   evidence the trial can produce, and it only works if the profiles are collected — ask for
   them at orientation, or the comparison is lost.
2. **Volume and drop-off.** Logs per teacher over time. A teacher who stopped logging in week
   five is a finding, and you will want to have asked them why at the time rather than
   guessing in December.

## Open decisions

- [ ] Teams channel or shared mailbox for log collection
- [ ] Whether teachers send `my-profile.md` at orientation (recommended — the baseline is
      the trial's best evidence and cannot be reconstructed later)
- [ ] Named contact at EDU Plugins, secured before orientation day
- [ ] Who else sees `What we're learning.md` while the trial is running, and when leadership
      first sees it
