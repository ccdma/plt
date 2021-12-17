from pathlib import Path
from share.blocks import Constructor, LabelOption, PlotBlock, ReturnmapBlock
from share.parse_csv import CsvSource, read_csv
from static import *

FILEPATH = BASEDIR / Path("bachelor/3.csv")
DATALEN = 4
LABELS = [ LabelOption(label=f"sin[t/{i+1}0]") for i in range(DATALEN) ]
NO_LABELS = [ LabelOption() for _ in range(DATALEN) ]
TITLE = ""

START = 1
STEP = DATALEN+1

BLOCKS = [
	PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=START,
			end=START+(DATALEN+1)-2
		)), 
		labels=NO_LABELS,
		title="source"
	),PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=START+(DATALEN+1),
			end=START+(DATALEN+1)*2-2
		)), 
		labels=NO_LABELS,
		title="mixed"
	),PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=START+(DATALEN+1)*2,
			end=START+(DATALEN+1)*3-2
		)), 
		labels=NO_LABELS,
		title="reconstruct"
	)
]

C = Constructor(BLOCKS, title=TITLE, align="v")
SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
C.save(SAVEFILE)