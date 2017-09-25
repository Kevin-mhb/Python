#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-19 22:28:55
# @Author  : kevin ma (mahaibin97@gmail.com)
# @Link    : http://www.aduxingzhe.com
# @Version : $Id$

import os
import requests
from bs4 import BeautifulSoup
import bs4

"""
def main():

	try:

		r=requests.get("http://jwc.njupt.edu.cn/2017/0922/c1594a113548/page.htm",timeout=30)	
		r.raise_for_status()
		r.encoding=r.apparent_encoding
	except:
		return "Error"

	metadata=r.text
	#print(metadata)
	soup=BeautifulSoup(metadata,"html.parser")
	for meta in soup.find_all('meta'):
		meta.find('meta', name="description")

	#print(file)
	#text=file.attrs['content']
	#print(text)

if __name__=='__main__':
	main()

	"""

file_news = open('C:/Users/马海斌/Desktop/文件/programing/Python/爬取文件/南邮教务处.txt',"w")
file_news.write("NJUPT:the news of njupt is null!")
file_news.close()


list1=[1,2,3,4]
list2=[23,34,45,56]
dict0={}

dict0=dict(zip(list1,list2))
print(dict0)

"""
for i in range(len(list1)):
	dict0={list1[i]:list2[i]}

	"""