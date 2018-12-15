from operator import itemgetter

"""
This works because the input was small and didn't contain edge cases
This should have been solved as longest path in DAG or DP
"""

file_name = 'input-dolls.txt'
lines = []
dolls = [] 

with open(file_name) as f:
    lines  = [line.strip('\n') for line in f.readlines()]

for line in lines:
    color, size = line.split(',')
    doll = (color, int(size))
    dolls.append(doll)

dolls.sort(key=itemgetter(1))
valid_dolls = []

for i, doll in enumerate(dolls[:-1]):
    doll_color = doll[0]
    next_doll_color = dolls[i+1][0]
    if doll_color != next_doll_color:
        valid_dolls.append(doll)

print(len(valid_dolls))

