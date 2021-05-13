from license import p
from time import sleep


i = 1341
while i >= 1244:
    content = f"https://boxnovel.com/novel/the-legendary-mechanic-boxnovel/chapter-{i}"
    print(f'add {content}')
    p.add(content)
    i -= 1
    sleep(1)
