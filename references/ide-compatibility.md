# IDE Compatibility Guide / 多 IDE 使用手册

Lean AI Dev Team Skill 本质是一套结构化 Prompt 系统，与任何支持系统提示词或上下文注入的 AI 编程工具兼容。

---

## Claude Code（原生支持）

```bash
git clone https://github.com/sky791016/lean-ai-dev-team ~/.claude/skills/dev-team
```

```
/dev-team [全新项目] 你的任务
/dev-team [重构优化] 你的任务
/dev-team [项目评审] 你的任务
```

---

## Cursor

1. 项目根目录创建 `.cursorrules`，粘贴 `SKILL.md` 全文
2. 对话框输入任务加场景前缀

---

## Windsurf

1. 项目根目录创建 `AGENTS.md`，粘贴 `SKILL.md` 全文
2. 对话框输入任务加场景前缀

---

## GitHub Copilot (VS Code)

1. 创建 `.github/copilot-instructions.md`，粘贴 `SKILL.md` 全文
2. Copilot Chat 输入 `@workspace [全新项目] 你的任务`

---

## JetBrains AI Assistant

1. Settings → Tools → AI Assistant → Prompts → 新建 `dev-team`
2. 粘贴 `SKILL.md` 全文
3. AI Chat 选择该 Prompt 后输入任务

---

## 通义灵码 / Tongyi Lingma（阿里云）

1. 对话框 → 自定义指令 → 新建，粘贴 `SKILL.md` 全文
2. 选择指令后输入任务

---

## CodeBuddy（腾讯云）

1. 指令库 → 新建，粘贴 `SKILL.md` 全文
2. 输入 `/dev-team` 触发，加任务描述

---

## 百度 Comate

1. 设置 → 系统提示词，粘贴 `SKILL.md` 全文
2. 对话框输入任务加场景前缀

---

## Augment Code

1. Instructions → Add Workspace Instructions
2. 粘贴 `SKILL.md` 全文

---

## Continue.dev

在 `~/.continue/config.json`:
```json
{ "systemMessage": "<SKILL.md 全文>" }
```

---

## 纯 API / Dify / Coze / FastGPT

将 `SKILL.md` 作为 `system` 角色消息或系统提示词，用户消息加场景前缀即可。

```python
# Python 示例
with open('SKILL.md') as f:
    skill = f.read()

response = client.chat.completions.create(
    model="your-model",
    messages=[
        {"role": "system", "content": skill},
        {"role": "user", "content": "[全新项目] 你的任务描述"}
    ]
)
```

---

## 通用场景前缀

| 场景 | 前缀 | 适用 |
|---|---|---|
| 全新项目 | `[全新项目]` | 新功能、新产品 |
| 重构优化 | `[重构优化]` | 性能问题、技术债 |
| 项目评审 | `[项目评审]` | 上线前评审、安全审查 |

详见 [`scenario-examples.md`](scenario-examples.md)。
