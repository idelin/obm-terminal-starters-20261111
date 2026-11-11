import json,sys
from plan import solve
for line in sys.stdin:
    print(json.dumps(solve(json.loads(line)),ensure_ascii=False),flush=True)
