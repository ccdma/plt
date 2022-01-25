from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

K = np.linspace(9, 50)
bers = cdma_ber(100, K)
plt.plot(K, bers)
plt.yscale("log")
plt.show()