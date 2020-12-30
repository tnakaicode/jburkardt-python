#! /usr/bin/env python
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


def r8poly_print(m, a, title):

    # *****************************************************************************80
    #
    # R8POLY_PRINT prints out a polynomial.
    #
    #  Discussion:
    #
    #    The power sum form is:
    #
    #      p(x) = a(0) + a(1) * x + ... + a(m-1) * x^(m-1) + a(m) * x^(m)
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 July 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the nominal degree of the polynomial.
    #
    #    Input, real A[0:M], the polynomial coefficients.
    #    A[0] is the constant term and
    #    A[M] is the coefficient of X^M.
    #
    #    Input, string TITLE, a title.
    #
    if (0 < len(title)):
        print('')
        print(title)
    print('')

    if (a[m] < 0.0):
        plus_minus = '-'
    else:
        plus_minus = ' '

    mag = abs(a[m])

    if (2 <= m):
        print('  p(x) = %c %g * x^%d' % (plus_minus, mag, m))
    elif (m == 1):
        print('  p(x) = %c %g * x' % (plus_minus, mag))
    elif (m == 0):
        print('  p(x) = %c %g' % (plus_minus, mag))

    for i in range(m - 1, -1, -1):

        if (a[i] < 0.0):
            plus_minus = '-'
        else:
            plus_minus = '+'

        mag = abs(a[i])

        if (mag != 0.0):

            if (2 <= i):
                print('         %c %g * x^%d' % (plus_minus, mag, i))
            elif (i == 1):
                print('         %c %g * x' % (plus_minus, mag))
            elif (i == 0):
                print('         %c %g' % (plus_minus, mag))


def r8poly_value_horner(m, c, x):

    # *****************************************************************************80
    #
    # R8POLY_VALUE_HORNER evaluates a polynomial using Horner's method.
    #
    #  Discussion:
    #
    #    The polynomial
    #
    #      p(x) = c0 + c1 * x + c2 * x^2 + ... + cm * x^m
    #
    #    is to be evaluated at the value X.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the degree.
    #
    #    Input, real C(0:M), the polynomial coefficients.
    #    C(I) is the coefficient of X^I.
    #
    #    Input, real X, the evaluation point.
    #
    #    Output, real VALUE, the polynomial value.
    #
    value = c[m]
    for i in range(m - 1, -1, -1):
        value = value * x + c[i]

    return value


def r8poly_print_test():

    # *****************************************************************************80
    #
    # R8POLY_PRINT_TEST tests R8POLY_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8POLY_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8POLY_PRINT prints an R8POLY.')

    m = 5
    c = np.array([12.0, -3.4, 56.0, 0.0, 0.78, 9.0])

    r8poly_print(m, c, '  The R8POLY:')

    print('')
    print('R8POLY_PRINT_TEST:')
    print('  Normal end of execution.')


def r8poly_value_horner_test():

    # *****************************************************************************80
    #
    # R8POLY_VALUE_HORNER_TEST tests R8POLY_VALUE_HORNER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    04 March 2016
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 4
    n = 16
    c = np.array([24.0, -50.0, +35.0, -10.0, 1.0])

    print('')
    print('R8POLY_VALUE_HORNER_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8POLY_VALUE_HORNER evaluates a polynomial at a point')
    print('  using Horners method.')

    r8poly_print(m, c, '  The polynomial coefficients:')

    x_lo = 0.0
    x_hi = 5.0
    x = np.linspace(x_lo, x_hi, n)

    print('')
    print('   I    X    P(X)')
    print('')

    for i in range(0, n):
        p = r8poly_value_horner(m, c, x[i])
        print('  %2d  %8.4f  %14.6g' % (i, x[i], p))

    print('')
    print('R8POLY_VALUE_HORNER_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    r8poly_print_test()
    timestamp()
