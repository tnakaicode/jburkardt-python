#! /usr/bin/env python3
#

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
#from r8lib.r8vec_transpose_print import r8vec_transpose_print
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


class BaseWedge(plot2d):

    def __init__(self):
        plot2d.__init__(self, aspect="equal")

    def monomial_integral(self, m, e):

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

    def sample(self, n, seed):

        #
        # WEDGE01_SAMPLE samples points uniformly from the unit wedge in 3D.
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
        for j in range(0, n):
            e, seed = r8vec_uniform_01(m + 1, seed)
            el = np.zeros(m)
            el_sum = 0.0
            for i in range(0, m):
                el[i] = - np.log(e[i])
                el_sum = el_sum + el[i]
            x[0, j] = el[0] / el_sum
            x[1, j] = el[1] / el_sum
            x[2, j] = 2.0 * e[3] - 1.0
        return x, seed


if (__name__ == '__main__'):
    timestamp()

    seed = 123456789

    obj = BaseWedge()

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
                q = 1 * np.sum(value) / float(n)
                exact = obj.monomial_integral(m, e)
                error = abs(q - exact)

                for i in range(0, m):
                    print('  %2d' % (e[i]), end='')
                print('  %14.6g  ' % (q), end='')
                print('  %14.6g  ' % (exact), end='')
                print('  %10.2g  ' % (error))
