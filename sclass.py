from os import system
import requests
from extract import Extractor
from time import sleep

ext = Extractor()
for i in range(1, 10):
    print(f"process page-{i}")
    url = f"https://www.lightnovelworld.com/novel/the-s-classes-that-i-raised/chapter-{i}"
    system(f'curl {url} -o sample.html')
    data = open('sample.html', 'rb').read().decode('utf-8', errors='ignore')
    if len(data) < 50:
        print('web response none')
        break
    extracted = ext.extract_content(data)
    final = []
    extracted = extracted.replace('.', '.  \n').replace('” ', '').replace('“',"  \n").replace('\\', '').replace('/', '').replace('>', '>  ')
    data = [row.lstrip() for row in extracted.split('\n') if row and 'lightn' not in row and 'velworld' not in row and row.strip() != 'com']
    extracted = "\n".join(data[:-8])
    extracted = f"# The S-Classes That I Raised {i}  \n" + extracted
    md_file = open(f"docs/SClassIRised-{i}.md", 'wb')
    md_file.write(extracted.encode('utf8', errors='ignore'))
    print(f'create file doc/SClassIRised-{i}.md')
    sleep(30)
