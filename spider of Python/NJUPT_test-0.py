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

	for tbody in soup.find_all(class_="listColumn wrapper"):
		for a in soup.find_all('a'):
			print(a.string)
		for link in soup.find_all('a'):
	   		print("http://www.njupt.edu.cn"+link.get('href'))



def main():
	ulist=[]
	url="http://www.njupt.edu.cn/72/list.htm"
	html=getPage(url)
	accessHtml(html,ulist)

main()