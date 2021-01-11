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

from i4lib.i4vec_sum import i4vec_sum
from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from monomial.mono_next_grlex import mono_next_grlex


def mono_upto_next_grlex(m, n, x):

    # *****************************************************************************80
    #
    # MONO_UPTO_NEXT_GRLEX: grlex next monomial, total degree up to N.
    #
    #  Discussion:
    #
    #    We consider all monomials in an M-dimensional space, with total
    #    degree N.
    #
    #    For example:
    #
    #    M = 3
    #    N = 3
    #
    #    #  X(1)  X(2)  X(3)  Degree
    #      +------------------------
    #    1 |  0     0     0        0
    #      |
    #    2 |  0     0     1        1
    #    3 |  0     1     0        1
    #    4 |  1     0     0        1
    #      |
    #    5 |  0     0     2        2
    #    6 |  0     1     1        2
    #    7 |  0     2     0        2
    #    8 |  1     0     1        2
    #    9 |  1     1     0        2
    #   10 |  2     0     0        2
    #      |
    #   11 |  0     0     3        3
    #   12 |  0     1     2        3
    #   13 |  0     2     1        3
    #   14 |  0     3     0        3
    #   15 |  1     0     2        3
    #   16 |  1     1     1        3
    #   17 |  1     2     0        3
    #   18 |  2     0     1        3
    #   19 |  2     1     0        3
    #   20 |  3     0     0        3
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the maximum degree.
    #    0 <= N.
    #
    #    Input, integer X[M], the current monomial.
    #    The first element is X = [ 0, 0, ..., 0, 0 ].
    #    The last is [ N, 0, ..., 0, 0 ].
    #
    #    Output, integer X[M], the next monomial.
    #

    if (n < 0):
        print('')
        print('MONO_UPTO_NEXT_GRLEX - Fatal error!')
        print('  N < 0.')
        exit('MONO_UPTO_NEXT_GRLEX - Fatal error!')

    if (i4vec_sum(m, x) < 0):
        print('')
        print('MONO_UPTO_NEXT_GRLEX - Fatal error!')
        print('  Input X sum is less than 0.')
        exit('MONO_UPTO_NEXT_GRLEX - Fatal error!')

    if (n < i4vec_sum(m, x)):
        print('')
        print('MONO_UPTO_NEXT_GRLEX - Fatal error!')
        print('  Input X sum is more than N.')
        exit('MONO_UPTO_NEXT_GRLEX - Fatal error!')

    if (n == 0):
        return x

    if (x[0] == n):
        x[0] = 0
    else:
        x = mono_next_grlex(m, x)

    return x


def mono_upto_next_grlex_test():

    # *****************************************************************************80
    #
    # MONO_UPTO_NEXT_GRLEX_TEST tests MONO_UPTO_NEXT_GRLEX.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3

    print('')
    print('MONO_UPTO_NEXT_GRLEX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_UPTO_NEXT_GRLEX can list the monomials')
    print('  in M variables, of total degree up to N,')
    print('  in grlex order, one at a time.')
    print('')
    print('  We start the process with (0,0,...,0,0).')
    print('  The process ends with (N,0,...,0,0)')

    n = 4

    print('')
    print('  Let M =   %d' % (m))
    print('      N =   %d' % (n))
    print('')

    x = np.array([0, 0, 0], dtype=np.int32)

    i = 1

    while (True):

        print('  %2d    ' % (i), end='')
        for k in range(0, m):
            print('%2d' % (x[k]), end='')
        print('')

        if (x[0] == n):
            break

        x = mono_upto_next_grlex(m, n, x)
        i = i + 1
#
#  Terminate.
#
    print('')
    print('MONO_UPTO_NEXT_GRLEX_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    mono_upto_next_grlex_test()
    timestamp()
