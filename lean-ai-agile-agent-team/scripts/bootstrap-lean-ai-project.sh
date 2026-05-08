#!/usr/bin/env bash

# Copyright (c) 2026 Kai Shi (史凯)
# Email: sky.kugua@gmail.com
# Title: Founder of Lean AI Method
#
# Licensed under the Apache License, Version 2.0 with Non-Commercial Restriction.
# Free for personal, educational, and non-commercial use.
# Commercial use requires written authorization — contact: sky.kugua@gmail.com
#
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

mkdir -p input docs docs/strategy docs/discovery docs/scenarios docs/metrics docs/ba docs/architecture docs/delivery docs/ops tasks

copy_if_missing() {
  local src="$1"
  local dst="$2"
  if [ ! -f "$dst" ]; then
    cp "$src" "$dst"
    echo "Created $dst"
  else
    echo "Skipped existing $dst"
  fi
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TPL="$SKILL_DIR/templates"

for f in "$TPL"/input/*.md; do copy_if_missing "$f" "input/$(basename "$f")"; done
copy_if_missing "$TPL/00-project-memory.md" "docs/00-project-memory.md"

for f in "$TPL"/strategy/*.md; do copy_if_missing "$f" "docs/strategy/$(basename "$f")"; done
for f in "$TPL"/discovery/*.md; do copy_if_missing "$f" "docs/discovery/$(basename "$f")"; done
for f in "$TPL"/scenarios/*.md; do copy_if_missing "$f" "docs/scenarios/$(basename "$f")"; done
for f in "$TPL"/metrics/*.md; do copy_if_missing "$f" "docs/metrics/$(basename "$f")"; done
for f in "$TPL"/ba/*.md; do copy_if_missing "$f" "docs/ba/$(basename "$f")"; done
for f in "$TPL"/architecture/*.md; do copy_if_missing "$f" "docs/architecture/$(basename "$f")"; done
for f in "$TPL"/delivery/*.md; do copy_if_missing "$f" "docs/delivery/$(basename "$f")"; done
for f in "$TPL"/ops/*.md; do copy_if_missing "$f" "docs/ops/$(basename "$f")"; done
for f in "$TPL"/tasks/*.md; do copy_if_missing "$f" "tasks/$(basename "$f")"; done

echo "Lean AI Agile Agent Team project structure initialized."
echo "Next: fill input/brief.md, then ask your agent:"
echo "Use lean-ai-agile-agent-team. Run goal alignment based on input/brief.md. Do not code yet."
