import requests

file_url = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-crisscross.txt'

r = requests.get(file_url)
data = r.text

x, y = 0, 0

for i in range(0, len(data)-1, 2):
    amount = int(data[i]) 
    direction = data[i+1]
    
    if direction == 'H':
        x += amount
    elif direction == 'V':
        x -= amount
    elif direction == 'B':
        y -= amount
    elif direction == 'F':
        y += amount

print(f'[{x},{y}]')

