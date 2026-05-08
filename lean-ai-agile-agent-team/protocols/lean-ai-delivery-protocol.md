<!--
Copyright (c) 2026 Kai Shi (史凯)
Email: sky.kugua@gmail.com
Title: Founder of Lean AI Method

Licensed under the Apache License, Version 2.0 with Non-Commercial Restriction.
Free for personal, educational, and non-commercial use.
Commercial use requires written authorization — contact: sky.kugua@gmail.com

SPDX-License-Identifier: Apache-2.0
-->

# Lean AI Delivery Protocol

This protocol allows any IDE or coding agent to run the project using the Lean AI Agile Agent Team method.

## Required Reading

The agent must read:

```text
.claude/skills/lean-ai-agile-agent-team/SKILL.md
.claude/skills/lean-ai-agile-agent-team/protocols/lean-ai-delivery-protocol.md
```

## Required Project Flow

1. Bootstrap project structure.
2. Align strategic goal.
3. Diverge requirements.
4. Converge requirements.
5. Build scenario canvas.
6. Prioritize scenarios.
7. Define MVP.
8. Define metrics.
9. Run BA pipeline.
10. Design Lean Data and AI architecture.
11. Run technical POC.
12. Plan sprint.
13. Implement small vertical slice.
14. Test.
15. Release.
16. Measure value.
17. Operate and improve.
18. Run controlled agent evolution.

## Core File Contract

Inputs:
- `input/brief.md`
- `input/business-context.md`
- `input/stakeholder-notes.md`
- `input/Design.md`

Primary outputs:
- `docs/strategy/`
- `docs/discovery/`
- `docs/scenarios/`
- `docs/metrics/`
- `docs/ba/`
- `docs/architecture/`
- `docs/delivery/`
- `docs/ops/`
- `tasks/`

## Core Rule

No implementation should begin until:

- goal is clear
- scenario is clear
- MVP is clear
- metric is clear
- acceptance / validation path is clear
- architecture risk is acceptable

## Lean AI Scenario Rule

Every feature must map to:

```text
Goal → Scenario → User → Data → Decision/Action → Metric → Feedback
```

If it cannot be mapped, remove it from MVP or move it to later backlog.

## Waste Reduction Rule

Before adding any feature, ask:

1. Does it support the strategic goal?
2. Does it belong to a selected scenario?
3. Does it improve a metric?
4. Is it required for MVP?
5. Can the same value be achieved with a simpler workflow?
6. Is AI actually necessary?

If the answer is no, defer or remove it.

## MVP Rule

The MVP must be the smallest loop that can prove value:

```text
User trigger → Required data → Action / decision → System or AI support → Output → User feedback → Metric review
```

## Metrics Rule

Every metric must define:

- name
- definition
- formula
- owner
- data source
- baseline
- target
- review frequency
- decision use

## AI Necessity Rule

AI is included only when it measurably improves:

- manual effort
- decision quality
- analysis speed
- personalization
- data processing
- knowledge retrieval
- workflow completion
- user experience

If rules, search, forms, or simple automation are enough, do not add AI to MVP.

## Operations Rule

After release, the team must review:

- adoption
- scenario completion
- business metric movement
- data quality
- AI quality
- user feedback
- incidents
- waste removed
- backlog changes
