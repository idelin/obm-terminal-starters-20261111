from collections import defaultdict

def pair_scores(request):
    score=defaultdict(int)
    for e in request['evidence']:
        if e['active']: score[tuple(sorted((e['a'],e['b'])))]+=e['weight']
    return score

def solve(request):
    ids=sorted(r['id'] for r in request['records'])
    return {'clusters':[{'records':[i],'score':0} for i in ids],'score':0}
