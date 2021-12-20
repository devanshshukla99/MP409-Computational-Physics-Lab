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
    "figure.figsize": (10, 5),
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

# t, x, y, z, vx, vy, vz
df = pd.read_csv("Particle3D.dat", engine="python", delimiter="   ", header=None, skipinitialspace=True, comment="#")
print(df)

angle = np.linspace(30, 360, 300)

time = df[0].values
pos_x = df[1].values
pos_y = df[2].values
pos_z = df[3].values
vel_x = df[4].values
vel_y = df[5].values
vel_z = df[6].values

gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1], hspace=0)
fig = plt.figure()
ax1 = fig.add_subplot(gs[0, 0], projection="3d")
ax2 = fig.add_subplot(gs[0, 1])


line1, = ax1.plot3D([], [], [], 'o', lw=2, label="particle")
trace, = ax1.plot3D([], [], [], '-', lw=1, label="trace")
time_template = "time = %.2fs"
time_text = ax1.text2D(0.05, 0.85, '', transform=ax1.transAxes)

line_vx, = ax2.plot([], [], '-', lw=2, label=r"$v_{x}(t)$")
line_vy, = ax2.plot([], [], '-', lw=2, label=r"$v_{y}(t)$")
line_vz, = ax2.plot([], [], '-', lw=2, label=r"$v_{z}(t)$")
ax2.legend()

line = [line1, line_vx, line_vy, line_vz,]
ax1.set_xlim3d([pos_x.min(), pos_x.max()])
ax1.set_xlabel("X", labelpad=0)
ax1.set_ylim3d([pos_y.min(), pos_y.max()])
ax1.set_ylabel("Y", labelpad=0)
ax1.set_zlim3d([pos_z.min(), pos_z.max()])
ax1.set_zlabel("Z", labelpad=0)

xline = np.linspace(pos_x.min(), pos_x.max())
ax1.plot(xline, [pos_y.min()]*len(xline), [pos_z.min()]*len(xline), "red", label=rf"$x={pos_x.min()},{pos_x.max()}$")
ax1.plot(xline, [pos_y.max()]*len(xline), [pos_z.min()]*len(xline), "red")
ax1.plot(xline, [pos_y.min()]*len(xline), [pos_z.max()]*len(xline), "red")
ax1.plot(xline, [pos_y.max()]*len(xline), [pos_z.max()]*len(xline), "red")

yline = np.linspace(pos_y.min(), pos_y.max())
ax1.plot([pos_x.min()]*len(yline), yline, [pos_z.min()]*len(yline), "red", label=rf"$y={pos_y.min()},{pos_y.max()}$")
ax1.plot([pos_x.max()]*len(yline), yline, [pos_z.min()]*len(yline), "red")
ax1.plot([pos_x.min()]*len(yline), yline, [pos_z.max()]*len(yline), "red")
ax1.plot([pos_x.max()]*len(yline), yline, [pos_z.max()]*len(yline), "red")

zline = np.linspace(pos_z.min(), pos_z.max())
ax1.plot([pos_x.min()]*len(zline), [pos_y.min()]*len(zline), zline, "red", label=rf"$z={pos_z.min()},{pos_z.max()}$")
ax1.plot([pos_x.max()]*len(zline), [pos_y.min()]*len(zline), zline, "red")
ax1.plot([pos_x.min()]*len(zline), [pos_y.max()]*len(zline), zline, "red")
ax1.plot([pos_x.max()]*len(zline), [pos_y.max()]*len(zline), zline, "red")

ax1.legend(loc="upper right")
ax1.view_init(30, 30)

ax2.set_xlim(0, 30) #time[-1]+5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_aspect(6)
ax2.set_xlabel(r"$Time(s)$")
ax2.set_ylabel(r"$Velocity(m/s)$")

def init():
    line[0].set_data([], [])
    trace.set_data([], [])
    return line, trace

def animate(i):
    global angle, ax1
    global time, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z

    line[0].set_data(pos_x[i], pos_y[i])
    line[0].set_3d_properties(pos_z[i])
    trace.set_data(pos_x[:i], pos_y[:i])
    trace.set_3d_properties(pos_z[:i])
    time_text.set_text(time_template % (time[i]))

    ax1.view_init(15, angle[i % 300])

    line[1].set_data(time[:i], vel_x[:i])
    line[2].set_data(time[:i], vel_y[:i])
    line[3].set_data(time[:i], vel_z[:i])

    if time[i] == 30.0:
        ax2.set_xlim(0, 60)
        ax2.set_aspect(12)
    captures = np.arange(2.0, 59.9, 2.0)
    captures = np.insert(captures, 0, 0.5)
    if time[i] in captures:
        toggle_capture()

    return line, trace, time_text

def toggle_capture(*args, **kwargs):
    global ani, capture_no
    ani.pause()
    plt.gcf().savefig(f"plots/3d_{capture_no}.pdf")
    capture_no += 1
    ani.resume()

capture_no = 0
ani = FuncAnimation(fig, animate, frames=len(time), interval=10, init_func=init, blit=False, repeat=False)
fig.canvas.mpl_connect('button_press_event', toggle_capture)
writer = FFMpegWriter(fps=10)
ani.save('animation.mp4', writer=writer)
plt.show()
