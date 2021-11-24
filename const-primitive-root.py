from matplotlib.pyplot import plot
from share import *
from static import *
from pica.ica import *

p = 173
q = 46
k = 1

fig, axes = subplots(nrows=2, ncols=2, figsize=(10,10))

def plot_primitive(p, q, ax):
	samplings = primitive_root_code(p, q)
	ax.scatter(samplings.real, samplings.imag, s=2)
	ax.plot(samplings.real, samplings.imag, lw=0.5)
	# ax.scatter(samplings.real[0], samplings.imag[0])
	# ax.scatter(samplings.real[-1], samplings.imag[-1])
	ax.set_title(f"p={p},q={q} primitive root code (generate)")

plot_primitive(173, 66, axes[0])
plot_primitive(173, 45, axes[1])
plot_primitive(173, 46, axes[2])
plot_primitive(173, 59, axes[3])

fig.tight_layout()
plt.show()