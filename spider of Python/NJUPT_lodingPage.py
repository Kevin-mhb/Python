#抓取南邮通知中心的通知列表，并且输出连接

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

	for a in soup.find_all('a'):
		print(a.string,end="\n\n")

	for link in soup.find_all('a'):
		print(list("http://www.njupt.edu.cn"+link.get('href'),end="\n\n"))

	'''
	for child in soup.table.children:
		print (child.name)
	if isinstance(tbody,bs4.element.Tag):
		tds=tbody('td')
		newsList=ulist.append([tds[0].string,tds[1].string])
		print(newsList)'''

def main():
	ulist=[]
	url="http://www.njupt.edu.cn/72/list.htm"
	html=getPage(url)
	accessHtml(html,ulist)

main()
