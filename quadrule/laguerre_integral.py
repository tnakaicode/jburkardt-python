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

from r8lib.r8_factorial import r8_factorial
from r8lib.r8_gamma import r8_gamma
from quadrule.imtqlx import imtqlx


def laguerre_integral(expon):

    # *****************************************************************************80
    #
    # LAGUERRE_INTEGRAL evaluates a monomial Laguerre integral.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      integral ( 0 <= x < +oo ) x^n * exp ( -x ) dx
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer EXPON, the exponent.
    #    0 <= EXPON.
    #
    #    Output, real EXACT, the value of the integral.
    #

    exact = r8_factorial(expon)

    return exact


def laguerre_integral_test():

    # *****************************************************************************80
    #
    # LAGUERRE_INTEGRAL_TEST tests LAGUERRE_INTEGRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('LAGUERRE_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LAGUERRE_INTEGRAL evaluates')
    print('  Integral ( 0 < x < oo ) x^n * exp(-x) dx')
    print('')
    print('         N         Value')
    print('')

    for n in range(0, 11):

        value = laguerre_integral(n)

        print('  %8d  %24.16g' % (n, value))
#
#  Terminate.
#
    print('')
    print('LAGUERRE_INTEGRAL_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    laguerre_integral_test()
    timestamp()
