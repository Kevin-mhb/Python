import requests
from bs4 import BeautifulSoup
import bs4
import re


def getHtmlText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "Error\n"


def fillUnivList(ulist,html):
	soup=BeautifulSoup(html,"html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds =tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[2].string])



def printUnivList(ulist,num):
	print("{:^20}\t{:^12}\t{:^20}".format("排名","学校名称","总分"))
    for i in range(num):
    	u=ulist[i]
    	print("{:^20}\t{:^12}\t{:^20}".format(u[0],u[1],u[2]))


def main():

	uinfo=[]
	url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
	html=getHtmlText(url)
	fillUnivList(unifo,html)
	printUnivList(unifo,20)

main()