from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal

data = pd.read_csv("./out/all.csv", delimiter="\t")
data = data.query("stddev == 0.01")

signals = data.loc[:, "signals"]
samplings = data.loc[:, "samplings"]
ber = data.loc[:, "ber"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(signals, samplings, ber)
# ax.set_title("Surface Plot")
ax.set_xlabel("Code Length")
ax.set_ylabel("K: Number of Users")
ax.set_zlabel("BER")

ax.set_zscale('log')
ax.set_zlim(10e-5, 1e-3)
fig.show()
plt.show()
