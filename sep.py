from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

np.random.seed(1)
K = 100

FILEPATHES = [
	BASEDIR / Path("receive/receive-f7f24.csv"),
	BASEDIR / Path("receive/receive-f13a0.csv"),
]

X_Raw = []
for path in FILEPATHES:
	data = read_csv(CsvSource(path, start=1, end=2))
	X_Raw.append(np.array(data[0]) + np.array(data[1])*1j)
X_Raw = np.array(X_Raw)

X = np.array([
	X_Raw[0][85*K:86*K],
	X_Raw[1][85*K+500:86*K+500]
])

rr = FastICA(X.real, _assert=False)
ri = FastICA(X.imag, _assert=False)
plt.scatter(rr.Y[0], ri.Y[0], s=1)
plt.plot(rr.Y[0], ri.Y[0], lw=0.1)
plt.show()