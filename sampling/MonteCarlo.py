#
#    Licensing:
#
#    This code is distributed under the GNU LGPL license.
#

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from rnd_uniform.uniform import r8vec_uniform_01, r8mat_uniform_01, r8_uniform_01
from rnd_uniform.sample import triangle01_sample, cube01_sample, ball01_sample, annulus_sample
from rnd_uniform.sample import circle01_sample_ergodic, circle01_sample_random
from rnd_uniform.sample import hypercube01_sample, polygon_sample, ellipsoid_sample
from base import PlotBase


class MonteCarlo (PlotBase):

    def __init__(self, aspect='equal'):
        PlotBase.__init__(self, aspect=aspect)
        self.create_tempdir(-1)

        v0 = np.array([
            [0.0, 0.0],
            [2.0, 0.0],
            [2.0, 1.0],
            [1.0, 1.0],
            [1.0, 2.0],
            [0.0, 1.0]])

        c0 = [0, 0]
        c1 = [1, -1]
        r1 = 1.0
        r2 = 2.0
        r3 = 0.5
        r4 = 3.0

        a = np.array([
            [9.0, 6.0, 3.0],
            [6.0, 5.0, 4.0],
            [3.0, 4.0, 9.0]])

        v1 = np.array([1.0, 2.0, 3.0])

        seed = 123456789
        n = 2**5
        while (n <= 2**14):
            self.PlotTest(*triangle01_sample(n, seed), title="triangle")
            self.PlotTest(*cube01_sample(n, seed), title="cube01")
            self.PlotTest(*ball01_sample(n, seed), title="ball")
            self.PlotTest(*annulus_sample(c0, r1, r2, n, seed),
                          title="annulus01")
            self.PlotTest(*annulus_sample(c1, r3, r4, n, seed))
            self.PlotTest(*polygon_sample(v0, n, seed), title="polygon01")
            self.PlotTest(*circle01_sample_ergodic(n, seed),
                          title="circle_ergodic")
            self.PlotTest(*circle01_sample_random(n, seed),
                          title="circle_random")
            self.PlotTest(*hypercube01_sample(3, n, seed), title="cube02")
            self.PlotTest(*ellipsoid_sample(3, n, a, v1, r1, seed), title="ellipoisd")
            n = 2 * n

    def PlotTest(self, x, seed, title=None):
        dim, num = x.shape
        self.new_fig(dim=dim)
        self.axs.scatter(*x, s=0.5)
        self.axs.set_title("{} n={:d}".format(title, num))
        if title == None:
            self.SavePng_Serial()
        else:
            self.SavePng_Serial(self.tempname + "_" + title + ".png")
        plt.close()


if (__name__ == '__main__'):
    obj = MonteCarlo()
