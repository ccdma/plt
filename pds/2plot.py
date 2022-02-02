import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./out/all.csv", delimiter="\t")
data = data.query("stddev == 0.01 & samplings == 3000")

x = data.loc[:, "signals"]
y = data.loc[:, "ber"]
# a, b, c = np.polyfit(x, y, 2)

plt.yscale('log')
plt.plot(x, y)
# plt.plot(x, a*x+b)
plt.xlabel("K: Number of Users")
plt.ylabel("BER")
plt.show()
