#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import platform
from scipy.spatial import Delaunay


def delaunay_test():

    # *****************************************************************************80
    #
    # DELAUNAY_TEST tests DELAUNAY and TRIPLOT.
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
    print('DELAUNAY_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  scipy.spatial.Delaunay computes the Delaunay triangulation of a set of points.')
    print('  matplotlib.pyplot.triplot will plot it.')

    nc = 25
    xy = np.random.random([nc, 2])
    triangulation = Delaunay(xy)

    plt.triplot(xy[:, 0], xy[:, 1], triangulation.simplices.copy())
    filename = 'delaunay_test.png'
    plt.savefig(filename)

    print('')
    print('  Saved graphics in file "%s"' % (filename))
    print('')
    print('DELAUNAY_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    delaunay_test()
    timestamp()
