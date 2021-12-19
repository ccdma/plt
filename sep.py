from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

np.random.seed(1)

def K(num: int):
	return int(num*1000)

FILEPATHES = [
	BASEDIR / Path("receive/receive-f7f24.csv"),
	BASEDIR / Path("receive/receive-f13a0.csv"),
]

X_Raw = []
for path in FILEPATHES:
	data = read_csv(CsvSource(path, start=1, end=2))
	X_Raw.append(np.array(data[0]) + np.array(data[1])*1j)
X_Raw = np.array(X_Raw)

slices = 4073
start = K(90)
end = start + 300
X = np.array([
	X_Raw[0][start:end],
	X_Raw[1][start+slices:end+slices]
])

rr = FastICA(X.real, _assert=False)
ri = FastICA(X.imag, _assert=False)

ncols = 2
nrows = 2
size = 4
fig, axes = subplots(ncols=ncols,nrows=nrows,figsize=(ncols*size,nrows*size))
for i in range(ncols):
	for j in range(nrows):
		ax = axes[i*nrows+j]
		px = rr.Y[i]
		py = ri.Y[j]
		C = px + py*1j
		C = C/np.abs(C)
		# C = C[:20]
		#### IQ
		ax.scatter(C.real, C.imag, s=1)
		ax.plot(C.real, C.imag, lw=0.2)
fig.tight_layout()
plt.show()