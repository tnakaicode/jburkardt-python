import numpy as np
import matplotlib.pyplot as plt


def plot_pnt(dat=np.zeros([3, 10]), name="prob"):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.grid()
    ax1.scatter(dat[:, 0], dat[:, 1], label=name + "-pdf")
    ax1.scatter(dat[:, 0], dat[:, 2], label=name + "-cdf")
    ax2.scatter(dat[:, 0], np.abs(dat[:, 0] - dat[:, 3]), color="RED")
    ax1.legend()
    ax1.set_ylim([0, 1])
    ax2.set_ylim([-0.002, 0.008])
    fig.savefig(name + ".png")
    plt.close()
