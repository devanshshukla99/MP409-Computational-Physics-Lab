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
    "figure.figsize": (8, 8),
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

# Read data file
df = pd.read_csv("SimplePendulum.dat", engine="python", delimiter="  ", header=None, skipinitialspace=True, comment="#")
print(df)

# Plot
gs = gridspec.GridSpec(3, 2)

fig = plt.figure()
ax = plt.subplot(gs[0, 0])
plt.plot(df[0], df[5], "o-", markersize=1.5, color="C0", label=r"$x(t)$")
plt.plot(df[0], df[6], "o-", markersize=1.5, color="C1", label=r"$y(t)$")
plt.title("Position")
ax.set_xlim(left=0)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Position(m)$")
plt.legend(loc="upper right")

ax = plt.subplot(gs[0, 1])
plt.plot(df[0], df[7], "o-", markersize=1.5, label=r"$v_{x}(t)$")
plt.plot(df[0], df[8], "o-", markersize=1.5, label=r"$v_{y}(t)$")
plt.title("Velocity")
ax.set_xlim(left=0)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Velocity(m/s)$")
plt.legend(loc="upper right")

ax = plt.subplot(gs[1, 0])
plt.plot(df[0], df[2], "o-", markersize=1.5, color="C0", label=r"$\theta(t)$")
plt.title(r"$\theta$ vs $t$")
ax.set_xlim(left=0)
ax.set_ylim(-1.0, 1.0)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$\theta(rad)$")
plt.legend(loc="upper right")

ax = plt.subplot(gs[1, 1])
plt.plot(df[0], df[3], "o-", markersize=1.5, color="C0", label=r"$\theta'(t)$")
plt.title(r"$\theta'$ vs $t$")
ax.set_xlim(left=0)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$\theta'(rad/s)$")
plt.legend(loc="upper right")

ax = plt.subplot(gs[2, 0])
plt.plot(df[0], df[4], "o-", markersize=1.5, color="C0", label=r"$\theta''(t)$")
plt.title(r"$\theta''$ vs $t$")
ax.set_xlim(left=0)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$\theta''(rad/s^2)$")
plt.legend(loc="upper right")

ax = plt.subplot(gs[2, 1])
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5,0)
ax.text(0.05, 1.025, 'X', transform=ax.transAxes)
ax.text(-0.025, 0.5, 'Y', transform=ax.transAxes)
# ax.set_aspect("equal")
plt.plot(df[5], df[6], "o-", markersize=1.5, color="C1", label="trace")
plt.title("Trajectory trace")
plt.legend(loc="upper right")


plt.suptitle("Simple Pendulum")
plt.savefig("plots/simple_params.pdf")
# plt.show()

# %%


