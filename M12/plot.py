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
mpl.use("pgf")
plt.ioff()

# In[2]
for n in [10000]:
    df = pd.read_csv(f"walk_{n}.dat", engine="python", delimiter="     ", header=None, skipinitialspace=True, comment="#")
    print(df)
    fig = plt.figure(figsize=(4, 4))
    gs = gridspec.GridSpec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    ax.plot(df[2], df[3], "-", markersize=1.5, color="C0")
    ax.set_xlabel("X-coordinate")
    ax.set_ylabel("Y-coordinate")
    plt.title(f"Random walk (n={n})")
    plt.savefig(f"outputs/walk_{n}.pdf")
