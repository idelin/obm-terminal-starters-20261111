"""Existing evidence projection; input tables are read-only to the candidate."""
import sqlite3

def request(conn):
    return {'records':[{'id':i,'channel':c} for i,c in conn.execute('SELECT id,channel FROM records ORDER BY id')], 'capacity':dict(conn.execute('SELECT channel,maximum FROM capacities')), 'evidence':[{'event_id':i,'a':a,'b':b,'weight':w,'active':bool(active)} for i,a,b,w,active in conn.execute('SELECT * FROM effective_evidence ORDER BY event_id')], 'cannot_link':[list(x) for x in conn.execute('SELECT a,b FROM cannot_links')]}
