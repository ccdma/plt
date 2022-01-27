import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./out/all.csv", delimiter="\t")
data = data.query("stddev == 0.05 & samplings == 3000")

x = data.loc[:, "signals"]
y = data.loc[:, "ber"]
a, b = np.polyfit(x, y, 1)
plt.yscale('log')
plt.scatter(x, y)
plt.plot(x, a*x+b)
plt.show()
