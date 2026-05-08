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

TARGET="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

mkdir -p "$TARGET/.claude/skills"
rm -rf "$TARGET/.claude/skills/lean-ai-agile-agent-team"
cp -R "$SKILL_DIR" "$TARGET/.claude/skills/lean-ai-agile-agent-team"

echo "Installed: $TARGET/.claude/skills/lean-ai-agile-agent-team"
echo "Next:"
echo "cd $TARGET"
echo "bash .claude/skills/lean-ai-agile-agent-team/scripts/bootstrap-lean-ai-project.sh"
