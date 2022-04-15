from cProfile import label
from pathlib import Path
from random import randint
import sys
from numpy import sqrt
from sympy import plot
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

np.random.seed(3)

def test(signal: int, N: int):
	bitlen = 100000
	length = N * bitlen
	norm_scale = 0.01
	# S = np.array([weyl_samples(i/signal+1/(2*N), 0, length) for i in range(signal)])
	S = np.array([const_powerd_samples(2, np.random.random(), length) for i in range(signal)])
	BITS = np.array([[ np.sign(np.random.randint(0, 2)-0.5) for i in range(bitlen) ] for _ in range(signal)])
	B = np.repeat(BITS, N, axis=1)

	T = B*S

	for i in range(1, signal):
		r = np.random.randint(0, N)
		T[i] = np.hstack([T[i, r:], T[i, :r]]) 

	A =  np.random.rand(signal) + 1.0 #np.ones(signal)
	X = A @ T + np.random.normal(0.0, norm_scale, length)

	B_R = np.tile(X, (signal, 1)) * S.conj()

	BITS_R = np.sign(B_R.reshape((signal, bitlen, N)).mean(axis=2).real)
	ber = np.abs(BITS_R[0] - BITS[0]).mean()/2
	return ber

K_List = np.arange(2, 20)
N = 63
bers = []
# for K in K_List: # number of users
# 	bers.append(test(K, N))
# plt.scatter(K_List, bers, label="simulation")

bers = cdma_ber(N, 0.01, K_List)
plt.plot(K_List, bers, label="formula")
plt.yscale("log")

plt.xlabel("K: Number of Users")
plt.ylabel("BER")
# plt.legend()
plt.show()
