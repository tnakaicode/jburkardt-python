#! /usr/bin/env python3
#
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.append(os.path.join('../'))
from base import plot2d

obj = plot2d()


def circle01_length():

    # *****************************************************************************80
    #
    # CIRCLE01_LENGTH: length of the circumference of the unit circle in 2D.
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
    #    Output, real VALUE, the length.
    #
    import numpy as np

    r = 1.0
    value = 2.0 * np.pi * r

    return value


def circle01_length_test():

    # *****************************************************************************80
    #
    # CIRCLE01_LENGTH tests CIRCLE01_LENGTH.
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
    print('CIRCLE01_LENGTH_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CIRCLE01_LENGTH returns the length of the unit circle.')

    value = circle01_length()

    print('')
    print('  CIRCLE01_LENGTH() = %g' % (value))
#
#  Terminate.
#
    print('')
    print('CIRCLE01_LENGTH_TEST')
    print('  Normal end of execution.')
    return


def circle01_monomial_integral(e):

    # *****************************************************************************80
    #
    # CIRCLE01_MONOMIAL_INTEGRAL: integrals on circumference of unit circle in 2D.
    #
    #  Discussion:
    #
    #    The integration region is
    #
    #      X^2 + Y^2 = 1.
    #
    #    The monomial is F(X,Y) = X^E(1) * Y^E(2).
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
    #    Philip Davis, Philip Rabinowitz,
    #    Methods of Numerical Integration,
    #    Second Edition,
    #    Academic Press, 1984, page 263.
    #
    #  Parameters:
    #
    #    Input, integer E(2), the exponents of X and Y in the
    #    monomial.  Each exponent must be nonnegative.
    #
    #    Output, real INTEGRAL, the integral.
    #
    from sys import exit

    if (e[0] < 0 or e[1] < 0):
        print('')
        print('CIRCLE01_MONOMIAL_INTEGRAL - Fatal error!')
        print('  All exponents must be nonnegative.')
        exit('CIRCLE01_MONOMIAL_INTEGRAL - Fatal error!')

    if (((e[0] % 2) == 1) or ((e[1] % 2) == 1)):

        integral = 0.0

    else:

        integral = 2.0

        for i in range(0, 2):
            integral = integral * r8_gamma(0.5 * float(e[i] + 1))

        integral = integral / r8_gamma(0.5 * float(e[0] + e[1] + 2))

    return integral


def circle01_monomial_integral_test():

    # *****************************************************************************80
    #
    # CIRCLE01_MONOMIAL_INTEGRAL_TEST tests CIRCLE01_MONOMIAL_INTEGRAL
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
    import numpy as np
    import platform

    m = 2
    n = 4192
    test_num = 20

    print('')
    print('CIRCLE01_MONOMIAL_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CIRCLE01_MONOMIAL_INTEGRAL returns the value of the')
    print('  integral of a monomial over the unit circle in 2D.')
    print('  Compare with a Monte Carlo estimate.')
#
#  Get sample points.
#
    seed = 123456789
    x, seed = circle01_sample_random(n, seed)

    print('')
    print('  Number of sample points used is %d' % (n))
#
#  Randomly choose X, Y exponents.
#
    print('')
    print('  If any exponent is odd, the integral is zero.')
    print('  We restrict this test to randomly chosen even exponents.')
    print('')
    print('  Ex  Ey     MC-Estimate           Exact      Error')
    print('')

    for test in range(0, test_num):

        e, seed = i4vec_uniform_ab(m, 0, 5, seed)

        e[0] = e[0] * 2
        e[1] = e[1] * 2

        value = monomial_value(m, n, e, x)

        result = circle01_length() * np.sum(value) / float(n)
        exact = circle01_monomial_integral(e)
        error = abs(result - exact)

        print('  %2d  %2d  %14.6g  %14.6g  %10.2g'
              % (e[0], e[1], result, exact, error))
#
#  Terminate.
#
    print('')
    print('CIRCLE01_MONOMIAL_INTEGRAL_TEST')
    print('  Normal end of execution.')
    return


def circle01_sample_ergodic(n, angle):

    # *****************************************************************************80
    #
    # CIRCLE01_SAMPLE_ERGODIC samples points on the circumference of the unit circle in 2D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 June 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of points.
    #
    #    Input/output, real ANGLE, an angle between 0 and 2 PI.
    #
    #    Output, real X(2,N), the points.
    #
    import numpy as np

    r = 1.0
    c = np.zeros(2)

    golden_ratio = (1.0 + np.sqrt(5.0)) / 2.0

    golden_angle = 2.0 * np.pi / golden_ratio ** 2

    x = np.zeros([2, n])

    for j in range(0, n):
        x[0, j] = c[0] + r * np.cos(angle)
        x[1, j] = c[1] + r * np.sin(angle)
        angle = np.mod(angle + golden_angle, 2.0 * np.pi)

    return x, angle


def circle01_sample_ergodic_test():

    # *****************************************************************************80
    #
    # CIRCLE01_SAMPLE_ERGODIC_TEST tests CIRCLE01_SAMPLE_ERGODIC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 June 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    import numpy as np

    e = np.zeros(2)
    e_test = np.array([
        [0, 0],
        [2, 0],
        [0, 2],
        [4, 0],
        [2, 2],
        [0, 4],
        [6, 0]])

    print('')
    print('CIRCLE01_SAMPLE_ERGODIC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CIRCLE01_SAMPLE_ERGODIC ergodically samples the unit circle.')
    print('  Use it to estimate integrals.')

    print('')
    print('         N        1              X^2             Y^2             X^4           X^2Y^2          Y^4          X^6')
    print('')

    n = 1
    while (n <= 65536):
        angle = 0.0
        x, angle = circle01_sample_ergodic(n, angle)
        print('  %8d' % (n), end='')
        for i in range(0, 7):
            for j in range(0, 2):
                e[j] = e_test[i, j]
            value = monomial_value(2, n, e, x)
            result = circle01_length() * np.sum(value) / float(n)
            print('  %14.10g' % (result), end='')

        print('')
        obj.axs.scatter(*x, s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.SavePng_Serial()
        plt.close()
        obj.new_fig()

        n = 2 * n

    print('')
    print('     Exact', end='')
    for i in range(0, 7):
        for j in range(0, 2):
            e[j] = e_test[i, j]
        exact = circle01_monomial_integral(e)
        print('  %14.10g' % (exact), end='')
    print('')
#
#  Terminate.
#
    print('')
    print('CIRCLE01_SAMPLE_ERGODIC_TEST')
    print('  Normal end of execution.')
    return


def circle01_sample_random(n, seed):

    # *****************************************************************************80
    #
    # CIRCLE01_SAMPLE_RANDOM samples points on the circumference of the unit circle in 2D.
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
    #    Output, real X(2,N), the points.
    #
    import numpy as np

    r = 1.0
    c = np.zeros(2)

    theta, seed = r8vec_uniform_01(n, seed)

    x = np.zeros([2, n])

    for j in range(0, n):
        x[0, j] = c[0] + r * np.cos(2.0 * np.pi * theta[j])
        x[1, j] = c[1] + r * np.sin(2.0 * np.pi * theta[j])

    return x, seed


def circle01_sample_random_test():

    # *****************************************************************************80
    #
    # CIRCLE01_SAMPLE_RANDOM_TEST tests CIRCLE01_SAMPLE_RANDOM.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 June 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    import numpy as np

    e = np.zeros(2)
    e_test = np.array([
        [0, 0],
        [2, 0],
        [0, 2],
        [4, 0],
        [2, 2],
        [0, 4],
        [6, 0]])

    print('')
    print('CIRCLE01_SAMPLE_RANDOM_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CIRCLE01_SAMPLE_RANDOM randomly samples the unit circle.')
    print('  Use it to estimate integrals.')

    print('')
    print('         N        1              X^2             Y^2             X^4           X^2Y^2          Y^4          X^6')
    print('')

    n = 1

    while (n <= 65536):
        seed = 123456789
        x, seed = circle01_sample_random(n, seed)
        print('  %8d' % (n), end='')
        for i in range(0, 7):
            for j in range(0, 2):
                e[j] = e_test[i, j]

            value = monomial_value(2, n, e, x)

            result = circle01_length() * np.sum(value) / float(n)
            print('  %14.10g' % (result), end='')

        print('')

        obj.axs.scatter(*x, s=0.5)
        obj.axs.set_title("n={:d}".format(n))
        obj.SavePng_Serial()
        plt.close()
        obj.new_fig()

        n = 2 * n

    print('')
    print('     Exact', end='')
    for i in range(0, 7):
        for j in range(0, 2):
            e[j] = e_test[i, j]
        exact = circle01_monomial_integral(e)
        print('  %14.10g' % (exact), end='')
    print('')
#
#  Terminate.
#
    print('')
    print('CIRCLE01_SAMPLE_RANDOM_TEST')
    print('  Normal end of execution.')
    return


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
    import platform

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
#
#  Terminate.
#
    print('')
    print('GAMMA_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_PRINT prints an I4VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    31 August 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the dimension of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    print('')
    print(title)
    print('')
    for i in range(0, n):
        print('%6d  %6d' % (i, a[i]))

    return


def i4vec_print_test():

    # *****************************************************************************80
    #
    # I4VEC_PRINT_TEST tests I4VEC_PRINT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import numpy as np
    import platform

    print('')
    print('I4VEC_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_PRINT prints an I4VEC.')

    n = 4
    v = np.array([91, 92, 93, 94], dtype=np.int32)
    i4vec_print(n, v, '  Here is an I4VEC:')
#
#  Terminate.
#
    print('')
    print('I4VEC_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_transpose_print(n, a, title):

    # *****************************************************************************80
    #
    # I4VEC_TRANSPOSE_PRINT prints an I4VEC "transposed".
    #
    #  Example:
    #
    #    A = (/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 /)
    #    TITLE = 'My vector:  '
    #
    #    My vector:
    #
    #       1    2    3    4    5
    #       6    7    8    9   10
    #      11
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of components of the vector.
    #
    #    Input, integer A(N), the vector to be printed.
    #
    #    Input, string TITLE, a title.
    #
    if (0 < len(title)):
        print('')
        print(title)

    if (0 < n):
        for i in range(0, n):
            print('%8d' % (a[i]), end='')
            if ((i + 1) % 10 == 0 or i == n - 1):
                print('')
    else:
        print('  (empty vector)')

    return


def i4vec_transpose_print_test():

    # *****************************************************************************80
    #
    # I4VEC_TRANSPOSE_PRINT_TEST tests I4VEC_TRANSPOSE_PRINT.
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
    import numpy as np
    import platform

    print('')
    print('I4VEC_TRANSPOSE_PRINT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_TRANSPOSE_PRINT prints an I4VEC')
    print('  with 5 entries to a row, and an optional title.')

    n = 12
    a = np.zeros(n, dtype=np.int32)

    for i in range(0, n):
        a[i] = i + 1

    i4vec_transpose_print(n, a, '  My array:  ')
#
#  Terminate.
#
    print('')
    print('I4VEC_TRANSPOSE_PRINT_TEST:')
    print('  Normal end of execution.')
    return


def i4vec_uniform_ab(n, a, b, seed):

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB returns a scaled pseudorandom I4VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    05 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer A, B, the minimum and maximum acceptable values.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, integer C(N), the randomly chosen integer vector.
    #
    #    Output, integer SEED, the updated seed.
    #
    import numpy as np
    from sys import exit

    i4_huge = 2147483647

    seed = np.floor(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('I4VEC_UNIFORM_AB - Fatal error!')
        print('  Input SEED = 0!')
        exit('I4VEC_UNIFORM_AB - Fatal error!')

    seed = np.floor(seed)
    a = round(a)
    b = round(b)

    c = np.zeros(n, dtype=np.int32)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        seed = (seed % i4_huge)

        if (seed < 0):
            seed = seed + i4_huge

        r = seed * 4.656612875E-10
#
#  Scale R to lie between A-0.5 and B+0.5.
#
        r = (1.0 - r) * (min(a, b) - 0.5) \
            + r * (max(a, b) + 0.5)
#
#  Use rounding to convert R to an integer between A and B.
#
        value = round(r)

        value = max(value, min(a, b))
        value = min(value, max(a, b))

        c[i] = value

    return c, seed


def i4vec_uniform_ab_test():

    # *****************************************************************************80
    #
    # I4VEC_UNIFORM_AB_TEST tests I4VEC_UNIFORM_AB.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 October 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    n = 20
    a = -100
    b = 200
    seed = 123456789

    print('')
    print('I4VEC_UNIFORM_AB_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  I4VEC_UNIFORM_AB computes pseudorandom values')
    print('  in an interval [A,B].')
    print('')
    print('  The lower endpoint A = %d' % (a))
    print('  The upper endpoint B = %d' % (b))
    print('  The initial seed is %d' % (seed))
    print('')

    v, seed = i4vec_uniform_ab(n, a, b, seed)

    i4vec_print(n, v, '  The random vector:')
#
#  Terminate.
#
    print('')
    print('I4VEC_UNIFORM_AB_TEST:')
    print('  Normal end of execution.')
    return


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
    import numpy as np

    v = np.ones(n)

    for i in range(0, m):
        if (0 != e[i]):
            for j in range(0, n):
                v[j] = v[j] * x[i, j] ** e[i]

    return v


def r8_gamma(x):

    # *****************************************************************************80
    #
    # R8_GAMMA evaluates Gamma(X) for a real argument.
    #
    #  Discussion:
    #
    #    This routine calculates the gamma function for a real argument X.
    #
    #    Computation is based on an algorithm outlined in reference 1.
    #    The program uses rational functions that approximate the gamma
    #    function to at least 20 significant decimal digits.  Coefficients
    #    for the approximation over the interval (1,2) are unpublished.
    #    Those for the approximation for 12 <= X are from reference 2.
    #
    #    PYTHON provides a GAMMA function, which is likely to be faster, and more
    #    accurate.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    24 July 2014
    #
    #  Author:
    #
    #    Original FORTRAN77 version by William Cody, Laura Stoltz.
    #    PYTHON version by John Burkardt.
    #
    #  Reference:
    #
    #    William Cody,
    #    An Overview of Software Development for Special Functions,
    #    in Numerical Analysis Dundee, 1975,
    #    edited by GA Watson,
    #    Lecture Notes in Mathematics 506,
    #    Springer, 1976.
    #
    #    John Hart, Ward Cheney, Charles Lawson, Hans Maehly,
    #    Charles Mesztenyi, John Rice, Henry Thatcher,
    #    Christoph Witzgall,
    #    Computer Approximations,
    #    Wiley, 1968,
    #    LC: QA297.C64.
    #
    #  Parameters:
    #
    #    Input, real X, the argument of the function.
    #
    #    Output, real VALUE, the value of the function.
    #
    import numpy as np
#
#  Coefficients for minimax approximation over (12, INF).
#
    c = np.array([
        -1.910444077728E-03,
        8.4171387781295E-04,
        -5.952379913043012E-04,
        7.93650793500350248E-04,
        -2.777777777777681622553E-03,
        8.333333333333333331554247E-02,
        5.7083835261E-03])
#
#  Mathematical constants
#
    r8_pi = 3.141592653589793
    sqrtpi = 0.9189385332046727417803297
#
#  Machine dependent parameters
#
    xbig = 171.624
    xminin = 2.23E-308
    eps = 2.22E-16
    xinf = 1.79E+308
#
#  Numerator and denominator coefficients for rational minimax
#  approximation over (1,2).
#
    p = np.array([
        -1.71618513886549492533811E+00,
        2.47656508055759199108314E+01,
        -3.79804256470945635097577E+02,
        6.29331155312818442661052E+02,
        8.66966202790413211295064E+02,
        -3.14512729688483675254357E+04,
        -3.61444134186911729807069E+04,
        6.64561438202405440627855E+04])

    q = np.array([
        -3.08402300119738975254353E+01,
        3.15350626979604161529144E+02,
        -1.01515636749021914166146E+03,
        -3.10777167157231109440444E+03,
        2.25381184209801510330112E+04,
        4.75584627752788110767815E+03,
        -1.34659959864969306392456E+05,
        -1.15132259675553483497211E+05])

    parity = 0
    fact = 1.0
    n = 0
    y = x
#
#  Argument is negative.
#
    if (y <= 0.0):

        y = - x
        y1 = np.floor(y)
        res = y - y1

        if (res != 0.0):

            if (y1 != np.floor(y1 * 0.5) * 2.0):
                parity = 1

            fact = - r8_pi / np.sin(r8_pi * res)
            y = y + 1.0

        else:

            res = xinf
            value = res
            return value
#
#  Argument is positive.
#
    if (y < eps):
        #
        #  Argument < EPS.
        #
        if (xminin <= y):
            res = 1.0 / y
        else:
            res = xinf

        value = res
        return value

    elif (y < 12.0):

        y1 = y
#
#  0.0 < argument < 1.0.
#
        if (y < 1.0):

            z = y
            y = y + 1.0
#
#  1.0 < argument < 12.0.
#  Reduce argument if necessary.
#
        else:

            n = int(np.floor(y) - 1)
            y = y - n
            z = y - 1.0
#
#  Evaluate approximation for 1.0 < argument < 2.0.
#
        xnum = 0.0
        xden = 1.0
        for i in range(0, 8):
            xnum = (xnum + p[i]) * z
            xden = xden * z + q[i]

        res = xnum / xden + 1.0
#
#  Adjust result for case  0.0 < argument < 1.0.
#
        if (y1 < y):

            res = res / y1
#
#  Adjust result for case 2.0 < argument < 12.0.
#
        elif (y < y1):

            for i in range(0, n):
                res = res * y
                y = y + 1.0

    else:
        #
        #  Evaluate for 12.0 <= argument.
        #
        if (y <= xbig):

            ysq = y * y
            sum = c[6]
            for i in range(0, 6):
                sum = sum / ysq + c[i]
            sum = sum / y - y + sqrtpi
            sum = sum + (y - 0.5) * np.log(y)
            res = np.exp(sum)

        else:

            res = xinf
            value = res
            return value
#
#  Final adjustments and return.
#
    if (parity):
        res = - res

    if (fact != 1.0):
        res = fact / res

    value = res

    return value


def r8vec_uniform_01(n, seed):

    # *****************************************************************************80
    #
    # R8VEC_UNIFORM_01 returns a unit pseudorandom R8VEC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Paul Bratley, Bennett Fox, Linus Schrage,
    #    A Guide to Simulation,
    #    Second Edition,
    #    Springer, 1987,
    #    ISBN: 0387964673,
    #    LC: QA76.9.C65.B73.
    #
    #    Bennett Fox,
    #    Algorithm 647:
    #    Implementation and Relative Efficiency of Quasirandom
    #    Sequence Generators,
    #    ACM Transactions on Mathematical Software,
    #    Volume 12, Number 4, December 1986, pages 362-376.
    #
    #    Pierre L'Ecuyer,
    #    Random Number Generation,
    #    in Handbook of Simulation,
    #    edited by Jerry Banks,
    #    Wiley, 1998,
    #    ISBN: 0471134031,
    #    LC: T57.62.H37.
    #
    #    Peter Lewis, Allen Goodman, James Miller,
    #    A Pseudo-Random Number Generator for the System/360,
    #    IBM Systems Journal,
    #    Volume 8, Number 2, 1969, pages 136-143.
    #
    #  Parameters:
    #
    #    Input, integer N, the number of entries in the vector.
    #
    #    Input, integer SEED, a seed for the random number generator.
    #
    #    Output, real X(N), the vector of pseudorandom values.
    #
    #    Output, integer SEED, an updated seed for the random number generator.
    #
    import numpy
    from sys import exit

    i4_huge = 2147483647

    seed = int(seed)

    if (seed < 0):
        seed = seed + i4_huge

    if (seed == 0):
        print('')
        print('R8VEC_UNIFORM_01 - Fatal error!')
        print('  Input SEED = 0!')
        exit('R8VEC_UNIFORM_01 - Fatal error!')

    x = numpy.zeros(n)

    for i in range(0, n):

        k = (seed // 127773)

        seed = 16807 * (seed - k * 127773) - k * 2836

        if (seed < 0):
            seed = seed + i4_huge

        x[i] = seed * 4.656612875E-10

    return x, seed


def timestamp():

    # *****************************************************************************80
    #
    # TIMESTAMP prints the date as a timestamp.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    06 April 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    None
    #
    import time

    t = time.time()
    print(time.ctime(t))

    return None


def circle_monte_carlo_test():

    # *****************************************************************************80
    #
    # CIRCLE_MONTE_CARLO_TEST tests the CIRCLE_MONTE_CARLO library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    02 June 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('CIRCLE_MONTE_CARLO_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the CIRCLE_MONTE_CARLO library.')

    circle01_length_test()
    circle01_monomial_integral_test()

    obj.create_tempdir(-1)
    circle01_sample_ergodic_test()

    obj.create_tempdir(-1)
    circle01_sample_random_test()
#
#  Terminate.
#
    print('')
    print('CIRCLE_MONTE_CARLO_TEST:')
    print('  Normal end of execution.')
    print('')
    return


if (__name__ == '__main__'):
    timestamp()
    circle_monte_carlo_test()
    timestamp()
