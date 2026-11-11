import hmac,hashlib

def token(secret,identity):
    a,b=identity['tenant'].encode(),identity['subject'].encode()
    raw=str(len(a)).encode()+b':'+a+str(len(b)).encode()+b':'+b
    return hmac.new(secret.encode(),raw,hashlib.sha256).hexdigest()

def solve(request):
    out={}
    for name,rows in request['tables'].items():
        out[name]=[{'redacted':False,'token':token(request['secret'],r['identity']),'payload':r['payload']} for r in rows]
    return {'tables':out}
