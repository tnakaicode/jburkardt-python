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
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write


def llsq0(n, x, y):

    # *****************************************************************************80
    #
    # LLSQ0 solves a linear least squares problem matching a line y=a*x to data.
    #
    #  Discussion:
    #
    #    A formula for a line of the form Y = A * X is sought, which
    #    will minimize the root-mean-square error to N data points ( X(I), Y(I) );
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2019
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data values.
    #
    #    Input, real X(N), Y(N), the coordinates of the data points.
    #
    #    Output, real A, the slope of the
    #    least-squares approximant to the data.
    #

    #
    #  Special case.
    #
    if (n == 1):

        if (x[0] == 0):
            a = 1.0
        else:
            a = y[0] / x[0]

    #
    #  Average X and Y.
    #
    else:

        top = np.dot(x.transpose(), y)
        bot = np.dot(x.transpose(), x)

        a = top / bot

    return a


def llsq(n, x, y):

    # *****************************************************************************80
    #
    # LLSQ solves a linear least squares problem matching a line to data.
    #
    #  Discussion:
    #
    #    A formula for a line of the form Y = A * X + B is sought, which
    #    will minimize the root-mean-square error to N data points ( X(I), Y(I) );
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of data values.
    #
    #    Input, real X(N), Y(N), the coordinates of the data points.
    #
    #    Output, real A, B, the slope and Y-intercept of the
    #    least-squares approximant to the data.
    #

    #
    #  Special case.
    #
    if (n == 1):

        a = 0.0
        b = y[0]

    #
    #  Average X and Y.
    #
    else:

        xbar = np.sum(x[0:n]) / float(n)
        ybar = np.sum(y[0:n]) / float(n)

        #
        #  Compute Beta.
        #
        xb = x - xbar
        yb = y - ybar

        top = np.dot(xb.transpose(), yb)
        bot = np.dot(xb.transpose(), xb)

        a = top / bot
        b = ybar - a * xbar

    return a, b


def llsq_test01():

    # *****************************************************************************80
    #
    # LLSQ_TEST01 calls LLSQ to match 15 data values.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 15

    x = np.array([
        1.47, 1.50, 1.52, 1.55, 1.57,
        1.60, 1.63, 1.65, 1.68, 1.70,
        1.73, 1.75, 1.78, 1.80, 1.83])

    y = np.array([
        52.21, 53.12, 54.48, 55.84, 57.20,
        58.57, 59.93, 61.29, 63.11, 64.47,
        66.28, 68.10, 69.92, 72.19, 74.46])

    print('')
    print('LLSQ_TEST01')
    print('  Python version: %s' % (platform.python_version()))
    print('  LLSQ can compute the formula for a line of the form')
    print('    y = A * x + B')
    print('  which minimizes the RMS error to a set of N data values.')

    a, b = llsq(n, x, y)

    print('')
    print('  Estimated relationship is y = %g * x + %g' % (a, b))
    print('  Expected value is         y = 61.272 * x - 39.062')
    print('')
    print('     I      X       Y        B+A*X      |error|')
    print('')

    error = 0.0

    for i in range(0, n):

        print('  %4d  %7f  %7f  %7f  %7f'
              % (i, x[i], y[i], b + a * x[i], b + a * x[i] - y[i]))

        error = error + (b + a * x[i] - y[i]) ** 2

    error = np.sqrt(error / float(n))

    print('')
    print('  RMS error =                           %g' % (error))
    print('')
    print('LLSQ_TEST01')
    print('  Normal end of execution.')


def llsq_test02():

    # *****************************************************************************80
    #
    # LLSQ_TEST02 calls LLSQ0 to match 14 data values.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2019
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 14

    x = np.array([
        0.00, 0.10, 0.15, 0.20, 0.25,
        0.30, 0.35, 0.40, 0.45, 0.50,
        0.55, 0.60, 0.65, 0.7])

    y = np.array([
        0.0000, 0.0865, 0.1015, 0.1106, 0.1279,
        0.1892, 0.2695, 0.2888, 0.2425, 0.3465,
        0.3225, 0.3764, 0.4263, 0.4562])

    print('')
    print('LLSQ_TEST02')
    print('  Python version: %s' % (platform.python_version()))
    print('  LLSQ can compute the formula for a line of the form')
    print('    y = A * x ')
    print('  which minimizes the RMS error to a set of N data values.')

    a = llsq0(n, x, y)

    print('')
    print('  Estimated relationship is y = %g * x' % (a))
    print('')
    print('     I      X       Y          A*X      |error|')
    print('')

    error = 0.0

    for i in range(0, n):

        print('  %4d  %7f  %7f  %7f  %7f'
              % (i, x[i], y[i], a * x[i], a * x[i] - y[i]))

        error = error + (a * x[i] - y[i]) ** 2

    error = np.sqrt(error / float(n))

    print('')
    print('  RMS error =                           %g' % (error))
    print('')
    print('LLSQ_TEST02')
    print('  Normal end of execution.')


def llsq_test():

    # *****************************************************************************80
    #
    # LLSQ_TEST tests LLSQ.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    29 August 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LLSQ_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test LLSQ.')

    llsq_test01()
    llsq_test02()

    print('')
    print('LLSQ_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    llsq_test()
    timestamp()
