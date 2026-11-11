import json,sys
from pathlib import Path
from engine import SessionEngine
from legacy import load
if __name__=='__main__':
    root,out=map(Path,sys.argv[1:]);config,seed=load(root/'seed.sqlite');ops=seed+[json.loads(line) for line in (root/'corrections.jsonl').read_text().splitlines() if line.strip()]
    engine=SessionEngine(**config);steps=[];ledger=[]
    for op in ops:
        value=engine.apply(op);steps.append(value);ledger.extend(value['emitted'])
    out.mkdir(parents=True,exist_ok=True)
    (out/'ledger.jsonl').write_text(''.join(json.dumps(row,sort_keys=True)+'\n' for row in ledger))
    (out/'report.json').write_text(json.dumps({'steps':steps,'view':engine.view()},sort_keys=True)+'\n')
