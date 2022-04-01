from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from numpy.polynomial.polynomial import polyfit
from math import log

mdf = pd.read_csv("TT.csv")
mdf.rename({"InA":"inA", "InB":"inB", "InC":"inC"}, axis=1, inplace=True)

mdf["inTT"] = mdf["inA"] + mdf["inB"] + mdf["inC"]
mdf["MinCC"] = mdf[["CC AB", "CC BC", "CC AC"]].min(axis=1)
mdf["inA/inTT"] = mdf["inA"] / mdf["inTT"]
mdf["inB/inTT"] = mdf["inB"] / mdf["inTT"]
mdf["inC/inTT"] = mdf["inC"] / mdf["inTT"]
mdf["inAB/inTT"] = (mdf["inA"]+mdf["inB"]) / mdf["inTT"]
mdf["inBC/inTT"] = (mdf["inC"]+mdf["inB"]) / mdf["inTT"]
mdf["inAC/inTT"] = (mdf["inA"]+mdf["inC"]) / mdf["inTT"]
mdf = mdf.dropna()

ccdf = mdf[["inA", "inB", "inC", "CC AB", "CC BC", "CC AC"]]
ccdf = ccdf.reindex()

print(mdf.head())
print(mdf.shape)

sns.set(rc={'figure.figsize':(5,3.5)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":16,"legend.title_fontsize":16,"font.size":16,"axes.titlesize":16,"axes.labelsize":16,"xtick.labelsize":16,"ytick.labelsize":16})
sns.set_context("paper")
sns.set_style("ticks")

iili = []
aili = []
for s in ["inA", "inB", "inC", "inTT"]:
    for d in ["MaxCC", "F1", "F2", "F3", "F1/F2", "MinCC"]:
        print([s,d])
        print(stats.spearmanr(mdf[s], mdf[d]))
        cc, pval = stats.spearmanr(mdf[s], mdf[d])
        #cc = abs(cc)
        #cc = f'{cc:.2f}'
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

ax = sns.heatmap(pldf, annot=ldf, cmap="Spectral", cbar_kws={'label': 'Correlation Coefficient'}, fmt="", linewidth=0.5)
plt.ylabel("In Degree Metrics")
plt.xlabel("TT Properties")
plt.tight_layout()
plt.savefig("F6B.svg",dpi=300)
plt.savefig("F6B.png",dpi=300, pad_inches=0)
plt.show()


sns.set(rc={'figure.figsize':(6,4)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":16,"legend.title_fontsize":16,"font.size":16,"axes.titlesize":16,"axes.labelsize":16,"xtick.labelsize":16,"ytick.labelsize":16})
sns.set_context("paper")
sns.set_style("ticks")

iili = []
aili = []
for s in ["inA/inTT", "inB/inTT", "inC/inTT", "inAB/inTT", "inBC/inTT", "inAC/inTT", "inTT"]:
    for d in ["CC AB", "CC BC", "CC AC", "MaxCC", "F1", "F2","F1/F2", "MinCC"]:
        print([s,d])
        print(stats.spearmanr(mdf[s], mdf[d]))
        cc, pval = stats.spearmanr(mdf[s], mdf[d])
        #cc = abs(cc)
        #cc = f'{cc:.2f}'
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

ax = sns.heatmap(pldf, annot=ldf, cmap="Spectral", cbar_kws={'label': 'Correlation Coefficient'}, fmt="", linewidth=0.5)
plt.ylabel("In Degree Metrics")
plt.xlabel("TT Properties")
plt.tight_layout()
plt.savefig("F6C.svg",dpi=300)
plt.savefig("F6C.png",dpi=300, pad_inches=0)
plt.show()

