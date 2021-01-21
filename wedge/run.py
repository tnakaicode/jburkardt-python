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


class BaseWedge(plot2d):

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
            p = self.unit_sample()
            q = self.unit_sample()
            t[i] = np.abs(p - q)

        bins = 20

        d = np.linspace(0.0, 1.0, 101)
        pdf = 2.0 * (1.0 - d)

        filename = 'line_distance_compare.png'
        self.new_2Dfig()
        self.axs.hist(t, bins=20, rwidth=0.95, density=True)
        self.axs.plot(d, pdf, 'r-', linewidth=2)
        self.axs.set_xlabel('<-- Distance -->')
        self.axs.set_ylabel('<-- Relative frequency -->')
        self.axs.set_title('Compare observed and theoretical PDF')
        self.SavePng_Serial(self.tmpdir + filename)
        print('  Graphics saved as "%s"' % (filename))

    def distance_histogram(self, m, n):

        #
        # line_distance_histogram histograms the data.
        #
        #  Parameters:
        #
        #    Input, integer N, the number of samples to use.
        #

        t = np.zeros(n)
        for i in range(0, n):
            p = self.unit_sample()
            q = self.unit_sample()
            t[i] = np.abs(p - q)

        filename = 'line_distance_histogram.png'
        self.new_2Dfig()
        self.axs.hist(t, bins=20, rwidth=0.95, density=True)
        self.axs.set_xlabel('<-- Distance -->')
        self.axs.set_ylabel('<-- Relative frequency -->')
        self.axs.set_title(
            'Distance between random point pairs in a unit line segment')
        self.SavePng_Serial(self.tmpdir + filename)
        print('  Graphics saved as "%s"' % (filename))

    def distance_pdf(self, m):

        #
        # line_distance_pdf plots the PDF for the line distance problem.
        #
        #  Reference:
        #
        #    Eric Weisstein,
        #    "Line Line Picking."
        #    From MathWorld--A Wolfram Web Resource.,
        #    http://mathworld.wolfram.com/LineLinePicking.html
        #

        d = np.linspace(0.0, 1.0, 101)
        pdf = 2.0 * (1.0 - d)

        filename = 'line_distance_pdf.png'
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
        # line_distance_stats estimates line distance statistics.
        #
        #  Parameters:
        #
        #    Input, integer N, the number of sample points to use.
        #
        #    Output, real MU, VAR, the estimated mean and variance of the
        #    distance between two random points in the unit line segment.
        #

        t = np.zeros(n)
        for i in range(0, n):
            p = self.unit_sample(m)
            q = self.unit_sample(m)
            t[i] = np.abs(p - q)

        mu = np.sum(t) / n
        if (1 < n):
            var = np.sum((t - mu)**2) / (n - 1)
        else:
            var = 0.0

        mu_exact = 1.0 / 3.0
        var_exact = 1.0 / 18.0
        print('')
        print('  Using N = %d sample points.' % (n))
        print('  Estimated mean distance = %g' % (mu))
        print('  Exact mean distance     = %g' % (mu_exact))
        print('  Estimated variance      = %g' % (var))
        print('  Exact variance          = %g' % (var_exact))

    def unit_sample(self):

        #
        # line_unit_sample returns a randomly selected point in the unit line segment.
        #
        #  Parameters:
        #
        #    Output, real P(1,1), a point selected uniformly at random from
        #    the interior of the unit line segment.
        #

        p = np.random.rand()
        return p

    def monomial_integral(self, m, e):

        #
        # LINE01_MONOMIAL_INTEGRAL: monomial integral over the unit line in 1D.
        #
        #  Discussion:
        #
        #    The integration region is
        #
        #      0 <= X <= 1.
        #
        #    The monomial is F(X) = X^E.
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
        #    Input, integer E, the exponent.
        #    E must not equal -1.
        #
        #    Output, real INTEGRAL, the integral.
        #

        if (e == -1):
            print('')
            print('LINE01_MONOMIAL_INTEGRAL - Fatal error!')
            print('  Exponent E = -1 is not allowed!')
            exit('LINE01_MONOMIAL_INTEGRAL - Fatal error!')

        integral = 1.0 / float(e + 1)
        return integral

    def sample(self, m, n, seed):

        #
        # LINE01_SAMPLE samples the unit line in 1D.
        #
        #  Parameters:
        #
        #    Input, integer N, the number of points.
        #
        #    Input/output, integer SEED, a seed for the random
        #    number generator.
        #
        #    Output, real X(N), the points.
        #

        x = np.zeros([1, n])
        x[0, :], seed = r8vec_uniform_01(n, seed)
        return x, seed


if (__name__ == '__main__'):
    timestamp()

    seed = 123456789

    obj = BaseWedge()
    obj.distance_pdf(m=20)
    obj.distance_compare(m=20, n=1000)
    obj.distance_histogram(m=20, n=1000)

    m, n = 1, 4192
    x, seed = obj.sample(m, n, seed)
    print('  Ex  Ey  Ez     MC-Estimate           Exact      Error')
    for test in range(20):
        e = np.zeros(m)
        e[0] = test

        value = monomial_value(1, n, e, x)
        result = 1.0 * np.sum(value) / float(n)
        exact = obj.monomial_integral(m, e)
        error = abs(result - exact)

        for i in range(0, m):
            print('  %2d' % (e[i]), end='')
        print('  %14.6g  ' % (result), end='')
        print('  %14.6g  ' % (exact), end='')
        print('  %10.2g  ' % (error))
