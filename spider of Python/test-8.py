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
      soup=BeautifulSoup(html,"html.parser")
      for tr in soup.find('tbody').children:          #tr 标签
            if isinstance(tr,bs4.element.Tag):
                  tds=tr('td')                        #td
                  ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printu(ulist,num):
      tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
      print(tplt.format("排名","学校名称","总分"，chr(12288)))
      for i in range(num):
            u=ulist[i]
            print(tplt.format(u[0],u[1],u[2],chr(12288)))
            
def main():
      uinfo=[]
      url="http://www.zuihaodaxue.cn/dingjianrencaipaiming2017.html"
      html=gethtml(url)
      fillu(uinfo,html)
      printu(uinfo,50)


main()

#http://www.zuihaodaxue.cn/dingjianrencaipaiming2017.html

