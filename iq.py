from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *

FILEPATH = BASEDIR / Path("write.csv")

DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j

CDATA = CDATA/np.abs(CDATA)

fig, axes = subplots(1,1,figsize=(5,5))
ax = axes[0]

#### IQ
ax.scatter(CDATA.real, CDATA.imag, s=2)
ax.plot(CDATA.real, CDATA.imag, lw=0.5)
ax.set_title(f"p={173},q={45} primitive root code (received)")

SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
plt.gca().set_aspect('equal','datalim')
plt.tight_layout()
fig.savefig(SAVEFILE)
