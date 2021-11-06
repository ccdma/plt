from pathlib import Path
from share.blocks import Constructor, LabelOption, PlotBlock, ReturnmapBlock
from share.parse_csv import CsvSource, read_csv
from static import *

FILEPATH = BASEDIR / Path("sin1-4.csv")
DATALEN = 4
LABELS = [ LabelOption(label=f"sin[x/(10*{i+1})]") for i in range(DATALEN) ]
NO_LABELS = [ LabelOption() for _ in range(DATALEN) ]
TITLE = "sin"

BLOCKS = [
	PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=1,
			end=4
		)), 
		labels=LABELS,
		title="source"
	),PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=6,
			end=9
		)), 
		labels=NO_LABELS,
		title="mixed"
	),PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=11,
			end=14
		)), 
		labels=NO_LABELS,
		title="reconstruct"
	)
]

C = Constructor(BLOCKS, title=TITLE, align="v")
SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
C.save(SAVEFILE)