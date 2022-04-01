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

for cc in ["CC AB", "CC BC", "CC AC"]:
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
        ax = sns.heatmap(pldf, annot=True, cmap="crest", vmin=-0.6, vmax=-0.1, cbar_kws={'label': ''})
        ax.invert_yaxis()
        plt.xlabel("In Degree of "+i2)
        plt.ylabel("In Degree of "+i1)
        plt.title(cc)
        plt.tight_layout()
        cc2 = cc.replace(" ", "")
        plt.savefig("S6"+cc2+i1+i2+".svg",dpi=300)
        plt.savefig("S6"+cc2+i1+i2+".png",dpi=300, pad_inches=0)
        plt.show()
