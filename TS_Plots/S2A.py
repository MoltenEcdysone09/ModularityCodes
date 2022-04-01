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
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":11,"legend.title_fontsize":11,"font.size":11,"axes.titlesize":11,"axes.labelsize":11,"xtick.labelsize":11,"ytick.labelsize":11})
#sns.set_context("paper", rc={"legend.fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
sns.set_style("ticks")

iili = []

for s in range(1,7):
    for d in range(1,7):
        sdf = mdf[(mdf["inA"]==s) & (mdf["inB"]==d)]
        if not sdf.empty:
            ccmean = round(np.mean(list(sdf["BiC A"])), 3)
            #ccstd = round(np.std(list(sdf["CC AB"])), 3)
            #iili.append([s,d,ccmean,ccstd])
            iili.append([s,d,ccmean])

ia = [item[0] for item in iili]
ib = [item[1] for item in iili]
ccm = [item[2] for item in iili]
ccmn = [abs(item)*100*5 for item in ccm]
#
#[print(item) for item in iili]

# HEATMAP CODE
pldf = pd.DataFrame(iili, columns=["X", "Y", "Value"])
pldf = pldf.pivot('X', 'Y', 'Value')
ax = sns.heatmap(pldf, annot=True, cmap="crest_r", cbar_kws={'label': ''})
ax.invert_yaxis()
plt.xlabel("In Degree of B")
plt.ylabel("In Degree of A")
plt.title("BiC A")
plt.tight_layout()
plt.savefig("S2Ai.svg",dpi=400)
plt.savefig("S2Ai.png",dpi=400, pad_inches=0)
plt.show()


iili = []

for s in range(1,7):
    for d in range(1,7):
        sdf = mdf[(mdf["inA"]==s) & (mdf["inB"]==d)]
        if not sdf.empty:
            ccmean = round(np.mean(list(sdf["BiC B"])), 3)
            #ccstd = round(np.std(list(sdf["CC AB"])), 3)
            #iili.append([s,d,ccmean,ccstd])
            iili.append([s,d,ccmean])

ia = [item[0] for item in iili]
ib = [item[1] for item in iili]
ccm = [item[2] for item in iili]
ccmn = [abs(item)*100*5 for item in ccm]
#
#[print(item) for item in iili]

# HEATMAP CODE
pldf = pd.DataFrame(iili, columns=["X", "Y", "Value"])
pldf = pldf.pivot('X', 'Y', 'Value')
ax = sns.heatmap(pldf, annot=True, cmap="crest_r", cbar_kws={'label': ''})
ax.invert_yaxis()
plt.xlabel("In Degree of B")
plt.ylabel("In Degree of A")
plt.title("BiC B")
plt.tight_layout()
plt.savefig("S2Aii.svg",dpi=400)
plt.savefig("S2Aii.png",dpi=400, pad_inches=0)
plt.show()
