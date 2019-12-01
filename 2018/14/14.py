import requests
from operator import itemgetter

file_url = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-bounding-crisscross.txt'

r = requests.get(file_url)
data = r.text.strip('\n')

directions = {
    'H': (1, 0),
    'V': (-1, 0),
    'F': (0, 1),
    'B': (0, -1)
}

path = set()
max_x, max_y, min_x, min_y = 0, 0, 0, 0
x, y = 0, 0
path.add((x, y))

for i in range(0, len(data), 2):
    amount = int(data[i])
    direction = data[i+1]

    for j in range(amount):
        x += directions[direction][0]
        y += directions[direction][1]
        path.add((x, y))


max_x = max(path, key=itemgetter(0))[0]
max_y = max(path, key=itemgetter(1))[1]
min_x = min(path, key=itemgetter(0))[0]
min_y = min(path, key=itemgetter(1))[1]

box_size = (max_x - min_x + 1) * (max_y - min_y + 1) 
visited = len(path)
not_visited = box_size - visited

magic_number = visited / not_visited
print(f'{magic_number:.16f}')

