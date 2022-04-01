from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from statannotations.Annotator import Annotator
from math import log
import itertools

mdf = pd.read_csv("TTv2.csv")

print(mdf.shape)
print(mdf)
print(mdf.shape)

sns.set(rc={'figure.figsize':(7,3)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":16,"legend.title_fontsize":16,"font.size":16,"axes.titlesize":16,"axes.labelsize":16,"xtick.labelsize":16,"ytick.labelsize":16})
#sns.set_context("paper", rc={"legend.fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
sns.set_style("ticks")


cb = sns.jointplot(data=mdf, x="In Degree of TT", y="MaxCC", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"])
cb.ax_joint.legend([],[], frameon=False)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("F6i.svg",dpi=400)
plt.savefig("F6i.png",dpi=400, pad_inches=0)

cc = sns.jointplot(data=mdf, x="In Degree of TT", y="F1/F2", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"])
#cc.ax_joint.legend(title="Mean Connectivity",bbox_to_anchor=(1.5, 1), loc=2, borderaxespad=0.)
cc.ax_joint.legend([],[], frameon=False)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("F6ii.svg",dpi=400)
plt.savefig("F6ii.png",dpi=400, pad_inches=0)


bb = sns.jointplot(data=mdf, x="F1", y="MaxCC", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"])
bb.ax_joint.legend([],[], frameon=False)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("F6iii.svg",dpi=400)
plt.savefig("F6iii.png",dpi=400, pad_inches=0)
