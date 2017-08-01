import requests
import re
from bs4 import BeautifulSoup
import bs4


def main():
	url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
	uinfo=[]
	html=getHtmlText(url)
	fillUnivList(html,info)
	printUnivList(unifo,30)

main()