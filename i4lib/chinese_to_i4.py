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

from i4lib.i4vec_product import i4vec_product
from i4lib.i4_to_chinese import i4_to_chinese
from subset.chinese_check import chinese_check
from subset.congruence import congruence


def chinese_to_i4(n, m, r):

    # *****************************************************************************80
    #
    # CHINESE_TO_I4 converts a set of Chinese remainders to an equivalent integer.
    #
    #  Discussion:
    #
    #    Given a set of N pairwise prime, positive moduluses M(I), and
    #    a corresponding set of remainders R(I), this routine finds an
    #    integer J such that, for all I,
    #
    #      J = R(I) mod M(I)
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
    #    Input, integer N, the number of moduluses.
    #
    #    Input, integer M(N), the moduluses.  These should be positive
    #    and pairwise prime.
    #
    #    Input, integer R(N), the Chinese remainder representation of the integer.
    #
    #    Output, integer J, the corresponding integer.
    #

    ierror = chinese_check(n, m)

    if (ierror != 0):
        print('')
        print('CHINESE_TO_I4 - Fatal error!')
        print('  The moduluses are not legal.')
        exit('CHINESE_TO_I4 - Fatal error!')
#
#  Set BIG_M.
#
    big_m = i4vec_product(n, m)
#
#  Solve BIG_M / M(I) * B(I) = 1, mod M(I)
#
    b = np.zeros(n)

    for i in range(0, n):
        a = big_m // m[i]
        c = 1
        b[i], ierror = congruence(a, m[i], c)
#
#  Set J = sum ( 1 <= I <= N ) ( R(I) * B(I) * BIG_M / M(I) ) mod M
#
    j = 0
    for i in range(0, n):
        j = ((j + r[i] * b[i] * (big_m // m[i])) % big_m)

    return j


def chinese_to_i4_test():

    # *****************************************************************************80
    #
    # CHINESE_TO_I4_TEST tests CHINESE_TO_I4.
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

    n = 4
    m = np.array([3, 4, 5, 7])

    print('')
    print('CHINESE_TO_I4_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CHINESE_TO_I4 computes an integer with the given')
    print('  Chinese Remainder representation.')

    i4vec_print(n, m, '  The moduli:')

    j = 37

    print('')
    print('  The number being analyzed is %d' % (j))

    r = i4_to_chinese(j, n, m)

    i4vec_print(n, r, '  The remainders:')

    j2 = chinese_to_i4(n, m, r)

    print('')
    print('  The reconstructed number is %d' % (j2))

    r = i4_to_chinese(j2, n, m)

    i4vec_print(n, r, '  The remainders of the reconstructed number:')
#
#  Terminate.
#
    print('')
    print('CHINESE_TO_I4_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    chinese_to_i4_test()
    timestamp()
