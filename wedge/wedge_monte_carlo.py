#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import random as rn
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
from i4lib.i4vec_transpose_print import i4vec_transpose_print
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some

from i4lib.i4vec_uniform_ab import i4vec_uniform_ab
from i4lib.i4mat_uniform_ab import i4mat_uniform_ab
from r8lib.r8_uniform_ab import r8vec_uniform_01, r8mat_uniform_ab
from monomial.monomial_value import monomial_value
from rnglib.sample import wedge01_sample


def wedge01_monomial_integral(e):

    # *****************************************************************************80
    #
    # WEDGE01_MONOMIAL_INTEGRAL: integral of a monomial in the unit wedge in 3D.
    #
    #  Discussion:
    #
    #    This routine returns the integral of
    #
    #      product ( 1 <= I <= 3 ) X(I)^E(I)
    #
    #    over the unit wedge.
    #
    #    The integration region is:
    #
    #      0 <= X
    #      0 <= Y
    #      X + Y <= 1
    #      -1 <= Z <= 1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Arthur Stroud,
    #    Approximate Calculation of Multiple Integrals,
    #    Prentice Hall, 1971,
    #    ISBN: 0130438936,
    #    LC: QA311.S85.
    #
    #  Parameters:
    #
    #    Input, integer E(3), the exponents.
    #
    #    Output, real VALUE, the integral of the monomial.
    #
    from sys import exit

    value = 1.0

    k = e[0]

    for i in range(1, e[1] + 1):
        k = k + 1
        value = value * float(i) / float(k)

    k = k + 1
    value = value / float(k)

    k = k + 1
    value = value / float(k)
    
    #
    #  Now account for integration in Z.
    #
    if (e[2] == - 1):
        print('')
        print('WEDGE01_MONOMIAL_INTEGRAL - Fatal error!')
        print('  E(3) = -1 is not a legal input.')
        exit('WEDGE01_MONOMIAL_INTEGRAL - Fatal error!')
    elif ((e[2] % 2) == 1):
        value = 0.0
    else:
        value = value * 2.0 / float(e[2] + 1)

    return value


def wedge01_monomial_integral_test():

    # *****************************************************************************80
    #
    # WEDGE01_MONOMIAL_INTEGRAL_TEST tests WEDGE01_MONOMIAL_INTEGRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    m = 3
    n = 500000
    e_max = 6

    print('')
    print('WEDGE01_MONOMIAL_INTEGRAL_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  WEDGE01_MONOMIAL_INTEGRAL computes the integral of a monomial')
    print('  over the interior of the unit wedge in 3D.')
    print('  Compare with a Monte Carlo estimate.')

    seed = 123456789
    x, seed = wedge01_sample(n, seed)

    print('')
    print('  Number of sample points used is %d' % (n))
    print('')
    print('   E1  E2  E3     MC-Estimate      Exact           Error')
    print('')
    #
    #  Check all monomials up to total degree E_MAX.
    #
    e = np.zeros(3, dtype=np.int32)

    for e3 in range(0, e_max + 1):
        e[2] = e3
        for e2 in range(1, e_max - e3 + 1):
            e[1] = e2
            for e1 in range(0, e_max - e3 - e2 + 1):
                e[0] = e1

                value = monomial_value(m, n, e, x)

                q = 1 * np.sum(value) / float(n)
                exact = wedge01_monomial_integral(e)
                error = abs(q - exact)

                print('  %2d  %2d  %2d  %14.6g  %14.6g  %14.6g'
                      % (e[0], e[1], e[2], q, exact, error))

    print('')
    print('WEDGE01_MONOMIAL_INTEGRAL_TEST:')
    print('  Normal end of execution.')


def wedge01_monte_carlo_test():

    # *****************************************************************************80
    #
    # WEDGE01_MONTE_CARLO_TEST uses WEDGE01_SAMPLE with an increasing number of points.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3

    e_test = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [2, 0, 0],
        [1, 1, 0],
        [0, 0, 2],
        [3, 0, 0]])

    print('')
    print('WEDGE01_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use WEDGE01_SAMPLE for a Monte Carlo estimate of an')
    print('  integral over the interior of the unit wedge in 3D.')

    seed = 123456789

    print('')
    print('         N        1               X               Y               Z                X^2            XY              Z^2            X^3')
    print('')

    n = 1

    e = np.zeros(3, dtype=np.int32)

    while (n <= 65536):

        x, seed = wedge01_sample(n, seed)

        print('  %8d' % (n), end='')

        for j in range(0, 8):

            e[0:m] = e_test[j, 0:m]

            value = monomial_value(m, n, e, x)

            result = 1 * np.sum(value[0:n]) / float(n)
            print('  %14.6g' % (result), end='')

        print('')

        n = 2 * n

    print('')
    print('     Exact', end='')

    for j in range(0, 8):

        e[0:m] = e_test[j, 0:m]
        result = wedge01_monomial_integral(e)
        print('  %14.6g' % (result), end='')

    print('')
    print('')
    print('WEDGE01_MONTE_CARLO_TEST')
    print('  Normal end of execution.')


def wedge_monte_carlo_test():

    # *****************************************************************************80
    #
    # WEDGE_MONTE_CARLO_TEST tests the WEDGE_MONTE_CARLO library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    13 November 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('WEDGE_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the WEDGE_MONTE_CARLO library.')

    wedge01_monomial_integral_test()
    wedge01_monte_carlo_test()

    print('')
    print('WEDGE_MONTE_CARLO_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    wedge_monte_carlo_test()
    timestamp()
