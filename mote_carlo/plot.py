import numpy as np
import matplotlib.pyplot as plt


def plot_1d(dat=np.zeros([4, 10]), name="monte_calro.png"):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.grid()
    ax1.plot(dat[:, 0], dat[:, 1], color="blue")
    ax2.plot(dat[:, 0], dat[:, -1], color="red")
    fig.savefig(name)
    plt.close()


def plot_1d_iter(dat=np.zeros([4, 10]), name="monte_calro.png"):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.grid()
    ax1.plot(dat[:, 0], dat[:, 1], color="blue")
    ax2.plot(dat[:, 0], dat[:, -1], color="red")
    fig.savefig(name)
    plt.close()


def plot_2d(dat=np.zeros([4, 10]), name="monte_calro.png"):
    plt.figure()
    plt.tricontourf(dat[:, 0], dat[:, 1], dat[:, 2], cmap="jet")
    plt.scatter(dat[:, 0], dat[:, 1], color="red")
    plt.grid()
    plt.savefig(name)
    plt.close()
