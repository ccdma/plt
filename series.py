from pathlib import Path
import matplotlib.pyplot as plt
from share.parse_csv import CsvSource, read_csv
from static import *

FILEPATH = BASEDIR / Path("0.tsv")

A=read_csv(CsvSource(
	path=FILEPATH,
	start=7,
	delimiter="\t"
)).T

plt.plot(A[0], A[1])
plt.grid()
plt.xlabel('signals')
plt.ylabel('mean squared error')

plt.savefig(FILEPATH.parent / (FILEPATH.stem + ".png"))