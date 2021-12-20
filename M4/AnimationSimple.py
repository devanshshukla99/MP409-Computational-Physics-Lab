#!/usr/bin/env python
"""
Author: Devansh Shukla
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

custom_rcparams = {
    "axes.labelsize": 6,
    "axes.titlesize": 8,
    "axes.grid": True,
    # Figure
    "figure.autolayout": True,
    "figure.titlesize": 9,
    "figure.figsize": (10, 3.5),
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

df = pd.read_csv("SimplePendulum.dat", engine="python", delimiter="  ", header=None, skipinitialspace=True, comment="#")

time = df[0].values
theta = df[2].values
pos_x = df[5].values
pos_y = df[6].values
vel_x = df[7].values        
vel_y = df[8].values

gs = mpl.gridspec.GridSpec(1, 2, width_ratios=[1, 1])
fig = plt.figure()
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])

line1, = ax1.plot([], [], 'o-', lw=2, label="Pendulum")
trace, = ax1.plot([], [], ',-', lw=1, label="trace")
_, = ax1.plot([], [], ',-', color="C4", lw=1, label="velocity vector")
time_template = "time = %.1fs"
time_text = ax1.text(0.05, 0.8, '', transform=ax1.transAxes)

patch = plt.Arrow(pos_x[0], pos_y[0], 0.1, 0.1, width=0.1, color="C4")
ax1.add_patch(patch)
ax1.legend()

line_theta, = ax2.plot([], [], '-', lw=2, label=r"$\theta(t)$")
ax2.legend()

line = [line1, line_theta,]

ax1.spines["top"].set_color("none")
ax1.spines["bottom"].set_position("zero")
ax1.spines["left"].set_position("zero")
ax1.spines["right"].set_color("none")
ax1.set_ylim(top=0.0, bottom=(min(pos_y)-1.0))
ax1.set_xlim(left=-(abs(max(pos_x))+1.0), right=(abs(max(pos_x))+1.0))
ax1.set_aspect("equal")
ax1.text(0.05, 1.025, "X", transform=ax1.transAxes)
ax1.text(-0.025, 0.5, "Y", transform=ax1.transAxes)

ax2.set_xlim(0, time[-1])
ax2.set_aspect(4)
ax2.set_ylabel(r"$\theta(rad)$")
ax2.set_xlabel("Time(s)")
ax2.set_ylim(-1.2, 1.2)
ax2.set_title(r"$\theta(t)$")

def init():
    line[0].set_data([], [])
    trace.set_data([], [])
    return line, trace

def animate(i):
    global time, pos_x, pos_y, vel_x, vel_y

    line[0].set_data([0, pos_x[i]], [0, pos_y[i]])
    trace.set_data(pos_x[:i], pos_y[:i])
    time_text.set_text(time_template % (time[i]))

    line[1].set_data(time[:i], theta[:i])
    global ax1, patch
    ax1.patches.remove(patch)
    patch = plt.Arrow(pos_x[i], pos_y[i], vel_x[i]/10, vel_y[i]/10, width=0.1, color="C4")  # Velocity rescaled for arrow length
    ax1.add_patch(patch)

    global captures
    if time[i] in captures:
        toggle_capture()
    return line, trace, time_text

def toggle_capture(*args, **kwargs):
    global ani, capture_no
    ani.pause()
    plt.gcf().savefig(f"plots/simple_capture_{capture_no}.pdf")
    capture_no += 1
    ani.resume()

capture_no = 0
captures = np.arange(2.5, 18.0, 1.0)
captures = np.insert(captures, 0, [0.5, 1.0, 1.5])

ani = FuncAnimation(fig, animate, frames=len(time), interval=10, init_func=init, blit=False, repeat=False)
fig.canvas.mpl_connect('button_press_event', toggle_capture)
writer = FFMpegWriter(fps=10)
ani.save('animation.mp4', writer=writer)
plt.show()
