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
    "figure.dpi": 150,
    "savefig.format": "pdf",
    "lines.linewidth": 1,
    # Legend
    "legend.fontsize": 6,
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
mpl.use('pgf')
plt.ioff()

df = pd.read_csv("CirclePolar.dat", engine="python", delimiter="  ", header=None, skipinitialspace=True, comment="#")
print(df)

# Assuming t0=0, x_at_0=x0+ Rcos(wt0)=1
x0 = df[3].iloc[0] - 1
y0 = df[4].iloc[0]
theta = np.arctan((df[4].values - y0)/(df[3].values - x0))

gs = gridspec.GridSpec(2, 1)

fig = plt.figure()
ax = plt.subplot(gs[0, 0])
plt.plot(df[0], theta, "o-", markersize=2, color="C0", label=r"$\theta(t)$")
plt.hlines(y=np.pi/2, xmin=df[0].values[0], xmax=df[0].values[-1], color="red", label=r"$\pi/2$")
plt.hlines(y=-np.pi/2, xmin=df[0].values[0], xmax=df[0].values[-1], color="red", label=r"$-\pi/2$")
plt.xlim(left=0)
plt.ylim(-np.pi, np.pi)
plt.title(r"$\theta(t)$")
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$\theta(rad)$")
plt.legend(loc="upper right")

ax = plt.subplot(gs[1, 0])
plt.plot(df[0], df[3], "o-", markersize=2, color="C0", label=r"$x(t)$")
plt.plot(df[0], df[4], "o--", markersize=2, color="C1", label=r"$y(t)$")
plt.title("Position")
plt.xlim(left=0)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Position(m)$")
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("plots/ii_params.pdf")

fig, ax = plt.subplots(subplot_kw={"projection":"polar"})
plt.plot(df[2], df[1], "o-", markersize=2, color="C0", label="trace")
ax.set_rmax(1.5)
plt.title("Trajectory")
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("plots/ii_polar.pdf")

fig, ax = plt.subplots()
plt.plot(df[3], df[4], "o-", markersize=2, color="C0", label="trace")
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title("Trajectory")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="upper right")
ax.set_aspect("equal")
plt.tight_layout()
plt.savefig("plots/ii_cart.pdf")

# plt.show()
# %%
