// ─── Lean AI Dev Team — 访问统计 & 日报 ──────────────────────────────────────
// 部署方式：Google Apps Script → 新建项目 → 粘贴此代码
// → 部署为网页应用（任何人可访问）→ 复制 URL → 填入 index.html

const EMAIL_TO   = 'sky.kugua@gmail.com';
const SHEET_NAME = '访问记录';
const SITE_URL   = 'https://sky791016.github.io/lean-ai-dev-team/';

// ── 获取或创建数据表 ────────────────────────────────────────────────────────────
function getSheet() {
  const files = DriveApp.getFilesByName('Lean AI Dev Team — 访问统计');
  let ss;
  if (files.hasNext()) {
    ss = SpreadsheetApp.open(files.next());
  } else {
    ss = SpreadsheetApp.create('Lean AI Dev Team — 访问统计');
    const link = ss.getUrl();
    GmailApp.sendEmail(EMAIL_TO, '访问统计表已创建', '数据表地址：' + link);
  }
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow(['时间', 'IP地址', '国家', '城市', '页面路径', '来源页面', 'User Agent']);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, 7).setFontWeight('bold');
  }
  return sheet;
}

// ── 接收访问埋点（GET 请求） ─────────────────────────────────────────────────────
function doGet(e) {
  try {
    const sheet = getSheet();

    const ip   = String(e.parameter.ip   || '').slice(0, 45);
    const page = String(e.parameter.page || '/').slice(0, 200);
    const ref  = String(e.parameter.ref  || '').slice(0, 300);
    const ua   = String(e.parameter.ua   || '').slice(0, 300);

    // 地理位置（免费，无需 key）
    let country = '', city = '';
    if (ip && ip !== 'unknown') {
      try {
        const geo = JSON.parse(
          UrlFetchApp.fetch('https://ip-api.com/json/' + ip + '?fields=country,city&lang=zh-CN', {muteHttpExceptions: true})
                    .getContentText()
        );
        country = geo.country || '';
        city    = geo.city    || '';
      } catch (_) {}
    }

    sheet.appendRow([new Date(), ip, country, city, page, ref, ua]);

  } catch (err) {
    // 静默失败，不影响用户
  }

  // 返回 1×1 透明 GIF，让 img.src 方式也能正常使用
  const gif = Utilities.newBlob(
    Utilities.base64Decode('R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7'),
    'image/gif'
  );
  return ContentService.createTextOutput('ok');
}

// ── 每日邮件报告（设置触发器后自动运行） ────────────────────────────────────────
function sendDailyReport() {
  const sheet = getSheet();
  const data  = sheet.getDataRange().getValues();
  if (data.length < 2) return;

  const rows = data.slice(1); // 去掉表头

  // 昨日时间范围
  const yd = new Date();
  yd.setDate(yd.getDate() - 1);
  yd.setHours(0, 0, 0, 0);
  const td = new Date(yd);
  td.setDate(td.getDate() + 1);

  const visits = rows.filter(r => {
    const ts = new Date(r[0]);
    return ts >= yd && ts < td;
  });

  const dateStr = yd.toLocaleDateString('zh-CN', {year: 'numeric', month: 'long', day: 'numeric'});

  if (visits.length === 0) {
    GmailApp.sendEmail(EMAIL_TO,
      'Lean AI Dev Team 日报 ' + dateStr + ' — 暂无访问',
      dateStr + ' 暂无访问记录。\n\n网站：' + SITE_URL);
    return;
  }

  // 统计
  const uniqueIPs    = [...new Set(visits.map(r => r[1]).filter(Boolean))];
  const pageCount    = {};
  const countryCount = {};
  visits.forEach(r => {
    const p = r[4] || '/';
    pageCount[p] = (pageCount[p] || 0) + 1;
    const c = r[2] || '未知';
    countryCount[c] = (countryCount[c] || 0) + 1;
  });

  // 邮件正文
  const line = '─'.repeat(40);
  let body = '';

  body += 'Lean AI Dev Team 访问日报\n';
  body += dateStr + '\n';
  body += line + '\n\n';

  body += '总访问次数：' + visits.length + '\n';
  body += '独立访客IP：' + uniqueIPs.length + '\n\n';

  body += line + '\n';
  body += '页面访问分布\n';
  body += line + '\n';
  Object.entries(pageCount)
    .sort((a, b) => b[1] - a[1])
    .forEach(([p, n]) => { body += '  ' + n + ' 次   ' + p + '\n'; });

  body += '\n' + line + '\n';
  body += '访客地区\n';
  body += line + '\n';
  Object.entries(countryCount)
    .sort((a, b) => b[1] - a[1])
    .forEach(([c, n]) => { body += '  ' + n + ' 人   ' + c + '\n'; });

  body += '\n' + line + '\n';
  body += '全部 IP 地址\n';
  body += line + '\n';
  uniqueIPs.forEach(ip => {
    const r = visits.find(row => row[1] === ip);
    const loc = r ? [r[3], r[2]].filter(Boolean).join(', ') : '';
    body += '  ' + ip + (loc ? '   (' + loc + ')' : '') + '\n';
  });

  body += '\n' + line + '\n';
  body += '详细访问记录（最近 50 条）\n';
  body += line + '\n';
  visits.slice(-50).forEach(r => {
    const ts  = new Date(r[0]).toLocaleString('zh-CN');
    const ip  = r[1] || '-';
    const loc = [r[3], r[2]].filter(Boolean).join(', ') || '未知';
    const pg  = r[4] || '/';
    const ref = r[5] ? '来自 ' + r[5] : '直接访问';
    body += '[' + ts + '] ' + ip + ' (' + loc + ')  ' + pg + '  ' + ref + '\n';
  });

  body += '\n' + line + '\n';
  body += '网站：' + SITE_URL + '\n';

  GmailApp.sendEmail(
    EMAIL_TO,
    'Lean AI Dev Team 日报 ' + dateStr + ' — ' + visits.length + '次访问 / ' + uniqueIPs.length + '个IP',
    body
  );
}

// ── 一次性：设置每日定时触发器 ────────────────────────────────────────────────
// 在 Apps Script 编辑器里手动运行一次此函数即可
function setupDailyTrigger() {
  // 删除同名旧触发器
  ScriptApp.getProjectTriggers().forEach(t => {
    if (t.getHandlerFunction() === 'sendDailyReport') {
      ScriptApp.deleteTrigger(t);
    }
  });
  // 每天上午 8:00 发送报告
  ScriptApp.newTrigger('sendDailyReport')
    .timeBased()
    .everyDays(1)
    .atHour(8)
    .create();
  Logger.log('定时触发器已设置：每天 08:00 发送日报');
}
