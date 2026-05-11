// api/health.js — Debug endpoint to check DB connectivity
import pkg from 'pg';
const { Pool } = pkg;

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');

  const connectionString = process.env.POSTGRES_URL || process.env.DATABASE_URL;
  const envUsed = process.env.POSTGRES_URL ? 'POSTGRES_URL' : (process.env.DATABASE_URL ? 'DATABASE_URL' : 'NONE');

  if (!connectionString) {
    return res.status(500).json({ ok: false, error: 'No DB env var found', checked: ['POSTGRES_URL', 'DATABASE_URL'] });
  }

  try {
    const pool = new Pool({ connectionString, ssl: { rejectUnauthorized: false } });
    const result = await pool.query('SELECT COUNT(*) as total FROM licenses');
    await pool.end();
    return res.status(200).json({ ok: true, env: envUsed, licenses: result.rows[0].total });
  } catch (err) {
    return res.status(500).json({ ok: false, env: envUsed, error: err.message });
  }
}
