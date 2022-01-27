import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./out/all.csv", delimiter="\t")
data = data.query("stddev == 0.05")
smpls = data["samplings"].unique()
_mins = data.iloc[0:0] # 型が同じ、空のDataFrameを作成
smpls.sort()
for smpl in smpls:
	targets = data.query(f"samplings == {smpl}")
	_mins = _mins.append(data.loc[targets["ber"].idxmin()])

a,b = np.polyfit(_mins.loc[:, "samplings"], _mins.loc[:, "signals"], 1)
print(f"y={a}x+{b}")
plt.scatter(_mins.loc[:, "samplings"], _mins.loc[:, "signals"])
plt.xlabel("Code Length")
plt.ylabel("K: Number of Users")
plt.plot(_mins.loc[:, "samplings"], a*_mins.loc[:, "samplings"]+b)
plt.show()
