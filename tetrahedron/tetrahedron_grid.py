#! /usr/bin/env python3
#


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


def tetrahedron_grid_count(n):

    # *****************************************************************************80
    #
    # TETRAHEDRON_GRID_COUNT counts the grid points inside a tetrahedron.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Output, integer NG, the number of grid points.
    #
    ng = ((n + 1) * (n + 2) * (n + 3)) // 6

    return ng


def tetrahedron_grid_count_test():

    # *****************************************************************************80
    #
    # TETRAHEDRON_GRID_COUNT_TEST tests TETRAHEDRON_GRID_COUNT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TETRAHEDRON_GRID_COUNT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TETRAHEDRON_GRID_COUNT can count the points in a grid')
    print('  with N+1 points on a side, based on any tetrahedron.')

    print('')
    print('     N        NG')
    print('')

    for n in [1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 100]:
        ng = tetrahedron_grid_count(n)
        print('  %4d  %8d' % (n, ng))
#
#  Terminate.
#
    print('')
    print('TETRAHEDRON_GRID_COUNT_TEST:')
    print('  Normal end of execution.')
    return


def tetrahedron_grid_display(xv, ng, xg, filename):

    # *****************************************************************************80
    #
    # TETRAHEDRON_GRID_DISPLAY displays grid points inside a tetrahedron.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real XV[4,3], the vertices.
    #
    #    Input, integer NG, the number of grid points.
    #
    #    Input, real XG[NG,3], the grid points.
    #
    #    Input, string FILENAME, the name of the plotfile to be created.
    #
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
#
#  Draw the grid points.
#
    ax.scatter(xg[:, 0], xg[:, 1], xg[:, 2], 'b')
#
#  Outline the region by its edges.
#
    ax.plot([xv[0, 0], xv[1, 0]], [xv[0, 1], xv[1, 1]],
            [xv[0, 2], xv[1, 2]], 'r')
    ax.plot([xv[0, 0], xv[2, 0]], [xv[0, 1], xv[2, 1]],
            [xv[0, 2], xv[2, 2]], 'r')
    ax.plot([xv[0, 0], xv[3, 0]], [xv[0, 1], xv[3, 1]],
            [xv[0, 2], xv[3, 2]], 'r')
    ax.plot([xv[1, 0], xv[2, 0]], [xv[1, 1], xv[2, 1]],
            [xv[1, 2], xv[2, 2]], 'r')
    ax.plot([xv[1, 0], xv[3, 0]], [xv[1, 1], xv[3, 1]],
            [xv[1, 2], xv[3, 2]], 'r')
    ax.plot([xv[2, 0], xv[3, 0]], [xv[2, 1], xv[3, 1]],
            [xv[2, 2], xv[3, 2]], 'r')

    ax.set_xlabel('<---X--->')
    ax.set_ylabel('<---Y--->')
    ax.set_zlabel('<---Z--->')
    ax.set_title('Grid points in tetrahedron')
    ax.grid(True)
# ax.axis ( 'equal' )

    plt.savefig(filename)
    plt.show(block=False)
    plt.clf()

    return


def tetrahedron_grid_display_test():

    # *****************************************************************************80
    #
    # TETRAHEDRON_GRID_DISPLAY displays grid points inside a tetrahedron.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('TETRAHEDRON_GRID_DISPLAY_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TETRAHEDRON_GRID_DISPLAY can display a grid of points in a tetrahedron.')

    xv = np.array([
        [0.0, 0.0, 0.0],
        [2.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
        [0.0, 0.0, 2.0]])

    ng = 10
    xg = np.array([
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [2.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 2.0, 0.0],
        [1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 1.0],
        [0.0, 1.0, 1.0],
        [0.0, 0.0, 2.0]])

    filename = 'tetrahedron_grid_display.png'

    tetrahedron_grid_display(xv, ng, xg, filename)
#
#  Terminate.
#
    print('')
    print('TETRAHEDRON_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')
    return


def tetrahedron_grid_points(n, xv, ng):

    # *****************************************************************************80
    #
    # TETRAHEDRON_GRID_POINTs computes points on a tetrahedral grid.
    #
    #  Discussion:
    #
    #    The grid is defined by specifying the coordinates of an enclosing
    #    tetrahedron T, and the number of subintervals each edge of the
    #    tetrahedron should be divided into.
    #
    #    Choosing N = 10, for instance, breaks each side into 10 subintervals,
    #    and produces a grid of ((10+1)*(10+2)*(10+3))/6 = 286 points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of subintervals.
    #
    #    Input, real XV[4,3], the vertices of the tetrahedron.
    #
    #    Input, integer NG, the number of grid points.
    #
    #    Output, real XG[NG,3], the tetrahedron grid points.
    #
    import numpy as np

    xg = np.zeros([ng, 3])

    p = 0

    for i in range(0, n + 1):
        for j in range(0, n + 1 - i):
            for k in range(0, n + 1 - i - j):
                l = n - i - j - k
                xg[p, 0] = (float(i) * xv[0, 0] + float(j) * xv[1, 0]
                            + float(k) * xv[2, 0] + float(l) * xv[3, 0]) / float(n)
                xg[p, 1] = (float(i) * xv[0, 1] + float(j) * xv[1, 1]
                            + float(k) * xv[2, 1] + float(l) * xv[3, 1]) / float(n)
                xg[p, 2] = (float(i) * xv[0, 2] + float(j) * xv[1, 2]
                            + float(k) * xv[2, 2] + float(l) * xv[3, 2]) / float(n)
                p = p + 1

    return xg


def tetrahedron_grid_points_test():

    # *****************************************************************************80
    #
    # TETRAHEDRON_GRID_POINTS_TEST tests TETRAHEDRON_GRID_POINTS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 November 2011
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('TETRAHEDRON_GRID_POINTS_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TETRAHEDRON_GRID_POINTS can define a tetrahedral grid')
    print('  with N+1 points on a side, based on any tetrahedron.')

    n = 5
    print('  N = %d' % (n))

    ng = tetrahedron_grid_count(n)
#
#  Define the tetrahedron vertices.
#
    xv = np.array([
        [0.0, 0.0, 0.0],
        [2.0, 1.0, 0.0],
        [1.0, 4.0, 0.0],
        [3.0, 3.0, 3.0]])

    r83col_print_part(4, xv, 20, '  Tetrahedron vertices:')

    xg = tetrahedron_grid_points(n, xv, ng)

    r83col_print_part(ng, xg, 20, '  Tetrahedron grid points:')
#
#  Write the data to a file.
#
    filename = 'tetrahedron_grid_points.xyz'

    r8mat_write(filename, ng, 3, xg)

    print('')
    print('  Data written to the file "%s".' % (filename))
#
#  Plot the data.
#
    filename = 'tetrahedron_grid_points.png'
    tetrahedron_grid_display(xv, ng, xg, filename)

    print('')
    print('  Plot written to the file "%s".' % (filename))
#
#  Terminate.
#
    print('')
    print('TETRAHEDRON_GRID_POINTS_TEST:')
    print('  Normal end of execution.')
    return


def tetrahedron_grid_test():

    # *****************************************************************************80
    #
    # TETRAHEDRON_GRID_TEST tests the TETRAHEDRONE_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('TETRAHEDRON_GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the TETRAHEDRON_GRID library.')
#
#  Library.
#
    tetrahedron_grid_count_test()
    tetrahedron_grid_display_test()
    tetrahedron_grid_points_test()
#
#  Terminate.
#
    print('')
    print('TETRAHEDRON_GRID_TEST:')
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


if (__name__ == '__main__'):
    timestamp()
    tetrahedron_grid_test()
    timestamp()
