#输出所有三位数的素数
#使用for循环

for n in range(100,1000):
      for i in range(2,n):
            if n%i==0:
                  break


      else:
            print(n)


