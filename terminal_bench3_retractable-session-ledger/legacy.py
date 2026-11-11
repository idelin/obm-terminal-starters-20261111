import sqlite3
from pathlib import Path

def load(path):
    con=sqlite3.connect(Path(path).resolve().as_uri()+'?mode=ro',uri=True)
    try:
        settings=dict(con.execute('SELECT name,value FROM settings'))
        partitions=dict(con.execute('SELECT code,name FROM partitions'))
        names=dict(con.execute('SELECT code,name FROM event_names'))
        keys=dict(con.execute('SELECT code,name FROM account_names'))
        ops=[]
        for _,kind,partition,event,key,tick,amount in con.execute('SELECT * FROM history ORDER BY position'):
            if kind==1:ops.append({'op':'put','partition':partitions[partition],'id':names[event],'key':keys[key],'time':tick+settings['tick_origin'],'value':amount*settings['value_scale']})
            elif kind==2:ops.append({'op':'remove','id':names[event]})
            elif kind==3:ops.append({'op':'advance','partition':partitions[partition],'time':tick+settings['tick_origin']})
            else:raise ValueError('legacy operation')
        return {'gap':settings['gap'],'lateness':settings['lateness'],'partitions':[partitions[k] for k in sorted(partitions)]},ops
    finally:con.close()
