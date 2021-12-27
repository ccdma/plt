import pandas as pd

csv = pd.read_csv("./out/r.csv", delimiter="\t")
out = []

smpls = list(set(csv["samplings"].tolist()))
smpls.sort()
for smpl in smpls:
	targets = csv.query(f"samplings == {smpl}")
	if targets.size < 2:
		raise Exception("size < 2")
	targets = targets.sort_values("signals")
	for i, target in targets[::-1].iterrows(): # reverse order
		if target["ber"] < 0.001:
			out.append(target.to_dict())
			break

csvo = pd.DataFrame(
	data=out
)
csvo.to_csv("./out.rw.csv")
