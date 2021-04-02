import numpy as np
import matplotlib.pyplot as  plt

x = np.array([1,2,6,4,7,8,9,21,4,32,3,5,6,2])
y = np.array([10,20,16,14,17,18,19,31,14,22,13,15,16,12])

func1=np.polyfit(x=x,y=y,deg=1)

print(func1)

plt.plot(x,y,'o')
plt.plot(x,np.polyval(func1,x),'r-')
plt.show()