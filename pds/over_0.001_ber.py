import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./out/all.csv", delimiter="\t")

data = data.query("stddev == 0.01")
out = []

smpls = list(set(data["samplings"].tolist()))
smpls.sort()
for smpl in smpls:
	targets = data.query(f"samplings == {smpl}")
	if targets.size < 2:
		raise Exception("size < 2")
	targets = targets.sort_values("signals")
	for i, target in targets[::-1].iterrows(): # reverse order
		if target["ber"] < 0.001:
			out.append(target.to_dict())
			break

over0001 = pd.DataFrame(
	data=out
)

x = over0001.loc[:, "signals"]
y = over0001.loc[:, "time(ms)"]
a, b = np.polyfit(x, y, 1)
plt.scatter(x, y)
print(f"y={a}x+{b}")

plt.plot(x, a*x+b)
plt.xlabel("Number of Users")
plt.ylabel("Code Length")
plt.show()
# over0001.to_csv("./out/over0001.csv")
