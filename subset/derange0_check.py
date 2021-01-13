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

from i4lib.i4vec_indicator0 import i4vec_indicator0
from i4lib.i4vec_transpose_print import i4vec_transpose_print


def derange0_check(n, a):

    # *****************************************************************************80
    #
    # % DERANGE0_CHECK checks if a vector is a derangement of ( 0, ..., N-1 ).
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
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of objects permuted.
    #
    #    Input, integer A(N), a permutation.
    #
    #    Output, logical CHECK, is TRUE if A is a derangement, and
    #    FALSE otherwise.
    #

    #
    #  Values must be between 0 and N - 1
    #
    for i in range(0, n):
        if (a[i] < 0 or n - 1 < a[i]):
            check = False
            return check
#
#  Every value must be represented.
#
    for j in range(0, n):
        check = False
        for i in range(0, n):
            if (a[i] == j):
                check = True
                break
        if (not check):
            return check
#
#  Values must be deranged.
#
    for i in range(0, n):
        if (a[i] == i):
            check = False
            return check

    check = True

    return check


def derange0_check_test():

    # *****************************************************************************80
    #
    # DERANGE0_CHECK_TEST tests DERANGE0_CHECK.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 5

    a_test = np.array([
        [1, 2, 3, 4, 0],
        [1, 4, 2, 0, 3],
        [1, 2, 3, 0, 3],
        [-1, 2, 3, 4, 0],
        [0, 3, 8, 1, 2]])

    a = np.zeros(n)

    print('')
    print('DERANGE0_CHECK_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DERANGE0_CHECK_checks whether a vector of N objects')
    print('  represents a derangement of (1,...,N).')

    for i in range(0, 5):

        for j in range(0, n):
            a[j] = a_test[i, j]

        i4vec_transpose_print(n, a, '  Potential derangement:')
        check = derange0_check(n, a)
        print('  CHECK = %s' % (check))
#
#  Terminate.
#
    print('')
    print('DERANGE0_CHECK_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    derange0_check_test()
    timestamp()
