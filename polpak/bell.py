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
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8vec_transpose import r8vec_transpose_print
from r8lib.r8mat_transpose import r8mat_transpose_print, r8mat_transpose_print_some

from i4lib.i4_choose import i4_choose


def bell(n):

    # *****************************************************************************80
    #
    # BELL returns the Bell numbers from 0 to N.
    #
    #  Discussion:
    #
    #    The Bell number B(N) is the number of restricted growth functions
    #    on N.
    #
    #    Note that the Stirling numbers of the second kind, S^m_n, count the
    #    number of partitions of N objects into M classes, and so it is
    #    true that
    #
    #      B(N) = S^1_N + S^2_N + ... + S^N_N.
    #
    #  Definition:
    #
    #    The Bell number B(N) is defined as the number of partitions (of
    #    any size) of a set of N distinguishable objects.
    #
    #    A partition of a set is a division of the objects of the set into
    #    subsets.
    #
    #  Examples:
    #
    #    There are 15 partitions of a set of 4 objects:
    #
    #      (1234), (123)(4), (124)(3), (12)(34), (12)(3)(4),
    #      (134)(2), (13)(24), (13)(2)(4), (14)(23), (1)(234),
    #      (1)(23)(4), (14)(2)(3), (1)(24)(3), (1)(2)(34), (1)(2)(3)(4)
    #
    #    and so B(4) = 15.
    #
    #  First values:
    #
    #     N         B(N)
    #     0           1
    #     1           1
    #     2           2
    #     3           5
    #     4          15
    #     5          52
    #     6         203
    #     7         877
    #     8        4140
    #     9       21147
    #    10      115975
    #
    #  Recursion:
    #
    #    B(I) = sum ( 1 <= J <= I ) Binomial ( I-1, J-1 ) * B(I-J)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of Bell numbers desired.
    #
    #    Output, integer B(1:N+1), the Bell numbers from 0 to N.
    #

    b = np.zeros(n + 1)
    b[0] = 1

    for i in range(1, n + 1):
        b[i] = 0
        for j in range(1, i + 1):
            b[i] = b[i] + i4_choose(i - 1, j - 1) * b[i - j]

    return b


def bell_test():

    # *****************************************************************************80
    #
    # BELL_TEST tests BELL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BELL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  BELL computes Bell numbers.')
    print('')
    print('   N  exact C(I)  computed C(I)')
    print('')

    n_data = 0

    while (True):

        n_data, n, c = bell_values(n_data)

        if (n_data == 0):
            break

        c2 = bell(n)

        print('  %2d  %8d  %8d' % (n, c, c2[n]))
    print('')
    print('BELL_TEST')
    print('  Normal end of execution.')


def bell_poly_coef(n):

    # *****************************************************************************80
    #
    # BELL_POLY_COEF: Coefficients of a Bell polynomial.
    #
    #  First terms:
    #
    #    N    0    1    2    3    4    5    6    7    8
    #
    #    0    1
    #    1    0    1
    #    2    0    1    1
    #    3    0    1    3    1
    #    4    0    1    7    6    1
    #    5    0    1   15   25   10    1
    #    6    0    1   31   90   65   15    1
    #    7    0    1   63  301  350  140   21    1
    #    8    0    1  127  966 1701 1050  266   28    1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the polynomial.
    #
    #    Output, integer C[0:N], the coefficients.
    #

    c = np.zeros(n + 1)
    c[0] = 1

    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            c[j] = j * c[j] + c[j - 1]
        c[0] = 0

    return c


def bell_poly_coef_test():

    # *****************************************************************************80
    #
    # BELL_POLY_COEF_TEST tests BELL_POLY_COEF.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    n_max = 10

    print('')
    print('BELL_POLY_COEF_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  BELL_POLY_COEF returns the coefficients of a Bell polynomial.')
    print('')
    print('  Table of polyomial coefficients:')
    print('')

    for n in range(0, n_max + 1):

        c = bell_poly_coef(n)
        print('  %2d:' % (n)),
        for i in range(0, n + 1):
            print('%5d' % (c[i])),
        print('')
    print('')
    print('BELL_POLY_COEF_TEST')
    print('  Normal end of execution.')


def bell_values(n_data):

    # *****************************************************************************80
    #
    # BELL_VALUES returns some values of the Bell numbers.
    #
    #  Discussion:
    #
    #    The Bell number B(N) is the number of restricted growth functions on N.
    #
    #    Note that the Stirling numbers of the second kind, S^m_n, count the
    #    number of partitions of N objects into M classes, and so it is
    #    true that
    #
    #      B(N) = S^1_N + S^2_N + ... + S^N_N.
    #
    #    The Bell numbers were named for Eric Temple Bell.
    #
    #    In Mathematica, the function can be evaluated by
    #
    #      Sum[StirlingS2[n,m],{m,1,n}]
    #
    #    The Bell number B(N) is defined as the number of partitions (of
    #    any size) of a set of N distinguishable objects.
    #
    #    A partition of a set is a division of the objects of the set into
    #    subsets.
    #
    #  Example:
    #
    #    There are 15 partitions of a set of 4 objects:
    #
    #      (1234),
    #      (123) (4),
    #      (124) (3),
    #      (12) (34),
    #      (12) (3) (4),
    #      (134) (2),
    #      (13) (24),
    #      (13) (2) (4),
    #      (14) (23),
    #      (1) (234),
    #      (1) (23) (4),
    #      (14) (2) (3),
    #      (1) (24) (3),
    #      (1) (2) (34),
    #      (1) (2) (3) (4).
    #
    #    and so B(4) = 15.
    #
    #  First values:
    #
    #     N         B(N)
    #     0           1
    #     1           1
    #     2           2
    #     3           5
    #     4          15
    #     5          52
    #     6         203
    #     7         877
    #     8        4140
    #     9       21147
    #    10      115975
    #
    #  Recursion:
    #
    #    B(I) = sum ( 1 <= J <=I ) Binomial ( I-1, J-1 ) * B(I-J)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Milton Abramowitz and Irene Stegun,
    #    Handbook of Mathematical Functions,
    #    US Department of Commerce, 1964.
    #
    #    Stephen Wolfram,
    #    The Mathematica Book,
    #    Fourth Edition,
    #    Wolfram Media / Cambridge University Press, 1999.
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, integer N, the order of the Bell number.
    #
    #    Output, integer C, the value of the Bell number.
    #

    n_max = 11
    c_vec = np.array((1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975))
    n_vec = np.array((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        n = 0
        c = 0
    else:
        n = n_vec[n_data]
        c = c_vec[n_data]
        n_data = n_data + 1

    return n_data, n, c


def bell_values_test():

    # *****************************************************************************80
    #
    # BELL_VALUES_TEST demonstrates the use of BELL_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BELL_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  BELL_VALUES returns values of')
    print('  the Bell numbers.')
    print('')
    print('     N        BELL(N)')
    print('')

    n_data = 0

    while (True):

        n_data, n, c = bell_values(n_data)

        if (n_data == 0):
            break

        print('%6d  %10d' % (n, c))
    print('')
    print('BELL_VALUES_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    bell_test()
    timestamp()
