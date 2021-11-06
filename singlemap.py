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
			start=43,
			end=46
		)), 
		labels=NO_LABELS,
		title="source"
	)
]

C = Constructor(BLOCKS, title=TITLE, align="h", w=4)
SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
C.save(SAVEFILE)