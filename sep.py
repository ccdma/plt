from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

np.random.seed(1)
K = 1000

FILEPATHES = [
	BASEDIR / Path("receive/receive-f7f24.csv"),
	BASEDIR / Path("receive/receive-f13a0.csv"),
]

X_Raw = []
for path in FILEPATHES:
	data = read_csv(CsvSource(path, start=1, end=2))
	X_Raw.append(np.array(data[0]) + np.array(data[1])*1j)
X_Raw = np.array(X_Raw)

slide = 450
X = np.array([
	X_Raw[0][85*K:86*K],
	X_Raw[1][85*K+slide:86*K+slide]
])

rr = FastICA(X.real, _assert=False)
ri = FastICA(X.imag, _assert=False)

ncols = 2
nrows = 2
size = 5
fig, axes = subplots(ncols=ncols,nrows=nrows,figsize=(ncols*size,nrows*size))

for i in range(ncols):
	for j in range(nrows):
		ax = axes[i*nrows+j]
		I = rr.Y[i]
		Q = ri.Y[j]
		# C = I + Q*1j
		# C = C/np.abs(C)
		# I = C.real
		# Q = C.imag
		ax.scatter(I, Q, s=1)
		ax.plot(I, Q, lw=0.1)
fig.tight_layout()
fig.suptitle(f"{slide}", fontsize=16)
plt.show()