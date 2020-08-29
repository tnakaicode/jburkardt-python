#! /usr/bin/env python3
#


def ellipsoid_grid_count(n, r, c):

    # *****************************************************************************80
    #
    # ELLIPSOID_GRID_COUNT counts the grid points inside an ellipsoid.
    #
    #  Discussion:
    #
    #    The ellipsoid is specified as
    #
    #      ( ( X - C0 ) / R0 )^2
    #    + ( ( Y - C1 ) / R1 )^2
    #    + ( ( Z - C2 ) / R2 )^2 = 1
    #
    #    The user supplies a number N.  There will be N+1 grid points along
    #    the shortest axis.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Input, real R[3], the half axis lengths.
    #
    #    Input, real C[3], the center of the ellipsoid.
    #
    #    Output, integer NG, the number of grid points inside the ellipsoid.
    #
    if (r[0] == min(r)):
        h = 2.0 * r[0] / float(2 * n + 1)
        ni = n
        nj = int(1.0 + r[1] / r[0]) * n
        nk = int(1.0 + r[2] / r[0]) * n
    elif (r[1] == min(r)):
        h = 2.0 * r[1] / float(2 * n + 1)
        nj = n
        ni = int(1.0 + r[0] / r[1]) * n
        nk = int(1.0 + r[2] / r[1]) * n
    else:
        h = 2.0 * r[2] / float(2 * n + 1)
        nk = n
        ni = int(1.0 + r[0] / r[2]) * n
        nj = int(1.0 + r[1] / r[2]) * n

    ng = 0

    for k in range(0, nk + 1):
        z = c[2] + float(k) * h
        for j in range(0, nj + 1):
            y = c[1] + float(j) * h
            for i in range(0, ni + 1):
                x = c[0] + float(i) * h
                if (1.0 < ((x - c[0]) / r[0]) ** 2
                    + ((y - c[1]) / r[1]) ** 2
                        + ((z - c[2]) / r[2]) ** 2):
                    break
#
#  At least one point is generated, but more possible by symmetry.
#
                np = 1
                if (0 < i):
                    np = 2 * np
                if (0 < j):
                    np = 2 * np
                if (0 < k):
                    np = 2 * np

                ng = ng + np

    return ng


def ellipsoid_grid_count_test():

    # *****************************************************************************80
    #
    # ELLIPSOID_GRID_COUNT_TEST tests ELLIPSOID_GRID_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('ELLIPSOID_GRID_COUNT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  ELLIPSOID_GRID_COUNT can count the points in a grid,')
    print('  with N+1 points on the most minor half axis,')
    print('  based on any ellipsoid.')

    n = 4
    r = np.array([2.0, 1.0, 1.5])
    c = np.array([1.0, 2.0, 1.5])

    print('')
    print('  We use N = %d' % (n))
    print('  Radius R = (%g,%g,%g)' % (r[0], r[1], r[2]))
    print('  Center C = (%g,%g,%g)' % (c[0], c[1], c[2]))

    ng = ellipsoid_grid_count(n, r, c)

    print('')
    print('  Number of grid points will be %d' % (ng))
#
#  Terminate.
#
    print('')
    print('ELLIPSOID_GRID_COUNT_TEST:')
    print('  Normal end of execution.')
    return


def ellipsoid_grid_display(r, c, ng, xg, filename):

    # *****************************************************************************80
    #
    # ELLIPSOID_GRID_DISPLAY displays grid points inside a ellipsoid.
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
    #    Input, real R[3], the half axis lengths.
    #
    #    Input, real C[3], the center of the ellipsoid.
    #
    #    Input, integer NG, the number of grid points inside the ellipsoid.
    #
    #    Input, real XYZ[NG,3], the grid point coordinates.
    #
    #    Input, string FILENAME, the name of the plotfile to be created.
    #
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xg[:, 0], xg[:, 1], xg[:, 2], 'b')

    ax.set_xlabel('<---X--->')
    ax.set_ylabel('<---Y--->')
    ax.set_zlabel('<---Z--->')
    ax.set_title('Grid points in ellipsoid')
    ax.grid(True)
# ax.axis ( 'equal' )
    plt.savefig(filename)
    plt.show(block=False)
    plt.clf()

    return


def ellipsoid_grid_display_test():

    # *****************************************************************************80
    #
    # ELLIPSOID_GRID_DISPLAY displays grid points inside a ellipsoid.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('ELLIPSOID_GRID_DISPLAY_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  ELLIPSOID_GRID_DISPLAY can display a grid of points in a ellipsoid.')

    n = 2
    r = np.array([2.0, 1.0, 1.5])
    c = np.array([1.0, 2.0, 1.5])

    ng = ellipsoid_grid_count(n, r, c)
    xg = ellipsoid_grid_points(n, r, c, ng)

    filename = 'ellipsoid_grid_display.png'

    ellipsoid_grid_display(r, c, ng, xg, filename)
#
#  Terminate.
#
    print('')
    print('ELLIPSOID_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')
    return


def ellipsoid_grid_points(n, r, c, ng):

    # *****************************************************************************80
    #
    # ELLIPSOID_GRID_POINTS generates the grid points inside an ellipsoid.
    #
    #  Discussion:
    #
    #    The ellipsoid is specified as
    #
    #      ( ( X - C0 ) / R0 )^2
    #    + ( ( Y - C1 ) / R1 )^2
    #    + ( ( Z - C2 ) / R2 )^2 = 1
    #
    #    The user supplies a number N.  There will be N+1 grid points along
    #    the shortest axis.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Input, real R[3], the half axis lengths.
    #
    #    Input, real C[3], the center of the ellipsoid.
    #
    #    Input, integer NG, the number of grid points inside the ellipsoid.
    #
    #    Output, real XYZ[NG,3], the grid point coordinates.
    #
    import numpy as np

    if (r[0] == min(r)):
        h = 2.0 * r[0] / float(2 * n + 1)
        ni = n
        nj = int(1.0 + r[1] / r[0]) * n
        nk = int(1.0 + r[2] / r[0]) * n
    elif (r[1] == min(r)):
        h = 2.0 * r[1] / float(2 * n + 1)
        nj = n
        ni = int(1.0 + r[0] / r[1]) * n
        nk = int(1.0 + r[2] / r[1]) * n
    else:
        h = 2.0 * r[2] / float(2 * n + 1)
        nk = n
        ni = int(1.0 + r[0] / r[2]) * n
        nj = int(1.0 + r[1] / r[2]) * n

    xyz = np.zeros((ng, 3))

    p = np.zeros((8, 3))

    ng2 = 0

    for k in range(0, nk + 1):
        z = c[2] + float(k) * h
        for j in range(0, nj + 1):
            y = c[1] + float(j) * h
            for i in range(0, ni + 1):
                x = c[0] + float(i) * h
#
#  If we have left the ellipsoid, the I loop is completed.
#
                if (1.0 < ((x - c[0]) / r[0]) ** 2
                    + ((y - c[1]) / r[1]) ** 2
                        + ((z - c[2]) / r[2]) ** 2):
                    break
#
#  At least one point is generated, but more possible by symmetry.
#
                p[0, 0] = x
                p[0, 1] = y
                p[0, 2] = z
                np = 1

                if (0 < i):
                    for l in range(0, np):
                        p[np + l, 0] = 2.0 * c[0] - p[l, 0]
                        p[np + l, 1] = p[l, 1]
                        p[np + l, 2] = p[l, 2]
                    np = 2 * np

                if (0 < j):
                    for l in range(0, np):
                        p[np + l, 0] = p[l, 0]
                        p[np + l, 1] = 2.0 * c[1] - p[l, 1]
                        p[np + l, 2] = p[l, 2]
                    np = 2 * np

                if (0 < k):
                    for l in range(0, np):
                        p[np + l, 0] = p[l, 0]
                        p[np + l, 1] = p[l, 1]
                        p[np + l, 2] = 2.0 * c[2] - p[l, 2]
                    np = 2 * np

                for l in range(0, np):
                    xyz[ng2 + l, 0] = p[l, 0]
                    xyz[ng2 + l, 1] = p[l, 1]
                    xyz[ng2 + l, 2] = p[l, 2]
                ng2 = ng2 + np

    return xyz


def ellipsoid_grid_points_test():

    # *****************************************************************************80
    #
    # ELLIPSOID_GRID_POINTS_TEST tests ELLIPSOID_GRID_POINTS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('ELLIPSOID_GRID_POINTS_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  ELLIPSOID_GRID_POINTS can define a grid of points')
    print('  with N+1 points on the minor half axis,')
    print('  based on any ellipsoid.')

    n = 4
    r = np.array([2.0, 1.0, 1.5])
    c = np.array([1.0, 2.0, 1.5])

    print('')
    print('  We use N = %d' % (n))
    print('  Radius R = (%g,%g,%g)' % (r[0], r[1], r[2]))
    print('  Center C = (%g,%g,%g)' % (c[0], c[1], c[2]))
#
#  Count the points.
#
    ng = ellipsoid_grid_count(n, r, c)

    print('')
    print('  Number of grid points will be %d' % (ng))
#
#  Compute the points.
#
    xyz = ellipsoid_grid_points(n, r, c, ng)

    r83col_print_part(ng, xyz, 20, '  Part of the grid point array:')
#
#  Write the data to a file.
#
    filename = 'ellipsoid_grid_points.xyz'

    r8mat_write(filename, ng, 3, xyz)

    print('')
    print('  Data written to the file "%s".' % (filename))
#
#  Plot the data.
#
    filename = 'ellipsoid_grid_points.png'
    ellipsoid_grid_display(r, c, ng, xyz, filename)

    print('')
    print('  Plot stored in the file "%s".' % (filename))
#
#  Terminate.
#
    print('')
    print('ELLIPSOID_GRID_POINTS_TEST:')
    print('  Normal end of execution.')
    return


def ellipsoid_grid_test():

    # *****************************************************************************80
    #
    # ELLIPSOID_GRID_TEST tests the ELLIPSOID_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('ELLIPSOID_GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the ELLIPSOID_GRID library.')
#
#  Library.
#
    ellipsoid_grid_count_test()
    ellipsoid_grid_display_test()
    ellipsoid_grid_points_test()
#
#  Terminate.
#
    print('')
    print('ELLIPSOID_GRID_TEST:')
    print('  Normal end of execution.')
    return


def r83col_print_part(n, a, max_print, title):

    # *****************************************************************************80
    #
    # R83COL_PRINT_PART prints "part" of an R83COL.
    #
    #  Discussion:
    #
    #    An R83COL is a (3,N) array of R8's.
    #
    #    The user specifies MAX_PRINT, the maximum number of lines to print.
    #
    #    If N, the size of the vector, is no more than MAX_PRINT, then
    #    the entire vector is printed, one entry per line.
    #
    #    Otherwise, if possible, the first MAX_PRINT-2 entries are printed,
    #    followed by a line of periods suggesting an omission,
    #    and the last entry.
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
    #    Input, integer N, the number of entries of the vector.
    #
    #    Input, real A(N,3), the vector to be printed.
    #
    #    Input, integer MAX_PRINT, the maximum number of lines
    #    to print.
    #
    #    Input, string TITLE, a title.
    #
    if (0 < max_print):

        if (0 < n):

            if (0 < len(title)):
                print('')
                print(title)

            print('')

            if (n <= max_print):

                for i in range(0, n):
                    print('  %4d  %14g  %14g  %14g' %
                          (i, a[i, 0], a[i, 1], a[i, 2]))

            elif (3 <= max_print):

                for i in range(0, max_print - 2):
                    print('  %4d  %14g  %14g  %14g' %
                          (i, a[i, 0], a[i, 1], a[i, 2]))
                print('  ....  ..............  ..............  ..............')
                i = n - 1
                print('  %4d  %14g  %14g  %14g' %
                      (i, a[i, 0], a[i, 1], a[i, 2]))

            else:

                for i in range(0, max_print - 1):
                    print('  %4d  %14g  %14g  %14g' %
                          (i, a[i, 0], a[i, 1], a[i, 2]))
                i = max_print - 1
                print('  %4d  %14g  %14g  %14g  ...more entries...'
                      % (i, a[i, 0], a[i, 1], a[i, 2]))

    return


def r83col_print_part_test():

    # *****************************************************************************80
    #
    # R83COL_PRINT_PART_TEST tests R83COL_PRINT_PART.
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
    import numpy as np
    import platform

    print('')
    print('R83COL_PRINT_PART_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R83COL_PRINT_PART prints part of an R83COL.')

    n = 10

    v = np.array([
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33],
        [41, 42, 43],
        [51, 52, 53],
        [61, 62, 63],
        [71, 72, 73],
        [81, 82, 83],
        [91, 92, 93],
        [101, 102, 103]])

    max_print = 2
    r83col_print_part(n, v, max_print, '  Output with MAX_PRINT = 2')

    max_print = 5
    r83col_print_part(n, v, max_print, '  Output with MAX_PRINT = 5')

    max_print = 25
    r83col_print_part(n, v, max_print, '  Output with MAX_PRINT = 25')
#
#  Terminate.
#
    print('')
    print('R83COL_PRINT_PART_TEST:')
    print('  Normal end of execution.')
    return


def r8mat_write(filename, m, n, a):

    # *****************************************************************************80
    #
    # R8MAT_WRITE writes an R8MAT to a file.
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
    #    Input, string FILENAME, the name of the output file.
    #
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    output = open(filename, 'w')

    for i in range(0, m):
        for j in range(0, n):
            s = '  %g' % (a[i, j])
            output.write(s)
        output.write('\n')

    output.close()

    return


def r8mat_write_test():

    # *****************************************************************************80
    #
    # R8MAT_WRITE_TEST tests R8MAT_WRITE.
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
    import numpy as np
    import platform

    print('')
    print('R8MAT_WRITE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test R8MAT_WRITE, which writes an R8MAT to a file.')

    filename = 'r8mat_write_test.txt'
    m = 5
    n = 3
    a = np.array((
        (1.1, 1.2, 1.3),
        (2.1, 2.2, 2.3),
        (3.1, 3.2, 3.3),
        (4.1, 4.2, 4.3),
        (5.1, 5.2, 5.3)))
    r8mat_write(filename, m, n, a)

    print('')
    print('  Created file "%s".' % (filename))
#
#  Terminate.
#
    print('')
    print('R8MAT_WRITE_TEST:')
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
    ellipsoid_grid_test()
    timestamp()
