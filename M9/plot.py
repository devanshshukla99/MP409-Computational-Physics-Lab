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

df = pd.read_csv("random_no_1.dat", engine="python", delimiter="    ", header=None, skipinitialspace=True, comment="#")

fig = plt.figure(figsize=(4,4))
gs = gridspec.GridSpec(1, 1)
ax = fig.add_subplot(gs[0, 0])
ax.plot(df[1], df[2], "x", markersize=4, color="C0")
ax.set_xlim(0, 102)
ax.set_ylim(0, 102)
ax.set_xlabel(r"$x_{i}$")
ax.set_ylabel(r"$x_{i+1}$")
plt.suptitle("RNG(263,71,100,79)")
plt.title(r"$n=10$")
fig.savefig("outputs/rng_1.pdf")

df = pd.read_csv("random_no_2.dat", engine="python", delimiter="    ", header=None, skipinitialspace=True, comment="#")

fig = plt.figure(figsize=(4,4))
gs = gridspec.GridSpec(1, 1)
ax = fig.add_subplot(gs[0, 0])
ax.plot(df[1], df[2], "x", markersize=4, color="C0")
ax.set_xlim(0, 31)
ax.set_ylim(0, 31)
ax.set_xlabel(r"$x_{i}$")
ax.set_ylabel(r"$x_{i+1}$")
plt.suptitle("RNG(13,0,31,1)")
plt.title(r"$n=10$")
fig.savefig("outputs/rng_2.pdf")
