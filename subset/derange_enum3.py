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

from i4lib.i4_factorial import i4_factorial


def derange_enum3(n):

    # *****************************************************************************80
    #
    # DERANGE_ENUM3 returns the number of derangements of N objects.
    #
    #  Discussion:
    #
    #    A derangement of N objects is a permutation which leaves no object
    #    unchanged.
    #
    #    A derangement of N objects is a permutation with no fixed
    #    points.  If we symbolize the permutation operation by "P",
    #    then for a derangment, P(I) is never equal to I.
    #
    #    The number of derangements of N objects is sometimes called
    #    the subfactorial function, or the derangement number D(N).
    #
    #  Recursion:
    #
    #      D(0) = 1
    #      D(1) = 0
    #      D(2) = 1
    #      D(N) = (N-1) * ( D(N-1) + D(N-2) )
    #
    #    or
    #
    #      D(0) = 1
    #      D(1) = 0
    #      D(N) = N * D(N-1) + (-1)^N
    #
    #  Formula:
    #
    #    D(N) = N! * ( 1 - 1/1! + 1/2! - 1/3! ... 1/N! )
    #
    #    Based on the inclusion/exclusion law.
    #
    #    D(N) is the number of ways of placing N non-attacking rooks on
    #    an N by N chessboard with one diagonal deleted.
    #
    #    Limit ( N -> Infinity ) D(N)/N! = 1 / e.
    #
    #    The number of permutations with exactly K items in the right
    #    place is COMB(N,K) * D(N-K).
    #
    #  First values:
    #
    #     N         D(N)
    #     0           1
    #     1           0
    #     2           1
    #     3           2
    #     4           9
    #     5          44
    #     6         265
    #     7        1854
    #     8       14833
    #     9      133496
    #    10     1334961
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of objects to be permuted.
    #
    #    Output, integer VALUE, the number of derangements of N objects.
    #

    if (n < 0):
        value = -1
    elif (n == 0):
        value = 1
    elif (n == 1):
        value = 0
    else:
        e = 2.718281828459045
        value = int(round(i4_factorial(n) / e))

    return value


def derange_enum3_test():

    # *****************************************************************************80
    #
    # DERANGE_ENUM3_TEST tests DERANGE_ENUM3.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('DERANGE_ENUM3_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DERANGE_ENUM3 counts derangements;')

    n = 10

    print('')
    print('  N    # of derangements')
    print('')

    for i in range(0, n + 1):
        print('  %8d  %8d' % (i, derange_enum3(i)))
#
#  Terminate.
#
    print('')
    print('DERANGE_ENUM3_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    derange_enum3_test()
    timestamp()
