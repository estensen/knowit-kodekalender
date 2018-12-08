from sys import argv
from urllib.request import urlopen


try:
    url = argv[1]
    filename = argv[2]
except IndexError:
    print('Provide a url to download from and a filename')
    exit(1)


with open(filename, 'a') as f:
    for line in urlopen(url):
        data = line.decode('utf-8')
        f.write(data)

