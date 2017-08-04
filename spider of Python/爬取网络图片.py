import requests
import os

#video's address:http://baishi.baidu.com/watch/06566430729376990497.html?&recFrom=site&list=24

url="http://baishi.baidu.com/watch/06566430729376990497.html?&recFrom=site&list=24"
root="C://Users//马海斌//Desktop//文件//movies & photos//"
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

