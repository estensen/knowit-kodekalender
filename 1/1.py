import requests

input_path = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-vekksort.txt'

r = requests.get(input_path)
data = r.text.split()
nums = list(map(int, data))
prev = nums[0]
num_sum = 0

for el in nums: 
    el = int(el)
    if el >= prev:
        num_sum += el
        prev = el 

print(num_sum)
# 12920419

