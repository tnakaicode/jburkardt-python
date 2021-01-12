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

from i4lib.i4vec_pairwise_prime import i4vec_pairwise_prime


def chinese_check(n, m):

    # *****************************************************************************80
    #
    # CHINESE_CHECK checks the Chinese remainder moduluses.
    #
    #  Discussion:
    #
    #    For a Chinese remainder representation, the moduluses M(I) must
    #    be positive and pairwise prime.  Also, in case this is not obvious,
    #    no more than one of the moduluses may be 1.
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
    #    Output, integer IERROR, an error flag.
    #    0, no error was detected.
    #    nonzero, an error was detected.
    #

    #
    #  Do not allow nonpositive entries.
    #
    ierror = 0

    for i in range(0, n):
        if (m[i] <= 0):
            ierror = 1
            return ierror
#
#  Allow one entry to be 1, but not two entries.
#
    for i in range(0, n):
        if (m[i] == 1):
            for j in range(i + 1, n):
                if (m[j] == 1):
                    ierror = 2
                    return ierror
#
#  Now check pairwise primeness.
#
    if (not i4vec_pairwise_prime(n, m)):
        ierror = 3
        return ierror

    return ierror


def chinese_check_test():

    # *****************************************************************************80
    #
    # CHINESE_CHECK_TEST tests CHINESE_CHECK.
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
    m1 = np.array([1, 3, 8, 25])
    m2 = np.array([1, 3, -8, 25])
    m3 = np.array([1, 3, 1, 25])
    m4 = np.array([1, 3, 8, 24])

    print('')
    print('CHINESE_CHECK_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CHINESE_CHECK checks a set of moduluses for use with')
    print('  the Chinese Remainder representation.')

    i4vec_print(n, m1, '  Modulus set #1:')
    ierror = chinese_check(n, m1)
    print('  IERROR = %d' % (ierror))

    i4vec_print(n, m2, '  Modulus set #2:')
    ierror = chinese_check(n, m2)
    print('  IERROR = %d' % (ierror))

    i4vec_print(n, m3, '  Modulus set #3:')
    ierror = chinese_check(n, m3)
    print('  IERROR = %d' % (ierror))

    i4vec_print(n, m4, '  Modulus set #4:')
    ierror = chinese_check(n, m4)
    print('  IERROR = %d' % (ierror))
#
#  Terminate.
#
    print('')
    print('CHINESE_CHECK_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    chinese_check_test()
    timestamp()
