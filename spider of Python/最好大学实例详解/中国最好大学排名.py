import requests
import re
from bs4 import BeautifulSoup
import bs4

def gethtml(url):
      try:
            r=requests.get(url,timeout=30)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            return r.text

      except:
            return " "

def fillu(ulist,html):
      for tr in soup.find('tbody').children:          #tr      
      soup=BeautifulSoup(html,"html.parser")#标签
            if isinstance(tr,bs4.element.Tag):
                  tds=tr('td')                        #td
                  ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printu(ulist,num):
      print("{:^20}\t{:^12}\t{:^20}".format("排名","学校名称","总分"))
      for i in range(num):
            u=ulist[i]
            print("{:^20}\t{:^12}\t{:^20}".format(u[0],u[1],u[2]))
            
def main():
      uinfo=[]
      url="http://www.zuihaodaxue.cn/dingjianrencaipaiming2017.html"
      html=gethtml(url)
      fillu(uinfo,html)
      printu(uinfo,50)


main()

#http://www.zuihaodaxue.cn/dingjianrencaipaiming2017.html

