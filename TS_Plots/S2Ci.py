from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from numpy.polynomial.polynomial import polyfit
from math import log

mdf = pd.read_csv("TSv2.csv")

print(mdf.head())
print(mdf.shape)


sns.set(rc={'figure.figsize':(4.0,3.5)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":9,"legend.title_fontsize":10,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
#sns.set_context("paper", rc={"legend.fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
sns.set_style("ticks")

# SCATTERPLOT CODE
mdf = mdf[(mdf["BiC A"] >= 0.55) & (mdf["BiC B"] >= 0.55)]
sns.scatterplot(data=mdf, x="InABR", y="CC AB", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"], palette=['#4c72b0', '#4c72b0', '#55a868', '#c44e52', '#8172b3'], style="Mean Connectivity", markers=["P","o","o","o","D"])

plt.legend([],[], frameon=False)
plt.xlabel("log2(InA/InB)")
plt.ylabel("CC AB")
plt.tight_layout()
plt.savefig("S2Ci.svg",dpi=400)
plt.savefig("S2Ci.png",dpi=400, pad_inches=0)
plt.show()
