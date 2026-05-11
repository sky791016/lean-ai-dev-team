// api/admin/licenses.js — 管理后台 API（需要 ADMIN_SECRET 验证）
// GET  /api/admin/licenses?secret=xxx          列出所有 licenses
// POST /api/admin/licenses?secret=xxx          创建新 license
// DELETE /api/admin/licenses?secret=xxx&key=xx 停用 license

import { sql } from '@vercel/postgres';
import crypto from 'crypto';

function checkAuth(req, res) {
  const secret = req.query.secret || req.headers['x-admin-secret'];
  if (!secret || secret !== process.env.ADMIN_SECRET) {
    res.status(401).json({ error: 'Unauthorized' });
    return false;
  }
  return true;
}

function generateKey() {
  const seg = () => crypto.randomBytes(2).toString('hex').toUpperCase();
  return `LAIPRO-${seg()}-${seg()}-${seg()}`;
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, x-admin-secret');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (!checkAuth(req, res)) return;

  // GET — 列出所有
  if (req.method === 'GET') {
    const result = await sql`
      SELECT id, key, email, name, created_at, expires_at, activated_at,
             activation_count, is_active, notes
      FROM licenses
      ORDER BY created_at DESC
    `;
    return res.status(200).json({ licenses: result.rows });
  }

  // POST — 创建新 License
  if (req.method === 'POST') {
    const { email, name, notes, months = 12 } = req.body || {};
    if (!email) return res.status(400).json({ error: 'email is required' });

    const key = generateKey();
    const expiresAt = new Date();
    expiresAt.setMonth(expiresAt.getMonth() + Number(months));

    await sql`
      INSERT INTO licenses (key, email, name, expires_at, notes)
      VALUES (${key}, ${email}, ${name || null}, ${expiresAt.toISOString()}, ${notes || null})
    `;

    return res.status(201).json({
      key,
      email,
      name,
      expires_at: expiresAt.toISOString(),
      message: `License created. Send key to ${email}: ${key}`,
    });
  }

  // DELETE — 停用
  if (req.method === 'DELETE') {
    const { key } = req.query;
    if (!key) return res.status(400).json({ error: 'key is required' });

    await sql`UPDATE licenses SET is_active = false WHERE key = ${key}`;
    return res.status(200).json({ message: `License ${key} deactivated.` });
  }

  return res.status(405).json({ error: 'Method not allowed' });
}
