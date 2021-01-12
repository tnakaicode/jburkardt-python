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


def polygon_grid_count(n, nv):

    # *****************************************************************************80
    #
    # POLYGON_GRID_COUNT counts the grid points inside a polygon.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals on a side.
    #
    #    Input, integer NV, the number of vertices.
    #    3 <= NV.
    #
    #    Output, integer NG, the number of grid points.
    #
    ng = 1 + nv * (n * (n + 1)) // 2

    return ng


def polygon_grid_count_test():

    # *****************************************************************************80
    #
    # POLYGON_GRID_COUNT_TEST tests POLYGON_GRID_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYGON_GRID_COUNT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_GRID_COUNT counts NG, the number of points in')
    print('  a grid defined with N+1 points on each side of a')
    print('  polygon of NV vertices.')

    for nv in range(3, 6):
        print('')
        print('  Polygonal vertex count NV = %d' % (nv))
        print('')
        print('   N     NG')
        print('')
        for n in range(0, 6):
            ng = polygon_grid_count(n, nv)
            print('  %2d  %5d' % (n, ng))
    print('')
    print('POLYGON_GRID_COUNT_TEST:')
    print('  Normal end of execution.')


def polygon_grid_display(n, nv, v, ng, xg, filename):

    # *****************************************************************************80
    #
    # POLYGON_GRID_DISPLAY displays grid points inside a polygon.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Input, integer NV, the number of vertices in the polygon.
    #
    #    Input, real V[NV,2], the coordinates of the vertices.
    #
    #    Input, integer NG, the number of grid points.
    #
    #    Input, real XG[NG,2], the grid points.
    #
    #    Input, string FILENAME, the name of the plotfile to be created.
    #

    #
    #  Determine the centroid.
    #
    vcx = 0.0
    vcy = 0.0
    for i in range(0, nv):
        vcx = vcx + v[i, 0]
        vcy = vcy + v[i, 1]
    vcx = vcx / float(nv)
    vcy = vcy / float(nv)

    #
    #  Plot the outline of the polygon.
    #
    obj.new_2Dfig()
    obj.axs.plot(v[0:nv, 0], v[0:nv, 1], linewidth=2.0, color='r')
    obj.axs.plot([v[nv - 1, 0], v[0, 0]], [v[nv - 1, 1],
                                           v[0, 1]], linewidth=2.0, color='r')

    #
    #  Plot the internal "ribs"
    #
    for i in range(0, nv):
        obj.axs.plot([v[i, 0], vcx], [v[i, 1], vcy], linewidth=2.0, color='k')

    #
    #  Plot the gridpoints.
    #
    obj.axs.plot(xg[0:ng, 0], xg[0:ng, 1], 'bs')

    #
    #  Cleanup and annotate.
    #
    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.axs.set_title('Grid points in polygon')
    obj.SavePng(filename)

    print('')
    print('  Graphics data saved in file "%s"' % (filename))


def polygon_grid_display_test():

    # *****************************************************************************80
    #
    # POLYGON_GRID_DISPLAY_TEST tests POLYGON_GRID_DISPLAY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYGON_GRID_DISPLAY_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_GRID_DISPLAY displays a grid of points in a polygon.')

    n = 2

    nv = 4
    v = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [2.0, 1.0],
        [1.0, 1.0]])

    ng = 13
    xg = np.array([
        [0.0, 0.0],
        [0.5, 0.0],
        [1.0, 0.0],
        [0.5, 0.25],
        [1.0, 0.25],
        [0.5, 0.5],
        [1.0, 0.5],
        [1.5, 0.5],
        [1.0, 0.75],
        [1.5, 0.75],
        [1.0, 1.0],
        [1.5, 1.0],
        [2.0, 1.0]])

    filename = 'polygon_grid_display_test.png'
    polygon_grid_display(n, nv, v, ng, xg, filename)

    print('')
    print('POLYGON_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')


def polygon_grid_points(n, nv, v, ng):

    # *****************************************************************************80
    #
    # POLYGON_GRID_POINTS computes points on a polygonal grid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Input, integer NV, the number of vertices in the polygon.
    #
    #    Input, real V[NV,2], the coordinates of the vertices.
    #
    #    Input, integer NG, the number of grid points.
    #
    #    Output, real XG[NG,2], the coordinates of the grid points.
    #

    xg = np.zeros([ng, 2])
    p = 0

    #
    #  Determine the centroid.
    #
    vc = np.zeros(2)
    for i in range(0, nv):
        vc[0] = vc[0] + v[i, 0]
        vc[1] = vc[1] + v[i, 1]
    vc[0] = vc[0] / float(nv)
    vc[1] = vc[1] / float(nv)

    #
    #  Use the centroid as the first grid point.
    #
    xg[p, 0] = vc[0]
    xg[p, 1] = vc[1]
    p = p + 1

    #
    #  Consider each triangle formed by two consecutive vertices and the centroid,
    #  but skip the first line of points.
    #
    for l in range(0, nv):
        lp1 = (l % nv)
        for i in range(1, n + 1):
            for j in range(0, n - i + 1):
                k = n - i - j
                xg[p, 0] = (float(i) * v[l, 0] + float(j) *
                            v[lp1, 0] + float(k) * vc[0]) / float(n)
                xg[p, 1] = (float(i) * v[l, 1] + float(j) *
                            v[lp1, 1] + float(k) * vc[1]) / float(n)
                p = p + 1

    return xg


def polygon_grid_points_test01():

    # *****************************************************************************80
    #
    # POLYGON_GRID_POINTS_TEST01 tests POLYGON_GRID_POINTS
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYGON_GRID_POINTS_TEST01:')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_GRID_POINTS returns grid points for a polygon')
    print('  of NV vertices, with N+1 points on a side')
    print('')
    print('  For this test, the polygon is a triangle.')

    #
    #  Define the polygon.
    #
    nv = 3
    v = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [0.5, 0.86602540378443860]])

    r8mat_print(nv, 2, v, '  Polygon vertices:')

    #
    #  Count the grid points.
    #
    n = 5
    ng = polygon_grid_count(n, nv)

    print('')
    print('  N = %d' % (n))
    print('  Number of grid points will be NG = %d' % (ng))

    #
    #  Compute the grid points.
    #
    xg = polygon_grid_points(n, nv, v, ng)
    r8mat_print(ng, 2, xg, '  The grid point array:')
    filename = 'polygon_grid_triangle.png'
    polygon_grid_display(n, nv, v, ng, xg, filename)
    filename = 'polygon_grid_triangle.xy'
    r8mat_write(filename, ng, 2, xg)

    print('')
    print('  Data written to the file "%s"' % (filename))
    print('')
    print('POLYGON_GRID_POINTS_TEST01:')
    print('  Normal end of execution.')


def polygon_grid_points_test02():

    # *****************************************************************************80
    #
    # POLYGON_GRID_POINTS_TEST02 tests POLYGON_GRID_POINTS
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYGON_GRID_POINTS_TEST02:')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_GRID_POINTS returns grid points for a polygon')
    print('  of NV vertices, with N+1 points on a side')
    print('')
    print('  For this test, the polygon is a convex quadrilateral')
    print('  with sides of varying length.')

    #
    #  Define the polygon.
    #
    nv = 4
    v = np.array([
        [1.0, 1.0],
        [2.0, 0.0],
        [4.0, 3.0],
        [0.0, 5.0]])

    r8mat_print(nv, 2, v, '  Polygon vertices:')

    #
    #  Count the grid points.
    #
    n = 7
    ng = polygon_grid_count(n, nv)

    print('')
    print('  N = %d' % (n))
    print('  Number of grid points will be NG = %d' % (ng))

    #
    #  Compute the grid points.
    #
    xg = polygon_grid_points(n, nv, v, ng)
    r8mat_print(ng, 2, xg, '  The grid point array:')
    filename = 'polygon_grid_quad.png'
    polygon_grid_display(n, nv, v, ng, xg, filename)
    filename = 'polygon_grid_quad.xy'
    r8mat_write(filename, ng, 2, xg)

    print('')
    print('  Data written to the file "%s"' % (filename))
    print('')
    print('POLYGON_GRID_POINTS_TEST02:')
    print('  Normal end of execution.')


def polygon_grid_points_test03():

    # *****************************************************************************80
    #
    # POLYGON_GRID_POINTS_TEST03 tests POLYGON_GRID_POINTS
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYGON_GRID_POINTS_TEST03:')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYGON_GRID_POINTS returns grid points for a polygon')
    print('  of NV vertices, with N+1 points on a side')
    print('')
    print('  For this test, the polygon is nonconvex and six sided.')
    print('  Two degenerate triangles are created, and some grid points')
    print('  are generated several times.')

    #
    #  Define the polygon.
    #
    nv = 6
    v = np.array([
        [0.0, 0.0],
        [2.0, 0.0],
        [2.0, 1.0],
        [1.0, 1.0],
        [1.0, 2.0],
        [0.0, 2.0]])

    r8mat_print(nv, 2, v, '  Polygon vertices:')

    #
    #  Count the grid points.
    #
    n = 5
    ng = polygon_grid_count(n, nv)

    print('')
    print('  N = %d' % (n))
    print('  Number of grid points will be NG = %d' % (ng))

    #
    #  Compute the grid points.
    #
    xg = polygon_grid_points(n, nv, v, ng)
    r8mat_print(ng, 2, xg, '  The grid point array:')
    filename = 'polygon_grid_ell.png'
    polygon_grid_display(n, nv, v, ng, xg, filename)
    filename = 'polygon_grid_ell.xy'
    r8mat_write(filename, ng, 2, xg)

    print('')
    print('  Data written to the file "%s"' % (filename))
    print('')
    print('POLYGON_GRID_POINTS_TEST03:')
    print('  Normal end of execution.')


def polygon_grid_test():

    # *****************************************************************************80
    #
    # POLYGON_GRID_TEST tests the POLYGON_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('POLYGON_GRID_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the POLYGON_GRID library.')

    polygon_grid_count_test()
    polygon_grid_display_test()

    polygon_grid_points_test01()
    polygon_grid_points_test02()
    polygon_grid_points_test03()

    print('')
    print('POLYGON_GRID_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polygon_grid_test()
    timestamp()
