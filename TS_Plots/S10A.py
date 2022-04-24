from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from numpy.polynomial.polynomial import polyfit
from math import log

dfli = ["710", "720", "730", "1220", "1240", "1260", "1730", "1760", "1790", "2240", "2280", "22120"]
#dfli = ["710", "1220", "1730", "2240"]
#dfli = ["720", "1240", "1760", "2280"]
#dfli = ["730", "1260", "1790",  "22120"]

mdf = pd.read_csv("TSv3.csv")

mdf["inABR"] = np.log2(mdf["inA"]/mdf["inB"])
mdf["BCABR"] = np.log2(mdf["BiC A"]/mdf["BiC B"])
mdf["PNRA"] = np.log2(mdf["PInA"]/mdf["NInA"])
mdf["PNRB"] = np.log2(mdf["PInB"]/mdf["NInB"])

print(mdf.head())
print(mdf.shape)

sns.set(rc={'figure.figsize':(4.5,3.5)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":12,"legend.title_fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
#sns.set_context("paper", rc={"legend.fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
sns.set_style("ticks")

# SCATTERPLOT CODE
plt.scatter(mdf["PNRA"], mdf["PNRB"], c=mdf["CC AB"],marker="o", cmap="Spectral", edgecolor="black", linewidth=0.7, alpha=0.8)
cbar = plt.colorbar()
plt.title("CC AB")
plt.xlabel("log2(+ve inA/-ve inA)")
plt.ylabel("log2(+ve inB/-ve inB)")
plt.tight_layout()
plt.savefig("S10Ai.svg",dpi=400)
plt.savefig("S10Ai.png",dpi=400, pad_inches=0)
plt.show()


plt.scatter(mdf["PNRA"], mdf["PNRB"], c=mdf["F1"],marker="o", cmap="Spectral", edgecolor="black", linewidth=0.7, alpha=0.8)
cbar = plt.colorbar()
plt.title("Fraction of 01 & 10 States")
plt.xlabel("log2(+ve inA/-ve inA)")
plt.ylabel("log2(+ve inB/-ve inB)")
plt.tight_layout()
plt.savefig("S10Aii.svg",dpi=400)
plt.savefig("S10Aii.png",dpi=400, pad_inches=0)
plt.show()












