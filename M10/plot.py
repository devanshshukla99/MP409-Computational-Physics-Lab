#!/usr/bin/env python
"""
Author: Devansh Shukla
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.style.use("rcStyleSheet.mplstyle")
mpl.use("pgf")
plt.ioff()

n=1000
df = pd.read_csv(f"random_no_{n}.dat", engine="python", delimiter="     ", header=None, skipinitialspace=True, comment="#")

fig = plt.figure(figsize=(4,4))
gs = gridspec.GridSpec(1, 1)
ax = fig.add_subplot(gs[0, 0])

ax.grid(True)
ax.set_aspect("equal")
ax.plot(df[1], df[2], "x", markersize=2.5, color="blue", label="dart")
ax.add_patch(plt.Circle((0, 0), 1, color='r'))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.legend(loc="upper right")
plt.title(rf"n={n}")

plt.suptitle(r"$\pi$-Estimation--Hit or miss")
fig.savefig(f"outputs/pi_est_dart_{n}.pdf")

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(gs[0, 0])

n=2000
df = pd.read_csv(f"random_no_{n}.dat", engine="python", delimiter="     ", header=None, skipinitialspace=True, comment="#")

ax.grid(True)
ax.set_aspect("equal")
ax.plot(df[1], df[2], "x", markersize=2.5, color="blue", label="dart")
ax.add_patch(plt.Circle((0, 0), 1, color='r'))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.legend(loc="upper right")
plt.title(rf"n={n}")

plt.suptitle(r"$\pi$-Estimation--Hit or miss")
fig.savefig(f"outputs/pi_est_dart_{n}.pdf")

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(gs[0, 0])

n=5000
df = pd.read_csv(f"random_no_{n}.dat", engine="python", delimiter="     ", header=None, skipinitialspace=True, comment="#")

ax.grid(True)
ax.set_aspect("equal")
ax.plot(df[1], df[2], "x", markersize=2.5, color="blue", label="dart")
ax.add_patch(plt.Circle((0, 0), 1, color='r'))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.legend(loc="upper right")
plt.title(rf"n={n}")

plt.suptitle(r"$\pi$-Estimation--Hit or miss")
fig.savefig(f"outputs/pi_est_dart_{n}.pdf")
