#!/usr/bin/env node
'use strict';

const { execSync } = require('child_process');
const os = require('os');
const path = require('path');
const fs = require('fs');

// ── Parse args ────────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const isPro  = args.includes('--pro') || args.includes('-p');
const isHelp = args.includes('--help') || args.includes('-h');

if (isHelp) {
  console.log(`
  Lean AI PRD Team — Skill Installer

  Usage:
    npx lean-ai-prd-team           Install Standard (free, 8 agents)
    npx lean-ai-prd-team --pro     Install Pro (10 agents, commercial license required)

  Options:
    --pro, -p     Install Pro version
    --help, -h    Show this help

  After install, open Claude Code in any project and run:
    /lean-ai-prd-team [全新项目] your task description
    /lean-ai-prd-team [重构优化] your task
    /lean-ai-prd-team [项目评审] your task

  Pro version commercial use: sky.kugua@gmail.com
  Website: https://sky791016.github.io/lean-ai-dev-team/
`);
  process.exit(0);
}

// ── Config ────────────────────────────────────────────────────────────────────
const REPO_URL  = 'https://github.com/sky791016/lean-ai-dev-team.git';
const TMP_DIR   = path.join(os.tmpdir(), 'lean-ai-prd-team-install');
const skillName = isPro ? 'lean-ai-prd-team-pro' : 'lean-ai-prd-team';
const srcDir    = path.join(TMP_DIR, skillName);
const destDir   = path.join(os.homedir(), '.claude', 'skills', skillName);

// ── Helpers ───────────────────────────────────────────────────────────────────
function run(cmd, opts = {}) {
  execSync(cmd, { stdio: 'inherit', ...opts });
}

function cleanTmp() {
  try { run(`rm -rf "${TMP_DIR}"`, { stdio: 'ignore' }); } catch (_) {}
}

// ── Main ──────────────────────────────────────────────────────────────────────
console.log('\n🤖 Lean AI PRD Team — Skill Installer');
console.log(`   ${isPro ? 'Pro (10 agents · commercial)' : 'Standard (8 agents · free)'}\n`);

// Check if already installed
if (fs.existsSync(destDir)) {
  console.log(`✅ Already installed at:\n   ${destDir}\n`);
  console.log('To update:');
  console.log(`  cd "${destDir}" && git pull\n`);
  process.exit(0);
}

// Ensure skills directory exists
fs.mkdirSync(path.dirname(destDir), { recursive: true });

// Check git is available
try {
  execSync('git --version', { stdio: 'ignore' });
} catch (_) {
  console.error('❌ git is required but not found. Please install git and try again.');
  process.exit(1);
}

// Clone
cleanTmp();
console.log('📥 Cloning from GitHub...');
try {
  run(`git clone --depth=1 --quiet "${REPO_URL}" "${TMP_DIR}"`);
} catch (err) {
  cleanTmp();
  console.error('\n❌ Clone failed. Check your internet connection and try again.');
  process.exit(1);
}

// Verify source exists
if (!fs.existsSync(srcDir)) {
  cleanTmp();
  console.error(`\n❌ Could not find ${skillName} in the cloned repository.`);
  process.exit(1);
}

// Copy to skills directory
console.log(`📦 Installing to:\n   ${destDir}\n`);
try {
  run(`cp -R "${srcDir}" "${destDir}"`);
} catch (err) {
  cleanTmp();
  console.error('\n❌ Copy failed:', err.message);
  process.exit(1);
}

cleanTmp();

// ── Success ───────────────────────────────────────────────────────────────────
console.log(`✅ Installed: ${skillName}\n`);
console.log('Open Claude Code in your project and run:\n');
if (isPro) {
  console.log(`  /lean-ai-prd-team-pro [全新项目] your task description`);
  console.log(`  /lean-ai-prd-team-pro [重构优化] your task`);
  console.log(`  /lean-ai-prd-team-pro [项目评审] your task`);
  console.log(`  /lean-ai-prd-team-pro [精益诊断] your task`);
  console.log('\n⚠️  Pro requires a commercial License Key.');
  console.log('   Contact: sky.kugua@gmail.com\n');
} else {
  console.log(`  /lean-ai-prd-team [全新项目] your task description`);
  console.log(`  /lean-ai-prd-team [重构优化] your task`);
  console.log(`  /lean-ai-prd-team [项目评审] your task`);
  console.log('\n💡 Pro version (Code Audit + FP Sizing + Value Assessor):');
  console.log('   npx lean-ai-prd-team --pro');
  console.log('   Commercial license: sky.kugua@gmail.com\n');
}
console.log('Docs: https://sky791016.github.io/lean-ai-dev-team/\n');
