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
    "figure.figsize": (12, 3.5),
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
df = pd.read_csv("Projectile.dat", engine="python", delimiter="     ", header=None, skipinitialspace=True, comment="#")
print(df)

time = df[0].values
pos_x = df[1].values
pos_y = df[2].values
vel_x = df[3].values
vel_y = df[4].values
vel = np.sqrt(vel_x*vel_x + vel_y*vel_y)

fig, (ax1, ax2) = plt.subplots(1,2)

line1, = ax1.plot([], [], 'o', lw=2, label="particle")
trace, = ax1.plot([], [], ',-', lw=1, label="trace")
time_template = "time = %.2fs"
time_text = ax1.text(0.05, 0.8, '', transform=ax1.transAxes)

line_v, = ax2.plot([], [], '-', lw=2, label=r"$v(t)$")
line_vx, = ax2.plot([], [], '-', lw=2, label=r"$v_{x}(t)$")
line_vy, = ax2.plot([], [], '-', lw=2, label=r"$v_{y}(t)$")
ax2.legend()

line = [line1, line_v, line_vx, line_vy,]
ax1.set_xlim(left=0, right=pos_x[-1] + 2.0)
ax1.set_ylim(0, 5)
ax1.set_title("Trajectory")
ax1.set_xlabel(r"$X$")
ax1.set_ylabel(r"$Y$")
ax1.legend(loc="upper right")

ax2.set_xlim(0, time[-1]+0.1)
ax2.set_ylim(-10, 15)
# ax2.set_aspect(4)
ax2.set_ylabel(r"$v(m/s)$")
ax2.set_xlabel("Time(s)")
ax2.legend(loc="upper right")

def init():
    line[0].set_data([], [])
    trace.set_data([], [])
    return line, trace

def animate(i):
    global time, pos_x, pos_y, vel_x, vel_y, vel

    line[0].set_data(pos_x[i], pos_y[i])
    trace.set_data(pos_x[:i], pos_y[:i])
    time_text.set_text(time_template % (time[i]))

    line[1].set_data(time[:i], vel[:i])
    line[2].set_data(time[:i], vel_x[:i])
    line[3].set_data(time[:i], vel_y[:i])
    return line, trace, time_text

def toggle_capture(*args, **kwargs):
    global ani, capture_no
    ani.pause()
    plt.gcf().savefig(f"plots/proj_{capture_no}.pdf")
    capture_no += 1
    ani.resume()

capture_no = 0
ani = FuncAnimation(fig, animate, frames=len(time), interval=100, init_func=init, blit=False, repeat=False)
fig.canvas.mpl_connect('button_press_event', toggle_capture)
writer = FFMpegWriter(fps=10)
ani.save('animation.mp4', writer=writer)
plt.show()
