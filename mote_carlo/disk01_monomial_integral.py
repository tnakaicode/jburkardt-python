#! /usr/bin/env python3
#


def disk01_monomial_integral(e):

    # *****************************************************************************80
    #
    # DISK01_MONOMIAL_INTEGRAL returns monomial integrals in the unit disk.
    #
    #  Discussion:
    #
    #    The integration region is
    #
    #      X^2 + Y^2 <= 1.
    #
    #    The monomial is F(X,Y) = X^E(1) * Y^E(2).
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
    #    Input, integer E(2), the exponents of X and Y in the
    #    monomial.  Each exponent must be nonnegative.
    #
    #    Output, real INTEGRAL, the integral.
    #
    from r8_gamma import r8_gamma
    from sys import exit

    r = 1.0

    if (e[0] < 0 or e[1] < 0):
        print('')
        print('DISK01_MONOMIAL_INTEGRAL - Fatal error!')
        print('  All exponents must be nonnegative.')
        exit('DISK01_MONOMIAL_INTEGRAL - Fatal error!')

    if (((e[0] % 2) == 1) or ((e[1] % 2) == 1)):

        integral = 0.0

    else:

        integral = 2.0

        for i in range(0, 2):
            arg = 0.5 * float(e[i] + 1)
            integral = integral * r8_gamma(arg)

        arg = 0.5 * float(e[0] + e[1] + 2)
        integral = integral / r8_gamma(arg)
#
#  The surface integral is now adjusted to give the volume integral.
#
    s = e[0] + e[1] + 2

    integral = integral * r ** s / float(s)

    return integral


def disk01_monomial_integral_test():

    # *****************************************************************************80
    #
    # DISK_INTEGRALS_TEST uses DISK01_SAMPLE to estimate various integrals.
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
    import numpy as np
    import platform
    from disk01_area import disk01_area
    from disk01_sample import disk01_sample
    from i4vec_uniform_ab import i4vec_uniform_ab
    from monomial_value import monomial_value

    m = 2
    n = 4192
    test_num = 20

    print('')
    print('DISK01_MONOMIAL_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  DISK01_MONOMIAL_INTEGRAL computes monomial integrals')
    print('  over the interior of the unit disk in 2D.')
    print('  Compare with a Monte Carlo value.')
#
#  Get sample points.
#
    seed = 123456789
    x, seed = disk01_sample(n, seed)

    print('')
    print('  Number of sample points used is %d' % (n))
#
#  Randomly choose X,Y exponents between 0 and 8.
#
    print('')
    print('  If any exponent is odd, the integral is zero.')
    print('  We will restrict this test to randomly chosen even exponents.')
    print('')
    print('  Ex  Ey     MC-Estimate           Exact      Error')
    print('')

    for test in range(0, test_num):

        e, seed = i4vec_uniform_ab(m, 0, 4, seed)

        e[0] = e[0] * 2
        e[1] = e[1] * 2

        value = monomial_value(m, n, e, x)

        result = disk01_area() * np.sum(value) / float(n)
        exact = disk01_monomial_integral(e)
        error = abs(result - exact)

        print('  %2d  %2d  %14.6g  %14.6g  %10.2g'
              % (e[0], e[1], result, exact, error))

#
#  Terminate.
#
    print('')
    print('DISK01_MONOMIAL_INTEGRAL_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    disk01_monomial_integral_test()
    timestamp()
