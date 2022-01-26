from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

np.random.seed(1)

SIGNALS = 4
N = 1000
BITLEN = 100
LENGTH = N * BITLEN
norm_scale = 0.0
S = np.array([const_powerd_samples(2, np.random.random(), LENGTH) for i in range(SIGNALS)])
BITS = np.array([[ np.sign(np.random.randint(0, 2)-0.5) for i in range(BITLEN) ] for _ in range(SIGNALS)])
B = np.repeat(BITS, N, axis=1)

T = B*S
A = np.ones((SIGNALS, SIGNALS))
X = A @ T + np.random.normal(0.0, norm_scale, (SIGNALS, LENGTH))

B_R = np.tile(X[0], (SIGNALS, 1)) * S.conj()

BITS_R = np.sign(B_R.reshape((SIGNALS, BITLEN, N)).mean(axis=2).real)
ber = np.abs(BITS_R - BITS).mean()/2
print(ber)
# plt.scatter(Y0.real, Y0.imag, s=1)
# plt.plot(Y0.real, Y0.imag, lw=0.4)
# plt.show()
