<div align="center">

<img src="assets/logo.png" alt="Lean AI Dev Team" width="100" />

# Lean AI Agent Team Skills

### 🌐 [sky791016.github.io/lean-ai-dev-team](https://sky791016.github.io/lean-ai-dev-team/)

[![Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Works with any IDE](https://img.shields.io/badge/Works_with-Any_IDE-6c63ff)](references/ide-compatibility.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Native-6c63ff)](https://claude.ai/code)
[![Lean AI](https://img.shields.io/badge/Lean_AI_Methodology-精益AI方法论-34d399)](https://sky791016.github.io/lean-ai-dev-team/)

</div>

---

## Two Skills, One Methodology

This repository contains two complementary skills built on the **Lean AI Methodology (精益AI方法论)** by Kai Shi.

| Skill | What it is | When to use |
|---|---|---|
| **`dev-team`** | 9-agent rapid delivery skill | You have a defined task — feature, refactor, or review. Scenario-first, minimum MVP, straight to code. |
| **`lean-ai-agile-agent-team`** | Full-lifecycle strategy-to-delivery system | You're starting from zero or need to align goal → MVP → BA → architecture → sprint → ops properly. |

---

## English

---

### Skill 1 · `dev-team` — 9-Agent Rapid Delivery

#### What It Does

A structured prompt system that routes your task through a **9-agent coordinated team** — scenario and value locked in before any code is written, minimum viable MVP delivered, token-efficient structured handoffs.

**Three core advantages:**

> **Scenario-first, value-first** — Business Planner and PM lock in the scenario, ROI, and MVP scope before any developer agent runs. No scenarioless code — the #1 AI waste.

> **Minimum viable end-to-end loop** — Business case → requirements → architecture → parallel code → 4-loop sign-off. The team asks "is this MVP necessary?" at every step. Shippable increment every run.

> **Saves tokens** — Structured phase handoffs replace open-ended chat. No iterative clarification loops. One prompt → 9 roles, complete coordinated output.

#### Install

**Claude Code:**
```bash
git clone https://github.com/sky791016/lean-ai-dev-team ~/.claude/skills/dev-team
```

**All other IDEs:**
Copy the contents of [`SKILL.md`](SKILL.md) into your IDE's system prompt / instruction file.

#### Three Scenarios

**1 · Greenfield**
```
[全新项目]
Background: Legal team reviews 50+ contracts/day, avg 2 hrs each
Goal: Build a contract risk AI agent — auto-flag high-risk clauses
Constraints: Core ERP (SAP) must not be modified; human final sign-off required
Stack: Python Flask + PostgreSQL + React
```

**2 · Refactor**
```
[重构优化]
Current: Order query P99 = 4.2s, 3-year-old code, no test coverage
Goal: P99 under 500ms + AI personalized recommendations
Files: src/order/OrderService.java
Scale: MySQL, 80M rows
```

**3 · Review**
```
[项目评审]
AI customer service system launching tomorrow — full review
Focus: Code security · AI hallucination risk · High concurrency · Data privacy
Files: src/chat/ChatController.java, src/ai/LLMService.java
Output: CTO-ready review report
```

#### The 10-Agent Team

```
Phase 0  Code Auditor               [required for refactor/review]
         OWASP security · N+1 detection · Architecture health score

Phase 1  Business Planner           [independent]
         L1-L5 scenario level · Business case · 3-phase roadmap

Phase 2  Product Manager            [independent]
         ROI model · Scenario card · KPI dashboard

Phase 3  Business Analyst           [independent]
         Epics · User stories · IFPUG FP analysis · Acceptance criteria

Phase 4  Technical Architect        [independent]
         ADRs · API contracts · Clean Core design

Phase 5  Frontend  ─┐
(parallel) Backend  ─┤  All implement against architect's contracts
         Data       ─┤
         Value      ─┘  Assessor: quantitative benefit evaluation

Phase 6  Compliance PM
         4-loop check · Conflict report · DoD sign-off
```

---

### Skill 2 · `lean-ai-agile-agent-team` — Full Lifecycle Delivery System

#### What It Does

A complete **Lean Data + Lean AI + Agile Agent Team** delivery system for projects that need disciplined strategy-to-execution alignment.

The full delivery path:

```
Strategic Goal Alignment
→ Divergent Requirements
→ Convergent Requirements
→ Scenario System & Prioritization
→ MVP Definition
→ Metrics System
→ BA Pipeline (Epic / Story / FP / PRD)
→ Lean Data Model
→ AI Capability Design
→ Architecture & Tech POC
→ Sprint Delivery
→ Testing & Release
→ Measurement & Value Review
→ Operations & Continuous Improvement
→ Controlled Agent Evolution
```

#### Install

**Claude Code:**
```bash
git clone https://github.com/sky791016/lean-ai-dev-team /tmp/lean-ai
mkdir -p ~/.claude/skills
cp -R /tmp/lean-ai/lean-ai-agile-agent-team ~/.claude/skills/
```

Or using the bundled script:
```bash
bash lean-ai-agile-agent-team/scripts/install.sh /path/to/your/project
```

#### Bootstrap an Empty Project

```bash
bash .claude/skills/lean-ai-agile-agent-team/scripts/bootstrap-lean-ai-project.sh
```

Generates:
```
input/
docs/strategy/   docs/discovery/   docs/scenarios/   docs/metrics/
docs/ba/         docs/architecture/ docs/delivery/    docs/ops/
tasks/
```

#### Common Prompts

```text
Use lean-ai-agile-agent-team. Bootstrap this empty project. Do not code yet.
```
```text
Use lean-ai-agile-agent-team. Run goal alignment based on input/brief.md.
```
```text
Use lean-ai-agile-agent-team. Diverge requirements, converge them, create scenario canvas, prioritize, define MVP, and create metrics system.
```
```text
Use lean-ai-agile-agent-team. Run BA pipeline: Epic Breakdown, Story Narrative, Functional Breakdown, PRD, validation system.
```
```text
Use lean-ai-agile-agent-team. Design Lean Data Model and AI Capability Design for the selected MVP scenarios.
```
```text
Use lean-ai-agile-agent-team. Start Sprint 1. Every task must link to scenario and metric.
```
```text
Use lean-ai-agile-agent-team. Run value realization review and update operations backlog.
```

#### 15 Agent Roles

| Role | Responsibility |
|---|---|
| Strategy Lead | Goal alignment, value hypothesis, constraints |
| Lean Data Strategist | Scenario-to-data mapping, data quality, governance |
| Lean AI Scenario Designer | AI opportunity identification, necessity test, human-in-loop design |
| Business Analyst | Epic Breakdown, Story Narrative, IFPUG FP, PRD |
| Product Manager | MVP definition, user value, roadmap, adoption |
| Architecture Planner | System boundary, architecture, integration decisions |
| Tech Lead | Tech stack, POC, engineering standards |
| Data Engineer | Master/transaction/event/knowledge data, pipelines |
| AI Engineer | Model / RAG / agent / prompt / evaluation |
| UX Designer | User journey, interface structure, usability |
| Development Engineers | Frontend, backend, integration, infrastructure |
| Test Engineer | Test strategy, UAT, regression, AI quality tests |
| Project Manager | Sprint plan, risk, dependencies, delivery rhythm |
| Operations Manager | Release ops, feedback channel, metric review |
| Agent Evolution Coach | Evidence-based improvement of the agent team |

---

### Works With Any IDE

| IDE / Tool | How |
|---|---|
| **Claude Code** | Native `/dev-team` slash command |
| **Cursor** | Paste `SKILL.md` → `.cursorrules` |
| **Windsurf** | Paste `SKILL.md` → `AGENTS.md` |
| **GitHub Copilot** | Paste → `.github/copilot-instructions.md` |
| **JetBrains AI** | Settings → AI → Prompts → new prompt |
| **通义灵码** | Custom Instructions → paste `SKILL.md` |
| **CodeBuddy** | Instruction library → new → paste `SKILL.md` |
| **百度 Comate** | System prompt → paste `SKILL.md` |
| **Augment Code** | Workspace Instructions |
| **Continue.dev** | `config.json` → `systemMessage` |
| **Dify / Coze / FastGPT** | System prompt → paste `SKILL.md` |
| **Pure API** | `system` role → `SKILL.md` content |

Full setup guide: [`references/ide-compatibility.md`](references/ide-compatibility.md)

---

### Repository Structure

```
lean-ai-dev-team/
├── SKILL.md                          ← dev-team skill (9-agent rapid delivery)
├── README.md
├── LICENSE
├── references/
│   ├── scenario-examples.md
│   └── ide-compatibility.md
├── docs/                             ← Official website source (GitHub Pages)
│   ├── index.html
│   ├── logo.png
│   └── assets/
└── lean-ai-agile-agent-team/         ← Full lifecycle skill
    ├── SKILL.md
    ├── README.md
    ├── MANIFEST.json
    ├── protocols/
    │   └── lean-ai-delivery-protocol.md
    ├── roles/                        ← 15 role definitions
    ├── scripts/
    │   ├── bootstrap-lean-ai-project.sh
    │   ├── install.sh
    │   └── run-lean-ai-quality-check.sh
    └── templates/                    ← 30 document templates (00–30)
        ├── input/
        ├── strategy/
        ├── discovery/
        ├── scenarios/
        ├── metrics/
        ├── ba/
        ├── architecture/
        ├── delivery/
        ├── ops/
        └── tasks/
```

---

### Real Results

| Case | Metric | Result |
|---|---|---|
| Contract Risk AI | Review time | −72% |
| Contract Risk AI | Annual savings | ¥2.4M |
| Customer Complaint AI | Response time | 8min → 90sec |
| Resume Screening AI | Screening time | 45min → 3min |

---

### Citation

```bibtex
@software{lean_ai_dev_team_2026,
  author  = {Kai Shi (史凯)},
  title   = {Lean AI Agent Team Skills},
  year    = {2026},
  url     = {https://github.com/sky791016/lean-ai-dev-team},
  license = {Apache-2.0}
}
```

---

### License

Copyright © 2026 **Kai Shi (史凯)** · sky.kugua@gmail.com · Founder of Lean AI Method

Apache 2.0 with Non-Commercial Restriction.
Free for personal, educational, non-commercial use.
Commercial use → sky.kugua@gmail.com

---
---

## 中文说明

---

### 两个 Skill，一套方法论

本仓库包含两个基于**精益AI方法论**（史凯 Kai Shi 著）的互补 Skill：

| Skill | 定位 | 适用场景 |
|---|---|---|
| **`dev-team`** | 9 智能体快速交付 | 任务已明确（功能开发、重构、评审），场景优先，最小MVP，直接跑到代码 |
| **`lean-ai-agile-agent-team`** | 完整生命周期交付系统 | 从零开始，或需要严格走：目标对齐 → MVP → BA → 架构 → Sprint → 运营 |

---

### Skill 1 · `dev-team` — 9 智能体快速交付

#### 这是什么

一套结构化 Prompt 系统，将你的任务路由给 **9 个协作 AI 智能体**：场景和价值优先锁定，最小 MVP 约束贯穿全程，结构化分阶段交接替代无目的对话，节约 Token。

**三大核心优势：**

> **场景驱动、价值优先** — 业务规划师和产品经理在任何开发智能体运行前先锁定场景、ROI 和 MVP 范围，消除无场景代码这一 AI 开发头号浪费。

> **围绕目标直接交付最小 MVP 的端到端闭环** — 先商业价值，再需求，再架构，再并行编码，最后四闭环签核。

> **大幅节约 Token** — 结构化分阶段交接取代无目的的来回对话。一个结构化 Prompt，10 个角色完整输出。

#### 安装

**Claude Code：**
```bash
git clone https://github.com/sky791016/lean-ai-dev-team ~/.claude/skills/dev-team
```

**其他所有 IDE：**
将 [`SKILL.md`](SKILL.md) 的内容复制到你的 IDE 系统提示词 / 指令文件中。

---

### Skill 2 · `lean-ai-agile-agent-team` — 完整生命周期交付系统

#### 这是什么

一套将"精益数据方法论 + 精益 AI 体系 + 敏捷智能体团队"合成的可执行协议。

让空项目也能从战略规划走到开发、测试、评估、运营闭环：

```
战略目标对齐 → 需求发散 → 需求收敛 → 场景识别 → 指标体系 → MVP 定义
→ BA 业务分析 → 数据模型 → AI 能力设计 → 架构设计 → 技术 POC
→ Sprint 开发 → 测试发布 → 度量评估 → 运营反馈 → Agent 团队进化
```

#### 安装

```bash
git clone https://github.com/sky791016/lean-ai-dev-team /tmp/lean-ai
mkdir -p ~/.claude/skills
cp -R /tmp/lean-ai/lean-ai-agile-agent-team ~/.claude/skills/
```

#### 初始化空项目

```bash
bash .claude/skills/lean-ai-agile-agent-team/scripts/bootstrap-lean-ai-project.sh
```

#### 常用 Prompt

```text
Use lean-ai-agile-agent-team. Bootstrap this empty project. Do not code yet.
```
```text
Use lean-ai-agile-agent-team. Run goal alignment based on input/brief.md.
```
```text
Use lean-ai-agile-agent-team. Diverge requirements, converge them, create scenario canvas, prioritize scenarios, define MVP, and create metrics system.
```
```text
Use lean-ai-agile-agent-team. Run BA pipeline after MVP definition: Epic Breakdown, Story Narrative, Functional Breakdown, PRD, and validation system.
```
```text
Use lean-ai-agile-agent-team. Start Sprint 1 for the selected MVP scenario. Every task must link to scenario and metric.
```
```text
Use lean-ai-agile-agent-team. Run value realization review and update operations backlog.
```

---

### 方法论

基于 **精益AI方法论（Lean AI Methodology）**，作者：**史凯（Kai Shi）**

> "AI 转型不是采购大模型，而是以业务场景为核心，对流程、数据、组织、技术、运营进行精益化重构。"

官网：[sky791016.github.io/lean-ai-dev-team](https://sky791016.github.io/lean-ai-dev-team/)

---

### 许可

Copyright © 2026 **Kai Shi (史凯)** · sky.kugua@gmail.com · Founder of Lean AI Method

Apache 2.0 附非商业限制。个人、教育、非商业用途免费。商业用途请联系 sky.kugua@gmail.com
