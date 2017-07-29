import requests

def getJD(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text[:1000]
	except:
		return "ERROR\n"

if __name__=="__main__":
	url="https://item.jd.com/3133859.html#crumb-wrap"
	print(getJD(url))