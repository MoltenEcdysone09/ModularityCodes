from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from statannotations.Annotator import Annotator
from math import log
import itertools

mdf = pd.read_csv("TS.csv")

print(mdf.head())
print(mdf)
print(mdf.shape)

sns.set(rc={'figure.figsize':(5.0,7)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":16,"legend.title_fontsize":16,"font.size":16,"axes.titlesize":16,"axes.labelsize":16,"xtick.labelsize":16,"ytick.labelsize":16})
sns.set_style("ticks")

meanCon = ["E:2N","E:4N","E:6N"]
norder = ["5N","10N","15N","20N"]

pairs = [
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

fig, axs = plt.subplots(2, 1)

cc = sns.boxplot(ax=axs[0],data=mdf, x="Mean Connectivity", y="BiC B", hue="Order")
#annotator = Annotator(cc, pairs, data=mdf, x="Order", y="CC AB", hue="Mean Connectivity")
#annotator.configure(test='Mann-Whitney', text_format='star').apply_and_annotate()
axs[0].set_ylim(0.2, 1)
axs[0].legend(title="Order",bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)


cp = sns.boxplot(ax=axs[1], data=mdf, x="Order", y="BiC B", hue="Mean Connectivity")
annotator = Annotator(cp, pairs, data=mdf, x="Order", y="BiC B", hue="Mean Connectivity")
annotator.configure(test='Mann-Whitney', text_format='star').apply_and_annotate()
axs[1].legend(title="Mean Con.",bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.)

plt.subplots_adjust(left=0.12, right=0.95, bottom=0.12, top=0.95, hspace=0, wspace=0)
plt.tight_layout()
plt.savefig("S1EF.svg",dpi=400)
plt.savefig("S1EF.png",dpi=400, pad_inches=0)
plt.show()
