from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

np.random.seed(1)

FILEPATH = BASEDIR / Path("data.csv")

DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j
# CDATA = weyl_samples(np.sqrt(0.1), 0.1, 1000)
print(f"datalen={CDATA.shape[0]}")
# CDATA = fix_rotate(CDATA, estimate_basearg(CDATA[:100], 2), 1400)
# CDATA = CDATA/np.abs(CDATA)

ncols = 1
nrows = 1
size = 6
fig, axes = subplots(ncols=ncols,nrows=nrows,figsize=(ncols*size,nrows*size))

# ax = axes[0]
# ax.scatter(CDATA.real, CDATA.imag, s=1)
# ax.plot(CDATA.real, CDATA.imag, lw=0.2)

for i in range(ncols*nrows):
	ax = axes[i]
	step = 1000
	start = 0 + i*step
	end = start + step
	C = CDATA[start:end]
	#### IQ
	ax.scatter(C.real, C.imag, s=1)
	ax.plot(C.real, C.imag, lw=0.41)
	ax.set_title(f"{start}-{end}")
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)

SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
plt.gca().set_aspect('equal','datalim')
# fig.suptitle(f"1024-circle SR=5M BW=10M", fontsize=16)
plt.tight_layout()
plt.show()
# fig.savefig(SAVEFILE)
print(SAVEFILE)