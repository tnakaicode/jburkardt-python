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
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write


def schroeder(n):

    # *****************************************************************************80
    #
    # SCHROEDER generates the Schroeder numbers.
    #
    #  Discussion:
    #
    #    The Schroeder number S(N) counts the number of ways to insert
    #    parentheses into an expression of N items, with two or more items within
    #    a parenthesis.
    #
    #    Note that the Catalan number C(N) counts the number of ways
    #    to legally arrange a set of N left and N right parentheses.
    #
    #  Example:
    #
    #    N = 4
    #
    #    1234
    #    12(34)
    #    1(234)
    #    1(2(34))
    #    1(23)4
    #    1((23)4)
    #    (123)4
    #    (12)34
    #    (12)(34)
    #    (1(23))4
    #    ((12)3)4
    #
    #  First Values:
    #
    #           1
    #           1
    #           3
    #          11
    #          45
    #         197
    #         903
    #        4279
    #       20793
    #      103049
    #      518859
    #     2646723
    #    13648869
    #    71039373
    #
    #  Formula:
    #
    #    S(N) = ( P(N)(3.0) - 3 P(N-1)(3.0) ) / ( 4 * ( N - 1 ) )
    #    where P(N)(X) is the N-th Legendre polynomial.
    #
    #  Recursion:
    #
    #    S(1) = 1
    #    S(2) = 1
    #    S(N) = ( ( 6 * N - 9 ) * S(N-1) - ( N - 3 ) * S(N-2) ) / N
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    R P Stanley,
    #    Hipparchus, Plutarch, Schroeder, and Hough,
    #    American Mathematical Monthly,
    #    Volume 104, Number 4, 1997, pages 344-350.
    #
    #    Laurent Habsieger, Maxim Kazarian, Sergei Lando,
    #    On the Second Number of Plutarch,
    #    American Mathematical Monthly, May 1998, page 446.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of Schroeder numbers desired.
    #
    #    Output, integer S(N), the Schroeder numbers.
    #

    s = np.zeros(n, dtype=np.int32)

    if (1 <= n):

        s[0] = 1

        if (2 <= n):

            s[1] = 1

            for i in range(3, n + 1):
                s[i - 1] = ((6 * i - 9) * s[i - 2] - (i - 3) * s[i - 3]) // i

    return s


def schroeder_test():

    # *****************************************************************************80
    #
    # SCHROEDER_TEST tests SCHROEDER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 10

    print('')
    print('SCHROEDER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SCHROEDER computes the Schroeder numbers.')

    s = schroeder(n)

    print('')
    print('     N        S(N)')
    print('')

    for i in range(0, n):
        print('  %4d  %8d' % (i, s[i]))

    print('')
    print('SCHROEDER_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    schroeder_test()
    timestamp()
