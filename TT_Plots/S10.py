from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from numpy.polynomial.polynomial import polyfit
from math import log

dfli = ["810", "820", "830", "1320", "1340", "1360", "1830", "1860", "1890", "2340", "2380", "23120"]


mdf = pd.read_csv("TT.csv")


mdf["InABR"] = np.log2(mdf["InA"]/mdf["InB"])
mdf["BCABR"] = np.log2(mdf["BC A"]/mdf["BC B"])
mdf["PNRA"] = np.log2(mdf["PInA"]/mdf["NInA"])
mdf["PNRB"] = np.log2(mdf["PInB"]/mdf["NInB"])

print(mdf.head())
print(mdf.shape)

sns.set(rc={'figure.figsize':(4.5,3.5)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":12,"legend.title_fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
#sns.set_context("paper", rc={"legend.fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
sns.set_style("ticks")

# SCATTERPLOT CODE
#mdf = mdf[(mdf["BC A"] >= 0.55) & (mdf["BC B"] >= 0.55)]
plt.scatter(mdf["PNRA"], mdf["PNRB"], c=mdf["MaxCC"],marker="o", cmap="Spectral", edgecolor="black", linewidth=0.7, alpha=0.8)
cbar = plt.colorbar()

plt.title("MaxCC")
plt.xlabel("log2(+ve inA/-ve inA)")
plt.ylabel("log2(+ve inB/-ve inB)")

##plt.title("E = 2N BC>=0.55")
plt.tight_layout()
plt.savefig("S10Bii.svg",dpi=400)
plt.savefig("S10Bii.png",dpi=400, pad_inches=0)
plt.show()


plt.scatter(mdf["PNRA"], mdf["PNRB"], c=mdf["F1/F2"],marker="o", cmap="Spectral", edgecolor="black", linewidth=0.7, alpha=0.8)
cbar = plt.colorbar()

plt.title("F1/F2")
plt.xlabel("log2(+ve inA/-ve inA)")
plt.ylabel("log2(+ve inB/-ve inB)")

##plt.title("E = 2N BC>=0.55")
plt.tight_layout()
plt.savefig("S10Bi.svg",dpi=400)
plt.savefig("S10Bi.png",dpi=400, pad_inches=0)
plt.show()












