#! /usr/bin/env python3
#

from types import resolve_bases
import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from scipy.special import beta, gamma
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

from i4lib.i4_normal_ab import i4_normal_ab
from i4lib.i4_uniform_ab import i4_uniform_ab
from i4lib.i4vec_uniform_ab import i4vec_uniform_ab
from i4lib.i4mat_uniform_ab import i4mat_uniform_ab

from r8lib.r8_uniform_01 import r8_uniform_01, r8_uniform_ab
from r8lib.r8vec_uniform_01 import r8vec_uniform_01, r8vec_uniform_ab
from r8lib.r8vec_norm import r8vec_norm
from r8lib.r8vec_normal_01 import r8vec_normal_01
from r8lib.r8vec_normal_ab import r8vec_normal_ab
from r8lib.r8mat_uniform_01 import r8mat_uniform_01
from r8lib.r8mat_uniform_ab import r8mat_uniform_ab
from r8lib.r8mat_normal_01 import r8mat_normal_01
from r8lib.r8mat_normal_ab import r8mat_normal_ab
from r8lib.r8vec_uniform_unit import r8vec_uniform_unit
from r8lib.r8vec_uniform_abvec import r8vec_uniform_abvec
from r8lib.r8mat_uniform_abvec import r8mat_uniform_abvec


def monomial_value(m, n, e, x):

    #
    # MONOMIAL_VALUE evaluates a monomial.
    #
    #  Discussion:
    #
    #    This routine evaluates a monomial of the form
    #
    #      product ( 1 <= i <= m ) x(i)^e(i)
    #
    #    The combination 0.0^0, if encountered, is treated as 1.0.
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of evaluation points.
    #
    #    Input, integer E(M), the exponents.
    #
    #    Input, real X(M,N), the point coordinates.
    #
    #    Output, real V(N), the monomial values.
    #

    v = np.ones(n)
    for i in range(0, m):
        if (0 != e[i]):
            for j in range(0, n):
                v[j] = v[j] * x[i, j] ** e[i]

    return v


class BaseTetrahedron(plot2d):

    def __init__(self):
        plot2d.__init__(self, aspect="equal")

    def mass(self):

        #
        # TETRAHEDRON01_VOLUME returns the volume of the unit tetrahedron.
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
        #    Output, real VOLUME, the volume.
        #
        value = 1.0 / 6.0
        return value

    def monomial_integral(self, m, e):

        #
        # TETRAHEDRON01_MONOMIAL_INTEGRAL: integrals in the unit tetrahedron in 3D.
        #
        #  Discussion:
        #
        #    The monomial is F(X,Y,Z) = X^E(1) * Y^E(2) * Z^E(3).
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
        #    Input, integer E(3), the exponents.
        #    Each exponent must be nonnegative.
        #
        #    Output, real INTEGRAL, the integral.
        #

        m = 3

        for i in range(0, m):
            if (e[i] < 0):
                print('')
                print('TETRAHEDRON01_MONOMIAL_INTEGRAL - Fatal error!')
                print('  All exponents must be nonnegative.')
                exit('TETRAHEDRON01_MONOMIAL_INTEGRAL - Fatal error!\n')

        k = 0
        integral = 1.0

        for i in range(0, m):
            for j in range(1, e[i] + 1):
                k = k + 1
                integral = integral * float(j) / float(k)

        for i in range(0, m):
            k = k + 1
            integral = integral / float(k)

        return integral

    def sample(self, n, seed):

        #
        # TETRAHEDRON01_SAMPLE samples the unit tetrahedron in 3D.
        #
        #  Reference:
        #
        #    Reuven Rubinstein,
        #    Monte Carlo Optimization, Simulation, and Sensitivity
        #    of Queueing Networks,
        #    Krieger, 1992,
        #    ISBN: 0894647644,
        #    LC: QA298.R79.
        #
        #  Parameters:
        #
        #    Input, integer N, the number of points.
        #
        #    Input/output, integer SEED, a seed for the random
        #    number generator.
        #
        #    Output, real X(3,N), the points.
        #

        m = 3
        x = np.zeros([m, n])
        el = np.zeros(m + 1)

        for j in range(0, n):
            e, seed = r8vec_uniform_01(m + 1, seed)
            el_sum = 0.0

            for i in range(0, m + 1):
                el[i] = - np.log(e[i])
                el_sum = el_sum + el[i]

            for i in range(0, m):
                x[i, j] = el[i] / el_sum

        return x, seed


if (__name__ == '__main__'):
    timestamp()

    seed = 123456789

    obj = BaseTetrahedron()

    m, n = 3, 50000
    e, e_max = np.zeros(3, dtype=np.int32), 6
    x, seed = obj.sample(n, seed)
    print('  Ex  Ey  Ez     MC-Estimate           Exact      Error')
    for e3 in range(0, e_max + 1):
        e[2] = e3
        for e2 in range(1, e_max - e3 + 1):
            e[1] = e2
            for e1 in range(0, e_max - e3 - e2 + 1):
                e[0] = e1
                value = monomial_value(m, n, e, x)
                resul = obj.mass() * np.sum(value) / float(n)
                exact = obj.monomial_integral(m, e)
                error = abs(resul - exact)

                for i in range(0, m):
                    print('  %2d' % (e[i]), end='')
                print('  %14.6g  ' % (resul), end='')
                print('  %14.6g  ' % (exact), end='')
                print('  %10.2g  ' % (error))
