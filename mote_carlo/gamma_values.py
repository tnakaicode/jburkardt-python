#! /usr/bin/env python
#


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


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    gamma_values_test()
    timestamp()
