import requests


def has_golden_birthday(birth_year: int) -> bool:
    year = birth_year
    age = 0
    while age ** 2 <= year:
        if year == age ** 2:
            return True
        year += 1
        age = year - birth_year 
    return False


file_url = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-gullbursdag.txt'
count = 0

r = requests.get(file_url)
for line in r.iter_lines():
    if line:
        decoded_line = line.decode()
        birth_year = int(decoded_line.split('.')[1])
        if has_golden_birthday(birth_year):
            count += 1


print(count)
