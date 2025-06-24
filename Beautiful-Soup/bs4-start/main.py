from bs4 import BeautifulSoup

with open('website.html') as website:
    content=website.read()

soup=BeautifulSoup(content, 'html.parser')
print(soup.h3)
print(soup.find_all(name='li'))
all_anchor_tags=soup.find_all(name='a')

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))
