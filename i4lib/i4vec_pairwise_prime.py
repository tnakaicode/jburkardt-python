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

from i4lib.i4_gcd import i4_gcd


def i4vec_pairwise_prime(n, a):

    # *****************************************************************************80
    #
    # I4VEC_PAIRWISE_PRIME checks whether a vector of integers is pairwise prime.
    #
    #  Discussion:
    #
    #    Two positive integers I and J are pairwise prime if they have no common
    #    factor greater than 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of values to check.
    #
    #    Input, integer A(N), the vector of integers.
    #
    #    Output, logical VALUE, is TRUE if the vector of integers
    #    is pairwise prime.
    #

    value = True

    for i in range(0, n):
        for j in range(i + 1, n):
            if (i4_gcd(a[i], a[j]) != 1):
                value = False
                break

    return value


def i4vec_pairwise_prime_test():

    # *****************************************************************************80
    #
    # I4VEC_PAIRWISE_PRIME_TEST tests I4VEC_PAIRWISE_PRIME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    n = 4
    test_num = 6

    x_test = np.array([
        [1, 3, 2, 4],
        [2, 2, 2, 2],
        [5, 7, 12, 29],
        [1, 13, 1, 11],
        [1, 4, 9, 16],
        [6, 35, 13, 77]])

    x = np.zeros(n)

    print('')
    print('I4VEC_PAIRWISE_PRIME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_PAIRWISE_PRIME determines if a vector of')
    print('  integers is pairwise prime.')
    print('')
    print('                          Pairwise')
    print('  Row Vector              Prime?')
    print(''
          )
    for test in range(0, test_num):

        for j in range(0, n):
            x[j] = x_test[test, j]

        value = i4vec_pairwise_prime(n, x)

        for j in range(0, n):
            print('  %3d' % (x[j])),
        print('  %s' % (value))
#
#  Terminate.
#
    print('')
    print('I4VEC_PAIRWISE_PRIME_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    i4vec_pairwise_prime_test()
    timestamp()
