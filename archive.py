from license import p, PocketException

try:
    with open('archive.txt', 'w+') as f:
        data = f.read()
        item = data[:-1]
        p.readd(item, 0)
    p.commit()
    f.close()
except PocketException as e:
    print(e)
