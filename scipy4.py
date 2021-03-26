import numpy as np
import scipy as sp
from scipy import fft
from scipy import linalg


#FFT
var1 = np.array([[2,4,6,8],[1,3,5,7]])
print(var1)

func1 = sp.fft(var1)
print(func1)

#Linear algebra
# A * X = B
#Solve for X!

arr1 = np.array([[1,3],[2,4]])
arr2 = np.array([[5,7],[6,8]])

print(arr1)
print(arr2)

func2 = sp.linalg.solve(arr1,arr2)
print(func2)

#arr1^-1
func3 = sp.linalg.inv(arr1)
print(func3)