#利用蒙特卡洛统计方法计算圆周率的值

from random import random
from math import sqrt
from time import clock

DARTS=10000000  #DARTS是抛洒点的数量
hits=0

clock()

for i in range(1,DARTS):
      x,y=random(),random()
      dist=sqrt(x**2+y**2)

      if dist<=1.0:
            hits=hits+1

pi=4*(hits/DARTS)

print("pi's value is : %s" % pi)
print("running time is : %-5.5ss" % clock())
