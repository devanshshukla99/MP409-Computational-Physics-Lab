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
    "figure.autolayout": True,
    "figure.figsize": (8, 8),
    "figure.titlesize": 11,
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

# t x y dx dy ddx ddy
df = pd.read_csv("CircleCartesian.dat", engine="python", delimiter="   ", header=None, skipinitialspace=True, comment="#")
print(df)

gs = gridspec.GridSpec(2, 2)

fig = plt.figure()
ax = plt.subplot(gs[0, 0])
plt.plot(df[0], df[1], "o-", markersize=1.5, color="C0", label=r"$x(t)$")
plt.plot(df[0], df[2], "o-", markersize=1.5, color="C1", label=r"$y(t)$")
plt.title("Position")
plt.xlim(left=0)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Position(m)$")
plt.legend(loc="upper right")

ax = plt.subplot(gs[0, 1])
plt.plot(df[1], df[2], "o-", markersize=1.5, color="C1", label="trace")
plt.title("Trajectory")
ax.set_aspect("equal")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.legend(loc="upper right")

ax = plt.subplot(gs[1, 0])
plt.plot(df[0], df[3], "o-", markersize=1.5, color="C0", label=r"$v_{x}(t)$")
plt.plot(df[0], df[4], "o-", markersize=1.5, color="C1", label=r"$v_{y}(t)$")
plt.title("Velocity")
plt.xlim(left=0)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Velocity(m/s)$")
plt.legend(loc="upper right")

ax = plt.subplot(gs[1, 1])
plt.plot(df[0], df[5], "o-", markersize=1.5, color="C0", label=r"$a_{x}(t)$")
plt.plot(df[0], df[6], "o-", markersize=1.5, color="C1", label=r"$a_{y}(t)$")
plt.title("Acceleration")
plt.xlim(left=0)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Acceleration(m/s^2)$")
plt.legend(loc="upper right")

plt.suptitle("Circular Motion", fontsize=12)
plt.savefig("plots/i_params.pdf")

# plt.show()
# %%
