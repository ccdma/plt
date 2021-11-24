from matplotlib.pyplot import savefig
from share import *
from static import *
from pica.ica import *

p = 173
q = 59
k = 1

fig, axes = subplots(nrows=2,figsize=(5,10))

samplings = const_powerd_samples(q, -2*np.pi*k/p, p)
ax = axes[0]
ax.scatter(samplings.real, samplings.imag, s=2)
ax.plot(samplings.real, samplings.imag, lw=0.5)
ax.scatter(samplings.real[0], samplings.imag[0])
ax.scatter(samplings.real[-1], samplings.imag[-1])
ax.set_title(f"p={p},q={q} primitive root code (send)")

samplings = primitive_root_code(p, q)
ax = axes[1]
ax.scatter(samplings.real, samplings.imag, s=2)
ax.plot(samplings.real, samplings.imag, lw=0.5)
ax.scatter(samplings.real[0], samplings.imag[0])
ax.scatter(samplings.real[-1], samplings.imag[-1])
ax.set_title(f"p={p},q={q} primitive root code (send)")

fig.tight_layout()
plt.show()