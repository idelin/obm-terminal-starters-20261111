"""Read the existing export projection without modifying its database."""
import json,sqlite3
from pathlib import Path

def load(db,job):
    conn=sqlite3.connect(Path(db).resolve().as_uri()+'?mode=ro',uri=True)
    try:
        conn.execute('BEGIN')
        secret=conn.execute('SELECT secret FROM exports WHERE job=?',(job,)).fetchone()
        if secret is None:raise ValueError('unknown job')
        rows=conn.execute('SELECT seq,table_name,tenant,subject,event_time,payload FROM legacy_rows ORDER BY seq').fetchall()
        return {'secret':secret[0], 'links':[{'a':{'tenant':a,'subject':b},'b':{'tenant':c,'subject':d},'start':s,'end':e} for a,b,c,d,s,e in conn.execute('SELECT * FROM links')], 'withdrawals':[{'identity':{'tenant':t,'subject':s},'at':a} for t,s,a in conn.execute('SELECT * FROM withdrawals')], 'rows':[{'seq':n,'table':table,'identity':{'tenant':t,'subject':s},'time':time,'payload':json.loads(p)} for n,table,t,s,time,p in rows]}
    finally:conn.close()
