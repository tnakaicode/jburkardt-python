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

from r8lib.r8mat_print import r8mat_print
from r8lib.r8mat_indicator import r8mat_indicator


def r8mat_transpose(m, n, a):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE transposes an R8MAT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of A.
    #
    #    Input, real A(M,N), the matrix to be transposed.
    #
    #    Output, real AT(N,M), the transposed matrix.
    #

    at = np.zeros((n, m))
    for j in range(0, n):
        for i in range(0, m):
            at[j, i] = a[i, j]
    return at


def r8mat_transpose_test():

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_TEST tests R8MAT_TRANSPOSE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 5
    n = 4

    print('')
    print('R8MAT_TRANSPOSE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_TRANSPOSE transposes an R8MAT.')

    a = r8mat_indicator(m, n)
    r8mat_print(m, n, a, '  Matrix A:')

    at = r8mat_transpose(m, n, a)
    r8mat_print(n, m, at, '  Transposed matrix At:')

    print('')
    print('R8MAT_TRANSPOSE_TEST')
    print('  Normal end of execution.')


def r8mat_transpose_print(m, n, a, title):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT prints an R8MAT, transposed.
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
    #    Input, integer M, the number of rows in A.
    #
    #    Input, integer N, the number of columns in A.
    #
    #    Input, real A(M,N), the matrix.
    #
    #    Input, string TITLE, a title.
    #

    r8mat_transpose_print_some(m, n, a, 0, 0, m - 1, n - 1, title)

    return


def r8mat_transpose_print_test():

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_TEST tests R8MAT_TRANSPOSE_PRINT.
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

    print('')
    print('R8MAT_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_TRANSPOSE_PRINT prints an R8MAT.')

    m = 4
    n = 3
    v = np.array([
        [11.0, 12.0, 13.0],
        [21.0, 22.0, 23.0],
        [31.0, 32.0, 33.0],
        [41.0, 42.0, 43.0]], dtype=np.float64)
    r8mat_transpose_print(m, n, v, '  Here is an R8MAT, transposed:')

    print('')
    print('R8MAT_TRANSPOSE_PRINT_TEST:')
    print('  Normal end of execution.')


def r8mat_transpose_print_some(m, n, a, ilo, jlo, ihi, jhi, title):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_SOME prints a portion of an R8MAT, transposed.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of the matrix.
    #
    #    Input, real A(M,N), an M by N matrix to be printed.
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

    for i2lo in range(max(ilo, 0), min(ihi, m - 1), incx):

        i2hi = i2lo + incx - 1
        i2hi = min(i2hi, m - 1)
        i2hi = min(i2hi, ihi)

        print('')
        print('  Row: ', end='')

        for i in range(i2lo, i2hi + 1):
            print('%7d       ' % (i), end='')

        print('')
        print('  Col')

        j2lo = max(jlo, 0)
        j2hi = min(jhi, n - 1)

        for j in range(j2lo, j2hi + 1):

            print('%7d :' % (j), end='')

            for i in range(i2lo, i2hi + 1):
                print('%12g  ' % (a[i, j]), end='')

            print('')


def r8mat_transpose_print_some_test():

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_PRINT_SOME_TEST tests R8MAT_TRANSPOSE_PRINT_SOME.
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

    print('')
    print('R8MAT_TRANSPOSE_PRINT_SOME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_TRANSPOSE_PRINT_SOME prints some of an R8MAT, transposed.')

    m = 4
    n = 6
    v = np.array([
        [11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        [21.0, 22.0, 23.0, 24.0, 25.0, 26.0],
        [31.0, 32.0, 33.0, 34.0, 35.0, 36.0],
        [41.0, 42.0, 43.0, 44.0, 45.0, 46.0]], dtype=np.float64)
    r8mat_transpose_print_some(
        m, n, v, 0, 3, 2, 5, '  R8MAT, rows 0:2, cols 3:5:')

    print('')
    print('R8MAT_TRANSPOSE_PRINT_SOME_TEST:')
    print('  Normal end of execution.')


def r8mat_transpose_write(filename, m, n, a):

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_WRITE writes the transpose of an R8MAT to a file.
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
    for j in range(0, n):
        for i in range(0, m):
            s = '  %g' % (a[i, j])
            output.write(s)
        output.write('\n')
    output.close()


def r8mat_transpose_write_test():

    # *****************************************************************************80
    #
    # R8MAT_TRANSPOSE_WRITE_TEST tests R8MAT_TRANSPOSE_WRITE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8MAT_TRANSPOSE_WRITE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test R8MAT_TRANSPOSE_WRITE, which writes the transpose of an R8MAT to a file.')

    filename = 'r8mat_transpose_write_test.txt'
    m = 5
    n = 3
    a = np.array((
        (1.1, 1.2, 1.3),
        (2.1, 2.2, 2.3),
        (3.1, 3.2, 3.3),
        (4.1, 4.2, 4.3),
        (5.1, 5.2, 5.3)))
    r8mat_transpose_write(filename, m, n, a)

    print('')
    print('  Created file "%s".' % (filename))
    print('')
    print('R8MAT_TRANSPOSE_WRITE_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    r8mat_transpose_test()
    r8mat_transpose_print_test()
    r8mat_transpose_print_some_test()
    r8mat_transpose_write_test()
    timestamp()
