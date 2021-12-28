from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *

np.random.seed(1)

FILEPATH = BASEDIR / Path("receive/receive-f13a0.csv")

DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j
print(f"datalen={CDATA.shape[0]}")
# CDATA = np.array(np.exp(np.linspace(0, 2*np.pi, 1024)*1j))
# CDATA = np.tile(primitive_root_code(19, 2), 20)
CDATA = CDATA * np.exp(np.full(CDATA.shape, -1.75)*1j)
# CDATA = np.tile(const_powerd_samples(2, np.pi/(1+np.sqrt(2)), 1024), 2)
# CDATA = CDATA - np.mean(CDATA)
CDATA = CDATA/np.abs(CDATA)
# CDATA = CDATA * np.tile(np.exp(np.linspace(0, 2*np.pi, 1100)*(-1j)), 10)[:CDATA.shape[0]]
# CDATA = np.random.permutation(CDATA)

ncols = 5
nrows = 2
size = 3
fig, axes = subplots(ncols=ncols,nrows=nrows,figsize=(ncols*size,nrows*size))

# ax = axes[0]
# ax.scatter(CDATA.real, CDATA.imag, s=1)
# ax.plot(CDATA.real, CDATA.imag, lw=0.2)

for i in range(ncols*nrows):
	ax = axes[i]
	step = 100
	start = 8*100 + i*step
	end = start + step
	C = CDATA[start:end]
	#### IQ
	ax.scatter(C.real, C.imag, s=1)
	ax.plot(C.real, C.imag, lw=0.41)
	ax.set_title(f"{start-800}-{end-800}")
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)

SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
plt.gca().set_aspect('equal','datalim')
# fig.suptitle(f"1024-circle SR=5M BW=10M", fontsize=16)
plt.tight_layout()
fig.savefig(SAVEFILE)
