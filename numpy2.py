import numpy as np

#Linspace, generate array consisting 37 numbers from 10 to 50
var2 = np.linspace(10,50,37)
print(var2)

var1=np.array([(2,4,6),(1,3,5),(21,41,61),(12,32,52),(23,43,63),(14,34,54)])
#indexing/slicing
print(var1[1])
print(var1[0,1])
print(var1[0:,1])
print(var1[1:,1])


print(var1.max())
print(var1.sum())



