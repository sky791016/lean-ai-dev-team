-- 初始化 License 数据库表
-- 在 Vercel Postgres 控制台执行此 SQL

CREATE TABLE IF NOT EXISTS licenses (
  id          SERIAL PRIMARY KEY,
  key         TEXT UNIQUE NOT NULL,
  email       TEXT NOT NULL,
  name        TEXT,
  created_at  TIMESTAMPTZ DEFAULT NOW(),
  expires_at  TIMESTAMPTZ NOT NULL,
  activated_at TIMESTAMPTZ,
  activation_count INTEGER DEFAULT 0,
  is_active   BOOLEAN DEFAULT true,
  notes       TEXT
);

CREATE INDEX IF NOT EXISTS idx_licenses_key ON licenses(key);
CREATE INDEX IF NOT EXISTS idx_licenses_email ON licenses(email);

-- 示例：插入一条测试 License（激活后删除）
-- INSERT INTO licenses (key, email, name, expires_at)
-- VALUES ('LAIPRO-TEST-0000-0000', 'test@example.com', 'Test User', NOW() + INTERVAL '1 year');
