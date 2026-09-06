# Shared troubleshooting

**Maintained centrally by Steve Reid.** Teachers receive a copy of this file with the kit.
Distribute updated copies after a shared fix; local copies do not update themselves.

**Agent: read this before telling a teacher that something can't be done.** If you solve
something that isn't listed here, say so, and suggest the teacher mention it so it can be
added for everyone.

**Teachers: don't edit this file** — your edits will be overwritten when an updated version
is sent round. Put local notes in `Context/my-profile.md` instead.

*Last updated: 7 September 2026.*

---

## Getting help at all

**During orientation, Steve is in the room.** If a quick fix does not work, ask him
to help with the failed step.

**After orientation, the agent is the first line of support.** If something isn't working, tell your agent
before you email anyone. It has these notes, it can read the actual error, and it can try
things. If it can't solve it, it will write up the problem — what you were doing, what
happened, what it already ruled out — and you can send that on. A diagnosed problem gets a
much faster answer than "it's not working".

---

## Known issues

### The agent can't find my OneDrive folder

Cloud storage paths differ between Mac and Windows and between accounts.

- macOS — usually `~/Library/CloudStorage/OneDrive-DepartmentofEducation/`
- Windows — usually `%USERPROFILE%\OneDrive - Department of Education\`

If there are several OneDrive folders, the Department one is the one to use, not a personal
one. If nothing is there, OneDrive may not be set up on that machine — that is an IT job, not
a Codex one.

### Files I saved aren't showing up / are out of date

OneDrive sync lag, usually. Give it a minute. Files-On-Demand can also mean a file exists but
its contents aren't downloaded yet — the agent will report it as unreadable. Open the file
once in Finder or Explorer to force it down, then try again.

### The agent invented a curriculum code or achievement standard

Expected, and the reason for the rule in `AGENTS.md`: curriculum wording is quoted from
official text, never written from memory. If you haven't saved the actual text into the
workspace, the agent has nothing to quote and will produce something fluent and wrong.

Save the descriptor text you need from the official site into your own folder, and tell the
agent to use it. If you are using a curriculum plugin or tool, tell the agent that is the
source of truth.

### The agent rewrote a file I didn't want touched

An explicit editing request authorises that scoped change, but not unrelated edits.
Tell the agent what went beyond your request. `AGENTS.md` is an instruction, not a lock;
the actual permissions determine technical access. See `Context/codex-setup.md`.

For recovery, check OneDrive version history for a synced prior version before restoring.
If there is no version available, tell Steve; do not promise recovery or overwrite more
files trying to fix it. Practise on the disposable setup file during orientation.

### Output is too long / too generic

Say so, bluntly, in the session. Then get it written into `Context/my-profile.md` under
Working preferences, or it will happen again next session. Anything you find yourself
correcting twice belongs in that file.

### It won't do something because of the boundaries file

Check `Context/boundaries.md` — the rule and the reason are both in there. If you think the
boundary is wrong for a genuine task, that's a conversation with Steve, not something to
argue with the agent about.

---

## Not yet reported

Nothing else yet. This file grows as the trial runs — if you hit something that isn't here,
that's genuinely useful information, not a nuisance.
