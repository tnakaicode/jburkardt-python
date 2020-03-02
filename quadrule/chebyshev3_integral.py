#! /usr/bin/env python
#


def chebyshev3_integral(expon):

    # *****************************************************************************80
    #
    # CHEBYSHEV3_INTEGRAL evaluates a monomial Chebyshev type 3 integral.
    #
    #  Discussion:
    #
    #    The integral:
    #
    #      integral ( -1 <= x <= +1 ) x^n / sqrt ( 1 - x^2 ) dx
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer EXPON, the exponent.
    #
    #    Output, real EXACT, the value of the exact integral.
    #
    import numpy as np
#
#  Get the exact value of the integral.
#
    if ((expon % 2) == 0):

        top = 1.0
        bot = 1.0
        for i in range(2, expon + 1, 2):
            top = top * float(i - 1)
            bot = bot * float(i)

        value = np.pi * float(top) / float(bot)

    else:

        value = 0.0

    return value


def chebyshev3_integral_test():

    # *****************************************************************************80
    #
    # CHEBYSHEV3_INTEGRAL_TEST tests CHEBYSHEV3_INTEGRAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    14 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('CHEBYSHEV3_INTEGRAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CHEBYSHEV3_INTEGRAL evaluates')
    print('  Integral ( -1 < x < +1 ) x^n / (1-x*x) dx')
    print('')
    print('         N         Value')
    print('')

    for n in range(0, 11):

        value = chebyshev3_integral(n)

        print('  %8d  %24.16g' % (n, value))
#
#  Terminate.
#
    print('')
    print('CHEBYSHEV3_INTEGRAL_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    chebyshev3_integral_test()
    timestamp()
