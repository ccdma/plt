from pathlib import Path
import sys
from numpy import sqrt
from share import *
from static import *
from pica.ica import *
import matplotlib.pyplot as plt

print(np.mean(np.square(const_powerd_samples(2, 0.1, 1000000).imag)))
print(10*np.log10(0.5/0.005**2))
print(10*np.log10(0.5/0.01**2))
print(10*np.log10(0.5/0.02**2))
print(10*np.log10(0.5/0.05**2))