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