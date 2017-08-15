import requests
from bs4 import BeautifulSoup
import re

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text

soup=BeautifulSoup(demo,"html.parser")

print(soup.prettify())

#find_all()方法中的五个参数---name
for tag in soup.find_all(re.compile('b')):
	print(tag.name)

#find_all()方法中的五个参数---attrs
for link in soup.find_all(id=re.compile('link')):
	print(link)

#find_all()方法中的五个参数---recursive


#find_all()方法中的五个参数---string
soup.find_all(string=re.compile("Pyhton"))
