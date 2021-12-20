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
    "axes.labelsize": 7,
    "axes.titlesize": 8,
    "axes.grid": True,
    # Figure
    "figure.autolayout": True,
    "figure.titlesize": 9,
    "savefig.format": "pdf",
    "lines.linewidth": 1,
    # Legend
    "legend.fontsize": 8,
    "legend.frameon": True,
    # Ticks
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
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
df = pd.read_csv("Projectile.dat", engine="python", delimiter="    ", header=None, skipinitialspace=True, comment="#")
print(df)

gs = gridspec.GridSpec(2, 2)

ax = plt.subplot(gs[0, 0])
ax.plot(df[0], df[1], "o-", markersize=1.5, color="C0", label=r"$x(t)$")
ax.plot(df[0], df[2], "o-", markersize=1.5, color="C1", label=r"$y(t)$")
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Position(m)$")
ax.legend(loc="upper left")
plt.title("Position")

ax = plt.subplot(gs[0, 1])
ax.plot(df[0], df[3], "o-", markersize=1.5, color="C0", label=r"$v_{x}(t)$")
ax.plot(df[0], df[4], "o-", markersize=1.5, color="C1", label=r"$v_{y}(t)$")
ax.set_xlim(left=0)
ax.set_ylim(-8, 10)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Velocity(m/s)$")
ax.legend(loc="lower left")
plt.title("Velocity")

ax = plt.subplot(gs[1,:])
ax.plot(df[1], df[2], "o-", markersize=1.5, color="C0", label=r"trace")
ax.set_xlim(left=0, right=12)
ax.set_ylim(bottom=0, top=3)
ax.set_xlabel(r"$X$")
ax.set_ylabel(r"$Y$")
ax.legend(loc="upper right")
plt.title("Trajectory")

# plt.show()
plt.savefig("plots/projectile.pdf")

# %%
