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

from i4lib.i4vec_transpose_print import i4vec_transpose_print


def catalan_row_next(ido, n, row_old):

    # *****************************************************************************80
    #
    # CATALAN_ROW_NEXT computes row N of Catalan's triangle.
    #
    #  Example:
    #
    #    I\J 0   1   2   3   4   5   6
    #
    #    0   1
    #    1   1   1
    #    2   1   2   2
    #    3   1   3   5   5
    #    4   1   4   9  14  14
    #    5   1   5  14  28  42  42
    #    6   1   6  20  48  90 132 132
    #
    #  Recursion:
    #
    #    C(0,0) = 1
    #    C(I,0) = 1
    #    C(I,J) = 0 for I < J
    #    C(I,J) = C(I,J-1) + C(I-1,J)
    #    C(I,I) is the I-th Catalan number.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer IDO, indicates whether this is a call for
    #    the 'next' row of the triangle.
    #    IDO = 0, this is a startup call.  Row N is desired, but
    #    presumably this is a first call, or row N-1 was not computed
    #    on the previous call.
    #    IDO = 1, this is not the first call, and row N-1 was computed
    #    on the previous call.  In this case, much work can be saved
    #    by using the information from the previous values of IROW
    #    to build the next values.
    #
    #    Input, integer N, the index of the row of the triangle desired.
    #
    #    Input, integer ROW_OLD(1:N), the row of coefficients.
    #    If IDO = 0, then ROW_OLD is not required to be set on input.
    #    If IDO = 1, then ROW_OLD must be set on input to the value of
    #    row N-1.
    #
    #    Output, integer ROW_NEW(1:N+1), the next row of coefficients.
    #
    import numpy as np

    row_new = np.zeros(n + 1)

    if (ido == 0):

        row_new[0] = 1

        for i in range(1, n + 1):

            im1 = i - 1
            row_new[0] = 1

            for j in range(0, im1):
                row_new[j + 1] = row_new[j + 1] + row_new[j]

            row_new[i] = row_new[i - 1]

    else:

        for i in range(0, n):
            row_new[i] = row_old[i]
        row_new[n] = 0

        row_new[0] = 1

        for j in range(0, n - 1):
            row_new[j + 1] = row_new[j + 1] + row_new[j]

        if (1 <= n):
            row_new[n] = row_new[n - 1]

    return row_new


def catalan_row_next_test():

    # *****************************************************************************80
    #
    # CATALAN_ROW_NEXT_TEST tests CATALAN_ROW_NEXT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('CATALAN_ROW_NEXT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CATALAN_ROW_NEXT computes a row of Catalan\'s triangle.')
    print('')
    print('  First, compute row 7 from scratch.')

    ido = 0
    i = 7
    c = np.zeros(0)
    c = catalan_row_next(ido, i, c)

    i4vec_transpose_print(i + 1, c, '  Row 7:')

    print('')
    print('  Now compute rows one at a time:')
    print('')

    n = 10
    ido = 0
    c = np.zeros(0)

    for i in range(0, n + 1):
        c = catalan_row_next(ido, i, c)
        i4vec_transpose_print(i + 1, c, '')
        ido = 1
#
#  Terminate.
#
    print('')
    print('CATALAN_ROW_NEXT_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    catalan_row_next_test()
    timestamp()
