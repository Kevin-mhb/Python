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
	for tag in soup.find_all():#遍历tag
		print(tag.name)
	for tag in soup.find_all(re.compile('tr')):#查找tr标签的信息
		print(tag.name)
	for link in soup.find_all(id=re.compile('link')):#search the tags with 'link';
		print(link)
	for string in soup.find_all(string=re.compile("南京")):
		print(string)

if __name__=="__main__":
	url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
	
	demo=getHtml(url)
	print(demo)
	takeBS4(demo)

