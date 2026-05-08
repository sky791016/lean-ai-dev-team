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

echo "Checking Lean AI Agile project structure..."

required=(
  "docs/strategy/01-goal-alignment.md"
  "docs/discovery/04-divergent-requirements.md"
  "docs/discovery/05-converged-requirements.md"
  "docs/scenarios/07-scenario-canvas.md"
  "docs/scenarios/09-mvp-definition.md"
  "docs/metrics/10-metrics-system.md"
  "docs/ba/12-epic-breakdown.md"
  "docs/architecture/17-lean-data-model.md"
  "docs/architecture/18-ai-capability-design.md"
  "docs/delivery/24-test-strategy.md"
  "docs/ops/29-value-realization-review.md"
)

for f in "${required[@]}"; do
  if [ ! -f "$f" ]; then
    echo "Missing: $f"
    exit 1
  fi
done

grep -q "| 系统 | 模块（Epic） | 一级功能点（Feature） | 二级功能点（Story） | 三级功能点（具体功能点） | 功能点类型 | 功能描述 | 拆分判断依据 | 复用程度 | 功能点系数 |" docs/ba/14-functional-breakdown.md || {
  echo "Functional Breakdown table header is not compliant."
  exit 1
}

echo "Lean AI Agile project structure looks compliant."
