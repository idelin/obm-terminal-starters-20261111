import json,sys
from pathlib import Path
if __name__=='__main__':
    data=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    rules=json.loads((data/'rules.json').read_text())
    (out/'result.json').write_text(json.dumps({'shared':[],'north':[],'south':[]}))
