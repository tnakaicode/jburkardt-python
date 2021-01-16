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
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

obj = plot2d()


def ball_distance_compare(n):

    # *****************************************************************************80
    #
    # ball_distance_compare compares observed and theoretical PDF's.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of samples to use.
    #

    t = np.zeros(n)
    d = np.linspace(0.0, 2.0, 101)

    for i in range(0, n):
        p = ball_unit_sample()
        q = ball_unit_sample()
        t[i] = np.linalg.norm(p - q)

    obj.new_2Dfig(aspect="auto")
    filename = 'ball_distance_compare.png'
    obj.axs.hist(t, bins=20, rwidth=0.95, density=True)

    pdf = (3.0 / 16.0) * (d - 2.0)**2 * d**2 * (d + 4.0)
    obj.axs.plot(d, pdf, 'r-', linewidth=2)

    obj.axs.set_xlabel('<-- Distance -->')
    obj.axs.set_ylabel('<-- Relative frequency -->')
    obj.axs.set_title('Compare observed and theoretical PDFs')
    obj.SavePng(filename)
    plt.clf()
    print('  Graphics saved as "%s"' % (filename))


def ball_distance_histogram(n):

    # *****************************************************************************80
    #
    # ball_distance_histogram histograms ball distance statistics.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of samples to use.
    #

    t = np.zeros(n)

    for i in range(0, n):
        p = ball_unit_sample()
        q = ball_unit_sample()
        t[i] = np.linalg.norm(p - q)

    obj.new_2Dfig(aspect="auto")
    filename = 'ball_distance_histogram.png'
    obj.axs.hist(t, bins=20, rwidth=0.95, density=True)
    obj.axs.set_xlabel('<-- Distance -->')
    obj.axs.set_ylabel('<-- Frequency -->')
    obj.axs.set_title(
        'Distance between a pair of random points in a unit ball')
    obj.SavePng(filename)
    plt.clf()
    print('  Graphics saved as "%s"' % (filename))


def ball_distance_pdf():

    # *****************************************************************************80
    #
    # ball_distance_pdf plots the PDF for the ball distance problem.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    d = np.linspace(0.0, 2.0, 101)
    pdf = (3.0 / 16.0) * (d - 2.0)**2 * d**2 * (d + 4.0)

    obj.new_2Dfig(aspect="auto")
    filename = 'ball_distance_pdf.png'
    obj.axs.plot(d, pdf, 'r-', linewidth=2)
    obj.axs.set_xlabel('<-- Distance -->')
    obj.axs.set_ylabel('<-- Probability -->')
    obj.axs.set_title(
        'PDF for distance between pairs of random points in unit ball')
    obj.SavePng(filename)
    plt.clf()
    print('  Graphics saved as "%s"' % (filename))


def ball_distance_stats(n):

    # *****************************************************************************80
    #
    # ball_distance_stats estimates ball distance statistics.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of sample points to use.
    #
    #    Output, real MU, VAR, the estimated mean and variance of the
    #    distance between two random points in the unit ball.
    #

    t = np.zeros(n)
    for i in range(0, n):
        p = ball_unit_sample()
        q = ball_unit_sample()
        t[i] = np.linalg.norm(p - q)

    mu = np.sum(t) / n
    if (1 < n):
        var = np.sum((t - mu) ** 2) / (n - 1)
    else:
        var = 0.0

    mu_exact = 36.0 / 35.0
    print('')
    print('  Using N = %d sample points,' % (n))
    print('  Estimated mean distance = %g' % (mu))
    print('  Exact mean distance     = %g' % (mu_exact))
    print('  Estimated variance      = %g' % (var))

    return mu, var


def ball_distance_test():

    # *****************************************************************************80
    #
    # ball_distance_test tests ball_distance.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 May 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('ball_distance_test:')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test ball_distance.')

    n = 10000
    [mu, var] = ball_distance_stats(n)

    n = 10000
    ball_distance_histogram(n)
    ball_distance_pdf()

    n = 10000
    ball_distance_compare(n)

    print('')
    print('ball_distance_test:')
    print('  Normal end of execution.')


def ball_unit_sample():

    # *****************************************************************************80
    #
    # ball_unit_sample returns sample points in the unit ball.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 May 2019
    #
    #  Author:
    #
    #    John Burkardt
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
    #    Output, real X(3), the point.
    #

    x = np.random.randn(3)

    #
    #  Normalize the vector.
    #
    x = x / np.linalg.norm(x)

    #
    #  Now compute a value to map the point ON the sphere INTO the sphere.
    #
    r = np.random.rand(1)
    x = r ** (1.0 / 3.0) * x

    return x


if (__name__ == '__main__'):
    timestamp()
    ball_distance_test()
    timestamp()
