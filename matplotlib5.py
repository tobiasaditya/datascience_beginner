import matplotlib.pyplot as plt
from matplotlib import style

style.use("bmh")

x=[3,6,7,9,10]
y=[5,10,25,3,1]

plt.scatter(x,y)

plt.title("Scatter Example")
plt.xlabel("Test X")
plt.ylabel("Test Y")

plt.show()