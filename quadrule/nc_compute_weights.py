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

def nc_compute_weights(n, x_min, x_max, x):

    # *****************************************************************************80
    #
    # NC_COMPUTE_WEIGHTS computes weights for a Newton-Cotes quadrature rule.
    #
    #  Discussion:
    #
    #    For the interval [X_MIN,X_MAX], the Newton-Cotes quadrature rule
    #    estimates
    #
    #      Integral ( X_MIN <= X <= X_MAX ) F(X) dX
    #
    #    using N abscissas X and weights W:
    #
    #      Sum ( 1 <= I <= N ) W(I) * F ( X(I) ).
    #
    #    For the CLOSED rule, the equally spaced abscissas include A and B.
    #    For the OPEN rule, the equally spaced abscissas do not include A and B.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 April 2010
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the order.
    #
    #    Input, real X_MIN, X_MAX, the endpoints of the interval.
    #
    #    Input, real X(N), the abscissas.
    #
    #    Output, real W(N), the weights.
    #
    import numpy as np

    d = np.zeros(n)
    w = np.zeros(n)

    for i in range(1, n + 1):
        #
        #  Compute the Lagrange basis polynomial which is 1 at X(I),
        #  and zero at the other nodes.
        #
        d = np.zeros(n)
        d[i - 1] = 1.0

        for j in range(2, n + 1):
            for k in range(j, n + 1):
                d[n + j - k - 1] = (d[n + j - k - 1 - 1] - d[n + j - k - 1]
                                    ) / (x[n + 1 - k - 1] - x[n + j - k - 1])

        for j in range(1, n):
            for k in range(1, n - j + 1):
                d[n - k - 1] = d[n - k - 1] - x[n - k - j] * d[n - k]
#
#  Evaluate the antiderivative of the polynomial at the endpoints.
#
        yvala = d[n - 1] / float(n)
        for j in range(n - 1, 0, -1):
            yvala = yvala * x_min + d[j - 1] / float(j)
        yvala = yvala * x_min

        yvalb = d[n - 1] / float(n)
        for j in range(n - 1, 0, -1):
            yvalb = yvalb * x_max + d[j - 1] / float(j)
        yvalb = yvalb * x_max

        w[i - 1] = yvalb - yvala

    return w


def nc_compute_weights_test():

    # *****************************************************************************80
    #
    # % NC_COMPUTE_WEIGHTS_TEST tests NC_COMPUTE_WEIGHTS.
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

    print('')
    print('NC_COMPUTE_WEIGHTS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  NC_COMPUTE_WEIGHTS computes weights for')
    print('  a Newton-Cotes quadrature rule')
    print('')
    print('  Index       X             W')

    x_min = 0.0
    x_max = 1.0

    for n in range(1, 11):

        x = r8vec_linspace(n, x_min, x_max)

        w = nc_compute_weights(n, x_min, x_max, x)

        print('')

        for i in range(0, n):
            print('  %2d  %24.16g  %24.16g' % (i, x[i], w[i]))
#
#  Terminate.
#
    print('')
    print('NC_COMPUTE_WEIGHTS_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    nc_compute_weights_test()
    timestamp()
