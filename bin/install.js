#!/usr/bin/env node
'use strict';

const { execSync } = require('child_process');
const os = require('os');
const path = require('path');
const fs = require('fs');
const https = require('https');
const readline = require('readline');

// ── Parse args ────────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const isPro  = args.includes('--pro') || args.includes('-p');
const isHelp = args.includes('--help') || args.includes('-h');

if (isHelp) {
  console.log(`
  Lean AI PRD Team — Skill Installer

  Usage:
    npx lean-ai-prd-team           Install Standard (free, 8 agents)
    npx lean-ai-prd-team --pro     Install Pro (10 agents, License Key required)

  Options:
    --pro, -p     Install Pro version (requires valid License Key)
    --help, -h    Show this help

  After install, open Claude Code in any project and run:
    /lean-ai-prd-team [全新项目] your task
    /lean-ai-prd-team [重构优化] your task
    /lean-ai-prd-team [项目评审] your task

  Pro license: sky.kugua@gmail.com
  Website: https://sky791016.github.io/lean-ai-dev-team/
`);
  process.exit(0);
}

// ── Config ────────────────────────────────────────────────────────────────────
const REPO_URL      = 'https://github.com/sky791016/lean-ai-dev-team.git';
const VERIFY_API    = 'https://lean-ai-license.vercel.app/api/verify';
const TMP_DIR       = path.join(os.tmpdir(), 'lean-ai-prd-team-install');
const skillName     = isPro ? 'lean-ai-prd-team-pro' : 'lean-ai-prd-team';
const srcDir        = path.join(TMP_DIR, skillName);
const destDir       = path.join(os.homedir(), '.claude', 'skills', skillName);

// ── Helpers ───────────────────────────────────────────────────────────────────
function run(cmd, opts = {}) {
  execSync(cmd, { stdio: 'inherit', ...opts });
}

function cleanTmp() {
  try { run(`rm -rf "${TMP_DIR}"`, { stdio: 'ignore' }); } catch (_) {}
}

function prompt(question) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  return new Promise(resolve => rl.question(question, ans => { rl.close(); resolve(ans.trim()); }));
}

function verifyLicense(key) {
  return new Promise((resolve, reject) => {
    const url = `${VERIFY_API}?key=${encodeURIComponent(key)}`;
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(new Error('Invalid response from license server.')); }
      });
    }).on('error', reject);
  });
}

// ── Main ──────────────────────────────────────────────────────────────────────
async function main() {
  console.log('\n🤖 Lean AI PRD Team — Skill Installer');
  console.log(`   ${isPro ? 'Pro (10 agents · commercial)' : 'Standard (8 agents · free)'}\n`);

  // ── Pro: License Key 验证 ──────────────────────────────────────────────────
  if (isPro) {
    console.log('🔑 Pro version requires a valid License Key.');
    console.log('   Purchase: https://sky791016.github.io/lean-ai-dev-team/#pricing\n');

    const key = await prompt('   Enter your License Key (LAIPRO-XXXX-XXXX-XXXX): ');

    if (!key) {
      console.error('\n❌ No License Key provided.');
      process.exit(1);
    }

    process.stdout.write('   Verifying license...');

    let result;
    try {
      result = await verifyLicense(key);
    } catch (err) {
      console.log(' ⚠️  Could not reach license server.');
      console.log('   Please check your internet connection or contact sky.kugua@gmail.com');
      process.exit(1);
    }

    if (!result.valid) {
      console.log('');
      console.error(`\n❌ ${result.message}`);
      console.error('   Purchase a Pro license: sky.kugua@gmail.com\n');
      process.exit(1);
    }

    console.log(' ✅');
    console.log(`\n   ${result.message}`);
    if (result.expires_at) {
      const exp = new Date(result.expires_at).toLocaleDateString();
      console.log(`   License valid until: ${exp}\n`);
    }
  }

  // ── Already installed ──────────────────────────────────────────────────────
  if (fs.existsSync(destDir)) {
    console.log(`✅ Already installed at:\n   ${destDir}\n`);
    console.log('To update:');
    console.log(`  cd "${destDir}" && git pull\n`);
    process.exit(0);
  }

  // ── Ensure skills dir ──────────────────────────────────────────────────────
  fs.mkdirSync(path.dirname(destDir), { recursive: true });

  // ── Check git ─────────────────────────────────────────────────────────────
  try {
    execSync('git --version', { stdio: 'ignore' });
  } catch (_) {
    console.error('❌ git is required but not found. Please install git and try again.');
    process.exit(1);
  }

  // ── Clone ──────────────────────────────────────────────────────────────────
  cleanTmp();
  console.log('📥 Cloning from GitHub...');
  try {
    run(`git clone --depth=1 --quiet "${REPO_URL}" "${TMP_DIR}"`);
  } catch (err) {
    cleanTmp();
    console.error('\n❌ Clone failed. Check your internet connection and try again.');
    process.exit(1);
  }

  if (!fs.existsSync(srcDir)) {
    cleanTmp();
    console.error(`\n❌ Could not find ${skillName} in the repository.`);
    process.exit(1);
  }

  // ── Install ────────────────────────────────────────────────────────────────
  console.log(`📦 Installing to:\n   ${destDir}\n`);
  try {
    run(`cp -R "${srcDir}" "${destDir}"`);
  } catch (err) {
    cleanTmp();
    console.error('\n❌ Copy failed:', err.message);
    process.exit(1);
  }

  cleanTmp();

  // ── Success ────────────────────────────────────────────────────────────────
  console.log(`✅ Installed: ${skillName}\n`);
  console.log('Open Claude Code in your project and run:\n');

  if (isPro) {
    console.log(`  /lean-ai-prd-team-pro [全新项目] your task`);
    console.log(`  /lean-ai-prd-team-pro [重构优化] your task`);
    console.log(`  /lean-ai-prd-team-pro [项目评审] your task`);
    console.log(`  /lean-ai-prd-team-pro [精益诊断] your task`);
  } else {
    console.log(`  /lean-ai-prd-team [全新项目] your task`);
    console.log(`  /lean-ai-prd-team [重构优化] your task`);
    console.log(`  /lean-ai-prd-team [项目评审] your task`);
    console.log('\n💡 Upgrade to Pro (Code Audit + FP Sizing + Value Assessor):');
    console.log('   npx lean-ai-prd-team --pro');
    console.log('   Purchase: sky.kugua@gmail.com\n');
  }

  console.log('Docs: https://sky791016.github.io/lean-ai-dev-team/\n');
}

main().catch(err => {
  console.error('\n❌ Unexpected error:', err.message);
  process.exit(1);
});
