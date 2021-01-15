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


def euler_row(n):

    # *****************************************************************************80
    #
    # EULER_ROW returns the N-th row of Euler's triangle.
    #
    #  Discussion:
    #
    #    E(N,K) counts the number of permutations of the N digits that have
    #    exactly K "ascents", that is, K places where the Ith digit is
    #    less than the (I+1)th digit.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the row of Euler's triangle desired.
    #
    #    Output, integer A[0:N], the N-th row of Euler's
    #    triangle, A(K+1) contains the value of E(N,K).  Note
    #    that A(1) should be 1 and A(N+1) should be 0.
    #

    a = np.zeros(n + 1)

    a[0] = 1

    if (0 < n):
        a[1] = 0
        for irow in range(2, n + 1):
            a[irow] = 0
            for k in range(irow - 1, 0, -1):
                a[k] = (k + 1) * a[k] + (irow - k) * a[k - 1]
            a[0] = 1

    return a


def euler_row_test():

    # *****************************************************************************80
    #
    # EULER_ROW_TEST tests EULER_ROW.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    30 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    nmax = 9

    print('')
    print('EULER_ROW_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  EULER_ROW gets rows of Euler\'s triangle.')
    print('')

    for n in range(0, nmax + 1):
        ieuler = euler_row(n)
        for i in range(0, n + 1):
            print('  %d' % (ieuler[i])),
        print('')

    print('')
    print('EULER_ROW_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    euler_row_test()
    timestamp()
