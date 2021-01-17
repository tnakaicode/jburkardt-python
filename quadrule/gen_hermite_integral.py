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


def gen_hermite_integral(expon, alpha):

    # *****************************************************************************80
    #
    # GEN_HERMITE_INTEGRAL evaluates a monomial generalized Hermite integral.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      integral ( -oo < x < +oo ) x^n |x|^alpha exp(-x^2) dx
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, int EXPON, the exponent of the monomial.
    #
    #    Input, real ALPHA, the exponent of |X| in the integral.
    #    -1.0 < ALPHA.
    #
    #    Output, real VALUE, the value of the integral.
    #
    # from math import gamma

    if ((expon % 2) == 1):

        value = 0.0

    else:

        a = alpha + float(expon)

        if (a <= -1.0):

            value = - r8_huge()

        else:

            arg = (a + 1.0) / 2.0
            value = r8_gamma(arg)

    return value


def gen_hermite_integral_test():

    # *****************************************************************************80
    #
    # GEN_HERMITE_INTEGRAL_TEST tests GEN_HERMITE_INTEGRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    alpha = 0.5

    print('')
    print('GEN_HERMITE_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  GEN_HERMITE_INTEGRAL evaluates')
    print('  Integral ( -oo < x < +oo ) exp(-x^2) x^n |x|^alpha dx')
    print('')
    print('  Use ALPHA = %g' % (alpha))
    print('')
    print('         N         Value')
    print('')

    for n in range(0, 11):

        value = gen_hermite_integral(n, alpha)

        print('  %8d  %24.16g' % (n, value))
#
#  Terminate.
#
    print('')
    print('GEN_HERMITE_INTEGRAL_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    gen_hermite_integral_test()
    timestamp()
