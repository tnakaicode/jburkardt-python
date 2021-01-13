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


def power_series2(n, a):

    # *****************************************************************************80
    #
    # POWER_SERIES2 computes the power series for G(Z) = exp(F(Z)) - 1.
    #
    #  Discussion:
    #
    #    The power series for F(Z) is given.
    #
    #    The power series have the form:
    #
    #      F(Z) = A1*Z + A2*Z^2 + A3*Z^3 + ... + AN*Z^N
    #
    #      G(Z) = B1*Z + B2*Z^2 + B3*Z^3 + ... + BN*Z^N
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 June 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Albert Nijenhuis, Herbert Wilf,
    #    Combinatorial Algorithms,
    #    Academic Press, 1978, second edition,
    #    ISBN 0-12-519260-6.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of terms in the power series.
    #
    #    Input, real A(N), the power series coefficients for F(Z).
    #
    #    Output, real B(N), the power series coefficients for G(Z).
    #

    b = np.zeros(n)

    for j in range(1, n + 1):

        v = 0.0

        for i in range(1, j):
            v = v + b[i - 1] * a[j - i - 1] * float(j - i)

        b[j - 1] = a[j - 1] + v / float(j)

    return b


def power_series2_test():

    # *****************************************************************************80
    #
    # POWER_SERIES2_TEST tests POWER_SERIES2
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    09 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4
    a = np.zeros(n)
    a[0] = -4.0

    print('')
    print('POWER_SERIES2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POWER_SERIES2 composes a power series')
    print('  Here we compute the power series of G(x) = exp(F(x))-1')
    print('  The number of terms is N = %d' % (n))

    r8vec_print(n, a, '  Series for F(x):')

    b = power_series2(n, a)

    r8vec_print(n, b, '  Series for G(x):')
#
#  Terminate.
#
    print('')
    print('POWER_SERIES2_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    power_series2_test()
    timestamp()
