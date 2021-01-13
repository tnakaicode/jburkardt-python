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

from i4lib.i4_sqrt import i4_sqrt
from i4lib.i4_sqrt_cf import i4_sqrt_cf


def pell_basic(d):

    # *****************************************************************************80
    #
    # PELL_BASIC returns the fundamental solution for Pell's basic equation.
    #
    #  Discussion:
    #
    #    Pell's equation has the form:
    #
    #      X^2 - D * Y^2 = 1
    #
    #    where D is a given non-square integer, and X and Y may be assumed
    #    to be positive integers.
    #
    #  Example:
    #
    #     D   X0   Y0
    #
    #     2    3    2
    #     3    2    1
    #     5    9    4
    #     6    5    2
    #     7    8    3
    #     8    3    1
    #    10   19    6
    #    11   10    3
    #    12    7    2
    #    13  649  180
    #    14   15    4
    #    15    4    1
    #    17   33    8
    #    18   17    4
    #    19  170   39
    #    20    9    2
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2015
    #
    #  Author:
    #
    #   John Burkardt
    #
    #  Reference:
    #
    #    Mark Herkommer,
    #    Number Theory, A Programmer's Guide,
    #    McGraw Hill, 1999, pages 294-307
    #
    #  Parameters:
    #
    #    Input, integer D, the coefficient in Pell's equation.  D should be
    #    positive, and not a perfect square.
    #
    #    Output, integer X0, Y0, the fundamental or 0'th solution.
    #    If X0 = Y0 = 0, then the calculation was canceled because of an error.
    #    Both X0 and Y0 will be nonnegative.
    #

    max_term = 100
#
#  If these values are returned, an error has occurred.
#
    x0 = 0
    y0 = 0
#
#  Check D.
#
    if (d <= 0):
        print('')
        print('PELL_BASIC - Fatal error!')
        print('  Pell coefficient D <= 0.')
        exit('PELL_BASIC - Fatal error!')

    q, r = i4_sqrt(d)

    if (r == 0):
        print('')
        print('PELL_BASIC - Fatal error!')
        print('  Pell coefficient is a perfect square.')
        exit('PELL_BASIC - Fatal error!')
#
#  Find the continued fraction representation of sqrt ( D ).
#
    b, n_term = i4_sqrt_cf(d, max_term)
#
#  If necessary, go for two periods.
#
    if ((n_term % 2) == 1):

        n2_term = 2 * n_term
        b2 = np.zeros(n2_term)
        for i in range(0, n_term):
            b2[i] = b[i]
        for i in range(n_term, 2 * n_term):
            b2[i] = b[i - n_term]

        n_term = n2_term
        b = np.zeros(n_term)
        for i in range(0, n_term):
            b[i] = b2[i]
#
#  Evaluate the continued fraction using the forward recursion algorithm.
#
    pm2 = 0
    pm1 = 1
    qm2 = 1
    qm1 = 0

    for i in range(0, n_term):
        p = b[i] * pm1 + pm2
        q = b[i] * qm1 + qm2
        pm2 = pm1
        pm1 = p
        qm2 = qm1
        qm1 = q
#
#  Get the fundamental solution.
#
    x0 = p
    y0 = q

    return x0, y0


def pell_basic_test():

    # *****************************************************************************80
    #
    # PELL_BASIC_TEST tests PELL_BASIC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PELL_BASIC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PELL_BASIC solves the basic Pell equation.')
    print('')
    print('        D        X        Y        R')
    print('')

    for d in range(2, 21):

        q, r = i4_sqrt(d)

        if (r != 0):

            x0, y0 = pell_basic(d)

            r = x0 ** 2 - d * y0 ** 2

            print('  %7d  %7d  %7d  %7d' % (d, x0, y0, r))
#
#  Terminate.
#
    print('')
    print('PELL_BASIC_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    pell_basic_test()
    timestamp()
