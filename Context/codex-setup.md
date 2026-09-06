# Codex setup

Maintained centrally by Steve Reid. Check this in the installed project, before the
onboarding interview. Steve is in the room during orientation and can help with the UI.

## 1. Confirm the project and actual permissions

Check that the active project's working directory is the installed folder containing
`AGENTS.md`. Merely copying files there or changing a shell directory is not a project
handoff. If the task is still attached to the download, follow `START-HERE.md` to reopen.

Check the active permissions shown by Codex, rather than assuming a label such as `Auto`
guarantees particular behaviour. The trial default is workspace-limited editing with
approval for actions requiring broader access, not Full access. Where effective settings
are visible, the conventional configuration is `workspace-write` with `on-request`
approvals. If the configuration differs or is not visible, describe what you can establish
and have Steve help check it. Do not change global settings or broaden access silently.

Explain in two sentences: the agent can normally edit within its permitted workspace;
sandbox boundaries and approval rules determine which other actions need approval.
Reading outside the folder does **not** reliably trigger approval. Additional writable
folders, platform behaviour and configuration can affect the boundary. Do not claim that
all outside-folder actions ask, or deliberately probe unrelated files to demonstrate it.

`AGENTS.md` governs how you should behave; it is not a technical lock. An explicit request
to edit a file authorises the relevant change, without a second confirmation. The teacher
still reviews the output, and original student work stays unchanged.

## 2. Demonstrate saving and recovery with a disposable file

Create `My Subject/setup-practice.txt` containing only invented practice text, choosing a
new filename if that name exists. Tell the teacher this is a disposable example. Show its
location, make one small change, and show the result. This setup exercise authorises those
edits only; do not use an existing README or teaching resource for the demonstration.

With Steve, show OneDrive version history if it is available and a prior version has synced.
If no prior version is available, report that recovery has not yet been demonstrated; do
not promise that sync immediately provides a restorable version. Restore the practice text
from the known original for the exercise and clearly distinguish that from a OneDrive
restore. Leave the harmless file for the teacher to inspect. Never infer permissions from
whether an approval happened to appear during this example.

## 3. Confirm context

Read `AGENTS.md`, the school context, boundaries and exclusions. Give one specific detail
from `Context/meridan.md` as evidence that you have read it. Say: deidentified student work
without sensitive information is permitted; original writing is preserved and feedback
is saved separately. Local file storage does not mean AI processing is offline.

## 4. Check curriculum capability

The EDU Australian Curriculum plugin is intended to be installed before orientation.
Check whether its tools are actually available and try a small read-only curriculum
lookup relevant to the teacher's subject if known. Report success only from a returned
result. If unavailable or failing, tell Steve and record the limitation.

For curriculum alignment, use official text returned by the tool or supplied by the teacher,
recording its source, curriculum version and code where available. Never invent descriptor
wording or codes. Unrelated work can continue while the plugin is unavailable.

## What to report

Keep it short:

- Installed project path, and permissions verified or still needing Steve's check.
- Practice file location and what recovery was actually demonstrated.
- One school-context detail.
- Curriculum tool result or limitation and the usable fallback.

Record these results and the app version if visible in `Context/setup-state.md`.
Do not claim a version or setting was verified when it was not. At the end of orientation,
show the teacher how to reopen this project and start another task.

## Model

Use the account's available reasoning model for planning and review. Keep the default
unless the task needs a change; teachers do not need to choose a model to get started.

## Reference

Guidance checked against official OpenAI documentation on 7 September 2026; this is a
documentation check, not certification on school-managed devices:

- [Sandbox and approval controls](https://learn.chatgpt.com/docs/agent-approvals-security)
- [How AGENTS.md is discovered](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

Recheck actual behaviour on the school Mac and Windows app versions before rollout.
