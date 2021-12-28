import pandas as pd

csv = pd.read_csv("pds/r.csv", delimiter="\t")
merged = {}

key_str = "samplings"
group_str = "signals"
use_str = "cte"
groups = list(set(csv[group_str].tolist()))
groups.sort()
for group in groups:
	targets = csv.query(f"{group_str} == {group}")
	targets = targets.sort_values(key_str)
	for i, target in targets.iterrows():
		row = {key_str: target[key_str]}
		if target[key_str] in merged:
			row = merged[target[key_str]]
		row[f"{group_str}:{group}"] = target[use_str]
		merged[target[key_str]] = row

csvo = pd.DataFrame(
	data=merged.values()
)
csvo.to_csv("./rw.csv")