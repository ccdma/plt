from pathlib import Path
from share.blocks import Constructor, LabelOption, PlotBlock, ReturnmapBlock
from share.parse_csv import CsvSource, read_csv
from static import *

FILEPATH = BASEDIR / Path("result.csv")
DATALEN = 50
LABELS = [ LabelOption(label=f"sin[t/{i+1}0]") for i in range(DATALEN) ]
NO_LABELS = [ LabelOption() for _ in range(DATALEN) ]
TITLE = "sin"

START = 1
STEP = DATALEN+1

BLOCKS = [
	PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=START,
			end=START-2+STEP
		))[45:50], 
		labels=NO_LABELS,
		title="source"
	),PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=START+STEP*1,
			end=START-2+STEP*2
		))[:5], 
		labels=NO_LABELS,
		title="mixed"
	),PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=START+STEP*2,
			end=START-2+STEP*3
		))[0:10], 
		labels=NO_LABELS,
		title="reconstruct"
	)
]

C = Constructor(BLOCKS, title=TITLE, align="v")
SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
C.save(SAVEFILE)