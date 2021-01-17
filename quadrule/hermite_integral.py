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
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8vec_transpose_print import r8vec_transpose_print
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some

from r8lib.r8_gamma import r8_gamma
from r8lib.r8_huge import r8_huge
from r8lib.r8_factorial2 import r8_factorial2
from quadrule.imtqlx import imtqlx


def hermite_integral(n):

    # *****************************************************************************80
    #
    # HERMITE_INTEGRAL evaluates a monomial Hermite integral.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      Integral ( -oo < x < +oo ) x^n exp(-x^2) dx
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the integral.
    #    0 <= N.
    #
    #    Output, real VALUE, the value of the integral.
    #

    if (n < 0):

        value = - r8_huge()

    elif ((n % 2) == 1):

        value = 0.0

    else:

        value = r8_factorial2(n - 1) * np.sqrt(np.pi) / 2.0 ** (n // 2)

    return value


def hermite_integral_test():

    # *****************************************************************************80
    #
    # HERMITE_INTEGRAL_TEST tests HERMITE_INTEGRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('HERMITE_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  HERMITE_INTEGRAL evaluates')
    print('  Integral ( -oo < x < +oo ) exp(-x^2) x^m dx')
    print('')
    print('         N         Value')
    print('')

    for n in range(0, 11):

        value = hermite_integral(n)

        print('  %8d  %24.16g' % (n, value))
#
#  Terminate.
#
    print('')
    print('HERMITE_INTEGRAL_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    hermite_integral_test()
    timestamp()
