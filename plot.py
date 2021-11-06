from pathlib import Path
from share.blocks import Constructor, LabelOption, PlotBlock, ReturnmapBlock
from share.parse_csv import CsvSource, read_csv

FILEPATH = Path("result.csv")
DATALEN = 3
LABELS = [ LabelOption(label=f"sin{i+2}") for i in range(DATALEN) ]
NO_LABELS = [ LabelOption() for _ in range(DATALEN) ]

BLOCKS = [
	PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=1,
			end=3
		)), 
		labels=LABELS,
		title="source"
	),PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=5,
			end=7
		)), 
		labels=NO_LABELS,
		title="mixed"
	),PlotBlock(
		A=read_csv(CsvSource(
			path=FILEPATH,
			start=9,
			end=11
		)), 
		labels=NO_LABELS,
		title="reconstruct"
	)
]

C = Constructor(BLOCKS, title="sin", align="v")
C.save(Path("./graph.png"))