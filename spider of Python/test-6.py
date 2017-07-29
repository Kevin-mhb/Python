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
