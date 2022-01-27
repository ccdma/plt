from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

SAMPLES = 10000
stddevs = np.linspace(0, 0.1, 100)[1:]
ravgs = []
cavgs = []
for stddev in stddevs:
	norms1 = np.random.normal(0.0, stddev, SAMPLES)
	norms2 = np.random.normal(0.0, stddev, SAMPLES)
	norms = norms1 + 1j * norms2
	rpn = np.power(np.abs(norms1), 2).sum()
	cpn = np.power(np.abs(norms), 2).sum()
	rps = np.power(np.abs(chebyt_samples(2, 0.1, SAMPLES)), 2).sum()
	ravgs.append(10*np.log10(rps/rpn))
	cavgs.append(10*np.log10(SAMPLES/cpn))
plt.plot(stddevs, ravgs, label="real")
plt.plot(stddevs, cavgs, label="complex")
plt.ylabel("SNR [db]")
plt.xlabel("stddev")
plt.legend()
plt.show()
