#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-19 20:00:30
# @Author  : kevin ma (mahaibin97@gmail.com)
# @Link    : http://www.aduxingzhe.com
# @Version : $Id$

import requests
import re
import bs4
from bs4 import BeautifulSoup

def getPage(url):
	headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
	try:
		r=requests.get(url,timeout=30,headers=headers)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "Error!\n"

def accessHtml(html,ulist):
	soup=BeautifulSoup(html,'html.parser')

	links_part = soup.find_all('table',align="left")  
    
	for links in links_part:
		a = links.find_all('a')
		for one in a:
			href = one.attrs['href']
			news_title = one.get_text()
			print(news_title,end="")
			print("\thttp://www.njupt.edu.cn"+href,end="\n\n")
	return href,news_title


def main():
	ulist=[]
	url="http://www.njupt.edu.cn/72/list.htm"
	html=getPage(url)
	accessHtml(html,ulist)




main()


