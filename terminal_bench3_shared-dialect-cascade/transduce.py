V=set('aeiou')
def match(context,phone,boundary):
    if context=='':return True
    if context=='#':return boundary
    if boundary:return False
    if context=='V':return phone in V
    if context=='C':return phone not in V
    return phone==context
def apply(word,rule):
    out=[]
    for i,c in enumerate(word):
        yes=c==rule['src'] and match(rule['left'],word[i-1] if i else '',i==0) and match(rule['right'],word[i+1] if i+1<len(word) else '',i+1==len(word))
        out.append(rule['dst'] if yes else c)
    return ''.join(out)
def cascade(word,ids,rules):
    for rid in ids:word=apply(word,rules[rid])
    return word
