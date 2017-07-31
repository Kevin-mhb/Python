import requests
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text

soup=BeautifulSoup(demo,"html.parser")

for child in soup.body.contents:#此处遍历的是 body 标签的父辈标签； 
	
	print(child,end='\t')
