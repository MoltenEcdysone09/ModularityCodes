from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
from numpy.polynomial.polynomial import polyfit
from math import log
from glob import glob

sns.set(rc={'figure.figsize':(5.7,5), 'figure.dpi': 300})
sns.set_context("paper", rc={"font.weight":'bold',"legend.fontsize":14,"legend.title_fontsize":14,"font.size":14,"axes.titlesize":14,"axes.labelsize":14,"xtick.labelsize":14,"ytick.labelsize":14})
sns.set_style("ticks")

for csv in glob("inA*inB*.csv"):
    print(csv)
    df = pd.read_csv(csv)
    tsols = len(df)
    #["HH","LL","HL","LH"]
    stcnt = [0,0,0,0]
    for x in range(tsols):
        if df.iloc[x,0] > 0 and df.iloc[x,1] > 0: #HH
            stcnt[0] = stcnt[0] + 1
        elif df.iloc[x,0] < 0 and df.iloc[x,1] < 0: #LL
            stcnt[1] = stcnt[1] + 1
        elif df.iloc[x,0] > 0 and df.iloc[x,1] < 0: #HL
            stcnt[2] = stcnt[2] + 1
        else: #LH
            stcnt[3] = stcnt[3] + 1
    #Take percentage and convert
    stcnt = [str(round(i/tsols,2)) for i in stcnt]
    g = sns.jointplot(data=df, x="A", y="B", cmap="crest", kind="kde", fill=True, cbar=True, space=0, marginal_kws=dict(color="#254b7f", shade=True), cbar_kws=dict(format='%.2f'))
    g.fig.set_size_inches(6,5)
    plt.subplots_adjust(left=0.15, right=0.8, top=0.9, bottom=0.15)
    # get the current positions of the joint ax and the ax for the marginal x
    pos_joint_ax = g.ax_joint.get_position()
    pos_marg_x_ax = g.ax_marg_x.get_position()
    # reposition the joint ax so it has the same width as the marginal x ax
    g.ax_joint.set_position([pos_joint_ax.x0, pos_joint_ax.y0, pos_marg_x_ax.width, pos_joint_ax.height])
    # reposition the colorbar using new x positions and y positions of the joint ax
    g.fig.axes[-1].set_position([.83, pos_joint_ax.y0, .07, pos_joint_ax.height])
    #g = sns.displot(data=df, x="A", y="B", cmap="crest", cbar=True, kind="kde", fill=True, cbar_kws = dict(format = '%.2f'))
    #g = sns.jointplot(data=df, x="A", y="B", cmap="crest", kind="kde", fill=True, space=0, marginal_kws=dict(color="#254b7f", shade=True))
    g.ax_joint.set_xlim(g.ax_joint.get_xlim()[0]-0.1, g.ax_joint.get_xlim()[1]+0.1)
    g.ax_joint.set_ylim(g.ax_joint.get_ylim()[0]-0.4, g.ax_joint.get_ylim()[1]+0.5)
    g.ax_joint.text(0.75,0.90, stcnt[0]+"%",transform=g.ax_joint.transAxes, fontsize=15)
    g.ax_joint.text(0.05,0.05, stcnt[1]+"%",transform=g.ax_joint.transAxes, fontsize=15)
    g.ax_joint.text(0.75,0.05, stcnt[2]+"%",transform=g.ax_joint.transAxes, fontsize=15)
    g.ax_joint.text(0.05,0.90, stcnt[3]+"%",transform=g.ax_joint.transAxes, fontsize=15)
    g.refline(x=0, y=0, marginal = False, color="black")
    #plt.tight_layout()
    plt.savefig(csv[:-4]+".svg",dpi=400)
    plt.savefig(csv[:-4]+".png",dpi=400, pad_inches=0)
    plt.close()
    plt.clf()
