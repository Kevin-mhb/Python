#coding:utf-8

import xlsxwriter

work=xlsxwriter.Workbook("py_0.xlsx")

worksheet=work.add_worksheet()

expenses = (
	['item','    num','    value'],
    ['Rent', 1000,230],
    ['Gas',   100,356],
    ['Food',  300,238],
    ['Gym',    50,100],
)

row = 0
col = 0

for item, num,value in (expenses):
    worksheet.write(row, col,item)
    worksheet.write(row, col + 1, num)
    worksheet.write(row, col + 2, value)
    row += 1

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')
worksheet.write(row, 2, '=SUM(C1:C4)')

work.close()
