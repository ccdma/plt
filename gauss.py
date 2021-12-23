from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

SAMPLES = 10000
stddevs = np.linspace(0, 0.1, 100)
avgs = []
for stddev in stddevs:
	norms = np.random.normal(0.0, stddev, SAMPLES)
	pn = np.abs(norms).mean()
	ps = 1
	avgs.append(10*np.log10(ps/pn))
plt.plot(stddevs, avgs)
plt.ylabel("SNR [db]")
plt.xlabel("stddev")
plt.show()
