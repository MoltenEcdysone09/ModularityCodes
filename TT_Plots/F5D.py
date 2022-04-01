from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from statannotations.Annotator import Annotator
from math import log
import itertools

mdf = pd.read_csv("TT.csv")

print(mdf.head())
print(mdf)
print(mdf.shape)

sns.set(rc={'figure.figsize':(10.5,8)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":14,"legend.title_fontsize":14,"font.size":14,"axes.titlesize":14,"axes.labelsize":14,"xtick.labelsize":14,"ytick.labelsize":14})
#sns.set_context("paper", rc={"legend.fontsize":14,"font.size":14,"axes.titlesize":14,"axes.labelsize":14,"xtick.labelsize":14,"ytick.labelsize":14})
sns.set_style("ticks")

pairs1 = [
        [("5N", "E:2N"),("5N","E:4N")],
        [("5N", "E:4N"),("5N","E:6N")],
        [("5N", "E:6N"),("5N","E:2N")],
        [("10N", "E:2N"),("10N","E:4N")],
        [("10N", "E:4N"),("10N","E:6N")],
        [("10N", "E:6N"),("10N","E:2N")],
        [("15N", "E:2N"),("15N","E:4N")],
        [("15N", "E:4N"),("15N","E:6N")],
        [("15N", "E:6N"),("15N","E:2N")],
        [("20N", "E:2N"),("20N","E:4N")],
        [("20N", "E:4N"),("20N","E:6N")],
        [("20N", "E:6N"),("20N","E:2N")],
        ]

fig, axs = plt.subplots(1, 3, figsize=(14, 4))


cc = sns.boxplot(ax=axs[0],data=mdf, x="Order", y="F2", hue="Mean Connectivity")
annotator = Annotator(cc, pairs1, data=mdf, x="Order", y="F2", hue="Mean Connectivity")
annotator.configure(test='Mann-Whitney', text_format='star').apply_and_annotate()
axs[0].legend([],[], frameon=False)


cp = sns.boxplot(ax=axs[1], data=mdf, x="Order", y="F3", hue="Mean Connectivity")
annotator = Annotator(cp, pairs1, data=mdf, x="Order", y="F3", hue="Mean Connectivity")
annotator.configure(test='Mann-Whitney', text_format='star').apply_and_annotate()
axs[1].legend([],[], frameon=False)


cb = sns.boxplot(ax=axs[2],data=mdf, x="Order", y="F1/F2", hue="Mean Connectivity")
annotator = Annotator(cb, pairs1, data=mdf, x="Order", y="F1/F2", hue="Mean Connectivity")
annotator.configure(test='Mann-Whitney', text_format='star').apply_and_annotate()
axs[2].legend(title="Mean Connectivity",bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)
#axs[1,2].legend([],[], frameon=False)

plt.tight_layout()
plt.savefig("F5D.svg",dpi=400)
plt.savefig("F5D.png",dpi=400, pad_inches=0)
plt.show()
