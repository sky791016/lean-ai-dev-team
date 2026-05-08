#!/usr/bin/env bash
# ── Lean AI Dev Team — 一键部署 Google Apps Script 访问统计 ────────────────────
# 用法：bash analytics/deploy.sh
# 需要：Node.js + npm（用于 clasp CLI）

set -e
cd "$(dirname "$0")"   # 进入 analytics/ 目录

SCRIPT_TITLE="Lean AI Dev Team Tracker"
TRACKER_FILE="tracker.gs"
INDEX_HTML="../index.html"

echo ""
echo "═══════════════════════════════════════════════"
echo "  Lean AI Dev Team — 访问统计一键部署"
echo "═══════════════════════════════════════════════"
echo ""

# ── 1. 检查 clasp ─────────────────────────────────
if ! command -v clasp &>/dev/null; then
  echo "▶ 安装 clasp（Google Apps Script CLI）..."
  npm install -g @google/clasp
fi
echo "✅ clasp $(clasp --version)"

# ── 2. 登录 Google 账户 ───────────────────────────
echo ""
echo "▶ 登录 Google 账户（会打开浏览器，用你的 Gmail 账户授权）..."
echo "  提示：选择 sky.kugua@gmail.com"
echo ""
clasp login

# ── 3. 创建 Apps Script 项目 ──────────────────────
echo ""
echo "▶ 创建 Apps Script 项目：$SCRIPT_TITLE ..."

# 用一个临时目录存放项目文件
WORK_DIR="$(mktemp -d)"
cp "$TRACKER_FILE" "$WORK_DIR/Code.gs"

cd "$WORK_DIR"
clasp create --title "$SCRIPT_TITLE" --type standalone --rootDir .

# 获取 Script ID
SCRIPT_ID=$(cat .clasp.json | python3 -c "import sys,json; print(json.load(sys.stdin)['scriptId'])")
echo "✅ Script ID: $SCRIPT_ID"

# ── 4. 推送代码 ────────────────────────────────────
echo ""
echo "▶ 推送 tracker.gs 代码..."
clasp push --force
echo "✅ 代码已推送"

# ── 5. 创建部署（Web App）─────────────────────────
echo ""
echo "▶ 部署为网页应用（任何人可访问）..."

# clasp 部署并获取 deployment ID
DEPLOY_OUT=$(clasp deploy --description "v1 - visitor tracker")
echo "$DEPLOY_OUT"

DEPLOY_ID=$(echo "$DEPLOY_OUT" | grep -oE '[A-Za-z0-9_-]{50,}' | head -1)

if [ -z "$DEPLOY_ID" ]; then
  echo ""
  echo "⚠️  无法自动获取部署 URL，请手动完成："
  echo "   1. 打开 https://script.google.com/d/$SCRIPT_ID/edit"
  echo "   2. 点「部署」→「新建部署」→「网页应用」"
  echo "   3. 执行身份：我    谁可以访问：所有人"
  echo "   4. 复制 URL 后运行："
  echo "      bash analytics/deploy.sh --set-url YOUR_URL"
  cd -
  exit 1
fi

GAS_URL="https://script.google.com/macros/s/${DEPLOY_ID}/exec"
echo "✅ 部署 URL: $GAS_URL"

# ── 6. 写入 index.html ────────────────────────────
cd - >/dev/null
echo ""
echo "▶ 将 URL 写入 index.html ..."

if grep -q "YOUR_GAS_URL_HERE" "$INDEX_HTML"; then
  # macOS sed requires backup extension
  sed -i '' "s|YOUR_GAS_URL_HERE|$GAS_URL|g" "$INDEX_HTML"
  echo "✅ index.html 已更新"
else
  echo "⚠️  index.html 中未找到占位符，当前 TRACKER 值可能已设置"
fi

# ── 7. 设置每日定时触发器 ──────────────────────────
echo ""
echo "▶ 设置每日 08:00 邮件定时触发器..."
# 运行 setupDailyTrigger 函数
clasp run setupDailyTrigger --scriptId "$SCRIPT_ID" 2>/dev/null && \
  echo "✅ 触发器已设置：每天 08:00 发送日报到 sky.kugua@gmail.com" || \
  echo "⚠️  clasp run 需要额外授权，请在浏览器手动运行 setupDailyTrigger 函数"

# ── 8. 提交推送 ────────────────────────────────────
echo ""
echo "▶ 提交并推送 index.html ..."
cd ..
git add index.html analytics/
git commit -m "feat: activate visit tracking — GAS URL configured

Google Apps Script deployed at:
$GAS_URL

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push origin main && git push cnb main

echo ""
echo "═══════════════════════════════════════════════"
echo "  全部完成！"
echo ""
echo "  访问统计：每次页面加载自动记录 IP + 地区"
echo "  每日邮件：08:00 发送到 sky.kugua@gmail.com"
echo "  数据表格：Google Drive → Lean AI Dev Team — 访问统计"
echo "═══════════════════════════════════════════════"
echo ""
