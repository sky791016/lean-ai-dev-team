# 项目状态快照 — 2026-05-10

## 项目：Lean AI PRD Team

**GitHub Repo:** https://github.com/sky791016/lean-ai-dev-team
**官网：** https://sky791016.github.io/lean-ai-dev-team/
**本地路径：** `/Users/super_kai/.claude/skills/lean-ai-dev-team/`
**npm 包名：** `lean-ai-prd-team`
**版本：** v1.3.0

---

## 已完成内容

### ✅ Standard v1.3 (SKILL.md)
- Skill Activation 欢迎语
- 每个 agent OPENING 自我介绍
- 每阶段向用户输出关键发现
- 澄清门（Clarification Gates）
- 阶段交接消息（Phase Handoff Messages）
- Compliance PM 裁决卡（ASCII bordered verdict card）
- Kai Shi 引言分布全覆盖
- 执行规则更新为 11 条
- 已推送 GitHub ✅

### ✅ 官网更新（docs/index.html）
- 品牌名：Lean AI PRD Team（已统一）
- 命令：`/lean-ai-prd-team` / `/lean-ai-prd-team-pro`
- Release Notes 区块（v1.0 ~ v1.3）
- 新增 `#pricing` 定价区块：
  - Standard 免费卡 + Pro ¥199/$29/年卡
  - 4 种支付方式（WeChat/Alipay、Stripe、Ko-fi、PayPal）
  - WeChat 二维码已上传真实图片（`docs/assets/wechat-qr.png`）
  - 支付宝二维码：**仍为占位图**，待上传 `docs/assets/alipay-qr.png`
  - License Key 流程说明（付款→发邮件→24小时收Key）
  - npm/npx 安装展示区
  - Donate 捐赠区
- Nav 新增 Pricing 链接，CTA 改为 "✨ Get Pro →"
- 全部已推送 GitHub ✅

### ✅ npm 包文件
- `package.json`（包名：lean-ai-prd-team，v1.3.0）
- `bin/install.js`（npx 安装脚本，支持 `--pro` 参数）
- 已推送 GitHub ✅

---

## 🔴 未完成：npm 发布（阻塞中）

### 问题历史
1. 首次 `npm publish` → 报 403：需要 2FA bypass token
2. 尝试 `--otp` → 还是 403（账号设置层面的限制）
3. 用 Granular Token → 403 Read-only 权限不够
4. 用 Classic Automation Token → 命令有误（token 误加了 `w` 前缀变成 `wonpm_...`）
5. 清除旧 token 后：`~/.npmrc` 现有一个新 token（`npm_1GBm...`）是否有效未验证

### 当前 npmrc 状态
```
~/.npmrc 中：//registry.npmjs.org/:_authToken=<已移除，请用自己的Automation Token>
```
这个 token 可能是有效的 Automation token，**需要验证并重新执行发布**。

### 下次继续操作步骤

**方案A（最可能成功）：**
```bash
# 验证当前 token 是否有效
npm whoami

# 如果有效，直接发布
cd /Users/super_kai/.claude/skills/lean-ai-dev-team
npm publish --access public
```

**方案B（token 无效时）：**
1. 去 https://www.npmjs.com/settings/sky1031/tokens
2. Generate New Token → **Classic Token** → **Automation**
3. 复制 token
4. `npm config set //registry.npmjs.org/:_authToken 你的token`
5. `cd /Users/super_kai/.claude/skills/lean-ai-dev-team && npm publish --access public`

---

## 待处理（低优先级）

- [ ] 上传支付宝二维码 → `docs/assets/alipay-qr.png`
- [ ] Stripe Payment Link → 替换 pricing 区块中的邮件跳转链接
- [ ] npm 发布成功后，更新官网 npm install 区块为真实可用命令

---

## 文件结构（关键）

```
lean-ai-dev-team/
├── docs/
│   ├── index.html          ← 官网（GitHub Pages 服务此文件）
│   └── assets/
│       ├── logo.png
│       └── wechat-qr.png   ← 微信收款码（已上传）
├── lean-ai-prd-team/
│   └── SKILL.md            ← Standard v1.3
├── lean-ai-prd-team-pro/
│   └── SKILL.md            ← Pro v1.1（未更新到v1.3）
├── bin/
│   └── install.js          ← npx 安装脚本
├── package.json            ← npm 包定义
└── SKILL.md                ← 根目录 skill（Standard 副本）
```

---

## 联系信息
- 作者：史凯 Kai Shi
- Email：sky.kugua@gmail.com
- npm 账号：sky1031
