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

from r8lib.r8vec_print_part import r8vec_print_part
from r8lib.r8vec_uniform_ab import r8vec_uniform_ab


def r8vec_sqctb(n, x):

    # *****************************************************************************80
    #
    # % R8VEC_SQCTB computes a "slow" quarter cosine transform backward of an R8VEC.
    #
    #  Discussion:
    #
    #    This routine is provided for illustration and testing.  It is inefficient
    #    relative to optimized routines that use fast Fourier techniques.
    #
    #    For 0 <= I <= N-1,
    #
    #      Y(I) = X(0) + 2 Sum ( 1 <= J <= N-1 ) X(J) * cos ( PI * J * (I+1/2) / N )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    William Briggs, Van Emden Henson,
    #    The Discrete Fourier Transform,
    #    SIAM, 1995,
    #    LC: QA403.5 B75
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data values.
    #
    #    Input, real X(N), the data sequence.
    #
    #    Output, real Y(N), the transformed data.
    #

    y = np.zeros(n)
    for i in range(0, n):
        y[i] = x[0]

    for i in range(0, n):
        for j in range(1, n):
            theta = 0.5 * np.pi * float(j * (2 * i + 1)) / float(n)
            y[i] = y[i] + 2.0 * x[j] * np.cos(theta)

    return y


def r8vec_sqctf(n, x):

    # *****************************************************************************80
    #
    # % R8VEC_SQCTF computes a "slow" quarter cosine transform forward of an R8VEC.
    #
    #  Discussion:
    #
    #    This routine is provided for illustration and testing.  It is inefficient
    #    relative to optimized routines that use fast Fourier techniques.
    #
    #    For 0 <= I <= N-1,
    #
    #      Y(I) = (1/N) Sum ( 0 <= J <= N-1 ) X(J) * cos ( PI * I * (J+1/2) / N )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    William Briggs, Van Emden Henson,
    #    The Discrete Fourier Transform,
    #    SIAM, 1995,
    #    QA403.5 B75
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data values.
    #
    #    Input, real X(N), the data sequence.
    #
    #    Output, real Y(N), the transformed data.
    #

    y = np.zeros(n)

    for i in range(0, n):
        for j in range(0, n):
            theta = 0.5 * np.pi * float(i * (2 * j + 1)) / float(n)
            y[i] = y[i] + x[j] * np.cos(theta)

    for i in range(0, n):
        y[i] = y[i] / float(n)

    return y


def r8vec_sqct_test():

    # *****************************************************************************80
    #
    # % R8VEC_SQCT_TEST tests R8VEC_SQCTB and R8VEC_SQCTF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 256

    ahi = 5.0
    alo = 0.0

    print('')
    print('R8VEC_SQCT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_SQCTF does a forward slow quarter wave cosine transform')
    print('  R8VEC_SQCTB does a backward slow quarter wave cosine transform.')
    print('')
    print('  The number of data items is N = %d' % (n))
#
#  Set the data values.
#
    seed = 123456789

    x, seed = r8vec_uniform_ab(n, alo, ahi, seed)

    r8vec_print_part(n, x, 1, 10, '  The original data:')
#
#  Compute the coefficients.
#
    y = r8vec_sqctf(n, x)

    r8vec_print_part(n, y, 1, 10, '  The cosine coefficients:')
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

    x = r8vec_sqctb(n, y)

    r8vec_print_part(n, x, 1, 10, '  The retrieved data:')
#
#  Terminate.
#
    print('')
    print('R8VEC_SQCT_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    r8vec_sqct_test()
    timestamp()
