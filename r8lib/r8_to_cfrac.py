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


def r8_to_cfrac(r, n):

    # *****************************************************************************80
    #
    # R8_TO_CFRAC converts an R8 to a continued fraction.
    #
    #  Discussion:
    #
    #    The routine is given a real number R.  It computes a sequence of
    #    continued fraction approximations to R, returning the results as
    #    simple fractions of the form P(I) / Q(I).
    #
    #  Example:
    #
    #    X = 2 * PI
    #    N = 7
    #
    #    A = [ *, 6,  3,  1,  1,   7,   2,    146,      3 ]
    #    P = [ 1, 6, 19, 25, 44, 333, 710, 103993, 312689 ]
    #    Q = [ 0, 1,  3,  4,  7,  53, 113,  16551,  49766 ]
    #
    #    (This ignores roundoff error, which will cause later terms to differ).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Norman Richert,
    #    Strang's Strange Figures,
    #    American Mathematical Monthly,
    #    Volume 99, Number 2, February 1992, pages 101-107.
    #
    #  Parameters:
    #
    #    Input, real R, the real value.
    #
    #    Input, integer N, the number of convergents to compute.
    #
    #    Output, integer A(1:N+1), the partial quotients.
    #
    #    Output, integer P(1:N+2), Q(1:N+2), the numerators and denominators
    #    of the continued fraction approximations.
    #

    a = np.zeros(n + 1, dtype=np.int32)
    p = np.zeros(n + 2, dtype=np.int32)
    q = np.zeros(n + 2, dtype=np.int32)
    x = np.zeros(n + 1, dtype=np.float64)

    if (r == 0.0):
        for i in range(0, n + 2):
            q[i] = 1
        return a, p, q

    p[0] = 1
    q[0] = 0

    p[1] = int(abs(r))
    q[1] = 1
    x[0] = abs(r)
    a[0] = int(x[0])

    for i in range(1, n + 1):

        if ((x[i - 1] - a[i - 1]) == 0.0):
            break

        x[i] = 1.0 / (x[i - 1] - a[i - 1])
        a[i] = int(x[i])
        p[i + 1] = a[i] * p[i] + p[i - 1]
        q[i + 1] = a[i] * q[i] + q[i - 1]

    if (r < 0.0):
        for i in range(0, n + 2):
            p[i] = - p[i]

    return a, p, q


def r8_to_cfrac_test():

    # *****************************************************************************80
    #
    # R8_TO_CFRAC_TEST tests R8_TO_CFRAC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 7

    print('')
    print('R8_TO_CFRAC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_TO_CFRAC converts a real number to a sequence')
    print('  of continued fraction convergents.')

    r = 2.0 * np.pi

    print('')
    print('  Use the real number R = %g' % (r))

    a, p, q = r8_to_cfrac(r, n)

    print('')

    for i in range(0, n):
        temp = float(p[i + 1]) / float(q[i + 1])
        print('  %6d  %6d  %6d  %12f  %12f'
              % (a[i], p[i + 1], q[i + 1], temp, r - temp))

    print('')
    print('R8_TO_CFRAC_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    r8_to_cfrac_test()
    timestamp()
