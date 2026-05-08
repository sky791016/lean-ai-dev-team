#!/usr/bin/env bash
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
