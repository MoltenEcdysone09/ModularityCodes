from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from statannotations.Annotator import Annotator
from math import log
import itertools

mdf = pd.read_csv("TSv3.csv")

mdf["NInA"] = mdf["NInA"] - 1
mdf["NInB"] = mdf["NInB"] - 1
mdf["Fraction of +ve inTS"] = (mdf["PInA"] + mdf["PInB"])/(mdf["PInA"] + mdf["PInB"] + mdf["NInA"] + mdf["NInB"])
mdf["Fraction of -ve inTS"] = (mdf["NInA"] + mdf["NInB"])/(mdf["PInA"] + mdf["PInB"] + mdf["NInA"] + mdf["NInB"])
mdf["+ve inA"] = mdf["PInA"]/mdf["inA"]
mdf["-ve inA"] = mdf["NInA"]/mdf["inA"]
mdf["+ve inB"] = mdf["PInB"]/mdf["inB"]
mdf["-ve inB"] = mdf["NInB"]/mdf["inB"]


print(mdf.head())
print(mdf)
print(mdf.shape)

sns.set(rc={'figure.figsize':(10,7)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":16,"legend.title_fontsize":16,"font.size":16,"axes.titlesize":16,"axes.labelsize":16,"xtick.labelsize":16,"ytick.labelsize":16})
sns.set_style("ticks")

fig, axs = plt.subplots(2, 2)

r1c1 = sns.kdeplot(ax=axs[0,0], data=mdf, x="Fraction of +ve inTS", hue="Order", fill=True, common_norm=False, alpha=.1, linewidth=2)
axs[0,0].legend([],[], frameon=False)

r1c2 = sns.kdeplot(ax=axs[0,1], data=mdf, x="Fraction of -ve inTS", hue="Order", fill=True, common_norm=False, alpha=.1, linewidth=2)
axs[0,1].legend_.set_bbox_to_anchor((1.02, 1))
axs[0,1].legend_._set_loc(2)

r2c1 = sns.kdeplot(ax=axs[1,0], data=mdf, x="Fraction of +ve inTS", hue="Mean Connectivity", fill=True, common_norm=False, alpha=.1, linewidth=2)
axs[1,0].legend([],[], frameon=False)

r2c2 = sns.kdeplot(ax=axs[1,1], data=mdf, x="Fraction of -ve inTS", hue="Mean Connectivity", fill=True, common_norm=False, alpha=.1, linewidth=2)
axs[1,1].legend_.set_title("Mean Con.")
axs[1,1].legend_.set_bbox_to_anchor((1.02, 1))
axs[1,1].legend_._set_loc(2)

plt.tight_layout()
plt.savefig("S12.svg",dpi=400)
plt.savefig("S12.png",dpi=400, pad_inches=0)
plt.show()
