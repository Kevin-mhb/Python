import requests

rul="http://m.ip138.com/ip.asp?ip="
try:
	r=requests.get(url+'202.204.80.112')
	r.raise_for_status()
	r.apparent_encoding
	print(r.text[-500:])
except:
	print("Error\n")
