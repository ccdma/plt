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

results = []
slicerang = range(3900, 4200)
for i in slicerang:
	slices = i
	start = K(75)
	length = 300
	end = start + length
	X = np.array([
		X_Raw[0][start:end],
		X_Raw[1][start+slices:end+slices]
	]).real
	res = X[0]@X[1]/length
	results.append(res)
plt.plot(slicerang, results, lw=1)
plt.show()

