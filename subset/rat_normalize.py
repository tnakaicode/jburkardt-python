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
from i4lib.i4_huge import i4_huge
from subset.rat_to_s import rat_to_s


def rat_normalize(a, b):

    # *****************************************************************************80
    #
    # RAT_NORMALIZE normalizes a rational number.
    #
    #  Discussion:
    #
    #    If A = B = 0, return.
    #
    #    If A = 0 (and B nonzero) set B => 1 and return.
    #
    #    If A nonzero, and B = 0, then A => 1 and return.
    #
    #    If A = B, then set A => 1, B => 1 and return.
    #
    #    If B < 0, then A => -A, B => -B.
    #
    #    If 1 < C = GCD(|A|,|B|), A => A/C, B => B/C.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer A, B, the rational number.
    #
    #    Output, integer A, B, the normalized rational number.
    #

    #
    #  Cases where one or both is 0.
    #

    if (a == 0 and b == 0):
        return a, b
    elif (a == 0 and b != 0):
        b = 1
        return a, b
    elif (a != 0 and b == 0):
        a = 1
        return a, b

    if (a == b):
        a = 1
        b = 1
        return a, b

    if (b < 0):
        a = -a
        b = -b

    c = i4_gcd(abs(a), abs(b))

    if (1 < c):
        a = a // c
        b = b // c

    return a, b


def rat_normalize_test():

    # *****************************************************************************80
    #
    # RAT_NORMALIZE_TEST tests RAT_NORMALIZE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('RAT_NORMALIZE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAT_NORMALIZE normalizes a rational.')

    rat_num = 7
    rat_top = np.array([3, 1, 20, 8, -10, 9, -11])
    rat_bot = np.array([4, 1000, 1, 4, 7, -15, -11])

    print('')
    print('           A           B             A             B')
    print('                                 normalized     normalized')
    print('')

    for i in range(0, rat_num):
        a1 = rat_top[i]
        b1 = rat_bot[i]
        a2, b2 = rat_normalize(a1, b1)
        print('  %10d  %10d    %10d  %10d' % (a1, b1, a2, b2))

    return
#
#  Terminate.
#
    print('')
    print('RAT_NORMALIZE_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    rat_normalize_test()
    timestamp()
