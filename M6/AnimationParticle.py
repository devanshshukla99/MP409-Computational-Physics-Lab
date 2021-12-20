#!/usr/bin/env python
"""
Author: Devansh Shukla
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import matplotlib.gridspec as gridspec

custom_rcparams = {
    "axes.labelsize": 7,
    "axes.titlesize": 8,
    "axes.grid": True,
    # Figure
    "figure.autolayout": True,
    "figure.titlesize": 9,
    "figure.figsize": (10, 3),
    # "figure.dpi": 150,
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
}
mpl.rcParams.update(custom_rcparams)

# t, x, y, vx, vy
df = pd.read_csv("Particle1D.dat", engine="python", delimiter="   ", header=None, skipinitialspace=True, comment="#")
print(df)

time = df[0].values
pos_x = df[1].values
vel_x = df[2].values

gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1], hspace=0)

fig = plt.figure()
ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[0, 1])
plt.tight_layout()

line1, = ax1.plot([], [], 'o', lw=2, label="particle")
trace, = ax1.plot([], [], '-', lw=1, label="trace")
time_template = "time = %.2fs"
time_text = ax1.text(0.05, 0.8, '', transform=ax1.transAxes)

line_arrow = ax1.plot([], [], "-", color="C4", label=r"$v_x$")
patch = plt.Arrow(pos_x[0], 0, vel_x[0], 0, width=0.15, color="C4")
ax1.add_patch(patch)

line_vx, = ax2.plot([], [], '-', lw=2, label=r"$v_{x}(t)$")
ax2.legend()

line = [line1, line_vx, ]
ax1.set_xlim(left=pos_x.min()-1, right=pos_x.max()+1)
ax1.set_ylim(-2, 2)
ax1.vlines(pos_x.max(), -2, 2, "red", label=rf"$x={pos_x.max()}$")
ax1.vlines(pos_x.min(), -2, 2, "red", label=rf"$x={pos_x.min()}$")
ax1.set_xlabel(r"$X$", labelpad=-0.5)
ax1.set_ylabel(r"$Y$", labelpad=-0.5)
ax1.legend()

ax2.set_xlim(0, time[-1]+1)
ax2.set_ylim(-1.5, 1.5)
ax2.set_xlabel(r"$Time(s)$", labelpad=0)
ax2.set_ylabel(r"$v(m/s)$", labelpad=0)

def init():
    line[0].set_data([], [])
    line[1].set_data([], [])
    trace.set_data([], [])
    return line, trace

def animate(i):
    global time, pos_x, vel_x

    line[0].set_data(pos_x[i], 0)
    trace.set_data(pos_x[:i], 0)
    time_text.set_text(time_template % (time[i]))

    line[1].set_data(time[:i], vel_x[:i])

    global ax1, patch
    ax1.patches.remove(patch)
    patch = plt.Arrow(pos_x[i], 0, vel_x[i], 0, width=0.15, color="C4")
    ax1.add_patch(patch)
    return line, trace, time_text

def toggle_capture(*args, **kwargs):
    global ani, capture_no
    ani.pause()
    plt.gcf().savefig(f"plots/1d_{capture_no}.pdf")
    capture_no += 1
    ani.resume()

capture_no = 0
ani = FuncAnimation(fig, animate, frames=len(time), interval=10, init_func=init, blit=False, repeat=False)
fig.canvas.mpl_connect('button_press_event', toggle_capture)
writer = FFMpegWriter(fps=10)
ani.save('animation.mp4', writer=writer)
plt.show()
