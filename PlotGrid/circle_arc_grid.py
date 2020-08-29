#! /usr/bin/env python3
#


def circle_arc_grid_display(r, c, a, ng, cg, filename):

    # *****************************************************************************80
    #
    # CIRCLE_ARC_GRID_DISPLAY displays grid points along a circular arc.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real R, the radius of the disk.
    #
    #    Input, real C(2), the coordinates of the center of the disk.
    #
    #    Input, real A(2), the initial and final angles, in degrees.
    #
    #    Input, integer NG, the number of grid points inside the disk.
    #
    #    Input, real CG[NG,2], the grid points.
    #
    #    Input, string FILENAME, the name of the plotfile to be created.
    #
    import matplotlib.pyplot as plt
    import numpy as np
#
#  Make points on the circumference and plot them.
#
    cx = np.zeros(51)
    cy = np.zeros(51)
    angle = np.linspace(a[0] * np.pi / 180.0, a[1] * np.pi / 180.0, 51)

    for i in range(0, 51):
        cx[i] = c[0] + r * np.cos(angle[i])
        cy[i] = c[1] + r * np.sin(angle[i])

    plt.plot(cx, cy, linewidth=2.0, color='r')
#
#  Plot the gridpoints.
#
    plt.plot(cg[0:ng, 0], cg[0:ng, 1], 'bs')
#
#  Cleanup and annotate.
#
    plt.xlabel('<---X--->')
    plt.ylabel('<---Y--->')
    plt.title('Grid points along circular arc')
    plt.grid(True)
    plt.axis('equal')
# plt.show ( )
#
#  Save plot to file.
#
    plt.savefig(filename)

    plt.clf()

    print('')
    print('  Graphics data saved in file "%s"' % (filename))

    return


def circle_arc_grid_display_test():

    # *****************************************************************************80
    #
    # CIRCLE_ARC_GRID_DISPLAY displays grid points along a circular arc.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('CIRCLE_ARC_GRID_DISPLAY_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  CIRCLE_ARC_GRID_DISPLAY can display a grid of points along a circular arc.')

    r = 3.0
    c = np.array([4.0, 6.0])
    a = np.array([-30.0, 120.0])
    n = 20
#
#  Compute the data.
#
    xy = circle_arc_grid_points(r, c, a, n)
#
#  Plot the data.
#
    filename = 'circle_arc_grid_display.png'
    circle_arc_grid_display(r, c, a, n, xy, filename)
#
#  Terminate.
#
    print('')
    print('CIRCLE_ARC_GRID_DISPLAY_TEST:')
    print('  Normal end of execution.')
    return


def circle_arc_grid_points(r, c, a, n):

    # *****************************************************************************80
    #
    # % CIRCLE_ARC_GRID_POINTS computes grid points along a circular arc.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real R, the radius of the circle.
    #
    #    Input, real C(2), the coordinates of the center.
    #
    #    Input, real A(2), the angle of the first and last
    #    points, in DEGREES.
    #
    #    Input, integer N, the number of points.
    #
    #    Output, real XY[N,2], the grid points.
    #
    import numpy as np

    xy = np.zeros((n, 2))

    angle = np.linspace(a[0] * np.pi / 180.0, a[1] * np.pi / 180.0, n)

    for i in range(0, n):
        xy[i, 0] = c[0] + r * np.cos(angle[i])
        xy[i, 1] = c[1] + r * np.sin(angle[i])

    return xy


def circle_arc_grid_points_test():

    # *****************************************************************************80
    #
    # CIRCLE_ARC_GRID_POINTS_TEST demonstrates the use of CIRCLE_ARC_GRID.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('CIRCLE_ARC_GRID_POINTS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CIRCLE_ARC_GRID_POINTS returns points along a circular arc.')
    print('  In this example, we compute points on a 90 degree arc.')

    r = 2.0
    c = np.array([5.0, 5.0])
    a = np.array([0.0, 90.0])
    n = 20
#
#  Echo the input.
#
    print('')
    print('  Radius =           %g' % (r))
    print('  Center =           %g  %g\n' % (c[0], c[1]))
    print('  Angle 1 =          %g' % (a[0]))
    print('  Angle 2 =          %g' % (a[1]))
    print('  Number of points = %d' % (n))
#
#  Compute the data.
#
    xy = circle_arc_grid_points(r, c, a, n)
#
#  Print a little of the data.
#
    r82col_print_part(n, xy, 10, '  Some points on the arc:')
#
#  Write the data.
#
    filename = 'circle_arc_grid_points.xy'
    r8mat_write(filename, n, 2, xy)
    print(' ')
    print('  Data written to "%s"' % (filename))
#
#  Plot the data.
#
    filename = 'circle_arc_grid_points.png'
    circle_arc_grid_display(r, c, a, n, xy, filename)
    print('')
    print('  Plot saved in file "%s"' % (filename))
#
#  Terminate.
#
    print('')
    print('CIRCLE_ARC_GRID_POINTS_TEST:')
    print('  Normal end of execution.')
    return


def circle_arc_grid_test():

    # *****************************************************************************80
    #
    # CIRCLE_ARC_GRID_TEST tests the CIRCLE_ARCE_GRID library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('CIRCLE_ARC_GRID_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the CIRCLE_ARC_GRID library.')
#
#  Utilities:
#
    r82col_print_part_test()
    r8mat_write_test()
    timestamp_test()
#
#  Library.
#
    circle_arc_grid_display_test()
    circle_arc_grid_points_test()
#
#  Terminate.
#
    print('')
    print('CIRCLE_ARC_GRID_TEST:')
    print('  Normal end of execution.')
    return


def r82col_print_part(n, a, max_print, title):

    # *****************************************************************************80
    #
    # R82COL_PRINT_PART prints "part" of an R82COL.
    #
    #  Discussion:
    #
    #    An R82COL is an (N,2) array of R8's.
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
    #    19 December 2001
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries of the vector.
    #
    #    Input, real A(N,2), the vector to be printed.
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
                    print('  %4d  %14g  %14g' % (i, a[i, 0], a[i, 1]))

            elif (3 <= max_print):

                for i in range(0, max_print - 2):
                    print('  %4d  %14g  %14g' % (i, a[i, 0], a[i, 1]))
                print('  ....  ..............  ..............')
                i = n - 1
                print('  %4d  %14g  %14g' % (i, a[i, 0], a[i, 1]))

            else:

                for i in range(0, max_print - 1):
                    print('  %4d  %14g  %14g' % (i, a[i, 0], a[i, 1]))
                i = max_print - 1
                print('  %4d  %14g  %14g  ...more entries...' %
                      (i, a[i, 0], a[i, 1]))

    return


def r82col_print_part_test():

    # *****************************************************************************80
    #
    # R82COL_PRINT_PART_TEST tests R82COL_PRINT_PART.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('R82COL_PRINT_PART_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R82COL_PRINT_PART prints an R82COL.')

    n = 10

    v = np.array([
        [11, 12],
        [21, 22],
        [31, 32],
        [41, 42],
        [51, 52],
        [61, 62],
        [71, 72],
        [81, 82],
        [91, 92],
        [101, 102]])

    max_print = 2
    r82col_print_part(n, v, max_print, '  Output with MAX_PRINT = 2')

    max_print = 5
    r82col_print_part(n, v, max_print, '  Output with MAX_PRINT = 5')

    max_print = 25
    r82col_print_part(n, v, max_print, '  Output with MAX_PRINT = 25')
#
#  Terminate.
#
    print('')
    print('R82COL_PRINT_PART_TEST:')
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
    circle_arc_grid_test()
    timestamp()
