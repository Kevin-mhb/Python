import requests
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text 

soup=BeautifulSoup(demo,'html.parser')#html.parser是解释器
print(soup.prettify())
