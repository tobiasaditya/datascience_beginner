import matplotlib.pyplot as plt
from matplotlib import style

style.use("bmh")
x1=[2,4,6]
y1=[3,7,9]

x2=[1,2,3]
y2=[5,10,15]

x3=[1,4,7]
y3=[4,5,9]

plt.bar(x1,y1)
plt.bar(x2,y2)
plt.bar(x3,y3)

plt.title("Bar Graph")
plt.xlabel("Age (Years)")
plt.ylabel("DoB")


plt.show()

