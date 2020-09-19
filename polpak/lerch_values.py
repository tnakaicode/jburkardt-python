#! /usr/bin/env python
#
def lerch_values(n_data):

    # *****************************************************************************80
    #
    # LERCH_VALUES returns some values of the Lerch transcendent function.
    #
    #  Discussion:
    #
    #    The Lerch function is defined as
    #
    #      Phi(z,s,a) = Sum ( 0 <= k < Infinity ) z^k / ( a + k )^s
    #
    #    omitting any terms with ( a + k ) = 0.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      LerchPhi[z,s,a]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
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
    #    Output, real Z, the parameters of the function.
    #
    #    Output, integer S, the parameters of the function.
    #
    #    Output, real A, the parameters of the function.
    #
    #    Output, real F, the value of the function.
    #
    import numpy as np

    n_max = 12

    a_vec = np.array((
        0.0E+00,
        0.0E+00,
        0.0E+00,
        1.0E+00,
        1.0E+00,
        1.0E+00,
        2.0E+00,
        2.0E+00,
        2.0E+00,
        3.0E+00,
        3.0E+00,
        3.0E+00))

    f_vec = np.array((
        0.1644934066848226E+01,
        0.1202056903159594E+01,
        0.1000994575127818E+01,
        0.1164481052930025E+01,
        0.1074426387216080E+01,
        0.1000492641212014E+01,
        0.2959190697935714E+00,
        0.1394507503935608E+00,
        0.9823175058446061E-03,
        0.1177910993911311E+00,
        0.3868447922298962E-01,
        0.1703149614186634E-04))

    s_vec = np.array((
        2, 3, 10,
        2, 3, 10,
        2, 3, 10,
        2, 3, 10))

    z_vec = np.array((
        0.1000000000000000E+01,
        0.1000000000000000E+01,
        0.1000000000000000E+01,
        0.5000000000000000E+00,
        0.5000000000000000E+00,
        0.5000000000000000E+00,
        0.3333333333333333E+00,
        0.3333333333333333E+00,
        0.3333333333333333E+00,
        0.1000000000000000E+00,
        0.1000000000000000E+00,
        0.1000000000000000E+00))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        z = 0.0
        s = 0
        a = 0.0
        f = 0.0
    else:
        z = z_vec[n_data]
        s = s_vec[n_data]
        a = a_vec[n_data]
        f = f_vec[n_data]
        n_data = n_data + 1

    return n_data, z, s, a, f


def lerch_values_test():

    # *****************************************************************************80
    #
    # LERCH_VALUES_TEST demonstrates the use of LERCH_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    19 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('LERCH_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  LERCH_VALUES stores values of the Lerch function.')
    print('')
    print('        Z            S        A               F')
    print('')

    n_data = 0

    while (True):

        n_data, z, s, a, f = lerch_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %6d  %12f  %24.16f' % (z, s, a, f))
#
#  Terminate.
#
    print('')
    print('LERCH_VALUES_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    lerch_values_test()
    timestamp()
