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

from polynomial.polynomial_print import polynomial_print


def polynomial_scale(s, m, o, c, e):

    # *****************************************************************************80
    #
    # POLYNOMIAL_SCALE scales a polynomial.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 January 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real S, the scale factor.
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer O, the "order" of the polynomial.
    #
    #    Input, real C[O], the coefficients of the scaled polynomial.
    #
    #    Input, integer E[O], the indices of the exponents of
    #    the scaled polynomial.
    #
    #    Output, integer O, the "order" of the polynomial.
    #
    #    Output, real C[O], the coefficients of the scaled polynomial.
    #
    #    Output, integer E[O], the indices of the exponents of
    #    the scaled polynomial.
    #
    for i in range(0, o):
        c[i] = c[i] * s

    return o, c, e


def polynomial_scale_test():

    # *****************************************************************************80
    #
    # POLYNOMIAL_SCALE_TEST tests POLYNOMIAL_SCALE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3
    o = 6
    c = np.array([7.0, - 5.0, 9.0, 11.0, 0.0, - 13.0], dtype=np.float64)
    e = np.array([1, 2, 4, 5, 12, 33], dtype=np.int32)

    print('')
    print('POLYNOMIAL_SCALE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  POLYNOMIAL_SCALE scales a polynomial by a multiplier S.')

    print('')
    title = '  Original P(X):'
    polynomial_print(m, o, c, e, title)

    s = - 0.5
    print('')
    print('  Apply scale factor S = %g' % (s))
    o, c, e = polynomial_scale(s, m, o, c, e)

    print('')
    title = '  S * P(X):'
    polynomial_print(m, o, c, e, title)

    print('')
    print('POLYNOMIAL_SCALE_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    polynomial_scale_test()
    timestamp()
