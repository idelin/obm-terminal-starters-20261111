"""Existing dispatch input projection."""
import json

def request(conn):
    return {'horizon':conn.execute('SELECT horizon FROM settings').fetchone()[0], 'machines':[x[0] for x in conn.execute('SELECT id FROM machines ORDER BY id')], 'orders':[{'id':i,'weight':w,'release':r,'due':d,'operations':json.loads(o),'materials':json.loads(m)} for i,w,r,d,o,m in conn.execute("SELECT id,weight,release,due,operations,materials FROM orders WHERE status='ready' ORDER BY id")], 'lots':[{'id':i,'material':m,'qty':q,'expiry':e} for i,m,q,e in conn.execute('SELECT * FROM dispatch_lots ORDER BY id')], 'downtime':[{'machine':m,'start':s,'end':e} for m,s,e in conn.execute('SELECT * FROM dispatch_downtime')]}
