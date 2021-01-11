#! /usr/bin/env python
#
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
from r8lib.r8_factorial import r8_factorial


def laguerre_integral(p):

    # *****************************************************************************80
    #
    # LAGUERRE_INTEGRAL evaluates a monomial integral associated with L(n,x).
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      integral ( 0 <= x < +oo ) x^p * exp ( -x ) dx
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer P, the exponent.
    #    0 <= P.
    #
    #    Output, real S, the value of the integral.
    #

    s = r8_factorial(p)

    return s


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
    #    14 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('LAGUERRE_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LAGUERRE_INTEGRAL returns Laguerre integrals of monomials:')
    print('  M(k) = integral ( 0 <= x < +oo ) x^k exp(-x) dx')
    print('')
    print('     K            M(K)')
    print('')
    for k in range(0, 11):
        print('  %4d  %14.6g' % (k, laguerre_integral(k)))
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
