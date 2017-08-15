import requests
import bs4
from bs4 import BeautifulSoup
import re

r=requests.get("http://www.jianshu.com",timeout=30)
demo=r.text

soup=BeautifulSoup(demo,"html.parser")
t=soup.find_all(string=re.compile(" 生活家"))
print(t)
