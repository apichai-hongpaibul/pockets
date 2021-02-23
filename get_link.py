import requests
import lxml.html

data = []
r = requests.get("https://turb0translation.blogspot.com/p/blog-page.html")
root = lxml.html.fromstring(r.content)
#links = root.xpath('//li[@title="Bookmark Chapter"]/a')
links = root.xpath('//*[@id="post-body-6306637228371808967"]/div[2]/a')
for link in links:
    print(f"{link.text} = {link.get('href')}")
    data.insert(0, link.get('href'))
links = root.xpath('//*[@id="post-body-6306637228371808967"]/a')
for link in links:
    print(f"{link.text} = {link.get('href')}")
    data.insert(0, link.get('href'))
links = root.xpath('//*[@id="post-body-6306637228371808967"]/div/a')
for link in links:
    print(f"{link.text} = {link.get('href')}")
    data.insert(0, link.get('href'))
with open("link.txt", "w+") as f:
    for row in data:
        f.write(row + '\n')
