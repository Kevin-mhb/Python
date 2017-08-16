import requests
import re
import bs4
from bs4 import BeautifulSoup

def getPage(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "Error!\n"

def accessHtml(html,ulist):
	soup=BeautifulSoup(html,'html.parser')

	for content in soup.find_all('meta'):
		print(content.string)


def main():
	ulist=[]
	url="http://www.njupt.edu.cn/2017/0622/c72a108725/page.htm"
	html=getPage(url)
	accessHtml(html,ulist)

main()