from license import p, PocketException

try:
    with open('archive.txt', 'r+') as f:
        item = f.read()[:-1]
        print(f're add {item}')
        p.readd(item, 0)
    p.commit()
except PocketException as e:
    print(e)
