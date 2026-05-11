// api/verify.js — License Key 验证接口
// GET /api/verify?key=LAIPRO-XXXX-XXXX-XXXX

import pkg from 'pg';
const { Pool } = pkg;

// Neon Postgres via Vercel integration uses POSTGRES_URL; fall back to DATABASE_URL
const connectionString = process.env.POSTGRES_URL || process.env.DATABASE_URL;
const pool = new Pool({ connectionString, ssl: { rejectUnauthorized: false } });

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'GET') return res.status(405).json({ error: 'Method not allowed' });

  const { key } = req.query;
  if (!key || typeof key !== 'string') {
    return res.status(400).json({ valid: false, message: 'License key is required.' });
  }

  const normalizedKey = key.trim().toUpperCase();

  if (!/^LAIPRO-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}$/.test(normalizedKey)) {
    return res.status(200).json({ valid: false, message: 'Invalid license key format.' });
  }

  try {
    const result = await pool.query(
      'SELECT key, email, name, expires_at, is_active, activation_count FROM licenses WHERE key = $1 LIMIT 1',
      [normalizedKey]
    );

    if (result.rows.length === 0) {
      return res.status(200).json({ valid: false, message: 'License key not found.' });
    }

    const license = result.rows[0];

    if (!license.is_active) {
      return res.status(200).json({ valid: false, message: 'License key has been deactivated.' });
    }

    if (new Date(license.expires_at) < new Date()) {
      return res.status(200).json({ valid: false, message: 'License key has expired. Renew at sky.kugua@gmail.com' });
    }

    await pool.query(
      'UPDATE licenses SET activation_count = activation_count + 1, activated_at = COALESCE(activated_at, NOW()) WHERE key = $1',
      [normalizedKey]
    );

    return res.status(200).json({
      valid: true,
      message: `Welcome, ${license.name || license.email}! Pro license verified.`,
      expires_at: license.expires_at,
    });

  } catch (err) {
    console.error('DB error:', err.message || err);
    return res.status(500).json({ valid: false, message: 'Verification service error. Please try again or contact sky.kugua@gmail.com' });
  }
}
