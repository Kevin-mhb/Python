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

	links_part = soup.find_all('div',frag="窗口4")  
    
	for links in links_part:
		a = links.find_all('a')
		for one in a:
			href = one.attrs['href']
			href_list.append(href)
			news_title = one.get_text()
			news_title_list.append(news_title)
			print(news_title,end="")
			print("\tjwc.njupt.edu.cn"+href,end="\n\n")
	return href_list,news_title_list

'''
def getText(news_title_list，href_list):
	for href in href_list:
		html=requests.get(href)
		metadata=html.text
		soup=BeautifulSoup(metadata,"html.parser")
		file=soup.find_all('meta',"name="description"")
		text=file.attrs['content']
		print(text)
'''


def main():
	news_title_list=[]
	href_list=[]
	ulist=[]
	url="http://jwc.njupt.edu.cn/1594/list.htm"
	html=getPage(url)
	accessHtml(html,ulist)
	print(len(news_title_list))
	print(len(href_list))
	print(news_title_list[6]+href_list[6])
	#getText(news_title_list,href_list)


main()




