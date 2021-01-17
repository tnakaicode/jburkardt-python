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
from r8lib.r8_hyper_2f1 import r8_hyper_2f1


def gegenbauer_integral(expon, alpha):

    # *****************************************************************************80
    #
    # GEGENBAUER_INTEGRAL evaluates the integral of a monomial with Gegenbauer weight.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      Integral ( -1 <= X <= +1 ) x^EXPON (1-x^2)^ALPHA dx
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer EXPON, the exponent.
    #
    #    Input, real ALPHA, the exponent of (1-X^2) in the weight factor.
    #
    #    Output, real VALUE, the value of the integral.
    #

    if ((expon % 2) == 1):
        value = 0.0
        return value

    c = expon

    arg1 = - alpha
    arg2 = 1.0 + c
    arg3 = 2.0 + alpha + c
    arg4 = - 1.0

    value1 = r8_hyper_2f1(arg1, arg2, arg3, arg4)

    value = 2.0 * r8_gamma(1.0 + c) * r8_gamma(1.0 + alpha) \
        * value1 / r8_gamma(2.0 + alpha + c)

    return value


def gegenbauer_integral_test():

    # *****************************************************************************80
    #
    # GEGENBAUER_INTEGRAL_TEST tests GEGENBAUER_INTEGRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    alpha = 0.25

    print('')
    print('GEGENBAUER_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  GEGENBAUER_INTEGRAL evaluates')
    print('  Integral ( -1 < x < +1 ) x^n * (1-x*x)^alpha dx')
    print('')
    print('         N         Value')
    print('')

    for n in range(0, 11):
        value = gegenbauer_integral(n, alpha)
        print('  %8d  %24.16g' % (n, value))
    print('')
    print('GEGENBAUER_INTEGRAL_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    gegenbauer_integral_test()
    timestamp()
