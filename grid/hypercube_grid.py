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

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8mat_transpose_print import r8mat_transpose_print
from r8lib.r8vec_direct_product import r8vec_direct_product

obj = plot2d()


def hypercube_grid_points(m, n, ns, a, b, c):

    # *****************************************************************************80
    #
    # HYPERCUBE_GRID_POINTS: grid points in a hypercube in M dimensions.
    #
    #  Discussion:
    #
    #    In M dimensional space, a logically rectangular grid is to be created.
    #    In the I-th dimension, the grid will use S(I) points.
    #    The total number of grid points is
    #      N = product ( 1 <= I <= M ) S(I)
    #
    #    Over the interval [A(i),B(i)], we have 5 choices for grid centering:
    #      1: 0,   1/3, 2/3, 1
    #      2: 1/5, 2/5, 3/5, 4/5
    #      3: 0,   1/4, 2/4, 3/4
    #      4: 1/4, 2/4, 3/4, 1
    #      5: 1/8, 3/8, 5/8, 7/8
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of points.
    #    N = product ( 1 <= I <= M ) NS(I).
    #
    #    Input, integer NS(M), the number of points along
    #    each dimension.
    #
    #    Input, real A(M), B(M), the endpoints for each dimension.
    #
    #    Input, integer ( kind = 4 ) C(M), the grid centering for each dimension.
    #    1 <= C(*) <= 5.
    #
    #    Output, real X(M,N) = X(M*S(1),S(2),...,S(M)), the points.
    #

    #
    #  Create the 1D grids in each dimension.
    #
    x = np.zeros((m, n))

    contig = 0
    rep = 0
    skip = 0

    for i in range(0, m):

        s = ns[i]
        xs = np.zeros(s)

        for j in range(0, s):

            if (c[i] == 1):

                if (s == 1):
                    xs[j] = 0.5 * (a[i] + b[i])

                else:
                    xs[j] = ((s - j) * a[i] + (j - 1) * b[i]) / (s - 1)

            elif (c[i] == 2):
                xs[j] = ((s - j + 1) * a[i] + (j) * b[i]) / (s + 1)

            elif (c[i] == 3):
                xs[j] = ((s - j + 1) * a[i] + (j - 1) * b[i]) / (s)

            elif (c[i] == 4):
                xs[j] = ((s - j) * a[i] + (j) * b[i]) / (s)

            elif (c[i] == 5):
                xs[j] = ((2 * s - 2 * j + 1) * a[i] +
                         (2 * j - 1) * b[i]) / (2 * s)

        x, contig, rep, skip = r8vec_direct_product(
            i, s, xs, m, n, x, contig, rep, skip)

    return x


def hypercube_grid_points_test01():

    # *****************************************************************************80
    #
    # HYPERCUBE_GRID_TEST01 tests HYPERCUBE_GRID on a two dimensional example.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 2

    a = np.array([0.0, 0.0])
    b = np.array([1.0, 10.0])
    c = np.array([2, 4])
    ns = np.array([4, 5])

    n = np.prod(ns)

    print('')
    print('HYPERCUBE_GRID_POINTS_TEST01')
    print('  Python version: %s' % (platform.python_version()))
    print('  HYPERCUBE_GRID_POINTS creates a grid of points in a hypercube.')
    print('  Spatial dimension M = %d' % (m))
    print('  Number of grid points N = %d' % (n))
    print('')
    print('     I    NS     C      A         B')
    print('')
    for i in range(0, m):
        print('  %4d  %4d  %4d  %8.4f  %8.4f' % (i, ns[i], c[i], a[i], b[i]))

    x = hypercube_grid_points(m, n, ns, a, b, c)

    #
    #  Transpose the data.
    #
    x = np.transpose(x)

    #
    #  Print the points.
    #
    r8mat_print(n, m, x, '  Grid points:')

    #
    #  Write the data to a file.
    #
    filename = 'hypercube_grid_points_test01.xyz'
    r8mat_write(filename, n, m, x)
    print('')
    print('  Data written to the file "%s".' % (filename))
    print('')
    print('HYPERCUBE_GRID_POINTS_TEST01')
    print('  Normal end of execution.')


def hypercube_grid_points_test02():

    # *****************************************************************************80
    #
    # HYPERCUBE_GRID_TEST02 tests HYPERCUBE_GRID on a five dimensional example.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 5

    a = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    b = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
    c = np.array([1, 2, 3, 4, 5])
    ns = np.array([2, 2, 2, 2, 2])

    n = np.prod(ns)

    print('')
    print('HYPERCUBE_GRID_POINTS_TEST02')
    print('  Python version: %s' % (platform.python_version()))
    print('  HYPERCUBE_GRID_POINTS creates a grid of points in a hypercube.')
    print('  Spatial dimension M = %d' % (m))
    print('  Number of grid points N = %d' % (n))
    print('')
    print('     I    NS     C      A         B')
    print('')
    for i in range(0, m):
        print('  %4d  %4d  %4d  %8.4f  %8.4f' % (i, ns[i], c[i], a[i], b[i]))

    x = hypercube_grid_points(m, n, ns, a, b, c)

    #
    #  Transpose the data.
    #
    x = np.transpose(x)

    #
    #  Print the points.
    #
    r8mat_print(n, m, x, '  Grid points:')

    #
    #  Write the data to a file.
    #
    filename = 'hypercube_grid_points_test02.xyz'
    r8mat_write(filename, n, m, x)
    print('')
    print('  Data written to the file "%s".' % (filename))
    print('')
    print('HYPERCUBE_GRID_POINTS_TEST02')
    print('  Normal end of execution.')


def hypercube_grid_points_test03():

    # *****************************************************************************80
    #
    # HYPERCUBE_GRID_TEST03 tests HYPERCUBE_GRID on a three dimensional example.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3

    a = np.array([-1.0, -1.0, -1.0])
    b = np.array([+1.0, +1.0, +1.0])
    c = np.array([1, 1, 1])
    ns = np.array([3, 3, 3])

    n = np.prod(ns)

    print('')
    print('HYPERCUBE_GRID_POINTS_TEST03')
    print('  Python version: %s' % (platform.python_version()))
    print('  HYPERCUBE_GRID_POINTS creates a grid of points in a hypercube.')
    print('  Spatial dimension M = %d' % (m))
    print('  Number of grid points N = %d' % (n))
    print('')
    print('     I    NS     C      A         B')
    print('')
    for i in range(0, m):
        print('  %4d  %4d  %4d  %8.4f  %8.4f' % (i, ns[i], c[i], a[i], b[i]))

    x = hypercube_grid_points(m, n, ns, a, b, c)

    #
    #  Transpose the data.
    #
    x = np.transpose(x)
    r8mat_print(n, m, x, '  Grid points:')
    filename = 'hypercube_grid_points_test03.xyz'
    r8mat_write(filename, n, m, x)
    print('')
    print('  Data written to the file "%s".' % (filename))
    print('')
    print('HYPERCUBE_GRID_POINTS_TEST03')
    print('  Normal end of execution.')


def hypercube_grid_test():

    # *****************************************************************************80
    #
    # HYPERCUBE_GRID_TEST tests the HYPERCUBE_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('HYPERCUBE_GRID_TEST')
    print('  Python version:')
    print('  Test the HYPERCUBE_GRID library.')

    hypercube_grid_points_test01()
    hypercube_grid_points_test02()
    hypercube_grid_points_test03()

    print('')
    print('HYPERCUBE_GRID_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    hypercube_grid_test()
    timestamp()
