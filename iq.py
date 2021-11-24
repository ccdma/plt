from pathlib import Path
import sys
from numpy import sqrt
from share.parse_csv import CsvSource, read_csv
from static import *
from pica.ica import *

FILEPATH = BASEDIR / Path("const2.csv")

DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j

CDATA = CDATA/np.abs(CDATA)

# fig = plt.figure(figsize=(5,5))
fig, axes = plt.subplots(4,4,figsize=(10,10))
s=int(sys.argv[1]); l=30
axes = sum(axes.tolist(), [])

for i,ax in enumerate(axes):
	
	sliced = CDATA[s+i*l:s+l+i*l]

	#### IQ
	ax.scatter(sliced.real, sliced.imag, s=2)
	ax.plot(sliced.real, sliced.imag, lw=0.5)
	ax.set_title(f"{s+i*l}-{s+l+i*l}")

SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
plt.gca().set_aspect('equal','datalim')
plt.tight_layout()
fig.savefig(SAVEFILE)
