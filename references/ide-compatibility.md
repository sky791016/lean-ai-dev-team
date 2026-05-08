# IDE Compatibility Guide / 多 IDE 适配指南

## Claude Code（官方，推荐）

```bash
git clone https://github.com/sky791016/lean-ai-dev-team ~/.claude/skills/dev-team
```

在项目中：
```
/dev-team [全新项目] 你的任务描述
/dev-team [重构优化] 你的任务描述
/dev-team [项目评审] 你的任务描述
```

---

## Cursor / Windsurf

1. 把 `SKILL.md` 内容复制到项目根目录的 `.cursorrules`（Cursor）或 `AGENTS.md`（Windsurf/Codex）
2. 在对话框直接描述任务，前缀：
   - `[全新项目]`
   - `[重构优化]`  
   - `[项目评审]`

---

## 通义灵码 / Tongyi Lingma（阿里云）

1. 打开通义灵码插件对话框
2. 点击「添加上下文」→「自定义指令」
3. 粘贴 `SKILL.md` 全文作为系统指令
4. 在对话框输入任务，加前缀 `[全新项目]` / `[重构优化]` / `[项目评审]`

---

## CodeBuddy（腾讯云）

1. 在 CodeBuddy 对话框点击「指令」→「新建指令」
2. 名称：`dev-team`
3. 内容：粘贴 `SKILL.md` 中对应场景的 Prompt 模板
4. 使用时：输入 `/dev-team` 触发

---

## 百度 Comate

1. 打开 Comate 对话框
2. 点击「系统提示词」
3. 粘贴 `SKILL.md` 全文
4. 正常对话，描述任务时加场景前缀

---

## 纯 API / 自定义工具

```python
import anthropic

with open('SKILL.md') as f:
    skill_content = f.read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=8096,
    system=skill_content,
    messages=[{"role": "user", "content": "[全新项目] 你的任务描述"}]
)
```
