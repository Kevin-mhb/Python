'''
import requests

def getAmazon(url):
	try:
		kv={'user-agent':'Mozillia/5.0'}
		r=requests.get(url,headers=kv)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text[:500]
	except:
		return "Error!\n"
		
if __name__=="__main__":
	url="https://www.amazon.cn/%E6%9C%AA%E6%9D%A5%E7%AE%80%E5%8F%B2-%E5%B0%A4%E7%93%A6%E5%B0%94-%E8%B5%AB%E6%8B%89%E5%88%A9/dp/B01MZ4Z5DQ/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr="
	print(getAmazon(url))
'''
'''
import requests

def askBaidu(url,keyword):
	try:
		kv={'wd':keyword}	#baidu的关键词搜索链接为：http://www.baidu.com/s?wd=<keyword>
		r=requests.get(url,timeout=30,params=kv)
		r.raise_for_status()
		r.apparent_encoding
		return r.text[:500]
	except:
		return "Error !\n"

def main():
	print("Please Enter Your keyword:\n")
	keyword=str(input())
	url="http://www.baidu.com"
	print(askBaidu(url,keyword))

main()
'''

import requests
import os

url="http://image.nationalgeographic.com.cn/2015/1026/20151026120947696.jpg"
root="C://Users//马海斌//Desktop//文件//movies & photos//图片//"
path=root+url.split('/')[-1]

try:
      if not os.path.exists(root):
            os.mkdir(root)
      if not os.path.exists(path):
            r=requests.get(url)
            with open(path,'wb') as f:
                  
                  f.write(r.content)
                  f.close()
                  print("文件保存成功")
      else:
            
            print("文件已存在")
      
except:
      print("爬取失败")
