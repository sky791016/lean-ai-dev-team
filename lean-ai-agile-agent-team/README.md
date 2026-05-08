<!--
Copyright (c) 2026 Kai Shi (史凯)
Email: sky.kugua@gmail.com
Title: Founder of Lean AI Method

Licensed under the Apache License, Version 2.0 with Non-Commercial Restriction.
Free for personal, educational, and non-commercial use.
Commercial use requires written authorization — contact: sky.kugua@gmail.com

SPDX-License-Identifier: Apache-2.0
-->

# Lean AI Agile Agent Team Skill

这是一个面向 Claude Code 和任意 IDE Coding Agent 的完整项目交付 Skill。

它把“精益数据方法论 + 精益 AI 体系 + 敏捷智能体团队”合成一套可执行协议，让空项目也能从战略规划走到开发、测试、评估、运营闭环。

## 目录结构

解压后顶层只有：

```text
lean-ai-agile-agent-team/
  SKILL.md
  README.md
  MANIFEST.json
  roles/
  protocols/
  templates/
  scripts/
```

## 安装

在项目根目录：

```bash
mkdir -p .claude/skills
cp -R /path/to/lean-ai-agile-agent-team .claude/skills/
```

或：

```bash
bash lean-ai-agile-agent-team/scripts/install.sh /path/to/your/project
```

## 初始化空项目

```bash
bash .claude/skills/lean-ai-agile-agent-team/scripts/bootstrap-lean-ai-project.sh
```

会生成：

```text
input/
docs/strategy/
docs/discovery/
docs/scenarios/
docs/metrics/
docs/ba/
docs/architecture/
docs/delivery/
docs/ops/
tasks/
```

## 常用 Prompt

### 从空项目启动

```text
Use lean-ai-agile-agent-team. Bootstrap this empty project and create the full Lean AI delivery structure. Do not code yet.
```

### 目标对齐

```text
Use lean-ai-agile-agent-team. Run goal alignment based on input/brief.md. Output strategy docs. Do not code yet.
```

### 发散、收敛、场景、MVP

```text
Use lean-ai-agile-agent-team. Diverge requirements, converge them, create scenario canvas, prioritize scenarios, define MVP, and create metrics system.
```

### BA 流程

```text
Use lean-ai-agile-agent-team. Run BA pipeline after MVP definition: Epic Breakdown, Story Narrative, Functional Breakdown, PRD, and validation system.
```

### 架构与 AI 设计

```text
Use lean-ai-agile-agent-team. Design Lean Data Model, AI Capability Design, architecture, and tech stack POC for the selected MVP scenario.
```

### Sprint 交付

```text
Use lean-ai-agile-agent-team. Start Sprint 1 for the selected MVP scenario. Every task must link to scenario and metric.
```

### 价值复盘与运营

```text
Use lean-ai-agile-agent-team. Run value realization review and update operations backlog.
```

## 核心原则

```text
目标对齐
发散需求
收敛需求
场景驱动
指标约束
MVP 优先
减少浪费
数据就绪
AI 必要性验证
小步交付
测试度量
运营反馈
持续进化
```
