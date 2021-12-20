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
    "axes.titleweight": "normal",
    "axes.grid": True,
    # Figure
    "figure.autolayout": True,
    "figure.figsize": (9, 6),
    "figure.titlesize": 10,
    "savefig.format": "pdf",
    "lines.linewidth": 1,
    # Legend
    "legend.fontsize": 8,
    "legend.frameon": True,
    # Ticks
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
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

# t, x, y, z, vx, vy, vz
df = pd.read_csv("Particle3D.dat", engine="python", delimiter="   ", header=None, skipinitialspace=True, comment="#")

fig = plt.figure(figsize=(10,4))
gs = gridspec.GridSpec(1, 2)
ax = fig.add_subplot(gs[0, 0])
ax.plot(df[0], df[1], "o-", markersize=1.5, color="C0", label=r"$x(t)$")
ax.plot(df[0], df[2], "o-", markersize=1.5, color="C1", label=r"$y(t)$")
ax.plot(df[0], df[3], "o-", markersize=1.5, color="C2", label=r"$z(t)$")
ax.set_xlim(left=0)
ax.set_ylim(0, 12)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Position(m)$")
ax.legend(loc="upper right")
plt.title("Position")

ax = fig.add_subplot(gs[0, 1])
ax.plot(df[0], df[4], "o-", markersize=1.5, color="C0", label=r"$v_{x}(t)$")
ax.plot(df[0], df[5], "o-", markersize=1.5, color="C1", label=r"$v_{y}(t)$")
ax.plot(df[0], df[6], "o-", markersize=1.5, color="C2", label=r"$v_{z}(t)$")
ax.set_xlim(left=0)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel(r"$Time(s)$")
ax.set_ylabel(r"$Velocity(m/s)$")
ax.legend(loc="center right")
plt.title("Velocity")

plt.savefig("plots/3d.pdf")

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection="3d")
ax.plot3D(df[1], df[2], df[3], "o-", markersize=1.5, color="C0", label=r"$trace$")
ax.set_xlim3d([df[1].values.min(), df[1].values.max()])
ax.set_xlabel(r"$X$")
ax.set_ylim3d([df[2].values.min(), df[2].values.max()])
ax.set_ylabel(r"$Y$")
ax.set_zlim3d([df[3].values.min(), df[3].values.max()])
ax.set_zlabel(r"$Z$")
xline = np.linspace(df[1].values.min(), df[1].values.max())
ax.plot(xline, [df[2].values.min()]*len(xline), [df[3].values.min()]*len(xline), "red", label=rf"$x={df[1].min()},{df[1].max()}$")
ax.plot(xline, [df[2].values.max()]*len(xline), [df[3].values.min()]*len(xline), "red")
ax.plot(xline, [df[2].values.min()]*len(xline), [df[3].values.max()]*len(xline), "red")
ax.plot(xline, [df[2].values.max()]*len(xline), [df[3].values.max()]*len(xline), "red")

yline = np.linspace(df[2].values.min(), df[2].values.max())
ax.plot([df[1].values.min()]*len(yline), yline, [df[3].values.min()]*len(yline), "red", label=rf"$y={df[2].min()},{df[2].max()}$")
ax.plot([df[1].values.max()]*len(yline), yline, [df[3].values.min()]*len(yline), "red")
ax.plot([df[1].values.min()]*len(yline), yline, [df[3].values.max()]*len(yline), "red")
ax.plot([df[1].values.max()]*len(yline), yline, [df[3].values.max()]*len(yline), "red")

zline = np.linspace(df[3].values.min(), df[3].values.max())
ax.plot([df[1].values.min()]*len(zline), [df[2].values.min()]*len(zline), zline, "red", label=rf"$z={df[3].min()},{df[3].max()}$")
ax.plot([df[1].values.max()]*len(zline), [df[2].values.min()]*len(zline), zline, "red")
ax.plot([df[1].values.min()]*len(zline), [df[2].values.max()]*len(zline), zline, "red")
ax.plot([df[1].values.max()]*len(zline), [df[2].values.max()]*len(zline), zline, "red")
ax.legend()
ax.view_init(15, 60)
ax.set_title("Trajectory")

# plt.show()
plt.savefig("plots/3d_traj.pdf")

# %%
