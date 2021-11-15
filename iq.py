from pathlib import Path

from numpy import sqrt
from share.parse_csv import CsvSource, read_csv
from static import *
from pica.ica import *

FILEPATH = BASEDIR / Path("weyl.csv")

DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j

CDATA = CDATA[1000:1010]
REF = weyl_samples(np.sqrt(0.3), np.sqrt(0.5), CDATA.shape[0])

fig = plt.figure(figsize=(5,5))

# CDATA = CDATA/np.abs(CDATA)

#### IQ
plt.scatter(CDATA.real, CDATA.imag, s=2)
plt.plot(CDATA.real, CDATA.imag, lw=0.5)
# print(periodic_correlation(np.array([CDATA, REF]), 100))

SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
plt.gca().set_aspect('equal','datalim')
fig.savefig(SAVEFILE)
