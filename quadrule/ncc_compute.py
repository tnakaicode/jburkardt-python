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
from r8lib.r8vec_linspace import r8vec_linspace
from quadrule.imtqlx import imtqlx
from quadrule.nc_compute_weights import nc_compute_weights


def ncc_compute(n):

    # *****************************************************************************80
    #
    # NCC_COMPUTE computes a Newton-Cotes Closed quadrature rule.
    #
    #  Discussion:
    #
    #    For the interval [-1,+1], the Newton-Cotes Closed quadrature rule
    #    estimates
    #
    #      Integral ( -1 <= X <= +1 ) F(X) dX
    #
    #    using N abscissas X and weights W:
    #
    #      sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
    #
    #    For the CLOSED rule, the abscissas are equally spaced, and include
    #    the end points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the order.
    #
    #    Output, real X(N), the abscissas.
    #
    #    Output, real W(N), the weights.
    #

    x_min = -1.0
    x_max = +1.0
    x = r8vec_linspace(n, x_min, x_max)

    if (n == 1):

        w = np.zeros(n)
        w[0] = x_max - x_min

    else:

        w = nc_compute_weights(n, x_min, x_max, x)

    return x, w


def ncc_compute_test():

    # *****************************************************************************80
    #
    # NCC_COMPUTE_TEST tests NCC_COMPUTE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('NCC_COMPUTE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  NCC_COMPUTE computes a Newton-Cotes Closed quadrature rule')
    print('')
    print('  Index       X             W')

    for n in range(1, 11):

        x, w = ncc_compute(n)

        print('')

        for i in range(0, n):
            print('  %2d  %24.16g  %24.16g' % (i, x[i], w[i]))
#
#  Terminate.
#
    print('')
    print('NCC_COMPUTE_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    ncc_compute_test()
    timestamp()
