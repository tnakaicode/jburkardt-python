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


class HyperCube(plot2d):

    def __init__(self):
        plot2d.__init__(self, aspect="equal")

    def monomial_integral(self, m, e):

        #
        # HYPERCUBE01_MONOMIAL_INTEGRAL: integrals over the unit hypercube in M dimensions.
        #
        #  Discussion:
        #
        #    The integration region is
        #
        #      0 <= X(1:M) <= 1,
        #
        #    The monomial is F(X) = product ( 1 <= I <= M ) X(I)^E(I).
        #
        #  Reference:
        #
        #    Philip Davis, Philip Rabinowitz,
        #    Methods of Numerical Integration,
        #    Second Edition,
        #    Academic Press, 1984, page 263.
        #
        #  Parameters:
        #
        #    Input, integer M, the spatial dimension.
        #
        #    Input, integer E(M), the exponents.  Each exponent must be nonnegative.
        #
        #    Output, real INTEGRAL, the integral.
        #

        for i in range(0, m):
            if (e[i] < 0):
                print('')
                print('HYPERCUBE01_MONOMIAL_INTEGRAL - Fatal error!')
                print('  All exponents must be nonnegative.')
                exit()

        integral = 1.0
        for i in range(0, m):
            integral = integral / float(e[i] + 1)

        return integral

    def sample(self, m, n, seed):

        #
        # HYPERCUBE01_SAMPLE samples points in the unit hypercube in M dimensions.
        #
        #  Parameters:
        #
        #    Input, integer M, the spatial dimension.
        #
        #    Input, integer N, the number of points.
        #
        #    Input/output, integer SEED, a seed for the random
        #    number generator.
        #
        #    Output, real X(M,N), the points.
        #
        x, seed = r8mat_uniform_01(m, n, seed)

        return x, seed


if (__name__ == '__main__'):
    timestamp()

    seed = 123456789

    obj = HyperCube()

    m, n = 3, 4192
    x, seed = obj.sample(m, n, seed)
    print('  Ex  Ey  Ez     MC-Estimate           Exact      Error')
    for test in range(20):
        e, seed = i4vec_uniform_ab(m, 0, 4, seed)

        for i in range(m):
            e[i] = e[i] * 2

        value = monomial_value(m, n, e, x)
        result = 1.0 * np.sum(value) / float(n)
        exact = obj.monomial_integral(m, e)
        error = abs(result - exact)

        for i in range(0, m):
            print('  %2d' % (e[i]), end='')
        print('  %14.6g  ' % (result), end='')
        print('  %14.6g  ' % (exact), end='')
        print('  %10.2g  ' % (error))
