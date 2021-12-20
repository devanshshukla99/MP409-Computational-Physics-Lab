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
    # "figure.dpi": 200,
    "figure.figsize": (8, 3),
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

df = pd.read_csv("CircleCartesian.dat", engine="python", delimiter="   ", header=None, skipinitialspace=True, comment="#")

# Extract data
time = df[0].values[::1]
x0 = df[1].iloc[0] - 1
y0 = df[2].iloc[0]
pos_x = df[1].values[::1]
pos_y = df[2].values[::1]

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2)
line1, = ax1.plot([], [], 'o', lw=2, label="particle")
line2, = ax2.plot([], [], '-', lw=2, label=r"$x(t)$")
line3, = ax2.plot([], [], '-', lw=2, label=r"$y(t)$")
trace, = ax1.plot([], [], ',-', lw=1, label="trace")
time_template = "time = %.1fs"
time_text = ax1.text(0.05, 0.9, '', transform=ax1.transAxes)

line = [line1, line2, line3,]

ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.set_aspect("equal")
ax1.set_xlabel("X", labelpad=0)
ax1.set_ylabel("Y", labelpad=0)
ax1.legend()

ax2.set_xlim(left=0, right=time[-1])
ax2.set_ylim(-1.25, 1.25)
ax2.set_xlabel("Time(s)", labelpad=0)
ax2.set_ylabel("Position", labelpad=0)
ax2.set_aspect(5)
ax2.legend(loc="upper right")

def init():
    line[0].set_data([], [])
    line[1].set_data([], [])
    line[2].set_data([], [])
    trace.set_data([], [])
    return line, trace

def animate(i):
    global time, pos_x, pos_y, theta
    line[0].set_data(pos_x[i], pos_y[i])
    line[1].set_data(time[:i], pos_x[:i])
    line[2].set_data(time[:i], pos_y[:i])
    trace.set_data(pos_x[:i], pos_y[:i])
    time_text.set_text(time_template % (time[i]))
    return line, trace, time_text

def toggle_capture(*args, **kwargs):
    global ani, capture_no
    ani.pause()
    plt.gcf().savefig(f"plots/circle_cart_capture_{capture_no}.pdf")
    capture_no += 1
    ani.resume()

capture_no = 0
ani = FuncAnimation(fig, animate,  frames=len(time), interval=1, init_func=init, blit=False, repeat=False)
fig.canvas.mpl_connect('button_press_event', toggle_capture)
writer = FFMpegWriter(fps=10)
ani.save('animation.mp4', writer=writer)
plt.show()
