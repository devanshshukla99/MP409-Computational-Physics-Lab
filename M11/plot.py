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

plt.style.use("rcStyleSheet.mplstyle")
# mpl.use("pgf")
# plt.ioff()

# In[2]
x = np.linspace(0, 1, 1000)
func = (x**2 + 4*x + 9)**3 * (2*x + 4)

for n in [1000, 2000, 5000, 10000]:
    df = pd.read_csv(f"int_area_{n}.dat", engine="python", delimiter=" ", header=None, skipinitialspace=True, comment="#")
    missed_darts_x = []
    missed_darts_y = []
    hit_darts_x = []
    hit_darts_y = []

    for i in range(0, len(df[0])):
        if df[1][i] <= df[2][i]:
            hit_darts_x.append(df[0][i])
            hit_darts_y.append(df[1][i])
        else:
            missed_darts_x.append(df[0][i])
            missed_darts_y.append(df[1][i])

    fig = plt.figure(figsize=(6,4))
    gs = gridspec.GridSpec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    ax.plot(hit_darts_x, hit_darts_y, "x", markersize=3, color="C0", label=r"Hit")
    ax.plot(missed_darts_x, missed_darts_y, "x", markersize=3, color="C1", label=r"Missed")
    ax.plot(x, func, "-", linewidth=2, markersize=2, color="C5", label=r"$f(x)$")
    ax.set_xlim(left=0, right=1.1)
    ax.set_ylim(0, 18000)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.legend(loc="lower right")
    # plt.suptitle("Integration--Hit or miss")
    plt.title(f"Integration--Hit or miss (n={n})")
    plt.savefig(f"outputs/int_{n}.pdf")

# %%
