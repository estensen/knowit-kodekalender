import json
from hashlib import md5


def compute_md5(input: str) -> str:
    h = md5(input.encode())
    return h.hexdigest()


data = []
filename = 'input-hashchain.json' 
with open(filename) as f:
    lines = f.read()
    data = json.loads(lines)

answer = []
prev_hash = compute_md5('julekalender')
while data:
    for el in data:
        print(el)
        c, hash = el['ch'], el['hash']
        
        next_hash = compute_md5(prev_hash + c)
        if hash == next_hash:
            answer.append(c)
            data.remove(el)
            prev_hash = hash

print(''.join(answer))

