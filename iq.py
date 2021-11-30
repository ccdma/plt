from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *

np.random.seed(1)

FILEPATH = BASEDIR / Path("circle.csv")

DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j
CDATA = np.array(np.exp(np.linspace(0, 2*np.pi, 1024)*1j))
# CDATA = np.tile(primitive_root_code(1019, 2), 20)
# CDATA = CDATA * np.exp(np.random.normal(0, 0.1, CDATA.shape[0])*1j)

# CDATA = CDATA - np.mean(CDATA)
CDATA = CDATA/np.abs(CDATA)
# CDATA = np.random.permutation(CDATA)

ncols = 1
nrows = 1
fig, axes = subplots(ncols=ncols,nrows=nrows,figsize=(5,5))
ax = axes[0]
ax.scatter(CDATA.real, CDATA.imag, s=1)
ax.plot(CDATA.real, CDATA.imag, lw=0.2)

# for i in range(ncols*nrows):
# 	ax = axes[i]
# 	step = 120
# 	start = 1000 + i*step
# 	end = start + step
# 	C = CDATA[start:end]
# 	#### IQ
	# ax.scatter(C.real, C.imag, s=1)
	# ax.plot(C.real, C.imag, lw=0.2)
# 	ax.set_title(f"{start}-{end}")

SAVEFILE = FILEPATH.parent / (FILEPATH.stem + ".png")
plt.gca().set_aspect('equal','datalim')
# fig.suptitle(f"{' '.join(FILEPATH.stem.split('-'))}", fontsize=16)
plt.tight_layout()
fig.savefig(FILEPATH.parent / ("circle" + ".png"))
