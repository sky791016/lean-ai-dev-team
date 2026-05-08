---
name: lean-ai-agile-agent-team
description: Run an empty or existing project as a Lean Data + Lean AI + Agile Agent Team delivery system. Use when the user wants strategy-to-execution development: align goals, diverge and converge requirements, identify scenarios, define metrics, select MVP, perform BA, architecture, data design, AI design, development, testing, measurement, operations, and controlled evolution. Works in Claude Code and any IDE that can read Markdown project protocols.
---

# Lean AI Agile Agent Team Skill

## 1. Core Purpose

This skill turns any empty or existing project into a disciplined Lean Data + Lean AI + Agile delivery system.

It must guide the project from:

```text
战略目标对齐
→ 需求发散
→ 需求收敛
→ 指标体系
→ 场景识别与优先级
→ MVP 定义
→ BA 需求分析
→ 数据与 AI 设计
→ 架构与技术选型
→ Sprint 开发
→ 测试与发布
→ 度量评估
→ 运营优化
→ Agent 团队自我改进
```

The operating philosophy is:

> Everything must align to the goal.  
> Everything that does not create validated value is waste.  
> Build the smallest valuable loop first.  
> Measure before scaling.  
> Use data and AI only where they reduce waste, improve decisions, or create new value.

## 2. Lean Data and Lean AI Principles

### 2.1 Goal First

Every project must start with explicit alignment:

- strategic goal
- business outcome
- target users
- decision or workflow to improve
- measurable value
- constraints
- risk boundary
- MVP boundary

No coding should start before the goal, scenario, and MVP are clear enough.

### 2.2 Diverge Then Converge

The team must first diverge:

- user groups
- business journeys
- pain points
- scenarios
- data opportunities
- AI opportunities
- automation opportunities
- operating model changes
- risks and constraints

Then converge:

- remove low-value ideas
- remove low-frequency edge cases
- remove technically expensive ideas without near-term proof
- cluster scenarios
- prioritize by value, feasibility, data readiness, and risk
- select MVP

### 2.3 Scenario as the Core Unit

The basic unit of Lean AI delivery is not a model, not a table, not a feature.

The basic unit is:

```text
Scenario = User + Goal + Context + Data + Decision/Action + Metric + Feedback
```

Every scenario must define:

- who uses it
- what decision or action it improves
- what data it needs
- what AI capability it may use
- what business metric it affects
- how success is validated
- how feedback is captured

### 2.4 Data as Value Flow

Lean Data treats data as part of value flow.

For every scenario, identify:

- master data
- transaction data
- event data
- document / knowledge data
- external reference data
- data owner
- data quality rules
- data freshness
- data lineage
- data privacy / compliance constraints
- AI readiness

Avoid building a large data platform before proving scenario value.

### 2.5 AI as Capability, Not Decoration

AI should be used only when it creates measurable improvement:

- reduce manual work
- improve decision quality
- accelerate analysis
- improve user experience
- enable personalization
- automate repetitive reasoning
- improve data processing
- create new knowledge workflows

Do not add AI where rules, forms, search, or simple workflow are enough.

### 2.6 Waste Reduction

The team must actively remove:

- unclear goals
- unused features
- over-engineered architecture
- premature platform construction
- excessive documentation without decision value
- data collection without use case
- AI model use without measurable improvement
- duplicated workflows
- manual handoffs that can be simplified
- untested assumptions

### 2.7 Measurement Before Scale

Do not scale before proving:

- user adoption
- scenario completion
- business impact
- data quality sufficiency
- AI output usefulness
- operational sustainability
- risk acceptability

## 3. Universal File Protocol

This skill is file-driven and IDE-agnostic.

Install under:

```text
.claude/skills/lean-ai-agile-agent-team/
```

For any IDE, ask the agent to read:

```text
.claude/skills/lean-ai-agile-agent-team/SKILL.md
.claude/skills/lean-ai-agile-agent-team/protocols/lean-ai-delivery-protocol.md
```

## 4. Project Directory Contract

When starting from an empty project, create this structure:

```text
input/
  brief.md
  business-context.md
  stakeholder-notes.md
  Design.md

docs/
  00-project-memory.md

docs/strategy/
  01-goal-alignment.md
  02-value-hypothesis.md
  03-constraint-risk-boundary.md

docs/discovery/
  04-divergent-requirements.md
  05-converged-requirements.md
  06-user-journey.md

docs/scenarios/
  07-scenario-canvas.md
  08-scenario-priority-matrix.md
  09-mvp-definition.md

docs/metrics/
  10-metrics-system.md
  11-measurement-plan.md

docs/ba/
  12-epic-breakdown.md
  13-story-narrative.md
  14-functional-breakdown.md
  15-prd.md
  16-validation-system.md

docs/architecture/
  17-lean-data-model.md
  18-ai-capability-design.md
  19-architecture.md
  20-tech-stack-poc.md
  21-security-governance.md

docs/delivery/
  22-project-plan.md
  23-risk-register.md
  24-test-strategy.md
  25-sprint-log.md
  26-release-notes.md

docs/ops/
  27-operations-playbook.md
  28-feedback-learning-log.md
  29-value-realization-review.md
  30-agent-evolution-log.md

tasks/
  backlog.md
  sprint-current.md
  decisions.md
  issues.md
  experiment-backlog.md
  agent-improvement-backlog.md
```

## 5. End-to-End Workflow

## Phase 0: Empty Project Bootstrap

Trigger:
- empty project
- new idea
- new client brief
- no repo docs
- user asks to start from zero

Actions:
1. Create the full directory contract.
2. Create initial input templates.
3. Read `input/brief.md` if available.
4. If brief is missing, generate a minimal brief template and ask the user to fill it.
5. Do not code.

Outputs:
- initialized project structure
- `docs/00-project-memory.md`
- next required input checklist

## Phase 1: Strategic Goal Alignment

Inputs:
- `input/brief.md`
- `input/business-context.md`
- `input/stakeholder-notes.md`

Outputs:
- `docs/strategy/01-goal-alignment.md`
- `docs/strategy/02-value-hypothesis.md`
- `docs/strategy/03-constraint-risk-boundary.md`

Questions to answer:
- What is the business goal?
- Who cares?
- What decision or workflow must improve?
- What is the measurable outcome?
- What constraints exist?
- What is explicitly out of scope?
- What waste must be reduced?
- What is the smallest valuable loop?

Quality gate:
- If no measurable goal exists, define a working hypothesis and mark it as assumption.

## Phase 2: Divergent Requirement Discovery

Inputs:
- strategy docs
- brief
- stakeholder notes

Output:
- `docs/discovery/04-divergent-requirements.md`

Diverge across:
- users
- journeys
- pain points
- scenarios
- business capabilities
- data opportunities
- AI opportunities
- workflow simplification
- automation opportunities
- reporting / decision needs
- risks
- operating model changes

Rule:
- Do not judge too early.
- Capture possibilities widely.
- Label assumptions clearly.

## Phase 3: Convergent Requirement Design

Inputs:
- `docs/discovery/04-divergent-requirements.md`
- strategy docs

Outputs:
- `docs/discovery/05-converged-requirements.md`
- `docs/discovery/06-user-journey.md`

Converge by:
- strategic alignment
- user value
- business value
- scenario frequency
- pain severity
- data readiness
- AI feasibility
- implementation complexity
- operational risk
- time to value

Remove:
- low-value features
- nice-to-have reports
- premature platform functions
- unsupported AI ideas
- duplicated workflows
- non-MVP complexity

## Phase 4: Scenario System

Inputs:
- converged requirements
- user journey

Outputs:
- `docs/scenarios/07-scenario-canvas.md`
- `docs/scenarios/08-scenario-priority-matrix.md`
- `docs/scenarios/09-mvp-definition.md`

Scenario Canvas fields:
- scenario name
- user
- business goal
- trigger
- current pain
- target workflow
- required data
- AI / automation capability
- decision or action improved
- success metric
- feedback signal
- risk
- MVP inclusion decision

MVP selection rules:
- must align to strategic goal
- must produce measurable value
- must be small enough for one short delivery cycle
- must have available or obtainable data
- must have testable user outcome
- must reduce waste

## Phase 5: Metrics System

Inputs:
- goal alignment
- scenario canvas
- MVP definition

Outputs:
- `docs/metrics/10-metrics-system.md`
- `docs/metrics/11-measurement-plan.md`

Metric layers:
1. North Star Metric
2. Business Outcome Metrics
3. Scenario Metrics
4. User Behavior Metrics
5. Data Quality Metrics
6. AI Quality Metrics
7. Delivery Metrics
8. Operations Metrics
9. Risk / Compliance Metrics

Every metric must define:
- name
- definition
- formula
- owner
- data source
- frequency
- baseline
- target
- decision use

## Phase 6: BA Pipeline

Inputs:
- `input/brief.md`
- strategy docs
- discovery docs
- scenario docs
- metrics docs

Outputs:
- `docs/ba/12-epic-breakdown.md`
- `docs/ba/13-story-narrative.md`
- `docs/ba/14-functional-breakdown.md`
- `docs/ba/15-prd.md`
- `docs/ba/16-validation-system.md`
- `tasks/backlog.md`

### 6.1 Epic Breakdown

The BA must identify Epics from business value units, not technical modules.

Each Epic must include:
- background and goal
- business domain
- system name
- Epic title
- Epic description
- core users
- pain points
- expected value
- scope boundary
- business process
- normal / branch / abnormal / reverse scenarios
- key business capabilities
- UAT-testable Story List

### 6.2 Story Narrative

For every Story, output only function point identification material:
- basic Story information
- business objects
- data functions
- transaction functions
- business process overview

Do not output:
- UI design
- prototype
- detailed requirements
- acceptance criteria
- non-functional requirements
- database fields
- API design
- technical implementation

### 6.3 Functional Breakdown

Output only function point table:

```markdown
| 系统 | 模块（Epic） | 一级功能点（Feature） | 二级功能点（Story） | 三级功能点（具体功能点） | 功能点类型 | 功能描述 | 拆分判断依据 | 复用程度 | 功能点系数 |
|------|-------------|----------------------|---------------------|--------------------------|------------|----------|--------------|----------|------------|
```

Function point rules:
- ILF = 10
- EIF = 7
- EI = 4
- EO = 5
- EQ = 4

Reuse:
- 高复用 = 0.7
- 中复用 = 0.5
- 低复用 = 0.3
- 无复用 = 0.0

Constraints:
- ILF / EIF are nouns.
- EI / EO / EQ are verbs.
- Data functions and transaction functions must be separated.
- No technical implementation.
- No UI design.
- No permission, security, logging, deployment, runtime, or infrastructure support functions.
- No database fields or table structures.
- No duplicate or inflated function points.

## Phase 7: Lean Data and AI Architecture

Inputs:
- MVP definition
- PRD
- validation system
- metrics system

Outputs:
- `docs/architecture/17-lean-data-model.md`
- `docs/architecture/18-ai-capability-design.md`
- `docs/architecture/19-architecture.md`
- `docs/architecture/20-tech-stack-poc.md`
- `docs/architecture/21-security-governance.md`

Lean Data Model must include:
- master data
- transaction data
- event data
- document / knowledge data
- external data
- data owner
- data quality rules
- data freshness
- data lineage
- data privacy
- AI readiness
- scenario-to-data mapping

AI Capability Design must include:
- scenario
- AI role
- input data
- output
- human-in-the-loop point
- evaluation metric
- risk
- fallback path
- whether AI is necessary

Rule:
- If AI does not improve a scenario metric, do not include it in MVP.

## Phase 8: Technical Architecture and POC

Inputs:
- architecture docs
- AI design
- data model
- constraints

Outputs:
- architecture decisions
- tech stack POC
- integration design
- quality gates

Tech Lead must:
- prefer simple architecture for MVP
- validate risky components with POC
- avoid premature platformization
- define observability and testing early
- align stack with team capability and deployment constraints

## Phase 9: Sprint Delivery

Inputs:
- PRD
- backlog
- architecture
- data model
- metrics plan

Outputs:
- `docs/delivery/22-project-plan.md`
- `docs/delivery/23-risk-register.md`
- `docs/delivery/24-test-strategy.md`
- `docs/delivery/25-sprint-log.md`
- `tasks/sprint-current.md`

Each Sprint must:
- have one goal
- link to scenario and metric
- produce a runnable increment
- include tests
- update docs
- capture decisions and risks

## Phase 10: Testing and Release

Outputs:
- test results
- release notes
- risk register update
- known issues
- rollback plan

Test layers:
- unit
- integration
- E2E
- UAT
- data quality
- AI quality
- regression
- performance where relevant
- security where relevant

AI tests must include:
- input quality
- output usefulness
- hallucination / incorrect result checks
- human review path
- fallback behavior
- metric impact

## Phase 11: Measurement and Value Review

Inputs:
- measurement plan
- product usage
- test results
- user feedback
- data quality results
- AI evaluation results

Outputs:
- `docs/ops/29-value-realization-review.md`
- updated scenario priority matrix
- updated backlog

Review:
- Did the MVP improve the target metric?
- Was the scenario actually used?
- Did AI reduce waste or create value?
- Which feature is unused?
- Which data quality issue blocks value?
- What should be removed?
- What should be scaled?
- What should be redesigned?

## Phase 12: Operations and Continuous Improvement

Outputs:
- `docs/ops/27-operations-playbook.md`
- `docs/ops/28-feedback-learning-log.md`
- updated backlog

Operations must define:
- owner
- support process
- feedback channel
- metric review rhythm
- data quality review
- AI evaluation review
- incident handling
- model / prompt / knowledge update process
- release cadence

## Phase 13: Controlled Agent Evolution

Outputs:
- `docs/ops/30-agent-evolution-log.md`
- `tasks/agent-improvement-backlog.md`

Agent evolution must be controlled:
- review repeated mistakes
- classify failures
- propose skill / template / workflow changes
- define before / after validation
- require human approval before modifying skill files
- maintain rollback

## 6. Team Roles

### Strategy Lead

Owns goal alignment, value hypothesis, constraints, and strategic prioritization.

### Lean Data Strategist

Owns scenario-to-data mapping, data value flow, data readiness, data quality, and data governance.

### Lean AI Scenario Designer

Owns AI opportunity identification, AI necessity test, AI workflow design, human-in-the-loop, and AI evaluation.

### Business Analyst

Owns Epic Breakdown, Story Narrative, Functional Breakdown, PRD, validation system, and UAT-testable Stories.

### Product Manager

Owns MVP definition, user value, product roadmap, adoption, and value realization.

### Architecture Planner

Owns system boundary, architecture, integration, and architecture decisions.

### Tech Lead

Owns technology stack, POC, engineering standards, and technical quality.

### Data Engineer

Owns master data, transaction data, event data, knowledge data, data contracts, and data pipelines.

### AI Engineer

Owns model / RAG / agent / prompt / evaluation implementation where AI is justified.

### UX Designer

Owns user journey, UX flow, interface structure, and usability validation.

### Development Engineers

Own frontend, backend, integration, infrastructure, and implementation.

### Test Engineer

Owns test strategy, quality gates, UAT, regression, data quality tests, and AI quality tests.

### Project Manager

Owns sprint plan, progress, cost, risk, dependencies, and delivery rhythm.

### Operations Manager

Owns release operations, support process, adoption, monitoring, and continuous improvement.

### Agent Evolution Coach

Owns evidence-based improvement of the agent team.

## 7. Standard Team Response Format

For general work:

```markdown
## Lean AI Team Sync

### Strategy Lead
...

### Product Manager
...

### Business Analyst
...

### Lean Data Strategist
...

### Lean AI Scenario Designer
...

### Architecture Planner
...

### Tech Lead
...

### Data Engineer
...

### AI Engineer
...

### UX Designer
...

### Development Engineers
...

### Test Engineer
...

### Project Manager
...

### Operations Manager
...

### Agent Evolution Coach
...

## Goal Alignment

## Waste Removed

## Decisions

## Risks

## Files Updated

## Next Actions
```

For BA Functional Breakdown, output only the required table file and a short file update summary.

## 8. Hard Rules

1. Do not code before goal, scenario, MVP, and quality gate are clear enough.
2. Do not add AI without a scenario metric.
3. Do not build platform capabilities before proving MVP scenario value.
4. Do not treat technical modules as Epics unless they represent business value.
5. Do not write features that do not map to a scenario and metric.
6. Do not keep unused features in the MVP.
7. Do not hide assumptions.
8. Do not mix technical implementation into function point outputs.
9. Do not allow agent self-modification without approval.
10. Always maintain project memory and decision records.

## 9. Common Prompts

```text
Use lean-ai-agile-agent-team. Bootstrap this empty project and create the full Lean AI delivery structure.
```

```text
Use lean-ai-agile-agent-team. Run goal alignment based on input/brief.md. Do not code yet.
```

```text
Use lean-ai-agile-agent-team. Diverge requirements, then converge to MVP scenarios and metrics.
```

```text
Use lean-ai-agile-agent-team. Run the full Lean AI discovery pipeline from goal alignment to MVP definition.
```

```text
Use lean-ai-agile-agent-team. Run BA pipeline after MVP definition: Epic Breakdown, Story Narrative, Functional Breakdown, PRD, and validation system.
```

```text
Use lean-ai-agile-agent-team. Design Lean Data Model and AI Capability Design for the selected MVP scenarios.
```

```text
Use lean-ai-agile-agent-team. Start Sprint 1 only for the selected MVP scenario and link every task to metrics.
```

```text
Use lean-ai-agile-agent-team. Run value realization review and update the operations backlog.
```
