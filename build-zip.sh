#!/usr/bin/env bash
# Build the teacher kit from an explicit list of files in a Git commit.
# Usage: ./build-zip.sh [commit-or-tag]  (default: HEAD)
set -euo pipefail
cd "$(dirname "$0")"
REF="${1:-HEAD}"
COMMIT="$(git rev-parse --verify "${REF}^{commit}")"
OUT="../Codex-Teacher-Trial-Kit.zip"
TEMP_ARCHIVE="$(mktemp "${OUT}.tmp.XXXXXX")"
trap 'rm -f "$TEMP_ARCHIVE"' EXIT

# Exact paths only: never archive the working directory or entire context folders.
# git archive records COMMIT in the ZIP comment for provenance.
git archive --format=zip --output="$TEMP_ARCHIVE" "$COMMIT" -- \
  AGENTS.md START-HERE.md \
  Context/meridan.md Context/boundaries.md Context/exclusions.md \
  Context/troubleshooting.md Context/codex-setup.md \
  Routines/onboarding-interview.md Routines/worklog.md Routines/wrap-up.md \
  Logs/README.md 'My Subject/README.md'

# Replace an earlier build only after the complete archive was created.
mv -f "$TEMP_ARCHIVE" "$OUT"
printf 'Built %s from commit %s\n' "$OUT" "$COMMIT"
