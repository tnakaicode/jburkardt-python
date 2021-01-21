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


class BaseLine(plot2d):

    def __init__(self):
        plot2d.__init__(self, aspect="equal")

    def distance_compare(self, m, n):
        #
        # line_distance_compare compares the observed and theoretical PDF's.
        #
        #  Parameters:
        #
        #    Input, integer N, the number of samples to use.
        #

        t = np.zeros(n)
        for i in range(0, n):
            p = line_unit_sample()
            q = line_unit_sample()
            t[i] = np.abs(p - q)

        bins = 20
        plt.hist(t, bins=20, rwidth=0.95, density=True)

        d = np.linspace(0.0, 1.0, 101)
        pdf = 2.0 * (1.0 - d)
        plt.plot(d, pdf, 'r-', linewidth=2)

        plt.grid(True)
        plt.xlabel('<-- Distance -->')
        plt.ylabel('<-- Relative frequency -->')
        plt.title('Compare observed and theoretical PDF')
        filename = 'line_distance_compare.png'
        plt.savefig(filename)
        print('  Graphics saved as "%s"' % (filename))

    def distance_histogram(self, m, n):

        #
        #  Parameters:
        #
        #    Input, integer M, the spatial dimension.
        #
        #    Input, integer N, the number of samples to use.
        #

        filename = 'hypersphere_distance_histogram.png'
        t = np.zeros(n)
        for i in range(0, n):
            p = self.unit_sample(m)
            q = self.unit_sample(m)
            t[i] = np.linalg.norm(p - q)

        self.new_2Dfig()
        self.axs.hist(t, bins=20, rwidth=0.95, density=True)
        self.axs.set_xlabel('<-- Distance -->')
        self.axs.set_ylabel('<-- Frequency -->')
        self.axs.set_title(
            'Distance between a pair of random points on a unit hypersphere')
        self.SavePng_Serial(self.tmpdir + filename)
        print('  Graphics saved as "%s"' % (filename))

    def distance_pdf(self, m):

        #
        # hypersphere_distance_pdf plots the PDF for the hypersphere distance problem.
        #
        #  Reference:
        #
        #    Panagiotis Siridopoulos,
        #    The N-Sphere Chord Length Distribution,
        #    ARXIV,
        #    https://arxiv.org/pdf/1411.5639.pdf
        #
        #  Parameters:
        #
        #    Input, integer M, the spatial dimension.
        #

        filename = 'hypersphere_distance_pdf.png'
        d = np.linspace(0.0, 2.0, 101)
        pdf = d / beta((m - 1) / 2, 0.5) * \
            (d**2 - 0.25 * d**4) ** ((m - 3) / 2)

        self.new_2Dfig()
        self.axs.plot(d, pdf, 'r-', linewidth=2)
        self.axs.set_xlabel('<-- Distance -->')
        self.axs.set_ylabel('<-- Probability -->')
        self.axs.set_title(
            'PDF for pairwise distance of random points on unit hypersphere')
        self.SavePng_Serial(self.tmpdir + filename)
        print('  Graphics saved as "%s"' % (filename))

    def distance_stats(self, m, n):

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
            p = self.unit_sample(m)
            q = self.unit_sample(m)
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

    def unit_sample(self, m):

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

    def area(self, m):

        #
        # HYPERSPHERE01_AREA returns the surface area of the unit hypersphere.
        #
        #  Discussion:
        #
        #     M   Area
        #
        #     2    2        * PI
        #     3    4        * PI
        #     4  ( 2 /   1) * PI^2
        #     5  ( 8 /   3) * PI^2
        #     6  ( 1 /   1) * PI^3
        #     7  (16 /  15) * PI^3
        #     8  ( 1 /   3) * PI^4
        #     9  (32 / 105) * PI^4
        #    10  ( 1 /  12) * PI^5
        #
        #  Parameters:
        #
        #    Input, integer M, the spatial dimension.
        #
        #    Output, real VALUE, the area of the unit hypersphere.
        #

        if ((m % 2) == 0):
            m_half = (m // 2)
            value = 2.0 * np.pi ** m_half
            for i in range(1, m_half):
                value = value / float(i)
        else:
            m_half = ((m - 1) // 2)
            value = np.pi ** m_half * 2.0 ** m
            for i in range(m_half + 1, 2 * m_half + 1):
                value = value / float(i)

        return value

    def monomial_integral(self, m, e):

        #
        # HYPERSPHERE01_MONOMIAL_INTEGRAL: monomial integrals on the unit hypersphere.
        #
        #  Discussion:
        #
        #    The integration region is
        #
        #      sum ( 1 <= I <= M ) X(I)^2 = 1.
        #
        #    The monomial is F(X) = product ( 1 <= I <= M ) X(I)^E(I)
        #
        #  Parameters:
        #
        #    Input, integer M, the spatial dimension.
        #
        #    Input, integer E(M), the exponents of X(1) through X(M).
        #    Each exponent must be nonnegative.
        #
        #    Output, real INTEGRAL, the integral.
        #

        for i in range(0, m):
            if (e[i] < 0):
                print('')
                print('HYPERSPHERE01_MONOMIAL_INTEGRAL - Fatal error!')
                print('  All exponents must be nonnegative.')
                exit()
        for i in range(0, m):
            if ((e[i] % 2) == 1):
                integral = 0.0
                return integral

        integral = 2.0

        for i in range(0, m):
            arg = 0.5 * float(e[i] + 1)
            integral = integral * gamma(arg)

        s = 0
        for i in range(0, m):
            s = s + float(e[i] + 1)

        arg = 0.5 * float(s)
        integral = integral / gamma(arg)

        return integral

    def sample(self, m, n, seed):

        #
        # HYPERSPHERE01_SAMPLE uniformly samples the surface of the unit hypersphere.
        #
        #  Licensing:
        #
        #    This code is distributed under the GNU LGPL license.
        #
        #  Modified:
        #
        #    22 June 2015
        #
        #  Author:
        #
        #    John Burkardt
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

        x = np.zeros([m, n])

        for j in range(0, n):
            #  Fill a vector with normally distributed values.
            v, seed = r8vec_normal_01(m, seed)

            # Compute the length of the vector.
            norm = r8vec_norm(m, v)

            #  Normalize the vector.
            for i in range(0, m):
                x[i, j] = v[i] / norm

        return x, seed


if (__name__ == '__main__'):
    timestamp()

    seed = 123456789

    obj = BaseLine()
    obj.distance_pdf(m=20)
    obj.distance_compare(m=20, n=1000)
    obj.distance_histogram(m=20, n=1000)

    print('   M  Area')
    for m in range(5, 11):
        val = obj.area(m)
        print("{:d}\t{:.3f}".format(m, val))

    m, n = 3, 4192
    x, seed = obj.sample(m, n, seed)
    print('  Ex  Ey  Ez     MC-Estimate           Exact      Error')
    for test in range(20):
        e, seed = i4vec_uniform_ab(m, 0, 4, seed)

        for i in range(m):
            e[i] = e[i] * 2

        value = monomial_value(m, n, e, x)
        result = obj.area(m) * np.sum(value) / float(n)
        exact = obj.monomial_integral(m, e)
        error = abs(result - exact)

        for i in range(0, m):
            print('  %2d' % (e[i]), end='')
        print('  %14.6g  ' % (result), end='')
        print('  %14.6g  ' % (exact), end='')
        print('  %10.2g  ' % (error))
