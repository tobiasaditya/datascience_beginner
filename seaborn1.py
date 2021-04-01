import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset("diamonds")
print(database)

sb.distplot(database["carat"])
plt.show()