from pathlib import Path
from share.blocks import Constructor, LabelOption, ReturnmapBlock
from share.parse_csv import CsvSource, read_csv
from static import *

FILEPATH = BASEDIR / Path("result.csv")
DATALEN = 4
LABELS = [ LabelOption(label=f"T{i+2}") for i in range(DATALEN) ]
NO_LABELS = [ LabelOption() for _ in range(DATALEN) ]
TITLE = "chebyshev"

BLOCKS = [
	ReturnmapBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=1,
			end=3
		)), 
		labels=LABELS,
		title="source"
	),ReturnmapBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=5,
			end=7
		)), 
		labels=NO_LABELS,
		title="mixed"
	),ReturnmapBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=9,
			end=11
		)), 
		labels=NO_LABELS,
		title="reconstruct"
	)
]

C = Constructor(BLOCKS, title=TITLE, align="h", w=12)
SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
C.save(SAVEFILE)