from pathlib import Path
from share.parse_csv import CsvSource, read_csv
from static import *

FILEPATH = BASEDIR / Path("weyl.csv")

DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j

CDATA = CDATA

fig = plt.figure(figsize=(5,5))

#### ret
# plt.scatter(CDATA.real[:-1], CDATA.real[1:])


# CDATA = CDATA/np.abs(CDATA)

#### IQ
plt.scatter(CDATA.real, CDATA.imag, s=2)
# plt.plot(CDATA.real, CDATA.imag, lw=0.2)

SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
plt.gca().set_aspect('equal','datalim')
fig.savefig(SAVEFILE)