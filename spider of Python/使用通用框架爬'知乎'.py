import requests

def getHTMLText(url):
      try:
            r=requests.get(url,timeout=30)
            r.raise_for_status()#response函数
            r.encoding=r.apparent_encoding
            return r.text
      except:
            return "产生异常\n"

if __name__=="__main__":
      url="http://www.zhihu.com"
      print(getHTMLText(url))
