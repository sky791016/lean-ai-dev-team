// api/admin/licenses.js — 管理后台 API
import pkg from 'pg';
const { Pool } = pkg;
import crypto from 'crypto';

const pool = new Pool({ connectionString: process.env.DATABASE_URL, ssl: { rejectUnauthorized: false } });

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

  if (req.method === 'GET') {
    const result = await pool.query(
      'SELECT id, key, email, name, created_at, expires_at, activated_at, activation_count, is_active, notes FROM licenses ORDER BY created_at DESC'
    );
    return res.status(200).json({ licenses: result.rows });
  }

  if (req.method === 'POST') {
    const { email, name, notes, months = 12 } = req.body || {};
    if (!email) return res.status(400).json({ error: 'email is required' });

    const key = generateKey();
    const expiresAt = new Date();
    expiresAt.setMonth(expiresAt.getMonth() + Number(months));

    await pool.query(
      'INSERT INTO licenses (key, email, name, expires_at, notes) VALUES ($1, $2, $3, $4, $5)',
      [key, email, name || null, expiresAt.toISOString(), notes || null]
    );

    return res.status(201).json({
      key, email, name,
      expires_at: expiresAt.toISOString(),
      message: `License created. Send key to ${email}: ${key}`,
    });
  }

  if (req.method === 'DELETE') {
    const { key } = req.query;
    if (!key) return res.status(400).json({ error: 'key is required' });
    await pool.query('UPDATE licenses SET is_active = false WHERE key = $1', [key]);
    return res.status(200).json({ message: `License ${key} deactivated.` });
  }

  return res.status(405).json({ error: 'Method not allowed' });
}
