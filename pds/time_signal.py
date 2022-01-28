import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./out/all.csv", delimiter="\t")
data = data.query("stddev == 0.0 & samplings == 1000")

x = data.loc[:, "signals"]
y = data.loc[:, "time(ms)"]
a, b, c = np.polyfit(x, y, 2)

# plt.yscale('log')
plt.plot(x, y)
# plt.plot(x, a*x**2+b*x+c)
plt.xlabel("Number of Users")
plt.ylabel("time[ms]")
plt.show()
