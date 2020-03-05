#! /usr/bin/env python3
#


def i4mat_print(m, n, a, title):

    # *****************************************************************************80
    #
    # I4MAT_PRINT prints an I4MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, integer A(M,N), the matrix.
    #
    #    Input, string TITLE, a title.
    #
    i4mat_print_some(m, n, a, 0, 0, m - 1, n - 1, title)


def i4mat_print_test():

    # *****************************************************************************80
    #
    # I4MAT_PRINT_TEST tests I4MAT_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I4MAT_PRINT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test I4MAT_PRINT, which prints an I4MAT.')

    m = 5
    n = 6
    a = np.array((
        (11, 12, 13, 14, 15, 16),
        (21, 22, 23, 24, 25, 26),
        (31, 32, 33, 34, 35, 36),
        (41, 42, 43, 44, 45, 46),
        (51, 52, 53, 54, 55, 56)))
    title = '  A 5 x 6 integer matrix:'
    i4mat_print(m, n, a, title)
#
#  Terminate.
#
    print('')
    print('I4MAT_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def i4mat_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # I4MAT_PRINT_SOME prints out a portion of an I4MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 September 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of the matrix.
    #
    #    Input, integer A(M,N), an M by N matrix to be printed.
    #
    #    Input, integer ILO, JLO, the first row and column to print.
    #
    #    Input, integer IHI, JHI, the last row and column to print.
    #
    #    Input, string TITLE, a title.
    #
    incx = 5

    print('')
    print(title)

    if (m <= 0 or n <= 0):
        print('')
        print('  (None)')
        return

    for j2lo in range(max(jlo, 0), min(jhi + 1, n), incx):

        j2hi = j2lo + incx - 1
        j2hi = min(j2hi, n)
        j2hi = min(j2hi, jhi)

        print('')
        print('  Col: ', end='')

        for j in range(j2lo, j2hi + 1):
            print('%7d  ' % (j), end='')

        print('')
        print('  Row')

        i2lo = max(ilo, 0)
        i2hi = min(ihi, m)

        for i in range(i2lo, i2hi + 1):

            print(' %4d: ' % (i), end='')

            for j in range(j2lo, j2hi + 1):
                print('%7d  ' % (a[i, j]), end='')

            print('')

    return


def i4mat_print_some_test():

    # *****************************************************************************80
    #
    # I4MAT_PRINT_SOME_TEST tests I4MAT_PRINT_SOME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I4MAT_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4MAT_PRINT_SOME prints some of an I4MAT.')

    m = 4
    n = 6
    v = np.array([
        [11, 12, 13, 14, 15, 16],
        [21, 22, 23, 24, 25, 26],
        [31, 32, 33, 34, 35, 36],
        [41, 42, 43, 44, 45, 46]], dtype=np.int32)
    i4mat_print_some(m, n, v, 0, 3, 2, 5,
                     '  Here is I4MAT, rows 0:2, cols 3:5:')
#
#  Terminate.
#
    print('')
    print('I4MAT_PRINT_SOME_TEST:')
    print('  Normal end of execution.')
    return


def r8vec_print(n, a, title):

    # *****************************************************************************80
    #
    # R8VEC_PRINT prints an R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, real A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d:  %12g' % (i, a[i]))


def r8vec_print_test():

    # *****************************************************************************80
    #
    # R8VEC_PRINT_TEST tests R8VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R8VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_PRINT prints an R8VEC.')

    n = 4
    v = np.array([123.456, 0.000005, -1.0E+06, 3.14159265], dtype=np.float64)
    r8vec_print(n, v, '  Here is an R8VEC:')
#
#  Terminate.
#
    print('')
    print('R8VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def sphere_llq_grid_display(r, pc, lat_num, long_num, node_num, node_xyz,
                            line_num, line_data, filename):

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_DISPLAY displays points and lines of an LLQ grid on a sphere.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2015
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
    import matplotlib.pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
#
#  Draw the grid points.
#
    ax.scatter(node_xyz[:, 0], node_xyz[:, 1], node_xyz[:, 2], 'b')

    for i in range(0, line_num):
        i1 = line_data[i, 0]
        i2 = line_data[i, 1]
        ax.plot([node_xyz[i1, 0], node_xyz[i2, 0]],
                [node_xyz[i1, 1], node_xyz[i2, 1]],
                [node_xyz[i1, 2], node_xyz[i2, 2]], 'r')

    ax.set_xlabel('<---X--->')
    ax.set_ylabel('<---Y--->')
    ax.set_zlabel('<---Z--->')
    ax.set_title('LLQ grid on sphere')
    ax.grid(True)
# ax.axis ( 'equal' )

    plt.savefig(filename)
    plt.show(block=False)
    plt.clf()

    return


def sphere_llq_grid_display_test():

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_DISPLAY_TEST tests SPHERE_LLQ_GRID_DISPLAY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2015
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
    print('SPHERE_LLQ_GRID_DISPLAY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLQ_GRID_DISPLAY displays an LLQ grid on a sphere.')
    print('')
    print('  Number of latitudes is  %d' % (lat_num))
    print('  Number of longitudes is %d' % (long_num))
#
#  Get points.
#
    node_num = sphere_llq_grid_point_count(lat_num, long_num)

    print('')
    print('  The number of grid points is %d' % (node_num))

    node_xyz = sphere_llq_grid_points(r, pc, lat_num, long_num, node_num)
#
#  Get lines.
#
    line_num = sphere_llq_grid_line_count(lat_num, long_num)

    print('')
    print('  Number of line segments is %d' % (line_num))

    line_data = sphere_llq_grid_lines(lat_num, long_num, line_num)

    filename = 'sphere_llq_grid_{:03d}.png'.format(line_num)

    sphere_llq_grid_display(r, pc, lat_num, long_num, node_num, node_xyz,
                            line_num, line_data, filename)
#
#  Terminate.
#
    print('')
    print('SPHERE_LLQ_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')
    return


def sphere_llq_grid_line_count(lat_num, long_num):

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_LINE_COUNT counts lines for an LLQ grid on a sphere.
    #
    #  Discussion:
    #
    #    A SPHERE LLQ grid imposes a grid of quadrilaterals on a sphere,
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
    #    28 April 2015
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
    line_num = long_num * (lat_num + 1) + lat_num * long_num

    return line_num


def sphere_llq_grid_line_count_test():

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_LINE_COUNT_TEST tests SPHERE_LLQ_GRID_LINE_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    lat_num = 3
    long_num = 4

    print('')
    print('SPHERE_LLQ_GRID_LINE_COUNT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLQ_GRID_LINE_COUNT counts the lines used for a')
    print('  grid based on quadrilaterals defined by latitude and longitude')
    print('  lines on a sphere in 3D.')
    print('')
    print('     LAT_NUM    LONG_NUM   LINE_NUM')

    for lat_num in range(1, 19, 2):
        print('')
        long_num = 1
        for long_log in range(1, 5):
            long_num = long_num * 2
            line_num = sphere_llq_grid_line_count(lat_num, long_num)
            print('  %8d  %8d  %8d' % (lat_num, long_num, line_num))
#
#  Terminate.
#
    print('')
    print('SPHERE_LLQ_GRID_LINE_COUNT_TEST:')
    print('  Normal end of execution.')
    return


def sphere_llq_grid_lines(nlat, nlong, line_num):

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_LINES returns lines for an LLQ grid on a sphere.
    #
    #  Discussion:
    #
    #    A SPHERE LLQ grid imposes a grid of quadrilaterals on a sphere,
    #    using latitude and longitude lines.
    #
    #    The point numbering system is the same used in SPHERE_LLQ_GRID_POINTS,
    #    and that routine may be used to compute the coordinates of the points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 April 2015
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

    return line


def sphere_llq_grid_lines_test():

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_LINES_TEST tests SPHERE_LLQ_GRID_LINES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    lat_num = 3
    long_num = 4

    print('')
    print('SPHERE_LLQ_GRID_LINES_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLQ_GRID_LINES computes grid lines')
    print('  on a sphere in 3D.')
    print('')
    print('  Number of latitudes is  %d' % (lat_num))
    print('  Number of longitudes is %d' % (long_num))

    line_num = sphere_llq_grid_line_count(lat_num, long_num)

    print('')
    print('  Number of line segments is %d' % (line_num))

    line = sphere_llq_grid_lines(lat_num, long_num, line_num)

    i4mat_print(line_num, 2, line, '  Grid line vertices:')
#
#  Terminate.
#
    print('')
    print('SPHERE_LLQ_GRID_LINES_TEST:')
    print('  Normal end of execution.')
    return


def sphere_llq_grid_point_count(lat_num, long_num):

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_POINT_COUNT counts points for a SPHERE LLQ grid.
    #
    #  Discussion:
    #
    #    A SPHERE LLQ grid imposes a grid of quadrilaterals on a sphere,
    #    using latitude and longitude lines.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2015
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


def sphere_llq_grid_point_count_test():

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_POINT_COUNT_TEST tests SPHERE_LLQ_GRID_POINT_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    lat_num = 3
    long_num = 4

    print('')
    print('SPHERE_LLQ_GRID_POINT_COUNT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLQ_GRID_POINT_COUNT counts the points used for a')
    print('  grid based on quadrilaterals defined by latitude and longitude')
    print('  lines on a sphere in 3D.')
    print('')
    print('     LAT_NUM    LONG_NUM   POINT_NUM')

    for lat_num in range(1, 19, 2):
        print('')
        long_num = 1
        for long_log in range(1, 5):
            long_num = long_num * 2
            point_num = sphere_llq_grid_point_count(lat_num, long_num)
            print('  %8d  %8d  %8d' % (lat_num, long_num, point_num))
#
#  Terminate.
#
    print('')
    print('SPHERE_LLQ_GRID_POINT_COUNT_TEST:')
    print('  Normal end of execution.')
    return


def sphere_llq_grid_points(r, pc, lat_num, long_num, point_num):

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_POINTS produces points on an LLQ grid on a sphere.
    #
    #  Discussion:
    #
    #    A SPHERE LLQ grid imposes a grid of quadrilaterals on a sphere,
    #    using latitude and longitude lines.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2015
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


def sphere_llq_grid_points_test():

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_POINTS_TEST tests SPHERE_LLQ_GRID_POINTS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    lat_num = 3
    long_num = 4

    pc = np.array([0.0, 0.0, 0.0])
    r = 10.0

    print('')
    print('SPHERE_LLQ_GRID_POINTS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SPHERE_LLQ_POINTS produces latitude/longitude')
    print('  points on a sphere in 3D.')

    print('')
    print('  Radius = %g' % (r))

    r8vec_print(3, pc, '  Center:')

    print('')
    print('  The number of latitudes =  %d' % (lat_num))
    print('  The number of longitudes = %d' % (long_num))

    node_num = sphere_llq_grid_point_count(lat_num, long_num)

    print('')
    print('  The number of grid points is %d' % (node_num))

    node_xyz = sphere_llq_grid_points(r, pc, lat_num, long_num, node_num)

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
#
#  Terminate.
#
    print('')
    print('SPHERE_LLQ_GRID_POINTS_TEST:')
    print('  Normal end of execution.')
    return


def sphere_llq_grid_test():

    # *****************************************************************************80
    #
    # SPHERE_LLQ_GRID_TEST tests the SPHERE_LLQ_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('SPHERE_LLQ_GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the SPHERE_LLQ_GRID library.')
#
#  Library.
#
    sphere_llq_grid_point_count_test()
    sphere_llq_grid_points_test()
    sphere_llq_grid_line_count_test()
    sphere_llq_grid_lines_test()
    sphere_llq_grid_display_test()
#
#  Terminate.
#
    print('')
    print('SPHERE_LLQ_GRID_TEST:')
    print('  Normal end of execution.')
    return


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return None


def timestamp_test():

    # *****************************************************************************80
    #
    # TIMESTAMP_TEST tests TIMESTAMP.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import platform

    print('')
    print('TIMESTAMP_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TIMESTAMP prints a timestamp of the current date and time.')
    print('')

    timestamp()
#
#  Terminate.
#
    print('')
    print('TIMESTAMP_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    sphere_llq_grid_test()
    timestamp()
