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
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r83col_print_part import r83col_print_part

obj = plot2d()


def ball_grid_count(n, r, c):

    # *****************************************************************************80
    #
    # BALL_GRID computes grid points inside a ball.
    #
    #  Discussion:
    #
    #    The grid is defined by specifying the radius and center of the ball,
    #    and the number of subintervals N into which the horizontal radius
    #    should be divided.  Thus, a value of N = 2 will result in 5 points
    #    along that horizontal line.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Input, real R, the radius of the ball.
    #
    #    Input, real C(3), the coordinates of the center of the ball.
    #
    #    Output, integer NG, the number of grid points inside the ball.
    #
    ng = 0

    for i in range(0, n + 1):

        x = c[0] + r * float(2 * i) / float(2 * n + 1)

        for j in range(0, n + 1):

            y = c[1] + r * float(2 * j) / float(2 * n + 1)

            for k in range(0, n + 1):

                z = c[2] + r * float(2 * k) / float(2 * n + 1)

                if (r * r < (x - c[0]) ** 2
                    + (y - c[1]) ** 2
                        + (z - c[2]) ** 2):
                    break

                ng = ng + 1

                if (0 < i):
                    ng = ng + 1

                if (0 < j):
                    ng = ng + 1

                if (0 < k):
                    ng = ng + 1

                if (0 < i and 0 < j):
                    ng = ng + 1

                if (0 < i and 0 < k):
                    ng = ng + 1

                if (0 < j and 0 < k):
                    ng = ng + 1

                if (0 < i and 0 < j and 0 < k):
                    ng = ng + 1

    return ng


def ball_grid_count_test():

    # *****************************************************************************80
    #
    # BALL_GRID_REGULAR_COUNT counts the grid points inside a ball.
    #
    #  Discussion:
    #
    #    The grid is defined by specifying the radius and center of the ball,
    #    and the number of subintervals N into which the radius
    #    should be divided.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BALL_GRID_COUNT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  BALL_GRID_COUNT counts the number of grid points needed')
    print('  for a grid of points inside a ball of radius R and center C.')

    print('')
    print('  N = number of subintervals of the horizontal radius.')
    print('  NG = resulting number of grid points.')
    print('')
    print('     N        NG')
    print('')

    for n in [1, 2, 4, 8, 16]:
        r = 1.0
        c = np.array([0.0, 0.0, 0.0])
        ng = ball_grid_count(n, r, c)
        print('  %4d  %8d' % (n, ng))

    print('')
    print('BALL_GRID_COUNT_TEST:')
    print('  Normal end of execution.')


def ball_grid_display(r, c, ng, xg, filename):

    # *****************************************************************************80
    #
    # BALL_GRID_DISPLAY displays grid points inside a ball.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real R, the radius of the disk.
    #
    #    Input, real C(3), the coordinates of the center of the disk.
    #
    #    Input, integer NG, the number of grid points inside the ball.
    #
    #    Input, real XG(NG,3), the grid points.
    #
    #    Input, real R, the radius of the disk.
    #
    #    Input, string FILENAME, the name of the plotfile to be created.
    #

    obj.new_3Dfig()
    obj.axs.scatter(xg[:, 0], xg[:, 1], xg[:, 2], 'b')
    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.axs.set_zlabel('<---Z--->')
    obj.axs.set_title('Grid points in ball')
    obj.SavePng(filename)
    plt.clf()


def ball_grid_display_test():

    # *****************************************************************************80
    #
    # BALL_GRID_DISPLAY displays grid points inside a ball.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BALL_GRID_DISPLAY_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  BALL_GRID_DISPLAY can display a grid of points in a ball.')

    r = 2.0
    c = np.array([0.0, 0.0, 0.0])
    ng = 25
    xg = np.array([
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [-1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, -1.0],
        [1.0, 1.0, 0.0],
        [1.0, -1.0, 0.0],
        [1.0, 0.0, 1.0],
        [1.0, 0.0, -1.0],
        [-1.0, 1.0, 0.0],
        [-1.0, -1.0, 0.0],
        [-1.0, 0.0, 1.0],
        [-1.0, 0.0, -1.0],
        [0.0, 1.0, 1.0],
        [0.0, 1.0, -1.0],
        [0.0, -1.0, 1.0],
        [0.0, -1.0, -1.0],
        [2.0, 0.0, 0.0],
        [-2.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, -2.0, 0.0],
        [0.0, 0.0, 2.0],
        [0.0, 0.0, -2.0]])

    filename = 'ball_grid_display.png'
    ball_grid_display(r, c, ng, xg, filename)

    print('')
    print('BALL_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')


def ball_grid_points(n, r, c, ng):

    # *****************************************************************************80
    #
    # % BALL_GRID_POINTS computes grid points inside a ball.
    #
    #  Discussion:
    #
    #    The grid is defined by specifying the radius and center of the ball,
    #    and the number of subintervals N into which the horizontal radius
    #    should be divided.  Thus, a value of N = 2 will result in 5 points
    #    along that horizontal line.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Input, real R, the radius of the ball.
    #
    #    Input, real C(3), the coordinates of the center of the ball.
    #
    #    Input, integer NG, the number of grid points, as determined by
    #    BALL_GRID_COUNT.
    #
    #    Output, real BG(3,NG), the grid points inside the ball.
    #

    bg = np.zeros((ng, 3))

    p = 0

    for i in range(0, n + 1):

        x = c[0] + r * float(i) / float(n)

        for j in range(0, n + 1):

            y = c[1] + r * float(j) / float(n)

            for k in range(0, n + 1):

                z = c[2] + r * float(k) / float(n)

                if (r * r < (x - c[0]) ** 2
                    + (y - c[1]) ** 2
                        + (z - c[2]) ** 2):
                    break

                bg[p, 0] = x
                bg[p, 1] = y
                bg[p, 2] = z
                p = p + 1

                if (0 < i):
                    bg[p, 0] = 2.0 * c[0] - x
                    bg[p, 1] = y
                    bg[p, 2] = z
                    p = p + 1

                if (0 < j):
                    bg[p, 0] = x
                    bg[p, 1] = 2.0 * c[1] - y
                    bg[p, 2] = z
                    p = p + 1

                if (0 < k):
                    bg[p, 0] = x
                    bg[p, 1] = y
                    bg[p, 2] = 2.0 * c[2] - z
                    p = p + 1

                if (0 < i and 0 < j):
                    bg[p, 0] = 2.0 * c[0] - x
                    bg[p, 1] = 2.0 * c[1] - y
                    bg[p, 2] = z
                    p = p + 1

                if (0 < i and 0 < k):
                    bg[p, 0] = 2.0 * c[0] - x
                    bg[p, 1] = y
                    bg[p, 2] = 2.0 * c[2] - z
                    p = p + 1

                if (0 < j and 0 < k):
                    bg[p, 0] = x
                    bg[p, 1] = 2.0 * c[1] - y
                    bg[p, 2] = 2.0 * c[2] - z
                    p = p + 1

                if (0 < i and 0 < j and 0 < k):
                    bg[p, 0] = 2.0 * c[0] - x
                    bg[p, 1] = 2.0 * c[1] - y
                    bg[p, 2] = 2.0 * c[2] - z
                    p = p + 1

    return bg


def ball_grid_points_test():

    # *****************************************************************************80
    #
    # % BALL_GRID_POINTS_TEST tests BALL_GRID_POINTS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BALL_GRID_POINTS_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  BALL_GRID_POINTS can define a grid of points')
    print('  with N+1 points on a horizontal or vertical radius,')
    print('  based on any ball.')

    n = 4
    r = 2.0
    c = np.array([1.0, 5.0, 2.0])

    print('')
    print('  We use N = %d' % (n))
    print('  Radius R = %g' % (r))
    print('  Center C = (%g,%g,%g)' % (c[0], c[1], c[2]))

    ng = ball_grid_count(n, r, c)

    print('')
    print('  Number of grid points will be %d' % (ng))

    xg = ball_grid_points(n, r, c, ng)
    r83col_print_part(ng, xg, 20, '  Part of the grid point array:')
    filename = 'ball_grid_points.xyz'
    r8mat_write(filename, ng, 3, xg)

    print('')
    print('  Data written to the file "%s".' % (filename))

    filename = 'ball_grid_points.png'
    ball_grid_display(r, c, ng, xg, filename)

    print('')
    print('  Plot written to the file "%s".' % (filename))
    print('')
    print('BALL_GRID_POINTS_TEST:')
    print('  Normal end of execution.')


def ball_grid_test():

    # *****************************************************************************80
    #
    # BALL_GRID_TEST tests the BALLE_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BALL_GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the BALL_GRID library.')

    ball_grid_display_test()
    ball_grid_count_test()
    ball_grid_points_test()

    print('')
    print('BALL_GRID_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    ball_grid_test()
    timestamp()
