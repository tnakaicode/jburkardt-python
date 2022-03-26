#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


def cobweb_plot(f, x0, N, a=0, b=1):

    # *****************************************************************************80
    #
    # cobweb_plot makes a cobweb plot of a function iteration.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 February 2020
    #
    #  Author:
    #
    #    John D Cook.
    #    Modifications by John Burkardt
    #
    #  Reference:
    #
    #    John D Cook,
    #    Cobweb plots,
    #    https://www.johndcook.com/blog/2020/01/19/cobweb-plots/
    #    Posted 19 January 2020.
    #

    t = np.linspace(a, b, N)

    obj = plot2d()
    obj.axs.set_title("x0={:.2f}".format(x0))

    #
    #  Plot the function.
    #
    obj.axs.plot(t, f(t), 'k')

    #
    #  Plot the dotted line y = x.
    #
    obj.axs.plot(t, t, "k:")

    #
    #  Plot the iterates.
    #
    x = x0
    y = f(x0)
    for _ in range(N):
        fy = f(y)
        obj.axs.plot([x, y], [y, y], 'b', linewidth=1)
        obj.axs.plot([y, y], [y, fy], 'b', linewidth=1)
        x = y
        y = fy

    filename = 'cobweb_plot.png'
    obj.SavePng(filename)
    obj.SavePng_Serial()
    print('  Graphics saved as "%s"' % (filename))


def cobweb_plot_test():

    # *****************************************************************************80
    #
    # cobweb_plot_test tests cobweb_plot
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 February 2020
    #
    #  Author:
    #
    #    John D Cook.
    #    Modifications by John Burkardt
    #

    print('')
    print('cobweb_plot_test')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test cobweb_plot.')

    cobweb_plot(np.cos, 0.1, 30)
    cobweb_plot(np.cos, 0.5, 30)
    cobweb_plot(np.cos, 0.9, 30)
    cobweb_plot(np.cos, 1.0, 30)

    print('')
    print('cobweb_plot_test:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    cobweb_plot_test()
    timestamp()
