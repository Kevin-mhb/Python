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

def accessHtml(html):
	soup=BeautifulSoup(html,'html.parser')

	print(soup.prettify())
	'''
	links0=soup.find_all('link')
	for link in links0:
		print(link.name,link['href'],link.get_text)

	link1=soup.find('div',class_="wrapper" )
	print(link1.name,link1.get_text())
	'''

def main():
	url="http://www.njupt.edu.cn/72/list.htm"
	html=getPage(url)
	accessHtml(html)

main()
