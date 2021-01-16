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
from r8lib.r8mat_transpose_print import r8mat_transpose_print, r8mat_transpose_print_some

from i4lib.i4vec_print import i4vec_print
from i4lib.i4vec_transpose_print import i4vec_transpose_print
from i4lib.i4vec_uniform_ab import i4vec_uniform_ab

from r8lib.r8_gamma import r8_gamma
from r8lib.r8_normal_01 import r8_normal_01
from r8lib.r8_uniform_01 import r8_uniform_01
from r8lib.r8mat_uniform_ab import r8mat_uniform_ab
from r8lib.r8vec_normal_01 import r8vec_normal_01


def ball01_monomial_integral(e):

    # *****************************************************************************80
    #
    # BALL01_MONOMIAL_INTEGRAL returns monomial integrals in the unit ball.
    #
    #  Discussion:
    #
    #    The integration region is
    #
    #      X^2 + Y^2 + Z^2 <= 1.
    #
    #    The monomial is F(X,Y,Z) = X^E(1) * Y^E(2) * Z^E(3).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
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
    #    Input, integer E(3), the exponents of X, Y and Z in the
    #    monomial.  Each exponent must be nonnegative.
    #
    #    Output, real INTEGRAL, the integral.
    #

    if (e[0] < 0 or e[1] < 0 or e[2] < 0):
        print('')
        print('BALL01_MONOMIAL_INTEGRAL - Fatal error!')
        print('  All exponents must be nonnegative.')
        exit('BALL01_MONOMIAL_INTEGRAL - Fatal error!')
    
    #
    #  Integrate over the surface.
    #
    if (e[0] == 0 and e[1] == 0 and e[2] == 0):

        integral = 2.0 * np.sqrt(np.pi ** 3) / r8_gamma(1.5)

    elif ((e[0] % 2) == 1 or (e[1] % 2) == 1 or (e[2] % 2) == 1):

        integral = 0.0

    else:

        integral = 2.0

        for i in range(0, 3):
            integral = integral * r8_gamma(0.5 * float(e[i] + 1))

        integral = integral / r8_gamma(0.5 * float(e[0] + e[1] + e[2] + 3))
    
    #
    #  The surface integral is now adjusted to give the volume integral.
    #
    r = 1.0
    s = e[0] + e[1] + e[2] + 3

    integral = integral * r ** s / float(s)

    return integral


def ball01_monomial_integral_test():

    # *****************************************************************************80
    #
    # % BALL01_MONOMIAL_INTEGRAL_TEST tests BALL01_MONOMIAL_INTEGRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 3
    n = 4192
    test_num = 20

    print('')
    print('BALL01_MONOMIAL_INTEGRAL_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  BALL01_MONOMIAL_INTEGRAL returns the integral of a monomial')
    print('  over the interior of the unit ball in 3D.')
    print('  Compate against Monte Carlo estimates.')
    
    #
    #  Get sample points.
    #
    seed = 123456789
    x, seed = ball01_sample(n, seed)

    print('')
    print('  Number of sample points used is %d' % (n))
    
    #
    #  Randomly choose X,Y exponents between 0 and 8.
    #
    print('')
    print('  If any exponent is odd, the integral is zero.')
    print('  We will restrict this test to randomly chosen even exponents.')
    print('')
    print('  Ex  Ey  Ez     MC-Estimate           Exact      Error')
    print('')

    for test in range(0, test_num):

        e, seed = i4vec_uniform_ab(m, 0, 4, seed)

        for i in range(0, 3):
            e[i] = e[i] * 2

        value = monomial_value(m, n, e, x)

        result = ball01_volume() * np.sum(value) / float(n)
        exact = ball01_monomial_integral(e)
        error = abs(result - exact)

        print('  %2d  %2d  %2d  %14.6g  %14.6g  %10.2e'
              % (e[0], e[1], e[1], result, exact, error))

    print('')
    print('BALL01_MONOMIAL_INTEGRAL_TEST')
    print('  Normal end of execution.')


def ball01_sample(n, seed):

    # *****************************************************************************80
    #
    # BALL01_SAMPLE uniformly samples the unit ball.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
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

    x = np.zeros([3, n])

    for j in range(0, n):
        #
        #  Fill a vector with normally distributed values.
        #
        v, seed = r8vec_normal_01(3, seed)
        
        #
        #  Compute the length of the vector.
        #
        norm = np.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
        
        #
        #  Normalize the vector.
        #
        for i in range(0, 3):
            v[i] = v[i] / norm
        
        #
        #  Transfer the point from the surface to the interior.
        #
        r, seed = r8_uniform_01(seed)

        r = r ** (1.0 / 3.0)
        for i in range(0, 3):
            x[i, j] = r * v[i]

    return x, seed


def ball01_sample_test():

    # *****************************************************************************80
    #
    # BALL01_SAMPLE_TEST tests BALL01_SAMPLE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('BALL01_SAMPLE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  BALL01_SAMPLE samples the unit ball.')

    n = 10
    seed = 123456789
    x, seed = ball01_sample(n, seed)
    r8mat_transpose_print(3, n, x, '  Sample points in the unit ball.')

    print('')
    print('BALL01_SAMPLE_TEST')
    print('  Normal end of execution.')


def ball01_volume():

    # *****************************************************************************80
    #
    # BALL01_VOLUME returns the volume of the unit ball.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Output, real VALUE, the volume of the unit ball.
    #

    r = 1.0
    value = 4.0 * np.pi * r ** 3 / 3.0

    return value


def ball01_volume_test():

    # *****************************************************************************80
    #
    # BALL01_VOLUME_TEST tests BALL01_VOLUME.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BALL01_VOLUME_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  BALL01_VOLUME returns the volume of the unit ball.')

    value = ball01_volume()

    print('')
    print('  BALL01_VOLUME() = %g' % (value))
    print('')
    print('BALL01_VOLUME_TEST')
    print('  Normal end of execution.')


def ball_integrals_test():

    # *****************************************************************************80
    #
    # BALL_INTEGRALS_TEST tests the BALL_INTEGRALS library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('BALL_INTEGRALS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the BALL_INTEGRALS library.')

    gamma_values_test()

    ball01_monomial_integral_test()
    ball01_sample_test()
    ball01_volume_test()
    monomial_value_test()

    print('')
    print('BALL_INTEGRALS_TEST:')
    print('  Normal end of execution.')
    print('')


def gamma_values(n_data):

    # *****************************************************************************80
    #
    # GAMMA_VALUES returns some values of the Gamma function.
    #
    #  Discussion:
    #
    #    The Gamma function is defined as:
    #
    #      Gamma(Z) = Integral ( 0 <= T < Infinity) T^(Z-1) exp(-T) dT
    #
    #    It satisfies the recursion:
    #
    #      Gamma(X+1) = X * Gamma(X)
    #
    #    Gamma is undefined for nonpositive integral X.
    #    Gamma(0.5) = sqrt(PI)
    #    For N a positive integer, Gamma(N+1) = N!, the standard factorial.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      Gamma[x]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 July 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Milton Abramowitz, Irene Stegun,
    #    Handbook of Mathematical Functions,
    #    US Department of Commerce, 1964.
    #
    #    Stephen Wolfram,
    #    The Mathematica Book,
    #    Fourth Edition,
    #    Wolfram Media / Cambridge University Press, 1999.
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, real X, the argument of the function.
    #
    #    Output, real FX, the value of the function.
    #
    import numpy as np

    n_max = 25

    fx_vec = np.array((
        -0.3544907701811032E+01,
        -0.1005871979644108E+03,
        0.9943258511915060E+02,
        0.9513507698668732E+01,
        0.4590843711998803E+01,
        0.2218159543757688E+01,
        0.1772453850905516E+01,
        0.1489192248812817E+01,
        0.1164229713725303E+01,
        0.1000000000000000E+01,
        0.9513507698668732E+00,
        0.9181687423997606E+00,
        0.8974706963062772E+00,
        0.8872638175030753E+00,
        0.8862269254527580E+00,
        0.8935153492876903E+00,
        0.9086387328532904E+00,
        0.9313837709802427E+00,
        0.9617658319073874E+00,
        0.1000000000000000E+01,
        0.2000000000000000E+01,
        0.6000000000000000E+01,
        0.3628800000000000E+06,
        0.1216451004088320E+18,
        0.8841761993739702E+31))

    x_vec = np.array((
        -0.50E+00,
        -0.01E+00,
        0.01E+00,
        0.10E+00,
        0.20E+00,
        0.40E+00,
        0.50E+00,
        0.60E+00,
        0.80E+00,
        1.00E+00,
        1.10E+00,
        1.20E+00,
        1.30E+00,
        1.40E+00,
        1.50E+00,
        1.60E+00,
        1.70E+00,
        1.80E+00,
        1.90E+00,
        2.00E+00,
        3.00E+00,
        4.00E+00,
        10.00E+00,
        20.00E+00,
        30.00E+00))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        x = 0.0
        fx = 0.0
    else:
        x = x_vec[n_data]
        fx = fx_vec[n_data]
        n_data = n_data + 1

    return n_data, x, fx


def gamma_values_test():

    # *****************************************************************************80
    #
    # GAMMA_VALUE_TEST demonstrates the use of GAMMA_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 February 2009
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('GAMMA_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  GAMMA_VALUES stores values of the Gamma function.')
    print('')
    print('      X            GAMMA(X)')
    print('')

    n_data = 0

    while (True):

        n_data, x, fx = gamma_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %24.16f' % (x, fx))
    print('')
    print('GAMMA_VALUES_TEST:')
    print('  Normal end of execution.')


def monomial_value(m, n, e, x):

    # *****************************************************************************80
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
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2015
    #
    #  Author:
    #
    #    John Burkardt
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


def monomial_value_test():

    # *****************************************************************************80
    #
    # MONOMIAL_VALUE_TEST tests MONOMIAL_VALUE on sets of data in various dimensions.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('MONOMIAL_VALUE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Use monomial_value() to evaluate some monomials')
    print('  in dimensions 1 through 3.')

    e_min = -3
    e_max = 6
    n = 5
    seed = 123456789
    x_min = -2.0
    x_max = +10.0

    for m in range(1, 4):

        print('')
        print('  Spatial dimension M =  %d' % (m))

        e, seed = i4vec_uniform_ab(m, e_min, e_max, seed)
        i4vec_transpose_print(m, e, '  Exponents:')
        x, seed = r8mat_uniform_ab(m, n, x_min, x_max, seed)
        #
        #  To make checking easier, make the X values integers.
        #
        for i in range(0, m):
            for j in range(0, n):
                x[i, j] = round(x[i, j])

        v = monomial_value(m, n, e, x)

        print('')
        print('   V(X)         ', end='')
        for i in range(0, m):
            print('      X(%d)' % (i), end='')
        print('')
        print('')
        for j in range(0, n):
            print('%14.6g  ' % (v[j]), end='')
            for i in range(0, m):
                print('%10.4f' % (x[i, j]), end='')
            print('')

    print('')
    print('MONOMIAL_VALUE_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    ball_integrals_test()
    timestamp()
