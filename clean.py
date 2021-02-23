from license import p, PocketException

try:
    data = p.get(state='archive', offset=0, count=5000)
    dta = data[0]
    data = dta.get('list')
    index = 0
    for item in data:
        url = data[item].get('given_url')
        index += 1
        print(f'[{index}] remove {url} {item}')
        p.delete(item, 0)
    p.commit()
except PocketException as e:
    print(str(e))
