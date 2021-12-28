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

REF = np.tile(const_powerd_samples(2, np.pi/(1+np.sqrt(2)), 1024), 3)

FILEPATH = BASEDIR / Path("receive/receive-f13a0.csv")
DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j
CDATA = CDATA * np.exp(np.full(CDATA.shape, -1.75)*1j)
CDATA = CDATA/np.abs(CDATA)
CDATA = CDATA[800:1800]

# X_Raw = [CDATA, REF]
# results = []
# slicerang = range(0, 1024)
# for i in slicerang:
# 	slices = i
# 	start = 0
# 	length = 1000
# 	end = start + length
# 	X = np.array([
# 		X_Raw[0][start:end],
# 		X_Raw[1][start+slices:end+slices]
# 	]).real
# 	res = X[0]@X[1]/length
# 	results.append(res)
# plt.plot(slicerang, results, lw=1)
# plt.show()

sliced = 1015
REF = REF[sliced:1000+sliced]
print(CDATA.real@REF.real)
print(np.mean(np.abs(np.angle(REF) - np.angle(CDATA))))
