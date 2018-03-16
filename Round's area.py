#计算圆的面积

r=int(input("请输入圆的半径：\n"))
area = 3.14 * r ** 2
print("area=%f" % area)
print("range is {} area is {} ".format(r,area))

print("{1},{2},{0}".format(4,5,6))               #格式化输出
print("{0:<10},{1:<10},{2:<10}".format(4,5,6))   # < 居左对齐；> 居右对齐
print("{:.3f}".format(4.214343523))
