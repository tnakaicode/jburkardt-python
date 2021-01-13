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
from subset.pell_basic import pell_basic


def pell_next(d, x0, y0, xn, yn):

    # *****************************************************************************80
    #
    # % PELL_NEXT returns the next solution of Pell's equation.
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
    #    To compute X0, Y0, call PELL_BASIC.
    #    To compute X1, Y1, call this routine, with XN and YN set to X0 and Y0.
    #    To compute further solutions, call again with X0, Y0 and the previous
    #    solution.
    #
    #  Example:
    #
    #    ------INPUT--------  --OUTPUT--
    #
    #    D  X0  Y0   XN   YN  XNP1  YNP1
    #
    #    2   3   2    3    2    17    12
    #    2   3   2   17   12    99    70
    #    2   3   2   99   70   577   408
    #    2   3   2  577  408  3363  2378
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 June 2015
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
    #    Input, integer D, the coefficient in Pell's equation.
    #
    #    Input, integer X0, Y0, the fundamental or 0'th solution.
    #
    #    Input, integer XN, YN, the N-th solution.
    #
    #    Output, integer XNP1, YNP1, the N+1-th solution.
    #
    xnp1 = x0 * xn + d * y0 * yn
    ynp1 = x0 * yn + y0 * xn

    return xnp1, ynp1


def pell_next_test():

    # *****************************************************************************80
    #
    # PELL_NEXT_TEST tests PELL_NEXT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('PELL_NEXT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  PELL_NEXT computes the "next" solution of the Pell equation.')
    print('')
    print('       D       X        Y         R')
    print('')

    for d in range(2, 21):

        q, r = i4_sqrt(d)

        if (r != 0):

            x0, y0 = pell_basic(d)

            r = x0 ** 2 - d * y0 ** 2

            print('  %7d  %7d  %7d  %7d' % (d, x0, y0, r))

            x1, y1 = pell_next(d, x0, y0, x0, y0)

            r = x1 ** 2 - d * y1 ** 2

            print('           %7d  %7d  %7d' % (x1, y1, r))
#
#  Terminate.
#
    print('')
    print('PELL_NEXT_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    pell_next_test()
    timestamp()
