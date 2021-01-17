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

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r83col_print_part import r83col_print_part

obj = plot2d()


def wedge_grid_count(n):

    # *****************************************************************************80
    #
    # % WEDGE_GRID_COUNT counts the points in a grid of the unit wedge in 3D.
    #
    #  Discussion:
    #
    #    The interior of the unit wedge in 3D is defined by the constraints:
    #      0 <= X
    #      0 <= Y
    #           X + Y <= 1
    #     -1 <= Z <= +1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #    0 <= N.
    #
    #    Output, integer NG, the number of grid points.
    #
    ng = (n + 1) * ((n + 1) * (n + 2)) // 2

    return ng


def wedge_grid_count_test():

    # *****************************************************************************80
    #
    # WEDGE_GRID_COUNT_TEST tests WEDGE_GRID_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('WEDGE_GRID_COUNT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  WEDGE_GRID_COUNT can define a grid of points')
    print('  with N+1 points on a side')
    print('  over the interior of the unit wedge in 3D.')
    print('')
    print('   N    NG')
    print('')
    for n in range(1, 11):
        ng = wedge_grid_count(n)
        print('  %2d  %4d' % (n, ng))
    print('')
    print('WEDGE_GRID_COUNT_TEST:')
    print('  Normal end of execution.')


def wedge_grid_display(ng, xg, filename):

    # *****************************************************************************80
    #
    # WEDGE_GRID_DISPLAY displays grid points inside the unit wedge.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 April 2015
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
        [0.0, 0.0, -1.0],
        [1.0, 0.0, -1.0],
        [0.0, 1.0, -1.0],
        [0.0, 0.0, +1.0],
        [1.0, 0.0, +1.0],
        [0.0, 1.0, +1.0]
    ])

    obj.new_3Dfig()
    #
    #  Draw the grid points.
    #
    obj.axs.scatter(xg[:, 0], xg[:, 1], xg[:, 2], 'b')

    #
    #  Outline the hexahedron by its edges.
    #
    obj.axs.plot([xv[0, 0], xv[1, 0]], [xv[0, 1], xv[1, 1]],
                 [xv[0, 2], xv[1, 2]], 'r')
    obj.axs.plot([xv[1, 0], xv[2, 0]], [xv[1, 1], xv[2, 1]],
                 [xv[1, 2], xv[2, 2]], 'r')
    obj.axs.plot([xv[2, 0], xv[0, 0]], [xv[2, 1], xv[0, 1]],
                 [xv[2, 2], xv[0, 2]], 'r')

    obj.axs.plot([xv[3, 0], xv[4, 0]], [xv[3, 1], xv[4, 1]],
                 [xv[3, 2], xv[4, 2]], 'r')
    obj.axs.plot([xv[4, 0], xv[5, 0]], [xv[4, 1], xv[5, 1]],
                 [xv[4, 2], xv[5, 2]], 'r')
    obj.axs.plot([xv[5, 0], xv[3, 0]], [xv[5, 1], xv[3, 1]],
                 [xv[5, 2], xv[3, 2]], 'r')

    obj.axs.plot([xv[0, 0], xv[3, 0]], [xv[0, 1], xv[3, 1]],
                 [xv[0, 2], xv[3, 2]], 'r')
    obj.axs.plot([xv[1, 0], xv[4, 0]], [xv[1, 1], xv[4, 1]],
                 [xv[1, 2], xv[4, 2]], 'r')
    obj.axs.plot([xv[2, 0], xv[5, 0]], [xv[2, 1], xv[5, 1]],
                 [xv[2, 2], xv[5, 2]], 'r')

    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.axs.set_zlabel('<---Z--->')
    obj.axs.set_title('Grid points in unit wedge')
    obj.SavePng(filename)
    plt.clf()


def wedge_grid_display_test():

    # *****************************************************************************80
    #
    # WEDGE_GRID_DISPLAY displays grid points inside a unit wedge.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('WEDGE_GRID_DISPLAY_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  WEDGE_GRID_DISPLAY can display a grid of points in the unit wedge.')

    n = 3

    ng = wedge_grid_count(n)
    xg = wedge_grid_points(n, ng)
    filename = 'wedge_grid_display.png'
    wedge_grid_display(ng, xg, filename)

    print('')
    print('WEDGE_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')
    return


def wedge_grid_points(n, ng):

    # *****************************************************************************80
    #
    # % WEDGE_GRID_POINTS computes grid points in the unit wedge in 3D.
    #
    #  Discussion:
    #
    #    The interior of the unit wedge in 3D is defined by the constraints:
    #      0 <= X
    #      0 <= Y
    #           X + Y <= 1
    #     -1 <= Z <= +1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #    0 <= N.
    #
    #    Input, integer NG, the number of grid points.
    #    This can be computed by WEDGE_GRID_SIZE, or else determined by
    #    NG =(N+1)*((N+1)*(N+2))/2.
    #
    #    Output, real XG[NG,3], the coordinates
    #    of the grid points.
    #

    xg = np.zeros((ng, 3))

    if (n == 0):

        xg[0, 0] = 0.5
        xg[0, 1] = 0.5
        xg[0, 2] = 0.0

    else:

        p = 0

        for k in range(0, n + 1):
            kr = float(2 * k - n) / float(n)
            for j in range(0, n + 1):
                jr = float(j) / float(n)
                for i in range(0, n + 1 - j):
                    ir = float(i) / float(n)
                    xg[p, 0] = ir
                    xg[p, 1] = jr
                    xg[p, 2] = kr
                    p = p + 1

    return xg


def wedge_grid_points_test():

    # *****************************************************************************80
    #
    # % WEDGE_GRID_POINTS_TEST tests WEDGE_GRID_POINTS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('WEDGE_GRID_POINTS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  WEDGE_GRID_POINTS determines a unit wedge')
    print('  grid with N+1 points along each edge.')

    n = 6
    print('')
    print('  Grid parameter N = %d' % (n))

    ng = wedge_grid_count(n)
    print('')
    print('  Grid size NG = %d' % (ng))

    xg = wedge_grid_points(n, ng)
    r83col_print_part(ng, xg, 20, '  Wedge grid points:')

    #
    #  Write the data to a file.
    #
    filename = 'wedge_grid_points.xyz'
    r8mat_write(filename, ng, 3, xg)
    print('')
    print('  Data written to the file "%s".' % (filename))

    #
    #  Plot the data.
    #
    filename = 'wedge_grid_points.png'
    wedge_grid_display(ng, xg, filename)
    print('')
    print('  Plot written to the file "%s".' % (filename))

    print('')
    print('WEDGE_GRID_POINTS_TEST:')
    print('  Normal end of execution.')


def wedge_grid_test():

    # *****************************************************************************80
    #
    # WEDGE_GRID_TEST tests the WEDGEE_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('WEDGE_GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the WEDGE_GRID library.')

    wedge_grid_count_test()
    wedge_grid_display_test()
    wedge_grid_points_test()

    print('')
    print('WEDGE_GRID_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    wedge_grid_test()
    timestamp()
