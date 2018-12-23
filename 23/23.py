import requests


def control_num(nums, arr):
    checksum = sum([int(a) * b for a, b in zip(nums, arr)]) % 11
    return 0 if checksum == 0 else 11 - checksum


def valid_date(nums):
    valid_days = '00' < nums[:2] <= '31'
    valid_month = nums[2:4] == '08'
    return valid_month and valid_days


def valid_sex(nums):
    return int(nums[8]) % 2 == 0


def valid_c1(nums):
    multiplication_row1 = [3, 7, 6, 1, 8, 9, 4, 5, 2]
    checksum = sum([int(a) * b for a, b in zip(nums, multiplication_row1)]) % 11
    c1 = 0 if checksum == 0 else 11 - checksum
    return c1 == int(nums[9])


def valid_c2(nums):
    multiplication_row2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    checksum = sum([int(a) * b for a, b in zip(nums, multiplication_row2)]) % 11
    c2 = 0 if checksum == 0 else 11 - checksum
    return c2 == int(nums[10])


url = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-fnr.txt'
r = requests.get(url)
# Sol1

count = 0
for num in r.text.splitlines():
    if valid_date(num) and valid_sex(num) and valid_c1(num) and valid_c2(num):
        count += 1
        print(num)

print(count)


# Sol2
multiplication_row1 = [3, 7, 6, 1, 8, 9, 4, 5, 2]
multiplication_row2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
nums = r.text.splitlines()
females = [num for num in nums if int(num[8]) % 2 == 0]
august = [num for num in females if num[2:4] == '08']
valid_days = [num for num in august if '00' < num[:2] < '32']
valid_c1 = [num for num in valid_days if control_num(num, multiplication_row1) == int(num[9])]
valid_c2 = [num for num in valid_c1 if control_num(num, multiplication_row2) == int(num[10])]


print(len(valid_c2))
