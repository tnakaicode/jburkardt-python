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


def hypersphere_distance_stats(m, n):

    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Input, integer N, the number of sample points to use.
    #
    #    Output, real MU, VAR, the estimated mean and variance of the
    #       distance between two random points on the unit sphere.
    #

    t = np.zeros(n)
    for i in range(0, n):
        p = hypersphere_unit_sample(m)
        q = hypersphere_unit_sample(m)
        t[i] = np.linalg.norm(p - q)

    mu = np.sum(t) / n
    if (1 < n):
        var = np.sum((t - mu)**2) / (n - 1)
    else:
        var = 0.0

    mu_exact = np.sqrt(2.0)
    var_exact = 2.0 - 2.0**(2 * m - 2) * gamma(m / 2)**4 / np.pi \
        / gamma(m - 0.5)**2
    print('')
    print('  Using M = %d spatial dimension' % (m))
    print('  Using N = %d sample points,' % (n))
    print('  Estimated mean distance = %g' % (mu))
    print('  Exact mean distance     = %g' % (mu_exact))
    print('  Estimated variance      = %g' % (var))
    print('  Exact variance          = %g' % (var_exact))
    return mu, var


def hypersphere_unit_sample(m):

    #
    # hypersphere_unit_sample returns sample points on the unit hypersphere.
    #
    #  Reference:
    #
    #    Russell Cheng,
    #    Random Variate Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998, pages 168.
    #
    #    Reuven Rubinstein,
    #    Monte Carlo Optimization, Simulation, and Sensitivity
    #    of Queueing Networks,
    #    Wiley, 1986, page 232.
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #
    #    Output, real X(M,1), the point.
    #

    x = np.random.randn(m)
    x = x / np.linalg.norm(x)
    return x


class HyperBall(plot2d):

    def __init__(self):
        plot2d.__init__(self, aspect="equal")

    def volume(self, m):

        #
        # HYPERBALL01_VOLUME returns the volume of the unit hyperball in M dimensions.
        #
        #  Discussion:
        #
        #     M  Volume
        #
        #     1    2
        #     2    1        * PI
        #     3  ( 4 /   3) * PI
        #     4  ( 1 /   2) * PI^2
        #     5  ( 8 /  15) * PI^2
        #     6  ( 1 /   6) * PI^3
        #     7  (16 / 105) * PI^3
        #     8  ( 1 /  24) * PI^4
        #     9  (32 / 945) * PI^4
        #    10  ( 1 / 120) * PI^5
        #
        #  Parameters:
        #
        #    Input, integer M, the spatial dimension.
        #
        #    Output, real VOLUME, the volume of the unit ball.
        #

        if ( ( m % 2 ) == 0 ):
            m_half = ( m // 2 );
            volume = np.pi ** m_half
            for i in range ( 1, m_half + 1 ):
                volume = volume / float ( i )
        else:
            m_half = ( ( m - 1 ) // 2 )
            volume = np.pi ** m_half * 2.0 ** m
            for i in range ( m_half + 1, 2 * m_half + 2 ):
                volume = volume / float ( i )

        return volume

    def monomial_integral(self, m, e):

        #
        # HYPERBALL01_MONOMIAL_INTEGRAL: integrals in unit hyperball in M dimensions.
        #
        #  Discussion:
        #
        #    The integration region is
        #
        #      sum ( 1 <= I <= M ) X(I)^2 <= 1.
        #
        #    The monomial is F(X) = product ( 1 <= I <= M ) X(I)^E(I)
        #
        #  Reference:
        #
        #    Gerald Folland,
        #    How to Integrate a Polynomial Over a Sphere,
        #    American Mathematical Monthly,
        #    Volume 108, Number 5, May 2001, pages 446-448.
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
                print('HYPERBALL01_MONOMIAL_INTEGRAL - Fatal error!')
                print('  All exponents must be nonnegative.')
                exit()
        #
        #  Integrate over the surface.
        #
        for i in range(0, m):
            if ((e[i] % 2) == 1):
                integral = 0.0
                return integral

        integral = 2.0

        for i in range(0, m):
            integral = integral * gamma(0.5 * float(e[i] + 1))

        s = 0
        for i in range(0, m):
            s = s + e[i] + 1

        integral = integral / gamma(0.5 * float(s))
        #
        #  The surface integral is now adjusted to give the volume integral.
        #

        r = 1.0
        integral = integral * r ** s / float(s)

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

    obj = HyperBall()

    m, n = 3, 4192
    x, seed = obj.sample(m, n, seed)
    print('  Ex  Ey  Ez     MC-Estimate           Exact      Error')
    for test in range(20):
        e, seed = i4vec_uniform_ab(m, 0, 4, seed)

        for i in range(m):
            e[i] = e[i] * 2

        value = monomial_value(m, n, e, x)
        result = obj.volume(m) * np.sum(value) / float(n)
        exact = obj.monomial_integral(m, e)
        error = abs(result - exact)

        for i in range(0, m):
            print('  %2d' % (e[i]), end='')
        print('  %14.6g  ' % (result), end='')
        print('  %14.6g  ' % (exact), end='')
        print('  %10.2g  ' % (error))
