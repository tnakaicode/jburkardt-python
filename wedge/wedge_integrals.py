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

                q = wedge01_volume() * np.sum(value) / float(n)
                exact = wedge01_monomial_integral(e)
                error = abs(q - exact)

                print('  %2d  %2d  %2d  %14.6g  %14.6g  %14.6g'
                      % (e[0], e[1], e[2], q, exact, error))

    print('')
    print('WEDGE01_MONOMIAL_INTEGRAL_TEST:')
    print('  Normal end of execution.')


def wedge01_volume():

    # *****************************************************************************80
    #
    # WEDGE01_VOLUME returns the volume of the unit wedge in 3D.
    #
    #  Discussion:
    #
    #    The unit wedge is:
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
    #  Parameters:
    #
    #    Output, real VALUE, the volume of the unit wedge.
    #
    value = 1.0

    return value


def wedge01_volume_test():

    # *****************************************************************************80
    #
    # WEDGE01_VOLUME_TEST tests WEDGE01_VOLUME.
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

    print('')
    print('WEDGE01_VOLUME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  WEDGE01_VOLUME returns the volume of the unit wedge.')

    value = wedge01_volume()

    print('')
    print('  WEDGE01_VOLUME() = %g' % (value))
    print('')
    print('WEDGE01_VOLUME_TEST')
    print('  Normal end of execution.')


def wedge_integrals_test():

    # *****************************************************************************80
    #
    # WEDGE_INTEGRALS_TEST tests the WEDGE_INTEGRALS library.
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

    print('')
    print('WEDGE_INTEGRALS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the WEDGE_INTEGRALS library.')

    wedge01_monomial_integral_test()
    wedge01_volume_test()

    print('')
    print('WEDGE_INTEGRALS_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    wedge_integrals_test()
    timestamp()
