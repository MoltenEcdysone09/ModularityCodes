from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from statannotations.Annotator import Annotator
from math import log
import itertools

mdf = pd.read_csv("TTv4.csv")

mdf["NEdges"] = mdf["NEdges"] - 6

mdf["Fraction of -ve Edges"] = mdf["NEdges"]/(mdf["NEdges"] + mdf["PEdges"])
mdf["Fraction of +ve Edges"] = mdf["PEdges"]/(mdf["NEdges"] + mdf["PEdges"])

print(mdf.head())
print(mdf)
print(mdf.shape)

sns.set(rc={'figure.figsize':(8,4)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":16,"legend.title_fontsize":16,"font.size":16,"axes.titlesize":16,"axes.labelsize":16,"xtick.labelsize":16,"ytick.labelsize":16})
sns.set_style("ticks")

fig, axs = plt.subplots(1, 2)

r1c1 = sns.kdeplot(ax=axs[0], data=mdf, x="Fraction of +ve Edges", fill=True, common_norm=False, alpha=.1, linewidth=2)
axs[0].set_xticks([ 0.25, 0.5, 0.75])

r1c2 = sns.kdeplot(ax=axs[1], data=mdf, x="Fraction of -ve Edges", fill=True, common_norm=False, alpha=.1, linewidth=2)
axs[1].set_xticks([ 0.25, 0.5, 0.75])

plt.tight_layout()
plt.savefig("S11C.svg",dpi=400)
plt.savefig("S11C.png",dpi=400, pad_inches=0)
plt.show()
