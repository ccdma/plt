from pathlib import Path
import matplotlib.pyplot as plt
from share.parse_csv import CsvSource, read_csv
from static import *

FILEPATH = BASEDIR / Path("0.tsv")

A=read_csv(CsvSource(
	path=FILEPATH,
	start=5,
	delimiter="\t"
)).T

plt.plot(A[0], A[1])

plt.show()