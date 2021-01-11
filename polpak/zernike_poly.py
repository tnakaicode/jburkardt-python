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

from r8lib.r8mat_print import r8mat_print
from r8lib.r8mat_print_some import r8mat_print_some
from r8lib.r8mat_uniform_abvec import r8mat_uniform_abvec
from r8lib.r8vec2_print import r8vec2_print
from r8lib.r8poly_print import r8poly_print
from r8lib.r8poly_value_horner import r8poly_value_horner
from polpak.zernike_poly_coef import zernike_poly_coef


def zernike_poly(m, n, rho):

    # *****************************************************************************80
    #
    # ZERNIKE_POLY evaluates a Zernike polynomial at RHO.
    #
    #  Discussion:
    #
    #    This routine uses the facts that:
    #
    #    *) R^M_N = 0 if M < 0, or N < 0, or N < M.
    #    *) R^M_M = RHO^M
    #    *) R^M_N = 0 if mod ( N - M, 2 ) = 1.
    #
    #    and the recursion:
    #
    #    R^M_(N+2) = A * [ ( B * RHO^2 - C ) * R^M_N - D * R^M_(N-2) ]
    #
    #    where
    #
    #    A = ( N + 2 ) / ( ( N + 2 )^2 - M^2 )
    #    B = 4 * ( N + 1 )
    #    C = ( N + M )^2 / N + ( N - M + 2 )^2 / ( N + 2 )
    #    D = ( N^2 - M^2 ) / N
    #
    #    I wish I could clean up the recursion in the code, but for
    #    now, I have to treat the case M = 0 specially.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Eric Weisstein,
    #    "Zernike Polynomials",
    #    CRC Concise Encyclopedia of Mathematics,
    #    CRC Press, 1999,
    #    QA5.W45
    #
    #  Parameters:
    #
    #    Input, integer M, the upper index.
    #
    #    Input, integer N, the lower index.
    #
    #    Input, real RHO, the radial coordinate.
    #
    #    Output, real Z, the value of the Zernike
    #    polynomial R^M_N at the point RHO.
    #

    #
    #  Do checks.
    #
    if (m < 0):
        z = 0.0
        return z

    if (n < 0):
        z = 0.0
        return z

    if (n < m):
        z = 0.0
        return z

    if (((n - m) % 2) == 1):
        z = 0.0
        return z

    zm2 = 0.0
    z = rho ** m

    if (m == 0):

        if (n == 0):
            return z

        zm2 = z
        z = 2.0 * rho * rho - 1.0

        for nn in range(m + 2, n - 1, 2):

            a = float(nn + 2) / float((nn + 2) * (nn + 2) - m * m)

            b = 4.0 * float(nn + 1)

            c = float((nn + m) * (nn + m)) / float(nn) \
                + float((nn - m + 2) * (nn - m + 2)) / float(nn + 2)

            d = float(nn * nn - m * m) / float(nn)

            zp2 = a * ((b * rho * rho - c) * z - d * zm2)
            zm2 = z
            z = zp2

    else:

        for nn in range(m, n - 1, 2):

            a = float(nn + 2) / float((nn + 2) * (nn + 2) - m * m)

            b = 4.0 * float(nn + 1)

            c = float((nn + m) * (nn + m)) / float(nn) \
                + float((nn - m + 2) * (nn - m + 2)) / float(nn + 2)

            d = float(nn * nn - m * m) / float(nn)

            zp2 = a * ((b * rho * rho - c) * z - d * zm2)
            zm2 = z
            z = zp2

    return z


def zernike_poly_test():

    # *****************************************************************************80
    #
    # ZERNIKE_POLY_TEST tests ZERNIKE_POLY.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('ZERNIKE_POLY_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  ZERNIKE_POLY evaluates a Zernike polynomial directly.')
    print('')
    print('  Table of polynomial coefficients:')
    print('')
    print('   N   M')
    print('')

    for n in range(0, 6):

        print('')

        for m in range(0, n + 1):
            c = zernike_poly_coef(m, n)
            print('  %2d  %2d' % (n, m)),
            for i in range(0, n + 1):
                print('  %7f' % (c[i])),
            print('')

    rho = 0.987654321

    print('')
    print('  Z1: Compute polynomial coefficients,')
    print('  then evaluate by Horner\'s method;')
    print('  Z2: Evaluate directly by recursion.')
    print('')
    print('   N   M       Z1              Z2')
    print('')

    for n in range(0, 6):
        print('')
        for m in range(0, n + 1):

            c = zernike_poly_coef(m, n)
            z1 = r8poly_value_horner(n, c, rho)
            z2 = zernike_poly(m, n, rho)
            print('  %2d  %2d  %16f  %16f' % (n, m, z1, z2))

    print('')
    print('ZERNIKE_POLY_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    zernike_poly_test()
    timestamp()
