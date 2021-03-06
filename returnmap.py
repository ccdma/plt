from pathlib import Path
from share.blocks import Constructor, LabelOption, ReturnmapBlock
from share.parse_csv import CsvSource, read_csv
from static import *

FILEPATH = BASEDIR / Path("bachelor/3.csv")
DATALEN = 4
LABELS = [ LabelOption(label=f"T2 x0=0.{(i+1)}") for i in range(DATALEN) ]
NO_LABELS = [ LabelOption() for _ in range(DATALEN) ]
TITLE = ""

START = 1

BLOCKS = [
	ReturnmapBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=START,
			end=START+(DATALEN+1)-2
		)), 
		labels=NO_LABELS,
		title="source"
	),ReturnmapBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=START+(DATALEN+1),
			end=START+(DATALEN+1)*2-2
		)), 
		labels=NO_LABELS,
		title="mixed"
	),ReturnmapBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=START+(DATALEN+1)*2,
			end=START+(DATALEN+1)*3-2
		)), 
		labels=NO_LABELS,
		title="reconstruct"
	)
]

C = Constructor(BLOCKS, title=TITLE, align="h", w=12)
SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
C.save(SAVEFILE)