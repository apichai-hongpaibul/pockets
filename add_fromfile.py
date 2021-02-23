from license import p, PocketException
from time import sleep


with open('link.txt', 'r') as f:
    rows = f.readlines()
    for row in rows:
        content = row[:-1]
        print(content)
        p.add(content)
        sleep(1)
