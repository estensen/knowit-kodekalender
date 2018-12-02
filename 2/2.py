import requests
from collections import defaultdict

file_path = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-rain.txt'
slopes = defaultdict(int)

r = requests.get(file_path)
data = r.text.split()

for line in data:
    point1, point2 = line.split(';')

    x1, y1 = point1[1:-1].split(',')
    x1, y1 = int(x1), int(y1)

    x2, y2 = point2[1:-1].split(',')
    x2, y2 = int(x2), int(y2)

    x = abs(x2-x1)
    y = abs(y2-y1)

    slope = (x1-x2) / (y1-y2)
    slopes[slope] += 1

print(max(slopes.values()))
# 324
