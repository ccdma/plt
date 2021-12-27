from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

SAMPLINGS = 10000
RAD_0 = 0.3*np.pi
DATA = const_powerd_samples(2, 0.1, SAMPLINGS)
DATA = np.full(SAMPLINGS, np.exp(1j*RAD_0)) * DATA
print(f"mean={DATA.mean()}")

# plt.scatter(DATA.real, DATA.imag, s=1)
# plt.plot(DATA.real, DATA.imag, lw=0.3)
# plt.gca().set_aspect('equal','datalim')
# plt.hist(np.angle(DATA))
# plt.tight_layout()
# plt.show()