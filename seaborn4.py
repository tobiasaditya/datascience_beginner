import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset("tips")

print(database)

graph=sb.FacetGrid(database,col="sex",hue="smoker")
graph.map(plt.scatter,"total_bill","tip")

plt.show()
