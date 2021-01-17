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
from r8lib.r8_epsilon import r8_epsilon
from r8lib.r8vec_reverse import r8vec_reverse
from r8lib.r8vec_diff_norm_li import r8vec_diff_norm_li
from quadrule.imtqlx import imtqlx


def lobatto_compute(n):

    # *****************************************************************************80
    #
    # LOBATTO_COMPUTE computes a Lobatto quadrature rule.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      Integral ( -1 <= X <= 1 ) F(X) dX
    #
    #    The quadrature rule:
    #
    #      Sum ( 1 <= I <= N ) W(I) * F ( X(I) )
    #
    #    The quadrature rule will integrate exactly all polynomials up to
    #    X^(2*N-3).
    #
    #    The Lobatto rule is distinguished by the fact that both endpoints
    #    (-1 and 1) are always abscissas of the rule.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    01 April 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Milton Abramowitz, Irene Stegun,
    #    Handbook of Mathematical Functions,
    #    National Bureau of Standards, 1964,
    #    ISBN: 0-486-61272-4,
    #    LC: QA47.A34.
    #
    #    Claudio Canuto, Yousuff Hussaini, Alfio Quarteroni, Thomas Zang,
    #    Spectral Methods in Fluid Dynamics,
    #    Springer, 1993,
    #    ISNB13: 978-3540522058,
    #    LC: QA377.S676.
    #
    #    Arthur Stroud, Don Secrest,
    #    Gaussian Quadrature Formulas,
    #    Prentice Hall, 1966,
    #    LC: QA299.4G3S7.
    #
    #    Daniel Zwillinger, editor,
    #    CRC Standard Mathematical Tables and Formulae,
    #    30th Edition,
    #    CRC Press, 1996,
    #    ISBN: 0-8493-2479-3.
    #
    #  Parameters:
    #
    #    Input, integer N, the order.
    #
    #    Output, real X(N), the abscissas.
    #
    #    Output, real W(N), the weights,
    #

    x = np.zeros(n)
    w = np.zeros(n)

    if (n == 1):
        x[0] = -1.0
        w[0] = 2.0
        return x, w

    tol = 100.0 * r8_epsilon()
#
#  Initial estimate for the abscissas is the Chebyshev-Gauss-Lobatto nodes.
#
    for i in range(0, n):
        x[i] = np.cos(np.pi * float(i) / float(n - 1))

    xold = np.zeros(n)
    p = np.zeros([n, n])

    while (True):

        for i in range(0, n):
            xold[i] = x[i]

        for i in range(0, n):
            p[i, 0] = 1.0
            p[i, 1] = x[i]

        for j in range(2, n):
            for i in range(0, n):
                p[i, j] = (float(2 * j - 1) * x[i] * p[i, j - 1]
                           + float(- j + 1) * p[i, j - 2]) \
                    / float(j)

        for i in range(0, n):
            x[i] = xold[i] - (x[i] * p[i, n - 1] - p[i, n - 2]) \
                / (float(n) * p[i, n - 1])

        dif = r8vec_diff_norm_li(n, x, xold)

        if (dif <= tol):
            break

    x = r8vec_reverse(n, x)

    for i in range(0, n):
        w[i] = 2.0 / (float(n * (n - 1)) * p[i, n - 1] ** 2)

    return x, w


def lobatto_compute_test():

    # *****************************************************************************80
    #
    # LOBATTO_COMPUTE_TEST tests LOBATTO_COMPUTE.
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
    import platform

    print('')
    print('LOBATTO_COMPUTE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LOBATTO_COMPUTE computes a Lobatto rule')
    print('')
    print('         I      X             W')

    for n in range(4, 11, 3):

        x, w = lobatto_compute(n)

        print('')
        for i in range(0, n):
            print('  %8d  %12g  %12g' % (i, x[i], w[i]))
#
#  Terminate.
#
    print('')
    print('LOBATTO_COMPUTE_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    lobatto_compute_test()
    timestamp()
