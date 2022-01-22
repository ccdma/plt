from pathlib import Path
import sys
from numpy import average, sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

np.random.seed(1)

def K(num: int):
	return int(num*1000)

BERS = []
for i in range(1, 19):
	REF = np.tile(const_powerd_samples(2, np.pi/(1+np.sqrt(2)), 1024), 3)

	FILEPATH = BASEDIR / Path(f"receive/b/receive-fb9ce-{i}.csv")
	DATA = read_csv(CsvSource(FILEPATH, start=1, end=2))
	CDATA = np.array(DATA[0]) + np.array(DATA[1])*1j

	CDATA = fix_rotate(CDATA, estimate_basearg(CDATA[:100], 2), 1400)
	CDATA = CDATA/np.abs(CDATA)
	CDATA = CDATA[:1000]

	X_Raw = [CDATA, REF]
	results = []
	slicerang = range(0, 1024)
	for i in slicerang:
		slices = i
		start = 0
		length = 1000
		end = start + length
		X = np.array([
			X_Raw[0][start:end],
			X_Raw[1][start+slices:end+slices]
		]).real
		res = X[0]@X[1]/length
		results.append(res)
	# plt.plot(slicerang, results, lw=1)
	# plt.show()

	sliced = np.argmax(np.abs(np.array(results)))
	REF = REF[sliced:1000+sliced]
	mse_ = np.mean(np.abs(np.angle(REF) - np.angle(CDATA)))**2
	ber = np.abs(np.mean(np.sign(REF.real * CDATA.real + REF.imag *CDATA.imag)-1))/2
	# print(CDATA.real@REF.real)
	# print(f"mse={np.mean(np.abs(np.angle(REF) - np.angle(CDATA)))**2}")
	# print(f"ber={np.abs(np.mean(np.sign(REF.real * CDATA.real + REF.imag *CDATA.imag)-1))/2}")
	BERS.append(ber)
print(np.mean(np.array(BERS)))