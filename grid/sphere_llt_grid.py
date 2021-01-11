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

obj = plot2d()


def sphere_llt_grid_display(r, pc, lat_num, long_num, node_num, node_xyz,
                            line_num, line_data, filename):

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_DISPLAY displays points and lines of an LLT grid on a sphere.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real R, the radius of the sphere.
    #
    #    Input, real PC(1,3), the center of the sphere.
    #
    #    Input, integer LAT_NUM, LONG_NUM, the number of latitude and longitude
    #    lines to draw.  The latitudes do not include the North and South
    #    poles, which will be included automatically, so LAT_NUM = 5, for instance,
    #    will result in points along 7 lines of latitude.
    #
    #    Input, integer NODE_NUM, the number of grid points.
    #
    #    Input, real NODE_XYZ(NODE_NUM,3), the grid points.
    #
    #    Input, integer LINE_NUM, the number of grid lines.
    #
    #    Input, integer LINE_DATA(LINE_NUM,2), contains pairs of point indices for
    #    line segments that make up the grid.
    #
    #    Input, string FILENAME, the name of a file in which to store a copy
    #    of the plot.
    #

    obj.new_3Dfig()
    obj.axs.scatter(node_xyz[:, 0], node_xyz[:, 1], node_xyz[:, 2], 'b')

    for i in range(0, line_num):
        i1 = line_data[i, 0]
        i2 = line_data[i, 1]
        obj.axs.plot([node_xyz[i1, 0], node_xyz[i2, 0]],
                [node_xyz[i1, 1], node_xyz[i2, 1]],
                [node_xyz[i1, 2], node_xyz[i2, 2]], 'r')

    obj.axs.set_xlabel('<---X--->')
    obj.axs.set_ylabel('<---Y--->')
    obj.axs.set_zlabel('<---Z--->')
    obj.axs.set_title('LLT grid on sphere')
    obj.SavePng(filename)


def sphere_llt_grid_display_test():

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_DISPLAY_TEST tests SPHERE_LLT_GRID_DISPLAY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    lat_num = 10
    long_num = 12
    pc = np.array([0.0, 0.0, 0.0])
    r = 10.0

    print('')
    print('SPHERE_LLT_GRID_DISPLAY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLT_GRID_DISPLAY displays an LLT grid on a sphere.')
    print('')
    print('  Number of latitudes is  %d' % (lat_num))
    print('  Number of longitudes is %d' % (long_num))
#
#  Get points.
#
    node_num = sphere_llt_grid_point_count(lat_num, long_num)

    print('')
    print('  The number of grid points is %d' % (node_num))

    node_xyz = sphere_llt_grid_points(r, pc, lat_num, long_num, node_num)
    
    #
    #  Get lines.
    #
    line_num = sphere_llt_grid_line_count(lat_num, long_num)

    print('')
    print('  Number of line segments is %d' % (line_num))

    line_data = sphere_llt_grid_lines(lat_num, long_num, line_num)
    filename = 'sphere_llt_grid.png'
    sphere_llt_grid_display(r, pc, lat_num, long_num, node_num, node_xyz,
                            line_num, line_data, filename)
    print('')
    print('SPHERE_LLT_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')


def sphere_llt_grid_line_count(lat_num, long_num):

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_LINE_COUNT counts lines for an LLT grid on a sphere.
    #
    #  Discussion:
    #
    #    A SPHERE LLT grid imposes a grid of triangles on a sphere,
    #    using latitude and longitude lines.
    #
    #    The number returned is the number of pairs of points to be connected
    #    to form all the line segments.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer LAT_NUM, LONG_NUM, the number of latitude and
    #    longitude lines to draw.  The latitudes do not include the North and South
    #    poles, which will be included automatically, so LAT_NUM = 5, for instance,
    #    will result in points along 7 lines of latitude.
    #
    #    Output, integer LINE_NUM, the number of grid lines.
    #
    line_num = long_num * (lat_num + 1) \
        + long_num * lat_num \
        + long_num * (lat_num - 1)

    return line_num


def sphere_llt_grid_line_count_test():

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_LINE_COUNT_TEST tests SPHERE_LLT_GRID_LINE_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    lat_num = 3
    long_num = 4

    print('')
    print('SPHERE_LLT_GRID_LINE_COUNT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLT_GRID_LINE_COUNT counts the lines used for a')
    print('  grid based on triangles defined by latitude and longitude')
    print('  lines on a sphere in 3D.')
    print('')
    print('     LAT_NUM    LONG_NUM   LINE_NUM')

    for lat_num in range(1, 19, 2):
        print('')
        long_num = 1
        for long_log in range(1, 5):
            long_num = long_num * 2
            line_num = sphere_llt_grid_line_count(lat_num, long_num)
            print('  %8d  %8d  %8d' % (lat_num, long_num, line_num))
#
#  Terminate.
#
    print('')
    print('SPHERE_LLT_GRID_LINE_COUNT_TEST:')
    print('  Normal end of execution.')
    return


def sphere_llt_grid_lines(nlat, nlong, line_num):

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_LINES returns lines for an LLT grid on a sphere.
    #
    #  Discussion:
    #
    #    A SPHERE LLT grid imposes a grid of triangles on a sphere,
    #    using latitude and longitude lines.
    #
    #    The point numbering system is the same used in SPHERE_LLT_GRID_POINTS,
    #    and that routine may be used to compute the coordinates of the points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer NLAT, NLONG, the number of latitude and longitude
    #    lines to draw.  The latitudes do not include the North and South
    #    poles, which will be included automatically, so NLAT = 5, for instance,
    #    will result in points along 7 lines of latitude.
    #
    #    Input, integer LINE_NUM, the number of grid lines.
    #
    #    Output, integer LINE(LINE_NUM,2), contains pairs of point indices for
    #    line segments that make up the grid.
    #
    import numpy as np

    l = 0
    line = np.zeros([line_num, 2], dtype=np.int32)
#
#  "Vertical" lines.
#
    for j in range(0, nlong):

        old = 0
        new = j + 1
        line[l, 0] = old
        line[l, 1] = new
        l = l + 1

        for i in range(0, nlat - 1):

            old = new
            new = old + nlong
            line[l, 0] = old
            line[l, 1] = new
            l = l + 1

        old = new
        line[l, 0] = old
        line[l, 1] = 1 + nlat * nlong
        l = l + 1
#
#  "Horizontal" lines.
#
    for i in range(0, nlat):

        new = 1 + i * nlong

        for j in range(0, nlong - 1):
            old = new
            new = old + 1
            line[l, 0] = old
            line[l, 1] = new
            l = l + 1

        old = new
        new = 1 + i * nlong
        line[l, 0] = old
        line[l, 1] = new
        l = l + 1
#
#  "Diagonal" lines.
#
    for j in range(0, nlong):

        old = 0
        next = j + 1
        newcol = j

        for i in range(1, nlat):

            old = next
            next = old + nlong + 1
            newcol = newcol + 1

            if (nlong - 1 < newcol):
                newcol = 0
                next = next - nlong

            line[l, 0] = old
            line[l, 1] = next
            l = l + 1

    return line


def sphere_llt_grid_lines_test():

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_LINES_TEST tests SPHERE_LLT_GRID_LINES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    lat_num = 3
    long_num = 4

    print('')
    print('SPHERE_LLT_GRID_LINES_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLT_GRID_LINES computes grid lines')
    print('  on a sphere in 3D.')
    print('')
    print('  Number of latitudes is  %d' % (lat_num))
    print('  Number of longitudes is %d' % (long_num))

    line_num = sphere_llt_grid_line_count(lat_num, long_num)

    print('')
    print('  Number of line segments is %d' % (line_num))

    line = sphere_llt_grid_lines(lat_num, long_num, line_num)
    i4mat_print(line_num, 2, line, '  Grid line vertices:')

    print('')
    print('SPHERE_LLT_GRID_LINES_TEST:')
    print('  Normal end of execution.')


def sphere_llt_grid_point_count(lat_num, long_num):

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_POINT_COUNT counts points for a SPHERE LLT grid.
    #
    #  Discussion:
    #
    #    A SPHERE LLT grid imposes a grid of triangles on a sphere,
    #    using latitude and longitude lines.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer LAT_NUM, LONG_NUM, the number of latitude
    #    and longitude lines to draw.  The latitudes do not include the North and
    #    South poles, which will be included automatically, so LAT_NUM = 5, for
    #    instance, will result in points along 7 lines of latitude.
    #
    #    Output, integer POINT_NUM, the number of grid points.
    #
    point_num = 2 + lat_num * long_num

    return point_num


def sphere_llt_grid_point_count_test():

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_POINT_COUNT_TEST tests SPHERE_LLT_GRID_POINT_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    lat_num = 3
    long_num = 4

    print('')
    print('SPHERE_LLT_GRID_POINT_COUNT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLT_GRID_POINT_COUNT counts the points used for a')
    print('  grid based on triangles defined by latitude and longitude')
    print('  lines on a sphere in 3D.')
    print('')
    print('     LAT_NUM    LONG_NUM   POINT_NUM')

    for lat_num in range(1, 19, 2):
        print('')
        long_num = 1
        for long_log in range(1, 5):
            long_num = long_num * 2
            point_num = sphere_llt_grid_point_count(lat_num, long_num)
            print('  %8d  %8d  %8d' % (lat_num, long_num, point_num))
    print('')
    print('SPHERE_LLT_GRID_POINT_COUNT_TEST:')
    print('  Normal end of execution.')


def sphere_llt_grid_points(r, pc, lat_num, long_num, point_num):

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_POINTS produces points on an LLT grid on a sphere.
    #
    #  Discussion:
    #
    #    A SPHERE LLT grid imposes a grid of triangles on a sphere,
    #    using latitude and longitude lines.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real R, the radius of the sphere.
    #
    #    Input, real PC(1,3), the center of the sphere.
    #
    #    Input, integer LAT_NUM, LONG_NUM, the number of latitude and longitude
    #    lines to draw.  The latitudes do not include the North and South
    #    poles, which will be included automatically, so LAT_NUM = 5, for instance,
    #    will result in points along 7 lines of latitude.
    #
    #    Input, integer POINT_NUM, the number of grid points.
    #
    #    Output, real P(POINT_NUM,3), the grid points.
    #
    import numpy as np

    n = 0
    p = np.zeros([point_num, 3])
#
#  The north pole.
#
    theta = 0.0
    phi = 0.0
    p[n, 0] = pc[0] + r * np.sin(phi) * np.cos(theta)
    p[n, 1] = pc[1] + r * np.sin(phi) * np.sin(theta)
    p[n, 2] = pc[2] + r * np.cos(phi)
    n = n + 1
#
#  Do each intermediate ring of latitude.
#
    for lat in range(1, lat_num + 1):

        phi = np.pi * float(lat) / float(lat_num + 1)
#
#  Along that ring of latitude, compute points at various longitudes.
#
        for lon in range(0, long_num):

            theta = 2.0 * np.pi * float(lon) / float(long_num)

            p[n, 0] = pc[0] + r * np.sin(phi) * np.cos(theta)
            p[n, 1] = pc[1] + r * np.sin(phi) * np.sin(theta)
            p[n, 2] = pc[2] + r * np.cos(phi)
            n = n + 1
#
#  The south pole.
#
    theta = 0.0
    phi = np.pi
    p[n, 0] = pc[0] + r * np.sin(phi) * np.cos(theta)
    p[n, 1] = pc[1] + r * np.sin(phi) * np.sin(theta)
    p[n, 2] = pc[2] + r * np.cos(phi)
    n = n + 1

    return p


def sphere_llt_grid_points_test():

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_POINTS_TEST tests SPHERE_LLT_GRID_POINTS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    lat_num = 3
    long_num = 4

    pc = np.array([0.0, 0.0, 0.0])
    r = 10.0

    print('')
    print('SPHERE_LLT_GRID_POINTS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLT_POINTS produces latitude/longitude')
    print('  points on a sphere in 3D.')

    print('')
    print('  Radius = %g' % (r))

    r8vec_print(3, pc, '  Center:')

    print('')
    print('  The number of latitudes =  %d' % (lat_num))
    print('  The number of longitudes = %d' % (long_num))

    node_num = sphere_llt_grid_point_count(lat_num, long_num)

    print('')
    print('  The number of grid points is %d' % (node_num))

    node_xyz = sphere_llt_grid_points(r, pc, lat_num, long_num, node_num)

    print('')

    k = 0
    print('  %8d' % (k)),
    for i in range(0, 3):
        print('  %12f' % (node_xyz[k, i])),

    print('')

    for lat in range(0, lat_num):
        print('')
        for lon in range(0, long_num):
            k = k + 1
            print('  %8d' % (k)),
            for i in range(0, 3):
                print('  %12f' % (node_xyz[k, i])),
            print('')

    print('')

    k = k + 1
    print('  %8d' % (k)),
    for i in range(0, 3):
        print('  %12f' % (node_xyz[k, i])),
    print('')
    print('')
    print('SPHERE_LLT_GRID_POINTS_TEST:')
    print('  Normal end of execution.')


def sphere_llt_grid_test():

    # *****************************************************************************80
    #
    # SPHERE_LLT_GRID_TEST tests the SPHERE_LLT_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('SPHERE_LLT_GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SPHERE_LLT_GRID library.')

    sphere_llt_grid_point_count_test()
    sphere_llt_grid_points_test()
    sphere_llt_grid_line_count_test()
    sphere_llt_grid_lines_test()
    sphere_llt_grid_display_test()

    print('')
    print('SPHERE_LLT_GRID_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    sphere_llt_grid_test()
    timestamp()
