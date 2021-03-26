import numpy as np

var1=np.array([(2,4,6), (1,3,5)])
var2=np.array([(2,4,6), (1,3,5)])

var=var1+var2
print(var)
print(var.itemsize)
print(var.dtype)
print(var.ndim)
print(var.size)

#2 rows x 3 columns
print(var.shape)

#Reshape to 3 rows and 2 columns
var_t=var.reshape(3,2)
print(var_t)