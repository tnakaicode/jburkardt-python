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

from i4lib.i4_choose import i4_choose
from i4lib.i4_fall import i4_fall
from i4lib.i4_uniform_ab import i4_uniform_ab
from i4lib.i4vec_concatenate import i4vec_concatenate
from i4lib.i4vec_permute import i4vec_permute
from i4lib.i4vec_print import i4vec_print
from i4lib.i4vec_sort_heap_index_a import i4vec_sort_heap_index_a
from i4lib.i4vec_sum import i4vec_sum
from i4lib.i4vec_uniform_ab import i4vec_uniform_ab
from r8lib.r8vec_concatenate import r8vec_concatenate
from r8lib.r8vec_permute import r8vec_permute
from r8lib.r8vec_print import r8vec_print


def mono_total_next_grlex(m, n, x):

    # *****************************************************************************80
    #
    # MONO_TOTAL_NEXT_GRLEX: grlex next monomial, total degree equal to N.
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
    #    1 |  0     0     3        3
    #    2 |  0     1     2        3
    #    3 |  0     2     1        3
    #    4 |  0     3     0        3
    #    5 |  1     0     2        3
    #    6 |  1     1     1        3
    #    7 |  1     2     0        3
    #    8 |  2     0     1        3
    #    9 |  2     1     0        3
    #   10 |  3     0     0        3
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
    #    Input, integer N, the total degree.
    #    0 <= N1 <= N2.
    #
    #    Input, integer X[M], the current monomial.
    #    The first element is X = [ 0, 0, ..., 0, N ].
    #    The last is [ N, 0, ..., 0, 0 ].
    #
    #    Output, integer X[M], the next monomial.
    #

    if (n < 0):
        print('')
        print('MONO_TOTAL_NEXT_GRLEX - Fatal error!')
        print('  N < 0.')
        exit('MONO_TOTAL_NEXT_GRLEX - Fatal error!')

    if (i4vec_sum(m, x) != n):
        print('')
        print('MONO_TOTAL_NEXT_GRLEX - Fatal error!')
        print('  Input X sums is not N.')
        exit('MONO_TOTAL_NEXT_GRLEX - Fatal error!')

    if (n == 0):
        return x

    if (x[0] == n):
        x[0] = 0
        x[m - 1] = n
    else:
        x = mono_next_grlex(m, x)

    return x


def mono_total_next_grlex_test():

    # *****************************************************************************80
    #
    # MONO_TOTAL_NEXT_GRLEX_TEST tests MONO_TOTAL_NEXT_GRLEX.
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
    print('MONO_TOTAL_NEXT_GRLEX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_TOTAL_NEXT_GRLEX can list the monomials')
    print('  in M variables, of total degree N,')
    print('  in grlex order, one at a time.')
    print('')
    print('  We start the process with (0,0,...,0,N).')
    print('  The process ends with (N,0,...,0,0)')

    n = 3

    print('')
    print('  Let M =   %d' % (m))
    print('      N =   %d' % (n))
    print('')

    x = np.array([0, 0, n], dtype=np.int32)

    i = 1

    while (True):

        print('  %2d    ' % (i)),
        for k in range(0, m):
            print('%2d' % (x[k])),
        print('')

        if (x[0] == n):
            break

        x = mono_total_next_grlex(m, n, x)
        i = i + 1

    print('')
    print('MONO_TOTAL_NEXT_GRLEX_TEST')
    print('  Normal end of execution.')


def mono_next_grlex(m, x):

    # *****************************************************************************80
    #
    # MONO_NEXT_GRLEX returns the next monomial in grlex order.
    #
    #  Discussion:
    #
    #    Example:
    #
    #    M = 3
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
    #    Input, int M, the spatial dimension.
    #
    #    Input, int X[M], the current monomial.
    #    The first element is X = [ 0, 0, ..., 0, 0 ].
    #
    #    Output, int X[M], the next monomial.
    #

    #
    #  Ensure that 1 <= D.
    #
    if (m < 1):
        print('')
        print('MONO_NEXT_GRLEX - Fatal error!')
        print('  M < 1')
        exit('MONO_NEXT_GRLEX - Fatal error!')

    #
    #  Ensure that 0 <= X(I).
    #
    for i in range(0, m):
        if (x[i] < 0):
            print('')
            print('MONO_NEXT_GRLEX - Fatal error!')
            print('  X[I] < 0')
            exit('MONO_NEXT_GRLEX - Fatal error!')

    #
    #  Find I, the index of the rightmost nonzero entry of X.
    #
    i = 0
    for j in range(m, 0, -1):
        if (0 < x[j - 1]):
            i = j
            break

    #
    #  set T = X(I)
    #  set X(I) to zero,
    #  increase X(I-1) by 1,
    #  increment X(M) by T-1.
    #
    if (i == 0):
        x[m - 1] = 1
        return x
    elif (i == 1):
        t = x[0] + 1
        im1 = m
    elif (1 < i):
        t = x[i - 1]
        im1 = i - 1

    x[i - 1] = 0
    x[im1 - 1] = x[im1 - 1] + 1
    x[m - 1] = x[m - 1] + t - 1

    return x


def mono_next_grlex_test():

    # *****************************************************************************80
    #
    # MONO_NEXT_GRLEX_TEST tests MONO_NEXT_GRLEX.
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

    m = 4

    print('')
    print('MONO_NEXT_GRLEX_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  MONO_NEXT_GRLEX computes the next monomial')
    print('  in M variables in grlex order.')
    print('')
    print('  Let M =  %d' % (m))

    a = 0
    b = 3
    seed = 123456789

    for i in range(0, 10):

        x, seed = i4vec_uniform_ab(m, a, b, seed)
        print('')
        print('  '),
        for k in range(0, m):
            print('%2d' % (x[k])),
        print('')

        for j in range(0, 5):
            x = mono_next_grlex(m, x)
            print('  '),
            for k in range(0, m):
                print('%2d' % (x[k])),
            print('')
    print('')
    print('MONO_NEXT_GRLEX_TEST')
    print('  Normal end of execution.')


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

        print('  %2d    ' % (i)),
        for k in range(0, m):
            print('%2d' % (x[k])),
        print('')

        if (x[0] == n):
            break

        x = mono_upto_next_grlex(m, n, x)
        i = i + 1
    print('')
    print('MONO_UPTO_NEXT_GRLEX_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    mono_next_grlex_test()
    mono_upto_next_grlex_test()
    timestamp()
