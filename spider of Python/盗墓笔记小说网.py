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

	for fulu
	

def main():
	url="http://seputu.com"
	html=getPage(url)
	accessHtml(html)

main()
