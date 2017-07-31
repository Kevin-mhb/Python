'''
import requests
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")
demo=r.text

soup=BeautifulSoup(demo,"html.parser")
print(soup.prettify())
print("\n\n")
for parent in soup.p.parents:

      print(parent)
'''

import requests
from bs4 import BeautifulSoup
import re

def getHtml(url):
	try:
		r=requests.get(url,timeout=10)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		demo=r.text
		return demo
	except:
		return "Error!\n"

def takeBS4(demo):
      soup=BeautifulSoup(demo,'html.parser')

      print("遍历tag:\n")
      for tag in soup.find_all():
            print(tag.name[:10])

      print("查找tr标签的信息:\n")
      for tag in soup.find_all(re.compile('tr')):
            print(tag.name)
              
      print("search the tags with 'link':\n")
      for link in soup.find_all(id=re.compile('link')):
            print(link)
              
      print("All words including '南京':\n")
      for string in soup.find_all(string=re.compile("南京" )):
            print(string)

if __name__=="__main__":
      url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
	
      demo=getHtml(url)
      print(demo[:1000])
      takeBS4(demo)

