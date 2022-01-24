from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal

df = pd.read_csv("out/r.csv", delimiter="\t")

signals = df.loc[:, "signals"]
samplings = df.loc[:, "samplings"]
ber = df.loc[:, "ber"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(signals, samplings, ber)
ax.set_title("Surface Plot")
ax.set_zscale('log')
ax.set_zlim(10e-5, 2e-3)
fig.show()
plt.show()
