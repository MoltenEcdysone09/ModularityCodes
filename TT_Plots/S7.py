from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from numpy.polynomial.polynomial import polyfit
from math import log

mdf = pd.read_csv("TT.csv")

print(mdf.head())
print(mdf.shape)

sns.set(rc={'figure.figsize':(4,3.5)})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":10,"legend.title_fontsize":10,"font.size":10,"axes.titlesize":10,"axes.labelsize":10,"xtick.labelsize":10,"ytick.labelsize":10})
#sns.set_context("paper", rc={"legend.fontsize":12,"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"xtick.labelsize":12,"ytick.labelsize":12})
sns.set_style("ticks")

for cc in ["F1", "F2", "F3", "F1/F2"]:
    for ii in [["A", "B"], ["B", "C"], ["C", "A"]]:
        i1 = ii[0]
        i2 = ii[1]
        iili = []
        for s in range(1,8):
            for d in range(1,8):
                sdf = mdf[(mdf["In"+i1]==s) & (mdf["In"+i2]==d)]
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
            vmin, vmax = 0.475, 0.650
            cm="crest"
        elif cc == "F2":
            vmin, vmax = 0.320,0.475
            cm="crest_r"
        elif cc == "F3":
            vmin, vmax = 0.025,0.080
            cm="crest_r"
        elif cc == "F1/F2":
            vmin, vmax = 2.2,1.2
            cm="crest"
        ax = sns.heatmap(pldf, annot=True, cmap=cm, vmin=vmin, vmax=vmax, cbar_kws={'label': ''})
        ax.invert_yaxis()
        plt.xlabel("In Degree of "+i2)
        plt.ylabel("In Degree of "+i1)
        plt.title(cc)
        plt.tight_layout()
        if cc == "F1/F2":
            cc2 = cc.replace("/", "")
        else:
            cc2 = cc
        plt.savefig("S7"+cc2+i1+i2+".svg",dpi=300)
        plt.savefig("S7"+cc2+i1+i2+".png",dpi=300, pad_inches=0)
        plt.show()
