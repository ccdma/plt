from collections.abc import Iterable
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
from typing import List, Tuple

def subplots(nrows: int=1, ncols: int=1, **kwds) -> Tuple[Figure, List[plt.Axes]]:
	fig, axes = plt.subplots(nrows=nrows,ncols=ncols,**kwds)
	if not isinstance(axes, Iterable):
		axes = [axes]
	else:
		axes = axes.tolist()
	if isinstance(axes[0], Iterable):
		axes = sum(axes, [])	# flatten
	return (fig, axes)