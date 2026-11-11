import sys,json
from engine import SessionEngine
for line in sys.stdin:
    q=json.loads(line); e=SessionEngine(q['gap'],q['lateness'],q['partitions']); steps=[]
    for op in q['ops']:
        if op['op']=='snapshot': steps.append({'snapshot':e.snapshot()})
        elif op['op']=='restore': e=SessionEngine.restore(op['state']); steps.append({'emitted':[]})
        else: steps.append(e.apply(op))
    print(json.dumps({'steps':steps,'view':e.view()},sort_keys=True))
