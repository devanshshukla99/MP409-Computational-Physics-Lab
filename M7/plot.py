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
    "figure.figsize": (9, 6),
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
df = pd.read_csv("Particle2D.dat", engine="python", delimiter="   ", header=None, skipinitialspace=True, comment="#")

time = df[0].values
pos_x = df[1].values
pos_y = df[2].values

gs = gridspec.GridSpec(2, 2)

ax = plt.subplot(gs[0, 0])
ax.plot(df[0], df[1], "o-", markersize=1.5, color="C0", label=r"$x(t)$")
ax.plot(df[0], df[2], "o-", markersize=1.5, color="C1", label=r"$y(t)$")
ax.set_xlim(left=0)
ax.set_ylim(0, 12)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Position(m)$")
ax.legend(loc="upper left")
plt.title("Position")

ax = plt.subplot(gs[0, 1])
ax.plot(df[0], df[3], "o-", markersize=1.5, color="C0", label=r"$v_{x}(t)$")
ax.plot(df[0], df[4], "o-", markersize=1.5, color="C1", label=r"$v_{y}(t)$")
ax.set_xlim(left=0)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Velocity(m/s)$")
ax.legend(loc="center right")
plt.title("Velocity")

ax = plt.subplot(gs[1, :])
ax.plot(df[1], df[2], "o-", markersize=1.5, color="C0", label="trace")
ax.set_xlim(left=pos_x.min()-1, right=pos_x.max()+1)
ax.set_ylim(pos_y.min()-1, pos_y.max()+1)
ax.vlines(pos_x.max(), pos_y.min(), pos_y.max(), "red", label=rf"$x={pos_x.min()},{pos_x.max()}$")
ax.vlines(pos_x.min(), pos_y.min(), pos_y.max(), "red")
ax.hlines(pos_y.min(), pos_x.min(), pos_x.max(), "red", label=rf"$y={pos_y.min()},{pos_y.max()}$")
ax.hlines(pos_y.max(), pos_x.min(), pos_x.max(), "red")
ax.legend(loc="lower right")
ax.set_xlabel(r"$X$")
ax.set_ylabel(r"$Y$")
plt.title("Trajectory")

plt.savefig("plots/2d.pdf")
# plt.show()

# %%
