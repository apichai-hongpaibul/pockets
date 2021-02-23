from license import p
from time import sleep


i = 2881
while i > 2752:
    content = f"https://boxnovel.com/novel/chaotic-sword-god/chapter-{i}/"
    print(f'add {content}')
    p.add(content)
    i -= 1
    sleep(1)
