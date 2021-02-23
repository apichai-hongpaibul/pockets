from license import p, PocketException

try:
    data = p.get(offset=0, count=100)
    dta = data[0]
    data = dta.get('list')
    for item in data:
        url = data[item].get('given_url')
        print(f'remove {url} {item}')
        p.delete(item, 0)
    p.commit()
except PocketException as e:
    print(e)
