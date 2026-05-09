# Scenario Prompt Examples / 场景提示词示例

Three ready-to-use prompt templates. Copy, fill in `<YOUR_TASK>`, run.

---

## Scenario 1 · Greenfield / 全新项目

Use when: starting from scratch — new feature, new product, new AI system.

**All 9 agents activate.**

```
/dev-team [全新项目]

项目背景：<描述你的业务背景，例如：法务团队每天审查 50+ 份合同>

目标：<你想构建什么，例如：合同风险审查 AI 智能体，自动识别高风险条款>

约束：
- <技术约束，例如：核心 ERP 系统不能修改>
- <流程约束，例如：审查结果需要人工最终确认>

技术栈：<例如：Python Flask + PostgreSQL + React>
```

### Expected Output / 预期输出

| Phase | Agent | Output |
|---|---|---|
| 1 | 业务规划师 | Scenario level (L1–L5), value type, 3-phase roadmap |
| 2 | 产品经理 | ROI model, scenario card, KPI dashboard, stop conditions |
| 3 | 业务分析师 | User stories, Given/When/Then criteria, human-AI split |
| 4 | 技术架构师 | ADRs, API contracts, Clean Core + Cognitive Sidecar design |
| 5 | FE + BE + Data | File change lists, migration SQL, knowledge base schema |
| 6 | 合规PM | 4-loop check, execution checklist, DoD sign-off |

### Real Example Output Excerpt

```markdown
## 精益AI开发团队执行报告

### 一、业务规划
场景级别：L3 流程协同
价值类型：控险 + 增效
利益相关方：法务团队（使用者）/ CFO（受益者）/ 法务总监（决策者）

路线图：
- POC（6周）：单合同类型，人工验收率 > 80%
- MVP（3个月）：覆盖 5 类合同，系统采纳率 > 60%
- 规模复制（Q4）：全部合同类型，集成 ERP 审批流

### 二、产品经理 — ROI 测算
投入：开发 25 人天（¥125,000）+ 月均 Token 成本 ¥3,000
产出：
  节省工时：2h/份 × 50份/天 × 220天 × 0.7（AI覆盖率）= 15,400h/年
  人力单价：¥300/h → 人效收益：¥4,620,000/年
  风险识别率提升 +58% → 合同纠纷损失减少估算 ¥800,000/年
投资回收期：< 2 个月

### 四、技术架构（ADR-001）
决策：使用 Clean Core + Cognitive Sidecar 模式
背景：SAP ERP 不允许修改，AI 风险审查需要外挂
理由：认知侧车模式保持核心系统稳定，AI 层可独立迭代
代价：需要额外的集成层开发（约 3 人天）

API 契约（节选）：
POST /api/contracts/analyze
请求：{ contract_id, content_base64, contract_type }
响应：{ risk_score, risk_clauses: [{clause, risk_level, suggestion}] }
```

---

## Scenario 2 · Refactor / 重构优化

Use when: existing codebase has performance issues, tech debt, or needs AI capability added.

**Code Auditor runs first. Then targeted agents.**

```
/dev-team [重构优化]

当前状况：
- <性能问题，例如：订单查询 P99 延迟 4.2s>
- <技术债，例如：3 年前的代码，缺少测试覆盖>
- <新需求，例如：产品要加入 AI 个性化推荐>

目标：
1. <性能目标，例如：P99 降到 500ms>
2. <新能力目标，例如：接入推荐模型>

关键文件：
<文件路径1>
<文件路径2>

数据规模：<例如：MySQL，8000 万条订单>
```

### Expected Output / 预期输出

```
代码审计师 (Phase 0):
  架构健康度: 61/100
  🔴 必须修复:
    - N+1 查询: OrderMapper.xml L47 (orders.findByUserId 内循环查询 items)
    - 缺少索引: orders.user_id (当前全表扫描 8000万行)
  🟡 建议修复:
    - 3处重复的分页逻辑 (OrderService/UserService/ProductService)
    - LRU缓存 maxSize 配置硬编码，应外部化
  🟢 可以优化:
    - 命名不一致: getUserOrderList vs findOrdersByUser

业务规划师 (Phase 1):
  P99 4.2s → 500ms：用户放弃率预估下降 23%
  转化率提升 +3.2%（基于行业基准）
  推荐功能 CTR 预期 +8.5%（基于协同过滤基线）

技术架构师 (Phase 4):
  ADR-001: 引入 Redis 二级缓存（热点用户订单缓存 TTL 5min）
  ADR-002: 推荐服务独立微服务部署（避免影响核心订单链路）
  索引优化: CREATE INDEX idx_orders_user_id ON orders(user_id, created_at DESC)
```

---

## Scenario 3 · Review / 项目评审

Use when: pre-launch quality gate, security audit, AI compliance check.

**Code Auditor + Architect + Compliance PM. Produces CTO-ready report.**

```
/dev-team [项目评审]

系统名称：<系统名>
上线时间：<例如：明天上线>

评审重点：
1. <例如：代码安全漏洞>
2. <例如：AI 幻觉风险>
3. <例如：高并发稳定性>
4. <例如：数据隐私合规（GDPR / 个人信息保护法）>

关键文件（如已知）：
<文件路径1>
<文件路径2>

特殊要求：<例如：生成可给 CTO 汇报的评审报告>
```

### Expected Output / 预期输出

```
代码审计师 (Phase 0):
  架构健康度: 54/100
  🔴 必须修复（阻断上线）:
    1. SQL注入漏洞: ChatController.java L89
       问题: String query = "SELECT * FROM users WHERE id = " + userId
       修复: PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?")

    2. 会话Token明文存储: UserSessionRepository.java L34
       问题: redis.set("session:" + userId, token)  // 未加密
       修复: redis.set("session:" + userId, AES.encrypt(token, SECRET_KEY))

  🟡 建议修复（上线后处理）:
    3. LLM调用无超时保护: LLMService.java L67
       建议: 设置 timeout=30s，超时返回降级响应

技术架构师 (Phase 4):
  并发评估: 当前架构 QPS 上限约 500，预计峰值 800 → 存在风险
  建议: 在 LLMService 前加队列缓冲，削峰至 300 QPS
  AI幻觉防护: 当前无 Grounding 机制
  建议: 引入知识库检索，LLM 输出标注置信度

合规PM (Phase 6):
  个保法合规检查:
    ❌ 用户对话记录未脱敏即存储（姓名、手机号可见）
    ❌ 未实现数据留存期限（要求 ≤ 2年）
    ✅ 已有用户授权协议

  Go / No-Go 建议: ⚠️ 条件通过
  上线前必须修复: SQL注入、Token明文存储、数据脱敏（3项）
  上线后 2周内修复: LLM超时保护、队列缓冲（2项）
```
