import json,sys
from fst_runtime import apply
for line in sys.stdin:
    q=json.loads(line)
    print(json.dumps({'word':apply(sys.argv[1],q['branch'],q['word'])}),flush=True)
