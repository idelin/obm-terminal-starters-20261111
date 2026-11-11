PRAGMA foreign_keys=ON;
CREATE TABLE policies(tenant TEXT PRIMARY KEY, active INTEGER NOT NULL, min_time INTEGER NOT NULL, tier TEXT NOT NULL);
CREATE TABLE exports(job TEXT PRIMARY KEY, secret TEXT NOT NULL);
CREATE TABLE subjects(tenant TEXT NOT NULL, subject TEXT NOT NULL, PRIMARY KEY(tenant,subject));
CREATE TABLE links(a_tenant TEXT,a_subject TEXT,b_tenant TEXT,b_subject TEXT,start INTEGER,end INTEGER);
CREATE TABLE withdrawals(tenant TEXT,subject TEXT,at INTEGER);
CREATE TABLE log_rows(seq INTEGER PRIMARY KEY, table_name TEXT NOT NULL, tenant TEXT NOT NULL, subject TEXT NOT NULL, event_time INTEGER NOT NULL, payload TEXT NOT NULL, tombstone INTEGER NOT NULL DEFAULT 0);
CREATE VIEW legacy_rows AS SELECT r.seq,r.table_name,r.tenant,r.subject,r.event_time,
 json_object('content',json(r.payload),'tier',p.tier) AS payload
 FROM log_rows r JOIN policies p ON r.tenant=p.tenant
 WHERE p.active=1 AND r.tombstone=0 AND r.event_time>=p.min_time;
