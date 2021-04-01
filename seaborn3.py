import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset("flights")
print(database)

#Default kindnnya = "strip"
#sb.catplot(x="month",y="passengers",data=database,kind='violin')
sb.catplot(x="month",y="passengers",data=database,kind='box')


plt.show()