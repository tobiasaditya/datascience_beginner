import matplotlib.pyplot as plt
from matplotlib import style

style.use("bmh")

numbers=[10,20,30,40,50,60,70,80,90]
jumps = [0,15,30,45,60,75,90,105]

plt.title("Histogram Example")
plt.xlabel("Test-x label")
plt.ylabel("Test-y label")

plt.hist(numbers,jumps,histtype="bar")
#plt.hist(numbers,jumps,histtype="step")

plt.show()