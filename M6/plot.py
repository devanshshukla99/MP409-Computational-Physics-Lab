#!/usr/bin/env python
"""
Author: Devansh Shukla
"""
# In[0]
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

custom_rcparams = {
    "axes.labelsize": 8,
    "axes.titlesize": 10,
    "axes.grid": True,
    # Figure
    "figure.figsize": (8, 8),
    "figure.autolayout": True,
    "figure.titlesize": 10,
    "savefig.format": "pdf",
    "lines.linewidth": 1,
    # Legend
    "legend.fontsize": 8,
    "legend.frameon": True,
    # Ticks
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "xtick.minor.visible": True,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "ytick.minor.visible": True,
    # TeX
    "pgf.texsystem": "lualatex",
}
mpl.rcParams.update(custom_rcparams)
mpl.use("pgf")
plt.ioff()

# t, x, y, vx, vy
df = pd.read_csv("Particle1D.dat", engine="python", delimiter="    ", header=None, skipinitialspace=True, comment="#")

gs = gridspec.GridSpec(2, 2)

ax = plt.subplot(gs[0, 0])
ax.plot(df[0], df[1], "o-", markersize=1.5, color="C0", label=r"$x(t)$")
ax.set_xlim(left=0, right=34)
ax.set_ylim(-0.5, 11)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Position(m)$")
ax.legend(loc="upper right")
plt.title("Position")

ax = plt.subplot(gs[0, 1])
ax.plot(df[0], df[2], "o-", markersize=1.5, color="C0", label=r"$v_{x}(t)$")
ax.set_xlim(left=0)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Velocity(m/s)$")
ax.legend(loc="upper right")
plt.title("Velocity")

ax = plt.subplot(gs[1, :])
ax.plot(df[1], [0]*len(df[1]), "o-", markersize=1.5, color="C0", label=r"$trace$")
ax.vlines(df[1].values.max(), -2, 2, "red", label=rf"$x={df[1].values.max()}$")
ax.vlines(df[1].values.min(), -2, 2, "red", label=rf"$x={np.abs(df[1].values.min())}$")
ax.set_xlim(left=df[1].values.min()-1, right=df[1].values.max()+1)
ax.set_ylim(-2, 2)
ax.set_xlabel(r"$X$")
ax.set_ylabel(r"$Y$")
ax.legend(loc="upper right")
plt.title("Trajectory")

# plt.show()
plt.savefig("plots/1d.pdf")
