# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

#data definition
height = [178,165,168,152,175,175,165,162,164,170,169,155,153,162,168]
weight = [63,62,69,41,71,61,62,48,52,55,69,48,44,49,69]

def sumorg(list):
  sumorg = 0
  for i in range(len(list)):
   sumorg += list[i]
  return sumorg

def avrg(sumarg,list):
  return sumarg / len(list)

def cov(sum1,sum2,list1,list2):
  cov = 0
  for i in range(len(list1)):
    cov += (list1[i] - avrg(sum1,list1)) * (list2[i] - avrg(sum2,list2)) / len(list1)
  return cov

def var(list,avrg):
  var = 0
  for i in range(len(list)):
    var += (list[i] - avrg) * (list[i] - avrg) / len(list)
  return var

height_sum = sumorg(height)
weight_sum = sumorg(weight)

#print(cov(height_sum,weight_sum,height,weight))
#print(var(height,avrg(height_sum,height)))

a = cov(height_sum,weight_sum,height,weight)/var(height,avrg(height_sum,height))
b = avrg(weight_sum,weight) - a * avrg(height_sum,height)

#print(a)
#print(b)

plt.scatter(height,weight)
x = np.arange(150,180,0.01)
y = a * x +b
plt.plot(x,y)
plt.show()

#print(height_sum)
#print(weight_sum)
#print(avrg(height_sum,height))
#print(avrg(weight_sum,weight))