import csv
import numpy as np
import dataclasses
import pathlib

@dataclasses.dataclass
class CsvSource:
	path: pathlib.Path
	start: int = 1	# 1インデックス
	end: int = None
	dtype: np.dtype = float

def read_csv(source: CsvSource) -> np.ndarray:
	with source.path.open(encoding="utf-8") as f:
		lines = f.readlines()
		target_line = lines[source.start-1:source.end]
		reader = csv.reader(target_line, delimiter=',')
		dtyped_matrix = []
		for row in reader:
			if(row[-1] == ""):
				row = row[:-1]
			dtyped_matrix.append(row)
		return np.array(dtyped_matrix, dtype=source.dtype)
	raise Exception("csv parse error occured")

		