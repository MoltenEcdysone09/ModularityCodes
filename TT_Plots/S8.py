from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from numpy.polynomial.polynomial import polyfit
from math import log

Mdf = pd.read_csv("TT.csv")

print(Mdf.head())
print(Mdf.shape)

sns.set(rc={'figure.figsize':(4,3.5)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":10,"legend.title_fontsize":10,"font.size":10,"axes.titlesize":10,"axes.labelsize":10,"xtick.labelsize":10,"ytick.labelsize":10})
#sns.set_context("paper", rc={"legend.fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
sns.set_style("ticks")

for inc in [2,7]:
    mdf = Mdf[Mdf["InC"] == inc]
    for cc in ["F1", "F2", "F3", "F1/F2"]:
        iili = []
        for s in range(1,8):
            for d in range(1,8):
                sdf = mdf[(mdf["InA"]==s) & (mdf["InB"]==d)]
                if not sdf.empty:
                    ccmean = round(np.mean(list(sdf[cc])), 3)
                    iili.append([s,d,ccmean])

        ia = [item[0] for item in iili]
        ib = [item[1] for item in iili]
        ccm = [item[2] for item in iili]
        ccmn = [abs(item)*100*5 for item in ccm]

        # HEATMAP CODE
        pldf = pd.DataFrame(iili, columns=["X", "Y", "Value"])
        pldf = pldf.pivot('X', 'Y', 'Value')
        if cc == "F1":
            cmap="crest"
        elif cc == "F2":
            cmap="crest_r"
        elif cc == "F3":
            cmap="crest_r"
        elif cc == "F1/F2":
            cmap="crest"
        ax = sns.heatmap(pldf, annot=True, cmap=cmap, cbar_kws={'label': ''})
        ax.invert_yaxis()
        plt.xlabel("In Degree of B")
        plt.ylabel("In Degree of A")
        plt.title(cc)
        plt.tight_layout()
        if cc == "F1/F2":
            cc2 = cc.replace("/", "")
        else:
            cc2 = cc
        plt.savefig("S8"+cc2+str(inc)+".svg",dpi=300)
        plt.savefig("S8"+cc2+str(inc)+".png",dpi=300, pad_inches=0)
        plt.show()
