import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.zuihaodaxue.cn/Sport-Science-Schools-and-Departments-2016.html")
demo=r.content[:5000]
soup=BeautifulSoup(demo,"html.parser")
#print(soup.prettify())
#print(soup.meta.title)
#print(soup.meta.name)
#print(soup.meta.parent.name)
#print(soup.meta.attrs)
#print(soup.meta.string)

for sibling in soup.title.next_sibling:
  print(sibling)

