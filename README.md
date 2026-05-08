<div align="center">

<img src="assets/logo.png" alt="Lean AI PRD Team" width="100" />

# Lean AI PRD Team Skills

### 🌐 [sky791016.github.io/lean-ai-dev-team](https://sky791016.github.io/lean-ai-dev-team/)

[![Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Works with any IDE](https://img.shields.io/badge/Works_with-Any_IDE-6c63ff)](references/ide-compatibility.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Native-6c63ff)](https://claude.ai/code)
[![Lean AI](https://img.shields.io/badge/Lean_AI_Methodology-精益AI方法论-34d399)](https://sky791016.github.io/lean-ai-dev-team/)

</div>

---

## Three Skills, One Methodology

This repository contains three skills built on the **Lean AI Methodology (精益AI方法论)** by Kai Shi.

| Skill | Tier | Agents | When to use |
|---|---|---|---|
| **`lean-ai-prd-team`** | Standard · Free | 8 | Defined task — feature, fix, or refactor. Scenario-first, minimum MVP, straight to code. |
| **`lean-ai-prd-team-pro`** | Pro · Commercial | 10 | Enterprise delivery. Adds Code Audit, IFPUG FP sizing, ROI Value Assessment. |
| **`lean-ai-agile-agent-team`** | Strategy · Free | 15 | Start from zero. Full lifecycle: goal alignment → MVP → BA → sprint → ops → agent evolution. |

---

## English

---

### Skill 1 · `lean-ai-prd-team` — Standard (Free · 8 Agents)

#### What It Does

A structured prompt system that routes your task through an **8-agent coordinated team** — scenario and value locked in before any code is written, minimum viable MVP delivered, token-efficient structured handoffs.

**Three core advantages:**

> **Scenario-first, value-first** — Business Planner and PM lock in the scenario, ROI, and MVP scope before any developer agent runs.

> **Minimum viable end-to-end loop** — Business case → requirements → architecture → parallel code → 4-loop sign-off. Shippable increment every run.

> **Saves tokens** — Structured phase handoffs replace open-ended chat. One prompt → 8 roles, complete coordinated output.

#### Install

**Claude Code:**
```bash
git clone https://github.com/sky791016/lean-ai-dev-team ~/.claude/skills/lean-ai-prd-team
```

**All other IDEs:**
Copy [`lean-ai-prd-team/SKILL.md`](lean-ai-prd-team/SKILL.md) into your IDE's system prompt / instruction file.

#### Three Scenarios

**1 · Greenfield**
```
/lean-ai-prd-team [全新项目]
Background: Legal team reviews 50+ contracts/day, avg 2 hrs each
Goal: Build a contract risk AI agent — auto-flag high-risk clauses
Constraints: Core ERP (SAP) must not be modified; human final sign-off required
Stack: Python Flask + PostgreSQL + React
```

**2 · Refactor**
```
/lean-ai-prd-team [重构优化]
Current: Order query P99 = 4.2s, 3-year-old code, no test coverage
Goal: P99 under 500ms + AI personalized recommendations
Files: src/order/OrderService.java
Scale: MySQL, 80M rows
```

**3 · Review**
```
/lean-ai-prd-team [项目评审]
AI customer service system launching tomorrow — full review
Focus: Code security · AI hallucination risk · Concurrency · Data privacy
Files: src/chat/ChatController.java, src/ai/LLMService.java
```

#### The 8-Agent Team

```
Phase 1  Business Planner     L1-L5 scenario level · Business case · 3-phase roadmap
Phase 2  Product Manager      ROI model · Scenario card · KPI dashboard · Stop conditions
Phase 3  Business Analyst     Epics · User stories · Acceptance criteria · Human-AI design
Phase 4  Technical Architect  ADRs · API contracts · Clean Core design · Directory conventions

Phase 5  Frontend  ─┐
(parallel) Backend  ─┤  All implement against architect's contracts
         Data       ─┘

Phase 6  Compliance PM        4-loop check · Conflict report · DoD sign-off
```

> 🔼 Need Code Audit, IFPUG FP sizing, or ROI Validation? → use `lean-ai-prd-team-pro`

---

### Skill 2 · `lean-ai-prd-team-pro` — Pro (Commercial · 10 Agents)

#### What It Does

Everything in Standard, plus three Pro-only capabilities for enterprise delivery and value proof:

| Pro-Only | Description |
|---|---|
| **Code Auditor** | OWASP Top 10 scan, N+1 detection, Architecture Health Score /100 |
| **BA FP Sizing** | Full IFPUG analysis — ILF/EIF/EI/EO/EQ coefficients, UFP total |
| **Value Assessor** | 4-dimension benefit system, ROI validation vs. PM model, Realized Value Score /100 |

#### Install

**Claude Code:**
```bash
git clone https://github.com/sky791016/lean-ai-dev-team /tmp/lean-ai
cp -R /tmp/lean-ai/lean-ai-prd-team-pro ~/.claude/skills/
```

**Commercial use requires written authorization — contact: sky.kugua@gmail.com**

#### The 10-Agent Team

```
Phase 0  Code Auditor ★        OWASP security · N+1 detection · Health Score /100
Phase 1  Business Planner      L1-L5 scenario · Business case · 3-phase roadmap
Phase 2  Product Manager       ROI model · Scenario card · KPI dashboard
Phase 3  Business Analyst ★    Epics · Stories · IFPUG FP table (UFP total) · Acceptance criteria
Phase 4  Technical Architect   ADRs · API contracts · Clean Core design

Phase 5  Frontend  ─┐
(parallel) Backend  ─┤  All implement against architect's contracts
         Data       ─┤
         Value ★    ─┘  Assessor: Realized Value Score /100 vs. PM model

Phase 6  Compliance PM         4-loop check · Conflict report · DoD sign-off
```

#### Three Scenarios

```
/lean-ai-prd-team-pro [全新项目] ...
/lean-ai-prd-team-pro [重构优化] ...
/lean-ai-prd-team-pro [项目评审] ...
```

---

### Skill 3 · `lean-ai-agile-agent-team` — Full Lifecycle (Free · 15 Roles)

#### What It Does

A complete **Lean Data + Lean AI + Agile Agent Team** delivery system for projects that need disciplined strategy-to-execution alignment from zero.

```
Strategic Goal Alignment → Divergent Requirements → Convergent Requirements
→ Scenario System → MVP Definition → Metrics System
→ BA Pipeline (Epic / Story / FP / PRD)
→ Lean Data Model → AI Capability Design → Architecture & Tech POC
→ Sprint Delivery → Testing & Release
→ Measurement & Value Review → Operations → Controlled Agent Evolution
```

#### Install

**Claude Code:**
```bash
git clone https://github.com/sky791016/lean-ai-dev-team /tmp/lean-ai
cp -R /tmp/lean-ai/lean-ai-agile-agent-team ~/.claude/skills/
```

#### Common Prompts

```text
Use lean-ai-agile-agent-team. Bootstrap this empty project. Do not code yet.
Use lean-ai-agile-agent-team. Run goal alignment based on input/brief.md.
Use lean-ai-agile-agent-team. Diverge requirements, converge, create scenario canvas, define MVP, create metrics system.
Use lean-ai-agile-agent-team. Run BA pipeline: Epic Breakdown, Story Narrative, Functional Breakdown, PRD, validation system.
Use lean-ai-agile-agent-team. Start Sprint 1. Every task must link to scenario and metric.
Use lean-ai-agile-agent-team. Run value realization review and update operations backlog.
```

---

### Works With Any IDE

| IDE / Tool | How |
|---|---|
| **Claude Code** | Native slash command (`/lean-ai-prd-team` or `/lean-ai-prd-team-pro`) |
| **Cursor** | Paste `SKILL.md` → `.cursorrules` |
| **Windsurf** | Paste `SKILL.md` → `AGENTS.md` |
| **GitHub Copilot** | Paste → `.github/copilot-instructions.md` |
| **JetBrains AI** | Settings → AI → Prompts → new prompt |
| **通义灵码 / CodeBuddy / Comate** | Custom Instructions / System Prompt → paste |
| **Augment / Continue.dev** | Workspace Instructions / `config.json` → paste |
| **Dify / Coze / FastGPT** | System prompt → paste |
| **Pure API** | `system` role → `SKILL.md` content |

Full guide: [`references/ide-compatibility.md`](references/ide-compatibility.md)

---

### Repository Structure

```
lean-ai-dev-team/
├── SKILL.md                          ← lean-ai-prd-team Standard (one-line install)
├── README.md
├── LICENSE
├── references/
│   ├── scenario-examples.md
│   └── ide-compatibility.md
├── docs/                             ← Official website (GitHub Pages)
│   ├── index.html
│   ├── logo.png
│   └── assets/
├── lean-ai-prd-team/                 ← Standard skill (8 agents · free)
│   └── SKILL.md
├── lean-ai-prd-team-pro/             ← Pro skill (10 agents · commercial)
│   └── SKILL.md
└── lean-ai-agile-agent-team/         ← Full lifecycle skill (15 roles · free)
    ├── SKILL.md
    ├── MANIFEST.json
    ├── protocols/
    ├── roles/
    ├── scripts/
    └── templates/
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
@software{lean_ai_prd_team_2026,
  author  = {Kai Shi (史凯)},
  title   = {Lean AI PRD Team Skills},
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
Commercial use (Pro) → sky.kugua@gmail.com

---
---

## 中文说明

---

### 三个 Skill，一套方法论

| Skill | 版本 | 智能体 | 适用场景 |
|---|---|---|---|
| **`lean-ai-prd-team`** | 标准版 · 免费 | 8 | 任务明确（功能开发、重构、评审），场景优先，最小MVP，直接交付代码 |
| **`lean-ai-prd-team-pro`** | 专业版 · 商业授权 | 10 | 企业级交付，含代码审计、IFPUG 功能点估算、ROI 效益评估 |
| **`lean-ai-agile-agent-team`** | 战略版 · 免费 | 15 | 从零开始，完整生命周期：目标对齐 → MVP → BA → Sprint → 运营 → 进化 |

---

### Skill 1 · `lean-ai-prd-team` — 标准版（免费 · 8 智能体）

场景优先，价值优先，最小 MVP，结构化分阶段交接节约 Token。

**安装（Claude Code）：**
```bash
git clone https://github.com/sky791016/lean-ai-dev-team ~/.claude/skills/lean-ai-prd-team
```

**其他 IDE：** 将 [`lean-ai-prd-team/SKILL.md`](lean-ai-prd-team/SKILL.md) 内容粘贴到系统提示词。

**调用方式：**
```
/lean-ai-prd-team [全新项目] 你的任务描述
/lean-ai-prd-team [重构优化] 你的任务描述
/lean-ai-prd-team [项目评审] 你的任务描述
```

---

### Skill 2 · `lean-ai-prd-team-pro` — 专业版（商业授权 · 10 智能体）

在标准版基础上增加三项专业能力：

| 专业能力 | 说明 |
|---|---|
| **代码审计师** | OWASP Top 10 安全扫描、N+1 检测、架构健康评分 /100 |
| **BA 功能点分析** | 完整 IFPUG ILF/EIF/EI/EO/EQ 系数计算，UFP 总量 |
| **效益评估师** | 4 维度效益体系、ROI 验证、Realized Value Score /100 |

商业使用请联系：sky.kugua@gmail.com

---

### Skill 3 · `lean-ai-agile-agent-team` — 完整生命周期（免费 · 15 角色）

精益数据方法论 + 精益 AI + 敏捷智能体团队，让空项目从战略走到运营闭环。

**安装：**
```bash
git clone https://github.com/sky791016/lean-ai-dev-team /tmp/lean-ai
cp -R /tmp/lean-ai/lean-ai-agile-agent-team ~/.claude/skills/
```

---

### 方法论

基于 **精益AI方法论（Lean AI Methodology）**，作者：**史凯（Kai Shi）**

> "AI 转型不是采购大模型，而是以业务场景为核心，对流程、数据、组织、技术、运营进行精益化重构。"

官网：[sky791016.github.io/lean-ai-dev-team](https://sky791016.github.io/lean-ai-dev-team/)

---

### 许可

Copyright © 2026 **Kai Shi (史凯)** · sky.kugua@gmail.com · Founder of Lean AI Method

Apache 2.0 附非商业限制。个人、教育、非商业用途免费。专业版商业用途请联系 sky.kugua@gmail.com
