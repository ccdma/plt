from math import erfc
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss

def cdma_ber(N, sigma, K: np.array):
    return 1/2 * ss.erfc(N/np.sqrt(2*((K-1)*N + sigma**2)))

N = 62
sigma = 0.5 #0.01 # 36[db]
K = np.arange(3, 30)
BER = cdma_ber(N, sigma, K)

plt.yscale("log")
plt.plot(K, BER)
plt.xlabel("K: number of users")
plt.ylabel("BER")
plt.show()
