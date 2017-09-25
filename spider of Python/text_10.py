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


def accessHtml(html,news_title_list,href_list):
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
	return news_title_list,href_list


def getText(news_title_list,href_list):
	dicto={}
	keys=news_title_list
	values=href_list
	dicto=dict(zip(keys,values))
	print(dicto)
	file_news = open('C:/Users/马海斌/Desktop/文件/programing/Python/爬取文件/南邮教务处.txt',"w")
	for (k,v) in dicto.items():
		#print(k+"http://jwc.njupt.edu.cn/"+v+"\n\n")#测试
		text=k+"http://jwc.njupt.edu.cn/"+v+"\n\n"
		file_news.write(text)
	
	file_news.close()

	"""
		href_list.pop(0)
		for href in href_list:
		url2="http://jwc.njupt.edu.cn"+href

		print(url2)
		html=requests.get(url2,timeout=30)	#此行出现Bug，可能是URL未传过来
		metadata=html.text
		soup=BeautifulSoup(metadata,"html.parser")
		file=soup.find_all('meta',name="description")
		text=file.attrs['content']
		print(text)
	"""


def main():
	news_title_list=[]
	href_list=[]
	url="http://jwc.njupt.edu.cn/1594/list.htm"
	html=getPage(url)
	accessHtml(html,news_title_list,href_list)
	print(len(news_title_list))
	print(len(href_list))
	getText(news_title_list,href_list)


if __name__=='__main__':
	main()

