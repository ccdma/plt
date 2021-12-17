import dataclasses as d
import matplotlib.pyplot as plt
import numpy as np
from typing import List 
import pathlib
from collections.abc import Iterable 

class Constructor:

	def __init__(self, blocks: List, title: str="", h=5, w=10, align="v"):
		block_num = len(blocks)
		fig = None
		ax = None
		if align == "v":
			fig, ax = plt.subplots(block_num, 1)
		else:	# align == "h"
			fig, ax = plt.subplots(1, block_num)
		if not isinstance(ax, Iterable):
			ax = [ax]
		for i in range(block_num):
			blocks[i].plot(ax[i])
		fig.tight_layout()
		fig.suptitle(f"{title}", x=0.1, y=0.97)
		fig.set_figheight(h)
		fig.set_figwidth(w)
		self.fig = fig
		self.ax = ax

	def save(self, path: pathlib.Path):
		self.fig.savefig(path)

@d.dataclass
class LabelOption:
    label: str = None
    color: str = None

@d.dataclass
class ReturnmapBlock:
    # 描画する行列
    A: np.ndarray
    labels: List[LabelOption]
    title: str = None
    index_txt = False

    def plot(self, ax: plt.Axes):
        ax.set_title(self.title,fontsize=14)
        for j in range(self.A.shape[0]): # 各系列
            ax.scatter(self.A[j][0:-1], self.A[j][1:], s=6, alpha=0.5, label=self.labels[j].label)
            if self.index_txt:
                for i in range(self.A.shape[1]-1):
                    ax.text(self.A[j,i], self.A[j,i+1], str(i))
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=10)
        if any(map(lambda e : e.label != None, self.labels)):
            ax.legend(loc='upper right')
	
@d.dataclass
class PlotBlock:
    # 描画する行列
    A: np.ndarray
    labels: List[LabelOption]
    title: str = None

    def plot(self, ax: plt.Axes):
        ax.set_title(self.title)
        for j in range(self.A.shape[0]):
            ax.plot(self.A[j], alpha=0.7, label=self.labels[j].label)
        if any(map(lambda e : e.label != None, self.labels)):
            ax.legend(loc='upper right')