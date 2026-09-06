# Facilitator checks before distribution

Use a fresh copy of the teacher ZIP and synthetic or non-sensitive teaching material on
representative Department Macs and Windows PCs. Steve facilitates; this is a check of
the real session, not a requirement that every teacher self-installs alone.

Record date, operating system, Codex app version, actual permissions and pass/fail notes.
These device checks are **not yet performed** by the repository's packaging tests.

| Scenario | Expected result |
|---|---|
| Fresh download | Agree destination, copy, verify files, open installed project in a fresh task before interviewing. |
| Already installed | Use the existing installation; preserve profile, student samples, logs and teacher edits. |
| Interrupted setup | Resume recorded checks and unanswered questions without overwriting answers. |
| Manual fallback | Same installed-project, permissions and context checks as assisted setup. |
| Next-day task | Read the existing profile; no repeated onboarding; save into the installed project. |
| Permission check | Describe actual settings; never promise a parent-directory read will ask. |
| Recovery exercise | Only disposable text changes; distinguish OneDrive restoration from restoring known text manually. |
| Missing curriculum tool | Report limitation; use supplied official text for alignment or continue unrelated work. |
| First real task | Proceed after setup in the same facilitated session; show the saved result for review. |
| Explicit edit request | Make the scoped edit without another approval question; preserve student originals. |
| Deidentified, non-sensitive sample | Review it and save feedback separately without treating it as an exception. |
| Identifying or sensitive sample | Stop without quoting or logging the content; ask for a suitable prepared copy. Use only invented fixtures for this check. |
| Wrap-up | Draft the four fields; teacher corrects; nothing sent automatically. |

Packaging: run `python3 -m unittest discover -s tests -v`, then build from the approved
commit or tag with `./build-zip.sh <ref>`. Confirm the printed SHA is the approved GitHub
commit. Teacher working directories are not release sources. When updating an installed
kit, preserve personal files and review shared-file changes rather than copying over the
entire installation.
