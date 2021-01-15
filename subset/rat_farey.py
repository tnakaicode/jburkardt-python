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


def rat_farey(n, max_frac):

    # *****************************************************************************80
    #
    # RAT_FAREY computes the N-th row of the Farey fraction table.
    #
    #  Example:
    #
    #    N = 5
    #
    #    NUM_FRAC = 11
    #    A =  0  1  1  1  2  1  3  2  3  4  1
    #    B =  1  5  4  3  5  2  5  3  4  5  1
    #
    #  Discussion:
    #
    #    In this form of the Farey fraction table, fractions in row N lie between
    #    0 and 1, are in lowest terms, and have a denominator that is no greater
    #    than N.  Row N is computed directly, and does not require the computation
    #    of previous rows.
    #
    #    The data satisfy the relationship:
    #
    #      A(K+1) * B(K) - A(K) * B(K+1) = 1
    #
    #    The number of items in the N-th row is roughly N^2 / PI^2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Donald Knuth,
    #    The Art of Computer Programming,
    #    Volume 1, Fundamental Algorithms,
    #    Addison Wesley, 1968, page 157.
    #
    #  Parameters:
    #
    #    Input, integer N, the desired row number.  N must be positive.
    #
    #    Input, integer MAX_FRAC, the maximum number of fractions to compute.
    #
    #    Output, integer A(NUM_FRAC), B(NUM_FRAC), contains the
    #    numerators and denominators of the N-th row of the Farey fraction table.
    #
    #    Output, integer NUM_FRAC, the number of fractions computed.
    #

    a = np.zeros(max_frac)
    b = np.zeros(max_frac)

    if (max_frac <= 0):
        num_frac = 0
        return a, b, num_frac

    if (n <= 0):
        num_frac = 0
        return a, b, num_frac

    k = 0
    a[k] = 0
    b[k] = 1

    if (max_frac <= k + 1):
        num_frac = k + 1
        return a, b, num_frac

    k = 1
    a[k] = 1
    b[k] = n

    while (k + 1 < max_frac):

        if (a[k] == 1 and b[k] == 1):
            break

        k = k + 1
        c = ((b[k - 2] + n) // b[k - 1])
        a[k] = c * a[k - 1] - a[k - 2]
        b[k] = c * b[k - 1] - b[k - 2]

    num_frac = k + 1

    return a, b, num_frac


def rat_farey_test():

    # *****************************************************************************80
    #
    # RAT_FAREY_TEST tests RAT_FAREY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    max_frac = 20

    print('')
    print('RAT_FAREY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAT_FAREY computes a row of the Farey fraction table.')

    for n in range(1, 8):

        a, b, num_frac = rat_farey(n, max_frac)

        print('')
        print('  Row %d' % (n))
        print('  Number of fractions: %d' % (num_frac))

        for i in range(0, num_frac):
            print('  %d/%d' % (a[i], b[i])),
            if (((i + 1) % 10 == 0) or i == num_frac - 1):
                print('')

    print('')
    print('RAT_FAREY_TEST')
    print('  Normal end of execution.')


def rat_farey2(n, a, b):

    # *****************************************************************************80
    #
    # RAT_FAREY2 computes the next row of the Farey fraction table.
    #
    #  Example:
    #
    #    Input:
    #
    #      N = 3
    #      A =  0  1  1  2  1
    #      B =  1  3  2  3  1
    #
    #    Output:
    #
    #      A =  0  1  1  2  1  3  2  3  1
    #      B =  1  4  3  5  2  5  3  4  1
    #
    #  Discussion:
    #
    #    In this form of the Farey fraction table, fractions in row N lie between
    #    0 and 1, and are in lowest terms.  For every adjacent pair of input
    #    fractions, A1/B1 and A2/B2, the mediant (A1+A2)/(B1+B2) is computed
    #    and inserted between them.
    #
    #    The number of items in the N-th row is 1+2^(N-1).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the input row number.  N must be nonnegative.
    #    If N is zero, then the input values A and B are ignored, and the entries of
    #    row 1 are computed directly.
    #
    #    Input, integer A(1+2^(N-1)), B(1+2^(N-1)),the entries of row N.
    #
    #    Output, integer A2(1+2^N), B2(1+2^N), the entries of row N+1.
    #

    a2 = np.zeros(1 + 2 ** n)
    b2 = np.zeros(1 + 2 ** n)

    if (n == 0):

        a2[0] = 0
        a2[1] = 1
        b2[0] = 1
        b2[1] = 1

    else:
        #
        #  Shift the current data.
        #
        for i in range(2 ** (n - 1), -1, -1):
            a2[2 * i] = a[i]
            b2[2 * i] = b[i]

        #
        #  Compute the mediants.
        #
        for i in range(1, 2 ** n, 2):
            a2[i] = a2[i - 1] + a2[i + 1]
            b2[i] = b2[i - 1] + b2[i + 1]

    return a2, b2


def rat_farey2_test():

    # *****************************************************************************80
    #
    # RAT_FAREY2_TEST tests RAT_FAREY2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    max_n = 4

    print('')
    print('RAT_FAREY2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAT_FAREY2 computes a row of the Farey fraction table.')

    n = 0
    a = np.zeros(n)
    b = np.zeros(n)

    for n in range(0, 5):

        a, b = rat_farey2(n, a, b)
        num_frac = 2 ** n + 1

        print('')
        print('  Row %d' % (n))
        print('  Number of fractions: %d' % (num_frac))

        for i in range(0, num_frac):
            print('  %d/%d' % (a[i], b[i])),
            if (((i + 1) % 10 == 0) or i == num_frac - 1):
                print('')

    print('')
    print('RAT_FAREY2_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    rat_farey_test()
    rat_farey2_test()
    timestamp()
