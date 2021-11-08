from share.parse_csv import CsvSource, read_csv
from static import *

FILEPATH = BASEDIR / Path("r.csv")

A=read_csv(CsvSource(
	path=FILEPATH,
	start=1,
	end=2,
	delimiter=","
))

plt.scatter(A[0], A[1])
plt.grid()
plt.xlabel('I')
plt.ylabel('Q')

plt.savefig(FILEPATH.parent / (FILEPATH.stem + ".png"))

