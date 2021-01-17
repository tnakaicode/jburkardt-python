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
from quadrule.imtqlx import imtqlx


def jacobi_ek_compute(n, alpha, beta):

    # *****************************************************************************80
    #
    # JACOBI_EK_COMPUTE: Elhay-Kautsky method for Gauss-Jacobi quadrature rule.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      integral ( -1 <= x <= 1 ) (1-x)^alpha * (1+x)^beta * f(x) dx
    #
    #    The quadrature rule:
    #
    #      sum ( 1 <= i <= n ) w(i) * f ( x(i) )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 June 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    Sylvan Elhay, Jaroslav Kautsky,
    #    Algorithm 655: IQPACK, FORTRAN Subroutines for the Weights of
    #    Interpolatory Quadrature,
    #    ACM Transactions on Mathematical Software,
    #    Volume 13, Number 4, December 1987, pages 399-415.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of abscissas.
    #
    #    Input, real ALPHA, BETA, the exponents of (1-X) and
    #    (1+X) in the quadrature rule.  For simple Gauss-Legendre quadrature,
    #    set ALPHA = BETA = 0.0.  -1.0 < ALPHA and -1.0 < BETA are required.
    #
    #    Output, real X(N), the abscissas.
    #
    #    Output, real W(N), the weights.
    #

    #
    #  Define the zero-th moment.
    #
    zemu = 2.0 ** (alpha + beta + 1) \
        * r8_gamma(alpha + 1.0) \
        * r8_gamma(beta + 1.0) \
        / r8_gamma(alpha + beta + 2.0)
#
#  Define the Jacobi matrix.
#
    bj = np.zeros(n)

    bj[0] = 4.0 * (1.0 + alpha) * (1.0 + beta) \
        / ((3.0 + alpha + beta) * (2.0 + alpha + beta) ** 2)

    for i in range(1, n):
        ip1_r8 = float(i + 1)
        abi = 2.0 * ip1_r8 + alpha + beta
        bj[i] = 4.0 * ip1_r8 * (ip1_r8 + alpha) * (ip1_r8 + beta) \
            * (ip1_r8 + alpha + beta) \
            / ((abi - 1.0) * (abi + 1.0) * abi * abi)

    for i in range(0, n):
        bj[i] = np.sqrt(bj[i])

    x = np.zeros(n)
    x[0] = (beta - alpha) / (2.0 + alpha + beta)
    for i in range(1, n):
        ip1_r8 = float(i + 1)
        abi = 2.0 * ip1_r8 + alpha + beta
        x[i] = (beta + alpha) * (beta - alpha) / ((abi - 2.0) * abi)

    w = np.zeros(n)
    w[0] = np.sqrt(zemu)
#
#  Diagonalize the Jacobi matrix.
#
    x, w = imtqlx(n, x, bj, w)

    for i in range(0, n):
        w[i] = w[i] ** 2

    return x, w


def jacobi_ek_compute_test():

    # *****************************************************************************80
    #
    # JACOBI_EK_COMPUTE_TEST tests JACOBI_EK_COMPUTE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    16 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    alpha = 1.5
    beta = 0.5

    print('')
    print('JACOBI_EK_COMPUTE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  JACOBI_EK_COMPUTE computes')
    print('  a generalized Jacobi quadrature rule')
    print('  using the Elhay-Kautsky algorithm.')
    print('')
    print('  Using ALPHA = %g' % (alpha))
    print('')
    print('  Index       X             W')

    for n in range(1, 11):

        x, w = jacobi_ek_compute(n, alpha, beta)

        print('')

        for i in range(0, n):
            print('  %2d  %24.16g  %24.16g' % (i, x[i], w[i]))
#
#  Terminate.
#
    print('')
    print('JACOBI_EK_COMPUTE_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    jacobi_ek_compute_test()
    timestamp()
