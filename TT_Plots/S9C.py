from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from statannotations.Annotator import Annotator
from math import log
import itertools

mdf = pd.read_csv("TTv3.csv")

mdf["In Degree of TT"] = mdf["InA"] + mdf["InB"] + mdf["InC"]

#mdf = mdf[mdf.BF1 != 0]

print(mdf.head())
print(mdf)
print(mdf.shape)


sns.set(rc={'figure.figsize':(6,4)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":16,"legend.title_fontsize":16,"font.size":16,"axes.titlesize":16,"axes.labelsize":16,"xtick.labelsize":16,"ytick.labelsize":16})
sns.set_style("ticks")


cd = sns.scatterplot(data=mdf, x="In Degree of TT", y="Score", hue="Mean Connectivity")
cd.legend_.set_title("Mean Con.")
cd.legend_.set_bbox_to_anchor((1.02, 1))
cd.legend_._set_loc(2)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("S9Ci.svg",dpi=400)
plt.savefig("S9Ci.png",dpi=400, pad_inches=0)
plt.show()

cd = sns.scatterplot(data=mdf, x="In Degree of TT", y="ACoeff", hue="Mean Connectivity")
cd.legend_.set_title("Mean Con.")
cd.legend_.set_bbox_to_anchor((1.02, 1))
cd.legend_._set_loc(2)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("S9Cii.svg",dpi=400)
plt.savefig("S9Cii.png",dpi=400, pad_inches=0)
plt.show()


cd = sns.scatterplot(data=mdf, x="In Degree of TT", y="BCoeff", hue="Mean Connectivity")
cd.legend_.set_title("Mean Con.")
cd.legend_.set_bbox_to_anchor((1.02, 1))
cd.legend_._set_loc(2)
plt.tight_layout()
plt.subplots_adjust(wspace=0.0, hspace=0)
plt.savefig("S9Ciii.svg",dpi=400)
plt.savefig("S9Ciii.png",dpi=400, pad_inches=0)
plt.show()

