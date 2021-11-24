from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *

FILEPATH = BASEDIR / Path("primitive-1019-2.csv")

DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j

CDATA = CDATA/np.abs(CDATA)

fig, axes = subplots(4,4,figsize=(10,10))

for i in range(16):
	ax = axes[i]
	step = 30
	start = 1000 + i*step
	end = start + step
	C = CDATA[start:end]
	#### IQ
	ax.scatter(C.real, C.imag, s=2)
	ax.plot(C.real, C.imag, lw=0.5)
	ax.set_title(f"{start}-{end}")

SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
plt.gca().set_aspect('equal','datalim')
fig.suptitle(f"p={FILEPATH.stem.split('-')[1]},q={FILEPATH.stem.split('-')[2]} primitive root code (received)", fontsize=16)
plt.tight_layout()
fig.savefig(SAVEFILE)
