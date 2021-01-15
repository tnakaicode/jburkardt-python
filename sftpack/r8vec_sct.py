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


def r8vec_sct(n, x):

    # *****************************************************************************80
    #
    # R8VEC_SCT computes a forward or backward "slow" cosine transform of an R8VEC.
    #
    #  Discussion:
    #
    #    This routine is provided for illustration and testing.  It is inefficient
    #    relative to optimized routines that use fast Fourier techniques.
    #
    #      Y(1) = Sum ( 1 <= J <= N ) X(J)
    #
    #      For 2 <= I <= N-1:
    #
    #        Y(I) = 2 * Sum ( 1 <= J <= N ) X(J)
    #          * cos ( PI * ( I - 1 ) * ( J - 1 ) / ( N - 1 ) )
    #
    #      Y(N) = Sum ( X(1:N:2) ) - Sum ( X(2:N:2) )
    #
    #    Applying the routine twice in succession should yield the original data,
    #    multiplied by 2 * ( N + 1 ).  This is a good check for correctness
    #    and accuracy.
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

        y[i] = x[0] / 2.0

        for j in range(1, n - 1):
            angle = np.pi * float((i * j) % (2 * (n - 1))) / float(n - 1)
            y[i] = y[i] + x[j] * np.cos(angle)

        j = n - 1

        angle = np.pi * float((i * j) % (2 * (n - 1))) / float(n - 1)

        y[i] = y[i] + x[n - 1] * np.cos(angle) / 2.0

    for i in range(0, n):
        y[i] = 2.0 * y[i] * np.sqrt(float(n) / float(n - 1))

    return y


def r8vec_sct_test():

    # *****************************************************************************80
    #
    # R8VEC_SCT_TEST tests R8VEC_SCT.
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
    alo = 0.0
    ahi = 5.0

    print('')
    print('R8VEC_SCT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8VEC_SCT does a forward or backward slow cosine transform.')
    print('')
    print('  The number of data items is N = %d' % (n))
#
#  Set the data values.
#
    seed = 123456789

    c, seed = r8vec_uniform_ab(n, alo, ahi, seed)

    r8vec_print_part(n, c, 1, 10, '  The original data:')
#
#  Compute the coefficients.
#
    d = r8vec_sct(n, c)

    r8vec_print_part(n, d, 1, 10, '  The cosine coefficients:')
#
#  Now compute inverse transform of coefficients.  Should get back the
#  original data.

    e = r8vec_sct(n, d)

    for i in range(0, n):
        e[i] = e[i] / float(2 * n)

    r8vec_print_part(n, e, 1, 10, '  The retrieved data:')
#
#  Terminate.
#
    print('')
    print('R8VEC_SCT_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    r8vec_sct_test()
    timestamp()
