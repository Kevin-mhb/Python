

import xlsxwriter

#1.创建一个Excel文件

work=xlsxwriter.Workbook("text_0.xlsx")#文件名+路径

#2.创建一个表格
worksheet=work.add_worksheet("while")

#3.修改格式
#3.1 修改表格的格式
worksheet.set_column("A:A",20)
#3.2修改内容的格式


#3.写入内容
worksheet.write("A1","while")





#close file
work.close()
