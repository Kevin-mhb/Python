

import xlsxwriter

#1.创建一个Excel文件

work=xlsxwriter.Workbook("text_0.xlsx")#文件名+路径

#创建图表
chart=work.add_chart({'type':'column'})

#column柱状图、area面积图、bar条形图、line折线图、radar雷达图
#不可以添加空图表

#2.创建一个表格
worksheet=work.add_worksheet("while")


#添加数据--声明一个数据容器
title="abcdefghij"
data=[1,2,3,4,5,6,7,8,9,10]
for i,j in enumerate(title):
	point="B%d"%(i+1)
	worksheet.write(point,j)
for i,j in enumerate(data):
	point="C%d"%(i+1)
	worksheet.write(point,j)
	
#为图表添加数据
chart.add_series(
	{
		"categories":"=while!$b$1:$b$10",#类别biao签的范围
		"values":"=while!$c$1:$c$10",
		"line":{"color":"blue"}
	}
)
worksheet.insert_chart("B11",chart)




#3.修改格式

	#3.1 修改表格的格式
worksheet.set_column("A:A",20)
	#3.2修改内容的格式
bold=work.add_format({"bold":True})#定义一个内容样式

#4.写入内容
	#写入字符
worksheet.write("A1","while",bold)
	#写入图片
#SBworksheet.insert_image("A2","branches.png")
	#写入函数SUM
worksheet.write("A3",2,bold)
worksheet.write("A4",34,bold)
worksheet.write("A5","=SUM(A3:A4)",bold)



#close file
work.close()
