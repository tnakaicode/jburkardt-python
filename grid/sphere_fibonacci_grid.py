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
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8mat_transpose_write import r8mat_transpose_write
from r8lib.r82vec_print_part import r82vec_print_part

obj = plot2d()


def sphere_fibonacci_grid_display(ng, xg, filename):

    # *****************************************************************************80
    #
    # SPHERE_FIBONACCI_GRID_DISPLAY displays a Fibonacci grid on a sphere.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer NG, the number of grid points.
    #
    #    Input, real XG(3,NG), the coordinates of the grid points.
    #
    #    Input, string FILENAME, the name of the output file.
    #

    #
    #  Draw the grid points.
    #
    obj.new_3Dfig()
    obj.axs.scatter(xg[:, 0], xg[:, 1], xg[:, 2], 'b')
    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.axs.set_zlabel('<---Z--->')
    obj.axs.set_title('Fibonacci spiral on sphere')
    obj.SavePng(filename)

    print('  Graphics saved as "', filename, '"')


def sphere_fibonacci_grid_display_test():

    # *****************************************************************************80
    #
    # % SPHERE_FIBONACCI_GRID_DISPLAY_TEST tests SPHERE_FIBONACCI_GRID_DISPLAY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SPHERE_FIBONACCI_GRID_DISPLAY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_FIBONACCI_GRID_DISPLAY displays points on a sphere')
    print('  that lie on a Fibonacci spiral.')

    ng = 1000
    print('')
    print('  Number of points NG = %d' % (ng))

    xg = sphere_fibonacci_grid_points(ng)

    #

    #  Display the nodes.

    #
    filename = 'sphere_fibonacci_grid_display.png'

    sphere_fibonacci_grid_display(ng, xg, filename)

    print('')
    print('  Plot saved to file "%s".' % (filename))
    print('')
    print('SPHERE_FIBONACCI_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')


def sphere_fibonacci_grid_points(ng):

    # *****************************************************************************80
    #
    # SPHERE_FIBONACCI_GRID_POINTS: Fibonacci spiral gridpoints on a sphere.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Richard Swinbank, James Purser,
    #    Fibonacci grids: A novel approach to global modelling,
    #    Quarterly Journal of the Royal Meteorological Society,
    #    Volume 132, Number 619, July 2006 Part B, pages 1769-1793.
    #
    #  Parameters:
    #
    #    Input, integer NG, the number of points.
    #
    #    Output, real XG(3,N), the grid points.
    #

    phi = (1.0 + np.sqrt(5.0)) / 2.0

    theta = np.zeros(ng)
    sphi = np.zeros(ng)
    cphi = np.zeros(ng)

    for i in range(0, ng):
        i2 = 2 * i - (ng - 1)
        theta[i] = 2.0 * np.pi * float(i2) / phi
        sphi[i] = float(i2) / float(ng)
        cphi[i] = np.sqrt(float(ng + i2) * float(ng - i2)) / float(ng)

    xg = np.zeros((ng, 3))

    for i in range(0, ng):
        xg[i, 0] = cphi[i] * np.sin(theta[i])
        xg[i, 1] = cphi[i] * np.cos(theta[i])
        xg[i, 2] = sphi[i]

    return xg


def sphere_fibonacci_grid_points_test():

    # *****************************************************************************80
    #
    # % SPHERE_FIBONACCI_GRID_POINTS_TEST tests SPHERE_FIBONACCI_GRID_POINTS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SPHERE_FIBONACCI_GRID_POINTS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_FIBONACCI_GRID_POINTS computes points on a sphere')
    print('  that lie on a Fibonacci spiral.')

    ng = 1000
    print('')
    print('  Number of points NG = %d' % (ng))

    xg = sphere_fibonacci_grid_points(ng)

    r8mat_print_some(ng, 3, xg, 0, 0, 19, 2, '  Part of the grid array:')

    #
    #  Write the nodes to a file.
    #
    filename = 'sphere_fibonacci_grid_points.xyz'
    r8mat_write(filename, ng, 3, xg)

    print('')
    print('SPHERE_FIBONACCI_GRID_POINTS_TEST:')
    print('  Normal end of execution.')


def sphere_fibonacci_grid_test():

    # *****************************************************************************80
    #
    # SPHERE_FIBONACCI_GRID_TEST tests the SPHERE_FIBONACCI_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SPHERE_FIBONACCI_GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SPHERE_FIBONACCI_GRID library.')

    sphere_fibonacci_grid_points_test()
    sphere_fibonacci_grid_display_test()

    print('')
    print('SPHERE_FIBONACCI_GRID_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    sphere_fibonacci_grid_test()
    timestamp()
