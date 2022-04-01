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

sns.set(rc={'figure.figsize':(4.2,3.3)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":15,"legend.title_fontsize":15,"font.size":15,"axes.titlesize":15,"axes.labelsize":15,"xtick.labelsize":15,"ytick.labelsize":15})
sns.set_context("paper")
sns.set_style("ticks")

iili = []
aili = []
for s in ["inA", "inB", "inTS"]:
    for d in ["BiC A", "BiC B", "B:M", "F1", "CC AB" ]:
        print([s,d])
        print(stats.spearmanr(mdf[s], mdf[d]))
        cc, pval = stats.spearmanr(mdf[s], mdf[d])
        if pval < 0.05:
            cca = f'{cc:.2f}'+"*"
        else:
            cca = f'{cc:.2f}'
        iili.append([s,d,cc])
        aili.append([s,d,cca])

ia = [item[0] for item in iili]
ib = [item[1] for item in iili]
ccm = [item[2] for item in iili]

#Labels df
aia = [item[0] for item in aili]
aib = [item[1] for item in aili]
accm = [item[2] for item in aili]

# HEATMAP CODE
pldf = pd.DataFrame(iili, columns=["X", "Y", "Value"])
pldf = pldf.pivot('X', 'Y', 'Value')
#labels df
ldf = pd.DataFrame(aili, columns=["X", "Y", "Value"])
ldf = ldf.pivot('X', 'Y', 'Value').to_numpy()
ax = sns.heatmap(pldf, annot=ldf, cmap="Spectral", cbar_kws={'label': 'Correlation Coefficient'}, linewidth=0.5, fmt="")
plt.ylabel("In Degree Metrics")
plt.xlabel("TS Properties")
plt.tight_layout()
plt.savefig("F4D.svg",dpi=300)
plt.savefig("F4D.png",dpi=300, pad_inches=0)
plt.show()

