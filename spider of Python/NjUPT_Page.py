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

      print(soup.meta.string)

      print("\nI will take the link of 'lacie':\n")
      link1=soup.find('meta',content=re.compile('800x6002017年6月25日（周日）'))
      print(link1.name,link1['content'],link1.get_text())



      #for meta in soup.find_all('head'):
       #     print(meta)
       
def main():
      url="http://www.njupt.edu.cn/2017/0622/c72a108711/page.htm"
      html=getPage(url)
      #print("access the Page as following:\n")
      accessHtml(html)
      
main()
      
