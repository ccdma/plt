import pandas as pd

csv = pd.read_csv("./out/r.csv")
out = []

smpls = list(set(csv["samplings"].tolist())).sort()
for smpl in smpls:
	targets = csv.query(f"samplings == {smpl}")
	if targets.size < 2:
		raise Exception("size < 2")
	out.extend(targets[-2:-1].to_dict(orient='records'))

csvo = pd.DataFrame(
	data=out
)
csvo.to_csv("./out.rw.csv")
