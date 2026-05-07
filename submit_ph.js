const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false, slowMo: 400 });
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();

  console.log('Opening Product Hunt new post page...');
  await page.goto('https://www.producthunt.com/posts/new', { waitUntil: 'domcontentloaded' });

  console.log('Page loaded. Please log in if prompted, then the form will be filled automatically.');
  await page.waitForTimeout(5000);

  // Fill name
  try {
    const nameField = page.locator('input[name="name"], input[placeholder*="name"], input[placeholder*="Name"]').first();
    await nameField.fill('Lean AI Dev Team', { timeout: 8000 });
    console.log('✓ Name filled');
  } catch(e) { console.log('Name field not found yet — may need login first'); }

  // Fill tagline
  try {
    const tagline = page.locator('input[name="tagline"], input[placeholder*="tagline"], input[placeholder*="Tagline"]').first();
    await tagline.fill('8-agent AI dev team that thinks in business value, not just code', { timeout: 5000 });
    console.log('✓ Tagline filled');
  } catch(e) { console.log('Tagline field not found'); }

  // Fill description
  try {
    const desc = page.locator('textarea[name="description"], textarea[placeholder*="description"], textarea[placeholder*="Description"]').first();
    await desc.fill(
`An 8-agent Claude Code skill powered by the Lean AI Methodology (精益AI方法论) by Kai Shi.

Each task runs 6 phases:
1. 业务规划师 (Business Planner) — defines "why" before anything starts
2. 产品经理 (Product Manager) — ROI model, KPI dashboard, scenario card
3. 业务分析师 (Business Analyst) — user stories, As-Is→To-Be, acceptance criteria
4. 技术架构师 (Technical Architect) — ADRs, API contracts, Clean Core design
5. Frontend + Backend + Data Integration — run in parallel, honor API contracts
6. 合规项目管理 (Compliance PM) — four closed-loop check, conflict detection, DoD

Strategy first. Code last. Four closed loops guaranteed.
Free for non-commercial use. Apache 2.0.

GitHub: https://github.com/sky791016/lean-ai-dev-team
Website: https://sky791016.github.io/lean-ai-dev-team/
Methodology by: Kai Shi (史凯) · sky.kugua@gmail.com`, { timeout: 5000 });
    console.log('✓ Description filled');
  } catch(e) { console.log('Description field not found'); }

  // Fill website URL
  try {
    const url = page.locator('input[name="url"], input[placeholder*="url"], input[placeholder*="URL"], input[type="url"]').first();
    await url.fill('https://sky791016.github.io/lean-ai-dev-team/', { timeout: 5000 });
    console.log('✓ URL filled');
  } catch(e) { console.log('URL field not found'); }

  console.log('\n========================================');
  console.log('✅ Form pre-filled! Please:');
  console.log('   1. Log in to Product Hunt if not already');
  console.log('   2. Review the filled content');
  console.log('   3. Upload 5 gallery images');
  console.log('   4. Click Submit');
  console.log('========================================\n');

  // Keep browser open for user to complete submission
  await page.waitForTimeout(300000); // 5 minutes
  await browser.close();
})();
