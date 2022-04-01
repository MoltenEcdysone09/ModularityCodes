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


cb = sns.jointplot(data=mdf, x="In Degree of TT", y="F1", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"])
cb.ax_joint.legend([],[], frameon=False)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("S5Ai.svg",dpi=400)
plt.savefig("S5Ai.png",dpi=400, pad_inches=0)

cc = sns.jointplot(data=mdf, x="In Degree of TT", y="F2", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"])
#cc.ax_joint.legend(title="Mean Connectivity",bbox_to_anchor=(1.5, 1), loc=2, borderaxespad=0.)
cc.ax_joint.legend([],[], frameon=False)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("S5Aii.svg",dpi=400)
plt.savefig("S5Aii.png",dpi=400, pad_inches=0)


bb = sns.jointplot(data=mdf, x="In Degree of TT", y="F3", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"])
bb.ax_joint.legend([],[], frameon=False)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("S5Aiii.svg",dpi=400)
plt.savefig("S5Aiii.png",dpi=400, pad_inches=0)


cb = sns.jointplot(data=mdf, x="MaxCC", y="F2", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"])
cb.ax_joint.legend([],[], frameon=False)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("S5Bi.svg",dpi=400)
plt.savefig("S5Bi.png",dpi=400, pad_inches=0)

cc = sns.jointplot(data=mdf, x="MaxCC", y="F3", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"])
#cc.ax_joint.legend(title="Mean Connectivity",bbox_to_anchor=(1.5, 1), loc=2, borderaxespad=0.)
cc.ax_joint.legend([],[], frameon=False)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("S5Bii.svg",dpi=400)
plt.savefig("S5Bii.png",dpi=400, pad_inches=0)


bb = sns.jointplot(data=mdf, x="MaxCC", y="F1/F2", hue="Mean Connectivity", hue_order=["5N & E:2N","20N & E:2N", "E:2N" ,"E:4N", "E:6N"])
bb.ax_joint.legend([],[], frameon=False)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("S5Biii.svg",dpi=400)
plt.savefig("S5Biii.png",dpi=400, pad_inches=0)
