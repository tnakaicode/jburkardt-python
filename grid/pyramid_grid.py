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
from r8lib.r83col_print_part import r83col_print_part

obj = plot2d()


def pyramid_grid_count(n):

    # *****************************************************************************80
    #
    # PYRAMID_GRID_COUNT counts the points in a pyramid grid.
    #
    #  Discussion:
    #
    #    0:  x
    #
    #    1:  x  x
    #        x  x
    #
    #    2:  x  x  x
    #        x  x  x
    #        x  x  x
    #
    #    3:  x  x  x  x
    #        x  x  x  x
    #        x  x  x  x
    #        x  x  x  x
    #
    #    N  Size
    #
    #    0     1
    #    1     5 = 1 + 4
    #    2    14 = 1 + 4 + 9
    #    3    30 = 1 + 4 + 9 + 16
    #    4    55 = 1 + 4 + 9 + 16 + 25
    #    5    91 = 1 + 4 + 9 + 16 + 25 + 36
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Output, integer VALUE, the number of
    #    nodes in the grid of size N.
    #
    np1 = n + 1

    value = (np1 * (np1 + 1) * (2 * np1 + 1)) // 6

    return value


def pyramid_grid_count_test():

    # *****************************************************************************80
    #
    # PYRAMID_GRID_COUNT_TEST tests PYRAMID_GRID_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PYRAMID_GRID_COUNT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  PYRAMID_GRID_COUNT can count the grid points in a pyramid')
    print('  with N+1 points on a side.')

    print('')
    print('     N        NG')
    print('')

    for n in [1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 100]:
        ng = pyramid_grid_count(n)
        print('  %4d  %8d' % (n, ng))

    print('')
    print('PYRAMID_GRID_COUNT_TEST:')
    print('  Normal end of execution.')


def pyramid_grid_display(ng, xg, filename):

    # *****************************************************************************80
    #
    # PYRAMID_GRID_DISPLAY displays grid points inside the unit pyramid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer NG, the number of grid points.
    #
    #    Input, real XG[NG,3], the grid points.
    #
    #    Input, string FILENAME, the name of the plotfile to be created.
    #

    xv = np.array([
        [0.0, 0.0, +1.0],
        [-1.0, -1.0, 0.0],
        [+1.0, -1.0, 0.0],
        [+1.0, +1.0, 0.0],
        [-1.0, +1.0, 0.0]])

    obj.new_3Dfig()
    obj.axs.scatter(xg[:, 0], xg[:, 1], xg[:, 2], 'b')
    obj.axs.plot([xv[0, 0], xv[1, 0]], [xv[0, 1], xv[1, 1]],
                 [xv[0, 2], xv[1, 2]], 'r')
    obj.axs.plot([xv[0, 0], xv[2, 0]], [xv[0, 1], xv[2, 1]],
                 [xv[0, 2], xv[2, 2]], 'r')
    obj.axs.plot([xv[0, 0], xv[3, 0]], [xv[0, 1], xv[3, 1]],
                 [xv[0, 2], xv[3, 2]], 'r')
    obj.axs.plot([xv[0, 0], xv[4, 0]], [xv[0, 1], xv[4, 1]],
                 [xv[0, 2], xv[4, 2]], 'r')
    obj.axs.plot([xv[4, 0], xv[1, 0]], [xv[4, 1], xv[1, 1]],
                 [xv[4, 2], xv[1, 2]], 'r')
    obj.axs.plot([xv[1, 0], xv[2, 0]], [xv[1, 1], xv[2, 1]],
                 [xv[1, 2], xv[2, 2]], 'r')
    obj.axs.plot([xv[2, 0], xv[3, 0]], [xv[2, 1], xv[3, 1]],
                 [xv[2, 2], xv[3, 2]], 'r')
    obj.axs.plot([xv[3, 0], xv[4, 0]], [xv[3, 1], xv[4, 1]],
                 [xv[3, 2], xv[4, 2]], 'r')

    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.axs.set_zlabel('<---Z--->')
    obj.axs.set_title('Grid points in unit pyramid')
    obj.SavePng(filename)


def pyramid_grid_display_test(n=3):

    # *****************************************************************************80
    #
    # PYRAMID_GRID_DISPLAY displays grid points inside a unit pyramid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PYRAMID_GRID_DISPLAY_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  PYRAMID_GRID_DISPLAY can display a grid of points in the unit pyramid.')

    ng = pyramid_grid_count(n)
    xg = pyramid_grid_points(n, ng)

    filename = 'pyramid_grid_display_{:02d}.png'.format(n)
    pyramid_grid_display(ng, xg, filename)

    print('')
    print('PYRAMID_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')


def pyramid_grid_points(n, ng):

    # *****************************************************************************80
    #
    # PYRAMID_GRID_POINTS computes grid points in the unit pyramid.
    #
    #  Discussion:
    #
    #    The unit pyramid has base (-1,-1,0), (+1,1,0), (+1,+1,0), (-1,+1,0)
    #    and vertex (0,0,1).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Input, real NG, the number of nodes to generate,
    #    as determined by pyramid_grid_size().
    #
    #    Output, real XG[Ng,3], the grid point coordinates.
    #

    xg = np.zeros((ng, 3))
    g = 0

    for k in range(n, -1, -1):
        hi = n - k
        lo = - hi
        for j in range(lo, hi + 1, 2):
            for i in range(lo, hi + 1, 2):
                xg[g, 0] = float(i) / float(n)
                xg[g, 1] = float(j) / float(n)
                xg[g, 2] = float(k) / float(n)
                g = g + 1

    return xg


def pyramid_grid_points_test():

    # *****************************************************************************80
    #
    # % PYRAMID_GRID_POINTS_TEST tests PYRAMID_GRID_POINTS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PYRAMID_GRID_POINTS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PYRAMID_GRID_POINTS determines a unit pyramid')
    print('  grid with N+1 points along each edge.')

    n = 4

    print('')
    print('  Grid parameter N = %d' % (n))

    ng = pyramid_grid_count(n)

    print('')
    print('  Grid size NG = %d' % (ng))

    xg = pyramid_grid_points(n, ng)
    r83col_print_part(ng, xg, 20, '  Pyramid grid points:')
    filename = 'pyramid_grid_points.xyz'
    r8mat_write(filename, ng, 3, xg)

    print('')
    print('  Data written to the file "%s".' % (filename))
    filename = 'pyramid_grid_points.png'
    pyramid_grid_display(ng, xg, filename)

    print('')
    print('  Plot written to the file "%s".' % (filename))
    print('')
    print('PYRAMID_GRID_POINTS_TEST:')
    print('  Normal end of execution.')


def pyramid_grid_test():

    # *****************************************************************************80
    #
    # PYRAMID_GRID_TEST tests the PYRAMIDE_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PYRAMID_GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the PYRAMID_GRID library.')

    pyramid_grid_count_test()
    pyramid_grid_display_test(n=3)
    pyramid_grid_display_test(n=4)
    pyramid_grid_display_test(n=5)
    pyramid_grid_display_test(n=10)
    pyramid_grid_points_test()

    print('')
    print('PYRAMID_GRID_TEST:')
    print('  Normal end of execution.')


def pyramid_unit_vertices():

    # *****************************************************************************80
    #
    # PYRAMID_UNIT_VERTICES returns the vertices of the unit pyramid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real V1(3), V2(3), V3(3), V4(3), V5(3), the vertices.
    #

    v1 = np.array([0.0, 0.0, +1.0])
    v2 = np.array([-1.0, -1.0, 0.0])
    v3 = np.array([+1.0, -1.0, 0.0])
    v4 = np.array([+1.0, +1.0, 0.0])
    v5 = np.array([-1.0, +1.0, 0.0])

    return v1, v2, v3, v4, v5


if (__name__ == '__main__'):
    timestamp()
    pyramid_grid_test()
    timestamp()
