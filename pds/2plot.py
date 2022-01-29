import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./out/all.csv", delimiter="\t")
data = data.query("stddev == 0.0 & signals == 10")

x = data.loc[:, "samplings"]
y = data.loc[:, "time(ms)"]
a, b, c = np.polyfit(x, y, 2)

# plt.yscale('log')
plt.plot(x, y)
# plt.plot(x, a*x+b)
plt.xlabel("Code Length")
plt.ylabel("time[ms]")
plt.show()