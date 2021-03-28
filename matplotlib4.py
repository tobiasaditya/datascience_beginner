import matplotlib.pyplot as plt
from matplotlib import style

style.use("classic")

foods = ["pizza","burger","sushi"]
sold = [20,10,30]
color = ["red","blue","yellow"]

plt.pie(sold,labels=foods,colors=color)

plt.title("Pie Chart")


plt.show()