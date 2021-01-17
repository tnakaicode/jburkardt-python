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


def laguerre_ek_compute(n):

    # *****************************************************************************80
    #
    # LAGUERRE_EK_COMPUTE: Gauss-Laguerre, Elhay-Kautsky method.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      integral ( 0 < x < +oo ) exp ( -x ) * f(x) dx
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
    #    Output, real X(N), the abscissas.
    #
    #    Output, real W(N), the weights.
    #

    #
    #  Define the zero-th moment.
    #
    zemu = 1.0
#
#  Define the Jacobi matrix.
#
    bj = np.zeros(n)
    for i in range(0, n):
        ip1_r8 = float(i + 1)
        bj[i] = ip1_r8

    x = np.zeros(n)
    for i in range(0, n):
        x[i] = float(2 * i + 1)

    w = np.zeros(n)
    w[0] = np.sqrt(zemu)
#
#  Diagonalize the Jacobi matrix.
#
    x, w = imtqlx(n, x, bj, w)

    for i in range(0, n):
        w[i] = w[i] ** 2

    return x, w


def laguerre_ek_compute_test():

    # *****************************************************************************80
    #
    # LAGUERRE_EK_COMPUTE_TEST tests LAGUERRE_EK_COMPUTE.
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

    print('')
    print('LAGUERRE_EK_COMPUTE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LAGUERRE_EK_COMPUTE computes')
    print('  a Laguerre quadrature rule')
    print('  using the Elhay-Kautsky algorithm.')
    print('')
    print('  Index       X             W')

    for n in range(1, 11):

        x, w = laguerre_ek_compute(n)

        print('')

        for i in range(0, n):
            print('  %2d  %24.16g  %24.16g' % (i, x[i], w[i]))
#
#  Terminate.
#
    print('')
    print('LAGUERRE_EK_COMPUTE_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    laguerre_ek_compute_test()
    timestamp()
