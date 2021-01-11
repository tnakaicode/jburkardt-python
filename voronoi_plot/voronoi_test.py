#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import random as rn
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit
from scipy.spatial import Voronoi
from scipy.spatial import voronoi_plot_2d

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

obj = plot2d()


def voronoi_test():

    # *****************************************************************************80
    #
    # VORONOI_TEST tests VORONOI and VORONOI_PLOT_2D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 October 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('VORONOI_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  scipy.spatial.Voronoi computes the Voronoi diagram of a set of points.')
    print('  scipy.spatial.voronoi_plot_2d will plot it.')

    #
    #  Select the points.
    #
    nc = 25
    xy = np.random.random([nc, 2])

    #
    #  Compute the diagram.
    #
    diagram = Voronoi(xy)

    #
    #  Plot the diagram.
    #
    filename = 'voronoi_test.png'
    obj.new_2Dfig(aspect="auto")
    voronoi_plot_2d(diagram, ax=obj.axs)
    obj.SavePng(filename)
    print('')
    print('  Saved graphics in file "%s"' % (filename))
    print('')
    print('VORONOI_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    voronoi_test()
    timestamp()
