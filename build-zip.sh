#!/usr/bin/env bash
# Build the ZIP teachers receive.
#
# The repo root doubles as the kit, so this strips the things that are for us,
# not for them: git metadata, the repo README, and docs/.
# Output: ../Codex-Teacher-Trial-Kit.zip
set -euo pipefail
cd "$(dirname "$0")"

OUT="../Codex-Teacher-Trial-Kit.zip"
rm -f "$OUT"

zip -r -q "$OUT" . \
  -x '.git/*' '.git' \
  -x '.gitignore' \
  -x 'README.md' \
  -x 'docs/*' \
  -x 'build-zip.sh' \
  -x '.DS_Store' '*/.DS_Store' \
  -x 'Logs/*' -x 'My Subject/*' \
  -x 'my-profile.md' -x 'escalation-*.md'

# Logs/ and My Subject/ must still exist for the teacher, just empty.
zip -q "$OUT" 'Logs/README.md' 'My Subject/README.md'

echo "Built $OUT"
unzip -l "$OUT" | tail -n +4 | head -20
