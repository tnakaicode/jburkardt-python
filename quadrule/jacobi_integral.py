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
from quadrule.imtqlx import imtqlx


def jacobi_integral(expon, alpha, beta):

    # *****************************************************************************80
    #
    # JACOBI_INTEGRAL evaluates the integral of a monomial with Jacobi weight.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      Integral ( -1 <= X <= +1 ) x^EXPON (1-x)^ALPHA (1+x)^BETA dx
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
    #    Input, real ALPHA, the exponent of (1-X) in the weight factor.
    #
    #    Input, real BETA, the exponent of (1+X) in the weight factor.
    #
    #    Output, real VALUE, the value of the integral.
    #

    c = expon

    if ((expon % 2) == 0):
        s = +1.0
    else:
        s = -1.0

    arg1 = - alpha
    arg2 = 1.0 + c
    arg3 = 2.0 + beta + c
    arg4 = - 1.0

    value1 = r8_hyper_2f1(arg1, arg2, arg3, arg4)

    arg1 = - beta
    arg2 = 1.0 + c
    arg3 = 2.0 + alpha + c
    arg4 = - 1.0

    value2 = r8_hyper_2f1(arg1, arg2, arg3, arg4)

    value = r8_gamma(1.0 + c) * (
        s * r8_gamma(1.0 + beta) * value1 / r8_gamma(2.0 + beta + c)
        + r8_gamma(1.0 + alpha) * value2 / r8_gamma(2.0 + alpha + c))

    return value


def jacobi_integral_test():

    # *****************************************************************************80
    #
    # JACOBI_INTEGRAL_TEST tests JACOBI_INTEGRAL.
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
    import platform

    alpha = 1.5
    beta = 0.5

    print('')
    print('JACOBI_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  JACOBI_INTEGRAL evaluates')
    print('  Integral ( -1 < x < +1 ) x^n (1-x)^alpha (1+x)^beta dx')
    print('')
    print('  Use ALPHA = %g' % (alpha))
    print('      BETA =  %g' % (beta))
    print('')
    print('         N         Value')
    print('')

    for n in range(0, 11):

        value = jacobi_integral(n, alpha, beta)

        print('  %8d  %24.16g' % (n, value))
#
#  Terminate.
#
    print('')
    print('JACOBI_INTEGRAL_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    jacobi_integral_test()
    timestamp()
