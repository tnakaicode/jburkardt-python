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

from i4lib.i4_choose import i4_choose
from subset.derange_enum import derange_enum


def perm_fixed_enum(n, m):

    # ******************************************************************************/
    #
    # PERM_FIXED_ENUM enumerates the permutations of N objects with M fixed.
    #
    #  Discussion:
    #
    #    A permutation of N objects with M fixed is a permutation in which
    #    exactly M of the objects retain their original positions.  If
    #    M = 0, the permutation is a "derangement".  If M = N, the
    #    permutation is the identity.
    #
    #  Formula:
    #
    #    F(N,M) = ( N! / M! ) * ( 1 - 1/1! + 1/2! - 1/3! ... 1/(N-M)! )
    #           = COMB(N,M) * D(N-M)
    #
    #    where D(N-M) is the number of derangements of N-M objects.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 June 2007
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of objects to be permuted.
    #    N should be at least 1.
    #
    #    Input, integer M, the number of objects that retain their
    #    position.  M should be between 0 and N.
    #
    #    Output, integer VALUE, the number of derangements of N objects
    #    in which M objects retain their positions.
    #

    if (n <= 0):

        value = 1

    elif (m < 0):

        value = 0

    elif (n < m):

        value = 0

    elif (m == n):

        value = 1

    elif (n == 1):

        if (m == 1):
            value = 1
        else:
            value = 0

    else:

        value = i4_choose(n, m) * derange_enum(n - m)

    return value


def perm_fixed_enum_test():

    # *****************************************************************************80
    #
    # PERM_FIXED_ENUM_TEST tests PERM_FIXED_ENUM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    print('')
    print('PERM_FIXED_ENUM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PERM_FIXED_ENUM enumerates the permutations')
    print('  of N objects that leave M unchanged.')
    print('')
    print('  For this test, N = %d' % (n))
    print('')
    print('  M    F(N,M)')
    print('')

    for m in range(0, n + 1):
        value = perm_fixed_enum(n, m)
        print('  %2d  %8d' % (m, value))
#
#  Terminate.
#
    print('')
    print('PERM_FIXED_ENUM_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    perm_fixed_enum_test()
    timestamp()
