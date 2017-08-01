
def printUnivList(ulist,50):
	print("{:^20}\t{:^12}\t{:^20}".format("排名","学校","总分"))
	for i in range(num):
		u=ulist[i]
		print("{:^20}\t{:^12}\t{:^20}".format(u[0],u[1],u[2]))