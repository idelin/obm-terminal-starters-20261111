import json,subprocess,tempfile,time
from pathlib import Path
ALPHABET='aeiouptkbdgvrshnm'
def command(args,deadline=None):
    timeout=20 if deadline is None else deadline-time.monotonic()
    if timeout<=0:raise TimeoutError("word budget")
    return subprocess.run(args,check=True,capture_output=True,text=True,timeout=timeout).stdout

def transduce(word,path,deadline=None):
    with tempfile.TemporaryDirectory() as td:
        d=Path(td);lines=[f'{i} {i+1} {ALPHABET.index(c)+1} {ALPHABET.index(c)+1}' for i,c in enumerate(word)]+[str(len(word))]
        (d/'input.txt').write_text('\n'.join(lines)+'\n')
        command(['fstcompile',str(d/'input.txt'),str(d/'input.fst')],deadline)
        command(['fstcompose',str(d/'input.fst'),str(path),str(d/'composed.fst')],deadline)
        command(['fstproject','--project_type=output',str(d/'composed.fst'),str(d/'output.fst')],deadline)
        command(['fstrmepsilon',str(d/'output.fst'),str(d/'noeps.fst')],deadline)
        command(['fstdeterminize',str(d/'noeps.fst'),str(d/'det.fst')],deadline)
        text=command(['fstprint','--numeric=true',str(d/'det.fst')],deadline)
        arcs={};final=set()
        for line in text.splitlines():
            fields=line.split();state=int(fields[0])
            if len(fields)<=2:
                if len(fields)==2 and float(fields[1])!=0:raise ValueError('nonzero weight')
                final.add(state)
            else:
                if len(fields)==5 and float(fields[4])!=0:raise ValueError('nonzero weight')
                if fields[2]!=fields[3]:raise ValueError('output acceptor')
                label=int(fields[2])
                if not 1<=label<=len(ALPHABET):raise ValueError('output label')
                arcs.setdefault(state,[]).append((int(fields[1]),ALPHABET[label-1]))
        state=0;seen=set();out=[]
        while state not in seen:
            seen.add(state);nexts=arcs.get(state,[])
            if state in final:
                if nexts:raise ValueError('multiple outputs')
                return ''.join(out)
            if len(nexts)!=1:raise ValueError('nonfunctional transducer')
            state,char=nexts[0];out.append(char)
        raise ValueError('output cycle')

def apply(bundle,branch,word):
    deadline=time.monotonic()+10
    bundle=Path(bundle);manifest=json.loads((bundle/'pipeline.json').read_text())
    if manifest['alphabet']!=ALPHABET:raise ValueError('alphabet')
    for file in manifest[branch]:
        if Path(file).name!=file or not file.endswith('.fst'):raise ValueError('file path')
        word=transduce(word,bundle/file,deadline)
    return word
