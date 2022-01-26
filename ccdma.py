from cProfile import label
from pathlib import Path
import sys
from numpy import sqrt
from sympy import plot
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

np.random.seed(1)

def test(signal: int, N: int):
	bitlen = 1000
	length = N * bitlen
	norm_scale = 0.01
	S = np.array([const_powerd_samples(2, np.random.random(), length) for i in range(signal)])
	BITS = np.array([[ np.sign(np.random.randint(0, 2)-0.5) for i in range(bitlen) ] for _ in range(signal)])
	B = np.repeat(BITS, N, axis=1)

	T = B*S
	A = np.ones(signal)
	X = A @ T + np.random.normal(0.0, norm_scale, length)

	B_R = np.tile(X, (signal, 1)) * S.conj()

	BITS_R = np.sign(B_R.reshape((signal, bitlen, N)).mean(axis=2).real)
	ber = np.abs(BITS_R - BITS).mean()/2
	return ber

K = np.arange(2, 20)
N = 10
bers = []
for signal in K:
	bers.append(test(signal, N))
plt.plot(K, bers, label="simulation")
# bers = cdma_ber(N, K)
# plt.plot(K, bers, label="formula")
plt.yscale("log")

plt.xlabel("K: Number of Users")
plt.ylabel("BER")
plt.legend()
plt.show()
