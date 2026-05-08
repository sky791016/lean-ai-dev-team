# 访问统计 & 日报 — 部署指南

## 架构说明

```
访客浏览器
  └─ 获取自身 IP（ipify.org）
  └─ 发送埋点 → Google Apps Script Web App
                  └─ 写入 Google Sheets
                  └─ 每天 08:00 → Gmail 日报 → sky.kugua@gmail.com
```

## 一次性部署步骤（约 5 分钟）

### 第 1 步：创建 Apps Script 项目

1. 打开 https://script.google.com
2. 点击左上角「新建项目」
3. 项目名称改为：`Lean AI Dev Team Tracker`
4. 删除默认的 `myFunction()` 代码
5. 把 `tracker.gs` 全部内容粘贴进去
6. 保存（Ctrl+S）

### 第 2 步：部署为网页应用

1. 点击右上角「部署」→「新建部署」
2. 类型选「网页应用」
3. 配置：
   - **执行身份**：我（你的 Google 账户）
   - **谁可以访问**：所有人
4. 点击「部署」
5. 复制生成的 **网页应用 URL**（格式：`https://script.google.com/macros/s/xxxxx/exec`）

### 第 3 步：将 URL 填入网站

打开 `index.html`，找到这一行：

```javascript
var TRACKER = 'YOUR_GAS_URL_HERE';
```

把 `YOUR_GAS_URL_HERE` 替换成第 2 步复制的 URL，保存。

### 第 4 步：设置每日定时邮件

回到 Apps Script 编辑器：
1. 在函数下拉框选择 `setupDailyTrigger`
2. 点击「运行」按钮
3. 首次运行会弹出授权请求 → 点击「高级」→「转到 Lean AI Dev Team Tracker」→「允许」
4. 看到日志输出「定时触发器已设置：每天 08:00 发送日报」即成功

### 第 5 步：提交并推送

```bash
git add index.html
git commit -m "feat: add visit tracking"
git push origin main
```

## 验证

1. 访问网站
2. 去 Google Drive 查看是否出现「Lean AI Dev Team — 访问统计」电子表格
3. 表格里应出现刚才的访问记录（含 IP、地区、页面）
4. 可以在 Apps Script 手动运行 `sendDailyReport` 函数测试邮件

## 数据内容

每条访问记录包含：

| 列 | 内容 |
|---|---|
| 时间 | 访问时间（北京时间） |
| IP地址 | 访客真实 IP |
| 国家 | 如「中国」「美国」 |
| 城市 | 如「深圳」「旧金山」 |
| 页面路径 | 如 `/lean-ai-dev-team/` |
| 来源页面 | referrer URL |
| User Agent | 浏览器/设备信息 |

## 每日邮件示例

```
Lean AI Dev Team 访问日报
2026年5月21日
────────────────────────────────────────

总访问次数：47
独立访客IP：31

────────────────────────────────────────
页面访问分布
────────────────────────────────────────
  38 次   /lean-ai-dev-team/
   9 次   /lean-ai-dev-team/index.html

────────────────────────────────────────
访客地区
────────────────────────────────────────
  24 人   中国
   5 人   美国
   2 人   新加坡

────────────────────────────────────────
全部 IP 地址
────────────────────────────────────────
  112.x.x.x   (深圳, 中国)
  23.x.x.x    (旧金山, 美国)
  ...
```

## 免费额度说明

- Google Apps Script：6分钟/次执行，每天 90 分钟总计
- Gmail 发送：每天 100 封（个人账户）
- ip-api.com 地理位置：每分钟 45 次（远超需求）

以上额度对个人网站完全够用。
