元组（tuple）

example:
	tuple1=12,34,'ma',890
	emptyTuple=()

notes:
	与列表不同的是元组的元组值一旦确定就不能被修改


列表（list）

example：
	list1=[1,2,3,4,]
	emptyList=[]

control lists:
	1.元素赋值，list[2]=45
	2.删除元素，del list1[2]
	3.分片操作，list_2[6:] = list("hello")
	4.索引列表,list1[3]
	5.循环枚举，for i in list1:
					print(i)

Built-In-Functions:(均以list1为例说明)
	1.list1.append(34)//在原列表最后添加34这个元素
	2.list1.extend([34,45,456,])//可以在列表的末尾一次性添加多个元素
	3.list1.count(3)//用来统计某个元素在列表中出现的次数
	4.list1.index()//可以从列表中找出索引位置上元素的值
	5.list1.insert(2,909)//可以从列表中找出索引位置上元素的值,在2处插入909
	6.list1.pop()//用于移除列表中的一个元素，默认是最后一个，并且返回该元素的值
	7.list1.remove(2)//用于移除列表中某个元组值的第一个匹配项
	8.list1.reverse()//将列表中的元素逆序
	9.list1.sort()//用于给列表中的元素排序，默认升序


