import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

database = sb.load_dataset("tips")
print(database)

sb.jointplot(x='tip',y='total_bill',data=database)
plt.show()