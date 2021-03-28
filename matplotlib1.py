import matplotlib.pyplot as plt
from matplotlib import style

style.use("bmh")
#style.use("classic")
#style.use("dark_background")


x1=[2,4,8]
y1=[4,8,24]

x2=[3,6,9]
y2=[10,15,30]

plt.plot(x1,y1)
plt.plot(x2,y2)

plt.title("Test")
plt.xlabel("Time(s)")
plt.ylabel("Force(N)")

plt.show()
