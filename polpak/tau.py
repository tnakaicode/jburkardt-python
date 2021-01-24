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

from i4lib.i4_factor import i4_factor


def tau(n):

    # *****************************************************************************80
    #
    # TAU returns the value of TAU(N), the number of distinct divisors of N.
    #
    #  Discussion:
    #
    #    TAU(N) is the number of divisors of N, including 1 and N.
    #
    #  First values:
    #
    #     N   TAU(N)
    #
    #     1    1
    #     2    2
    #     3    2
    #     4    3
    #     5    2
    #     6    4
    #     7    2
    #     8    4
    #     9    3
    #    10    4
    #    11    2
    #    12    6
    #    13    2
    #    14    4
    #    15    4
    #    16    5
    #    17    2
    #    18    6
    #    19    2
    #    20    6
    #
    #  Formula:
    #
    #    If the prime factorization of N is
    #
    #      N = P1^E1 * P2^E2 * ... * PM^EM,
    #
    #    then
    #
    #      TAU(N) = ( E1 + 1 ) * ( E2 + 1 ) * ... * ( EM + 1 ).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the value to be analyzed.  N must be 1 or
    #    greater.
    #
    #    Output, integer TAUN, the value of TAU(N).  But if N is 0 or
    #    less, TAUN is returned as 0, a nonsense value.  If there is
    #    not enough room for factoring, TAUN is returned as -1.
    #

    if (n <= 0):
        value = 0
        return value

    if (n == 1):
        value = 1
        return value

    #
    #  Factor N.
    #
    nfactor, factor, power, nleft = i4_factor(n)

    if (nleft != 1):
        print('')
        print('TAU - Fatal error!')
        print('  Not enough factorization space.')

    value = 1
    for i in range(0, nfactor):
        value = value * (power[i] + 1)

    return value


def tau_test():

    # *****************************************************************************80
    #
    # TAU_TEST tests TAU.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('TAU_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  TAU computes the TAU function.')
    print('')
    print('         N      Exact         TAU(N)')

    n_data = 0

    while (True):

        n_data, n, c1 = tau_values(n_data)

        if (n_data == 0):
            break

        c2 = tau(n)

        print('  %8d  %12d  %12d' % (n, c1, c2))
    print('')
    print('TAU_TEST')
    print('  Normal end of execution.')


def tau_values(n_data):

    # *****************************************************************************80
    #
    # TAU_VALUES returns some values of the Tau function.
    #
    #  Discussion:
    #
    #    TAU(N) is the number of divisors of N, including 1 and N.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      DivisorSigma[1,n]
    #
    #  First values:
    #
    #     N   TAU(N)
    #
    #     1    1
    #     2    2
    #     3    2
    #     4    3
    #     5    2
    #     6    4
    #     7    2
    #     8    4
    #     9    3
    #    10    4
    #    11    2
    #    12    6
    #    13    2
    #    14    4
    #    15    4
    #    16    5
    #    17    2
    #    18    6
    #    19    2
    #    20    6
    #
    #  Formula:
    #
    #    If the prime factorization of N is
    #
    #      N = P1^E1 * P2^E2 * ... * PM^EM,
    #
    #    then
    #
    #      TAU(N) = ( E1 + 1 ) * ( E2 + 1 ) * ... * ( EM + 1 ).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 February 2015
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
    #    Output, integer N, the argument of the Tau function.
    #
    #    Output, integer C, the value of the Tau function.
    #

    n_max = 20

    c_vec = np.array((
        1, 2, 2, 3, 2, 4, 2, 4, 3, 4,
        2, 12, 12, 4, 18, 24, 2, 8, 14, 28))

    n_vec = np.array((
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        23, 72, 126, 226, 300, 480, 521, 610, 832, 960))

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


def tau_values_test():

    # *****************************************************************************80
    #
    # TAU_VALUES_TEST demonstrates the use of TAU_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('TAU_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  TAU_VALUES stores values of the TAU function.')
    print('')
    print('             N    TAU(N)')
    print('')

    n_data = 0

    while (True):

        n_data, n, c = tau_values(n_data)

        if (n_data == 0):
            break

        print('  %12d  %12d' % (n, c))
    print('')
    print('TAU_VALUES_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    tau_test()
    tau_values_test()
    timestamp()
