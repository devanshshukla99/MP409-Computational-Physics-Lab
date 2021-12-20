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
    "axes.labelsize": 6,
    "axes.titlesize": 8,
    "axes.grid": True,
    # Figure
    "figure.autolayout": True,
    "figure.titlesize": 9,
    # "figure.dpi": 200,
    "figure.figsize": (9, 4),
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

# Read data file
df = pd.read_csv("CirclePolar.dat", engine="python", delimiter="  ", header=None, skipinitialspace=True, comment="#")

# Extract data
time = df[0].values[::1]
radius = df[1].values[::1]
df_theta = df[2].values
x0 = df[3].iloc[0] - 1
y0 = df[4].iloc[0]
theta = np.arctan((df[4].values - y0)/(df[3].values - x0))
pos_x = df[3].values[::1]
pos_y = df[4].values[::1]

gs = gridspec.GridSpec(1, 2, width_ratios=[1.5, 1])
# Plot
fig = plt.figure()
ax1 = fig.add_subplot(gs[0, 0], projection="polar")
ax2 = fig.add_subplot(gs[0, 1], )
line1, = ax1.plot([], [], 'o', lw=2, label="particle")
line2, = ax2.plot([], [], '-', lw=2, label=r"$\theta(t)$")
trace, = ax1.plot([], [], ',-', lw=1, label="trace")
time_template = "time = %.1fs"
time_text = ax1.text(0, 1.0, '', transform=ax1.transAxes)

line = [line1, line2]

ax1.set_aspect("equal")
ax1.set_rmax(1.5)
ax1.legend()

ax2.hlines(np.pi/2, 0, 10*np.pi, color="red", label=r"$\theta=\pi/2$")
ax2.hlines(-np.pi/2, 0, 10*np.pi, color="red", label=r"$\theta=-\pi/2$")
ax2.set_ylim(-np.pi, np.pi)
ax2.set_xlim(0, 5*np.pi)
ax2.set_xlabel("Time(s)")
ax2.set_ylabel(r"$\theta(rad)$")
ax2.set_aspect(2)
ax2.legend(loc="upper right")

def init():
    line[0].set_data([], [])
    line[1].set_data([], [])
    trace.set_data([], [])
    return line, trace

def animate(i):
    global time, radius, df_theta, pos_x, pos_y, theta
    # line[0].set_data(pos_x[i], pos_y[i])
    line[0].set_data(df_theta[i], radius[i])
    line[1].set_data(time[:i], theta[:i])
    # trace.set_data(pos_x[:i], pos_y[:i])
    trace.set_data(df_theta[:i], radius[:i])
    time_text.set_text(time_template % (time[i]))
    return line, trace, time_text

def toggle_capture(*args, **kwargs):
    global ani, capture_no
    ani.pause()
    plt.gcf().savefig(f"plots/circle_capture_{capture_no}.pdf")
    capture_no += 1
    ani.resume()

capture_no = 0
ani = FuncAnimation(fig, animate,  frames=len(time), interval=1, init_func=init, blit=False, repeat=False)
fig.canvas.mpl_connect('button_press_event', toggle_capture)
writer = FFMpegWriter(fps=10)
ani.save('animation.mp4', writer=writer)
plt.show()