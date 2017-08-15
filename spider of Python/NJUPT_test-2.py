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
		print

	id_soup = BeautifulSoup('<p id="my id"></p>')
	id_soup.p['id']
# 'my id'

def main():
	ulist=[]
	url="http://www.njupt.edu.cn/2017/0606/c72a107204/page.htm"
	html=getPage(url)
	accessHtml(html,ulist)

main()