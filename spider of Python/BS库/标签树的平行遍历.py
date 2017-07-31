#标签树的平行遍历基于相同的父亲标签

import requests
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text

soup=BeautifulSoup(demo,"html.parser")

for sibling in soup.a.next_siblings:#此处遍历的是 a 标签的向下的平行标签； （next_siblings/previous_siblings)
	print(sibling)
