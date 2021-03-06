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

from i4lib.i4_gcd import i4_gcd
from i4lib.i4_huge import i4_huge
from subset.rat_to_s import rat_to_s


def rat_to_cfrac(p, q):

    # *****************************************************************************80
    #
    # RAT_TO_CFRAC converts a rational value to a continued fraction.
    #
    #  Discussion:
    #
    #    The routine is given a rational number represented by P/Q, and
    #    computes the monic or "simple" continued fraction representation
    #    with integer coefficients of the number:
    #
    #      A(1) + 1/ (A(2) + 1/ (A(3) + ... + 1/A(N) ...))
    #
    #    The user must dimension A to a value M which is "large enough".
    #    The actual number of terms needed in the continued fraction
    #    representation cannot be known beforehand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 August 2004
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
    #    Computer Approximations,
    #    Wiley, 1968.
    #
    #  Parameters:
    #
    #    Input, integer P, Q, the numerator and denominator of the
    #    rational value whose continued fraction representation is
    #    desired.
    #
    #    Output, integer N, the number of entries in A.
    #
    #    Output, integer A(N), contains the continued fraction
    #    representation of the number.
    #

    b = []

    n = 0

    while (True):

        b.append(p // q)
        n = n + 1
        p = (p % q)

        if (p == 0):
            break

        b.append(q // p)
        n = n + 1
        q = (q % p)

        if (q == 0):
            break

    a = np.zeros(n)
    for i in range(0, n):
        a[i] = b[i]

    return n, a


def rat_to_cfrac_test():

    # *****************************************************************************80
    #
    # RAT_TO_CFRAC_TEST tests RAT_TO_CFRAC.
    #
    #  Discussion:
    #
    #    Compute the continued fraction form of 4096/15625.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 April 2009
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 10

    print('')
    print('RAT_TO_CFRAC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAT_TO_CFRAC fraction => continued fraction,')
    print('')

    top = 4096
    bot = 15625

    print('  Regular fraction is %6d / %6d' % (top, bot))

    n, a = rat_to_cfrac(top, bot)

    i4vec_print(n, a, '  Continued fraction coefficients:')

    p, q = cfrac_to_rat(n, a)

    print('')
    print('  The continued fraction convergents.')
    print('  The last row contains the value of the continued')
    print('  fraction, written as a common fraction.')
    print('')
    print('  I, P(I), Q(I), P(I)/Q(I)')
    print('')

    for i in range(0, n):
        print('  %3d  %6d  %6d  %14f' % (i, p[i], q[i], p[i] / q[i]))
#
#  Terminate.
#
    print('')
    print('RAT_TO_CFRAC_TEST')
    print('  Normal end of execution.')
    return


def cfrac_to_rat(n, a):

    # *****************************************************************************80
    #
    # CFRAC_TO_RAT converts a monic continued fraction to an ordinary fraction.
    #
    #  Discussion:
    #
    #    The routine is given the monic or "simple" continued fraction with
    #    integer coefficients:
    #
    #      A(1) + 1 / ( A(2) + 1 / ( A(3) ... + 1 / A(N) ) )
    #
    #    and returns the N successive approximants P(I)/Q(I)
    #    to the value of the rational number represented by the continued
    #    fraction, with the value exactly equal to the final ratio P(N)/Q(N).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
    #    Computer Approximations,
    #    Wiley, 1968.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of continued fraction coefficients.
    #
    #    Input, integer A(N), the continued fraction coefficients.
    #
    #    Output, integer P(N), Q(N), the N successive approximations
    #    to the value of the continued fraction.
    #

    p = np.zeros(n)
    q = np.zeros(n)

    for i in range(0, n):

        if (i == 0):
            p[i] = a[i] * 1 + 0
            q[i] = a[i] * 0 + 1
        elif (i == 1):
            p[i] = a[i] * p[i - 1] + 1
            q[i] = a[i] * q[i - 1] + 0
        else:
            p[i] = a[i] * p[i - 1] + p[i - 2]
            q[i] = a[i] * q[i - 1] + q[i - 2]

    return p, q


def cfrac_to_rat_test():

    # *****************************************************************************80
    #
    # % CFRAC_TO_RAT_TEST tests CFRAC_TO_RAT.
    #
    #  Discussion:
    #
    #    Compute the continued fraction form of 4096/15625.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 10

    print('')
    print('CFRAC_TO_RAT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CFRAC_TO_RAT continued fraction => fraction.')
    print('')

    top = 4096
    bot = 15625

    print('  Regular fraction is %6d / %6d' % (top, bot))

    n, a = rat_to_cfrac(top, bot)

    i4vec_print(n, a, '  Continued fraction coefficients:')

    p, q = cfrac_to_rat(n, a)

    print('')
    print('  The continued fraction convergents.')
    print('  The last row contains the value of the continued')
    print('  fraction, written as a common fraction.')
    print('')
    print('  I, P(I), Q(I), P(I)/Q(I)')
    print('')

    for i in range(0, n):
        print('  %3d  %6d  %6d  %14f' % (i, p[i], q[i], p[i] / q[i]))
#
#  Terminate.
#
    print('')
    print('CFRAC_TO_RAT_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    rat_to_cfrac_test()
    timestamp()
