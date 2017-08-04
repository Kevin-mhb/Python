import requests
from bs4 import BeautifulSoup
import re
import os

def getPage(url):
      try:
            r=requests.get(url,timeout=30)
            r.raise_for_status
            r.encoding=r.apparent_encoding
            return r.content
      except:
            return "Faile"
def accessHtml(html):
      soup=BeautifulSoup(html,"html.parser")

      txt=soup.meta.string
      print(txt)


      #for child in soup.head.contents:
       #     print(child.name,end='\t')

      #for meta in soup.find_all('head'):
       #     print(meta)
       
def main():
      url="http://www.njupt.edu.cn/2017/0622/c72a108711/page.htm"
      html=getPage(url)
      print("access the Page as following:\n")
      accessHtml(html)
      
main()
      
