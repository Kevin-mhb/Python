import requests

def askBaidu(url,keyword):
	try:
		kv={'wd':'keyword'}	#baidu的关键词搜索链接为：http://www.baidu.com/s?wd=<keyword>
		r=requests.get(url,timeout=30,params=kv)
		r.raise_for_status()
		r.apparent_encoding
		return r.text[:500]
	except:
		return "Error !\n"

def main():
	print("Please Enter Your keyword:\n")
	keyword=str(input())
	url="http://www.baidu.com/s"
	print(askBaidu(url,keyword))

main()