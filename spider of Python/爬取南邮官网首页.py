
import requests

def getHtml(url):
      try:
            r=requests.get(url,timeout=30)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            return r.text
      except:
            return "ERROR"
if __name__=="__main__":
      url="http://www.njupt.edu.cn"
      print(getHtml(url[:1000]))

      
