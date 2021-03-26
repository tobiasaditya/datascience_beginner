import scipy as sp
from scipy import integrate

var1 = lambda x:x**3
func1 = integrate.quad(var1,0,6)

print(func1)

var2 = lambda y,x : x*y**4
#0,6 batas integral thd x, 0,1 batas integral thd y
func2=integrate.dblquad(var2,0,6,lambda i:0, lambda i:1)
print(func2)