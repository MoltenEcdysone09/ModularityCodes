from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from numpy.polynomial.polynomial import polyfit
from math import log

mdf = pd.read_csv("TS.csv")

print(mdf.head())
print(mdf.shape)


sns.set(rc={'figure.figsize':(4,3.5)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":12,"legend.title_fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
sns.set_style("ticks")


# SCATTERPLOT CODE
plt.scatter(mdf["InABR"], mdf["CC AB"], c=mdf["BCABR"],marker="o", cmap="Spectral", edgecolor="black", linewidth=0.7, alpha=0.8)
cbar = plt.colorbar()
cbar.set_label("log2(BC A/BC B)")

plt.xlabel("log2(InA/InB)")
plt.ylabel("CC AB")
plt.tight_layout()
plt.savefig("F4Aiii.svg",dpi=400)
plt.savefig("F4Aiii.png",dpi=400, pad_inches=0)
plt.show()

