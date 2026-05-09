<div align="center">

<img src="docs/assets/logo.png" alt="Lean AI PRD Team" width="100" />

# Lean AI PRD Team

### 🌐 [sky791016.github.io/lean-ai-dev-team](https://sky791016.github.io/lean-ai-dev-team/)

[![Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Works with any IDE](https://img.shields.io/badge/Works_with-Any_IDE-6c63ff)](references/ide-compatibility.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Native-6c63ff)](https://claude.ai/code)
[![Lean AI](https://img.shields.io/badge/Lean_AI_Methodology-精益AI方法论-34d399)](https://sky791016.github.io/lean-ai-dev-team/)

</div>

---

## Standard vs. Pro

| | `lean-ai-prd-team` · Standard | `lean-ai-prd-team-pro` · Pro |
|---|---|---|
| **Price** | Free | Commercial authorization required |
| **Agents** | 8 | 10 |
| **Scenarios** | Greenfield / Refactor / Review | Greenfield / Refactor / Review |
| Business Planner → PM → BA | ✅ | ✅ |
| Technical Architect | ✅ | ✅ |
| Frontend + Backend + Data | ✅ | ✅ |
| Compliance PM (4-loop) | ✅ | ✅ |
| **Code Auditor** (OWASP + Health Score /100) | ❌ | ✅ |
| **BA FP Sizing** (IFPUG UFP) | ❌ | ✅ |
| **Value Assessor** (Realized Value Score /100) | ❌ | ✅ |

---

## English

---

### Install Standard (Free)

```bash
git clone https://github.com/sky791016/lean-ai-dev-team ~/.claude/skills/lean-ai-prd-team
```

Then in Claude Code:
```
/lean-ai-prd-team [全新项目] your task
/lean-ai-prd-team [重构优化] your task
/lean-ai-prd-team [项目评审] your task
```

**Other IDEs:** Copy [`lean-ai-prd-team/SKILL.md`](lean-ai-prd-team/SKILL.md) into your system prompt / instruction file.

---

### Install Pro (Commercial)

```bash
git clone https://github.com/sky791016/lean-ai-dev-team /tmp/lean-ai
cp -R /tmp/lean-ai/lean-ai-prd-team-pro ~/.claude/skills/
```

Then:
```
/lean-ai-prd-team-pro [全新项目] your task
/lean-ai-prd-team-pro [重构优化] your task
/lean-ai-prd-team-pro [项目评审] your task
```

**Commercial use requires written authorization — contact: sky.kugua@gmail.com**

---

### The 8-Agent Team (Standard)

```
Phase 1  Business Planner     L1-L5 scenario · Business case · 3-phase roadmap
Phase 2  Product Manager      ROI model · Scenario card · KPI dashboard
Phase 3  Business Analyst     Epics · User stories · Acceptance criteria · Human-AI design
Phase 4  Technical Architect  ADRs · API contracts · Clean Core design

Phase 5  Frontend  ─┐
(parallel) Backend  ─┤  Implement against architect's contracts
         Data       ─┘

Phase 6  Compliance PM        4-loop check · Conflict report · DoD sign-off
```

### The 10-Agent Team (Pro)

```
Phase 0  Code Auditor ★       OWASP Top 10 · N+1 detection · Health Score /100
Phase 1  Business Planner
Phase 2  Product Manager
Phase 3  Business Analyst ★   + IFPUG FP table (UFP total)
Phase 4  Technical Architect

Phase 5  Frontend  ─┐
(parallel) Backend  ─┤
         Data       ─┤
         Value ★    ─┘  Assessor: 4-dimension benefit · Realized Value Score /100

Phase 6  Compliance PM
```

---

### Example Prompts

**Greenfield:**
```
/lean-ai-prd-team-pro [全新项目]

Background: Legal team reviews 50+ supplier contracts/day, avg 2 hours each.
Goal: AI agent to auto-flag high-risk clauses and suggest revisions.
Constraints: Core ERP (SAP) cannot be modified. Chinese contracts. Human sign-off required.
Stack: Python Flask + PostgreSQL + React
```

**Refactor:**
```
/lean-ai-prd-team-pro [重构优化]

Current: Order query P99 = 4.2s, no test coverage, 3-year-old code.
Goal: P99 < 500ms + AI personalized recommendations.
Files: src/order/OrderService.java
DB: MySQL, 80M rows
```

**Review:**
```
/lean-ai-prd-team-pro [项目评审]

AI customer service system launching tomorrow.
Focus: Security vulnerabilities · AI hallucination risk · Concurrency · Data privacy
Files: src/chat/ChatController.java, src/ai/LLMService.java
Output: CTO-ready report
```

---

### Works With Any IDE

| IDE | How |
|---|---|
| **Claude Code** | Native `/lean-ai-prd-team` or `/lean-ai-prd-team-pro` |
| **Cursor** | Paste `SKILL.md` → `.cursorrules` |
| **Windsurf** | Paste `SKILL.md` → `AGENTS.md` |
| **GitHub Copilot** | Paste → `.github/copilot-instructions.md` |
| **JetBrains AI** | Settings → AI → Prompts → paste |
| **通义灵码 / CodeBuddy / Comate** | System Prompt → paste |
| **Pure API** | `system` role → `SKILL.md` content |

---

### Repository Structure

```
lean-ai-dev-team/
├── SKILL.md                    ← Standard skill (root, for one-line install)
├── README.md
├── LICENSE
├── lean-ai-prd-team/           ← Standard (8 agents · free)
│   └── SKILL.md
├── lean-ai-prd-team-pro/       ← Pro (10 agents · commercial)
│   └── SKILL.md
├── docs/                       ← Website (GitHub Pages)
└── references/
```

---

### License

Copyright © 2026 **Kai Shi (史凯)** · sky.kugua@gmail.com · Founder of Lean AI Method

Apache 2.0 with Non-Commercial Restriction.
Free for personal, educational, non-commercial use.
Commercial use → sky.kugua@gmail.com

---

## 中文说明

### 标准版 vs 专业版

**标准版（免费）** — 8 个智能体，覆盖全新项目、重构优化、项目评审三种场景。

**专业版（商业授权）** — 在标准版基础上增加：
- **代码审计师** — OWASP Top 10 安全扫描 + 架构健康评分 /100
- **BA 功能点分析** — 完整 IFPUG ILF/EIF/EI/EO/EQ，输出 UFP 总量
- **效益评估师** — 4 维度效益体系，Realized Value Score /100，对比 PM 原始 ROI 模型

### 安装标准版

```bash
git clone https://github.com/sky791016/lean-ai-dev-team ~/.claude/skills/lean-ai-prd-team
```

### 安装专业版

```bash
git clone https://github.com/sky791016/lean-ai-dev-team /tmp/lean-ai
cp -R /tmp/lean-ai/lean-ai-prd-team-pro ~/.claude/skills/
```

商业使用请联系：sky.kugua@gmail.com

---

### 方法论

基于 **精益AI方法论（Lean AI Methodology）**，作者：**史凯（Kai Shi）**

> "AI 转型不是采购大模型，而是以业务场景为核心，对流程、数据、组织、技术、运营进行精益化重构。"

官网：[sky791016.github.io/lean-ai-dev-team](https://sky791016.github.io/lean-ai-dev-team/)

Copyright © 2026 **Kai Shi (史凯)** · sky.kugua@gmail.com
Apache 2.0 附非商业限制。专业版商业使用请联系 sky.kugua@gmail.com
