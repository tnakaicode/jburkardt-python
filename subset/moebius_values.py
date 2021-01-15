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


def moebius_values(n_data):

    # *****************************************************************************80
    #
    # MOEBIUS_VALUES returns some values of the Moebius function.
    #
    #  Discussion:
    #
    #    MU(N) is defined as follows:
    #
    #      MU(N) = 1 if N = 1;
    #              0 if N is divisible by the square of a prime;
    #              (-1)^K, if N is the product of K distinct primes.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      MoebiusMu[n]
    #
    #  First values:
    #
    #     N  MU(N)
    #
    #     1    1
    #     2   -1
    #     3   -1
    #     4    0
    #     5   -1
    #     6    1
    #     7   -1
    #     8    0
    #     9    0
    #    10    1
    #    11   -1
    #    12    0
    #    13   -1
    #    14    1
    #    15    1
    #    16    0
    #    17   -1
    #    18    0
    #    19   -1
    #    20    0
    #
    #    As special cases, MU(N) is -1 if N is a prime, and MU(N) is 0
    #    if N is a square, cube, etc.
    #
    #  Formula:
    #
    #    The Moebius function is related to Euler's totient function:
    #
    #      PHI(N) = Sum ( D divides N ) MU(D) * ( N / D ).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 February 2015
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
    #    Output, integer N, the argument of the Moebius function.
    #
    #    Output, integer C, the value of the Moebius function.
    #

    n_max = 20

    c_vec = np.array((
        1, -1, -1, 0, -1, 1, -1, 0, 0, 1,
        -1, 0, -1, 1, 1, 0, -1, 0, -1, 0))

    n_vec = np.array((
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

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


def moebius_values_test():

    # *****************************************************************************80
    #
    # MOEBIUS_VALUES_TEST demonstrates the use of MOEBIUS_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('MOEBIUS_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  MOEBIUS_VALUES stores values of the MOEBIUS function.')
    print('')
    print('             N    MOEBIUS(N)')
    print('')

    n_data = 0

    while (True):

        n_data, n, c = moebius_values(n_data)

        if (n_data == 0):
            break

        print('  %12d  %12d' % (n, c))

    print('')
    print('MOEBIUS_VALUES_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    moebius_values_test()
    timestamp()
