#! /usr/bin/env python
#


def hermite_integral(n):

    # *****************************************************************************80
    #
    # HERMITE_INTEGRAL evaluates a monomial Hermite integral.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      Integral ( -oo < x < +oo ) x^n exp(-x^2) dx
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the integral.
    #    0 <= N.
    #
    #    Output, real VALUE, the value of the integral.
    #
    import numpy as np
    from r8_factorial2 import r8_factorial2
    from r8_huge import r8_huge

    if (n < 0):

        value = - r8_huge()

    elif ((n % 2) == 1):

        value = 0.0

    else:

        value = r8_factorial2(n - 1) * np.sqrt(np.pi) / 2.0 ** (n // 2)

    return value


def hermite_integral_test():

    # *****************************************************************************80
    #
    # HERMITE_INTEGRAL_TEST tests HERMITE_INTEGRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('HERMITE_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  HERMITE_INTEGRAL evaluates')
    print('  Integral ( -oo < x < +oo ) exp(-x^2) x^m dx')
    print('')
    print('         N         Value')
    print('')

    for n in range(0, 11):

        value = hermite_integral(n)

        print('  %8d  %24.16g' % (n, value))
#
#  Terminate.
#
    print('')
    print('HERMITE_INTEGRAL_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    hermite_integral_test()
    timestamp()
