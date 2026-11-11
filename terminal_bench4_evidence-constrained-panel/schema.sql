PRAGMA foreign_keys=ON;
CREATE TABLE records(id TEXT PRIMARY KEY,channel TEXT NOT NULL);
CREATE TABLE capacities(channel TEXT PRIMARY KEY,maximum INTEGER NOT NULL);
CREATE TABLE authorities(source TEXT PRIMARY KEY,multiplier INTEGER NOT NULL);
CREATE TABLE evidence_versions(event_id TEXT NOT NULL,revision INTEGER NOT NULL,a TEXT NOT NULL,b TEXT NOT NULL,weight INTEGER NOT NULL,active INTEGER NOT NULL,source TEXT NOT NULL,PRIMARY KEY(event_id,revision));
CREATE TABLE cannot_links(a TEXT NOT NULL,b TEXT NOT NULL);
CREATE VIEW effective_evidence AS SELECT e.event_id,e.a,e.b,e.weight*p.multiplier AS weight,e.active FROM evidence_versions e JOIN authorities p ON e.source=p.source WHERE e.revision=(SELECT MAX(v.revision) FROM evidence_versions v WHERE v.event_id=e.event_id);
