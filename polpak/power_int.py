#! /usr/bin/env python
#
def sin_power_int(a, b, n):

    # *****************************************************************************80
    #
    # SIN_POWER_INT evaluates the sine power integral.
    #
    #  Discussion:
    #
    #    The function is defined by
    #
    #      SIN_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( sin ( t ))^n dt
    #
    #    The algorithm uses the following fact:
    #
    #      Integral sin^n ( t ) = (1/n) * (
    #        sin^(n-1)(t) * cos(t) + ( n-1 ) * Integral sin^(n-2) ( t ) dt )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters
    #
    #    Input, real A, B, the limits of integration.
    #
    #    Input, integer N, the power of the sine function.
    #
    #    Output, real VALUE, the value of the integral.
    #
    import numpy as np
    from sys import exit

    if (n < 0):
        print('')
        print('SIN_POWER_INT - Fatal error!')
        print('  Power N < 0.')
        exit('SIN_POWER_INT - Fatal error!')

    sa = np.sin(a)
    sb = np.sin(b)
    ca = np.cos(a)
    cb = np.cos(b)

    if ((n % 2) == 0):
        value = b - a
        mlo = 2
    else:
        value = ca - cb
        mlo = 3

    for m in range(mlo, n + 1, 2):
        value = ((m - 1) * value
                 + sa ** (m - 1) * ca
                 - sb ** (m - 1) * cb) / float(m)

    return value


def sin_power_int_test():

    # *****************************************************************************80
    #
    # SIN_POWER_INT_TEST tests SIN_POWER_INT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from sin_power_int_values import sin_power_int_values

    print('')
    print('SIN_POWER_INT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SIN_POWER_INT returns values of')
    print('  the integral of SIN(X)^N from A to B.')
    print('')
    print('      A         B          N      Exact           Computed')
    print('')

    n_data = 0

    while (True):

        n_data, a, b, n, fx = sin_power_int_values(n_data)

        if (n_data == 0):
            break

        fx2 = sin_power_int(a, b, n)

        print('  %8f  %8f  %6d  %14e  %14e' % (a, b, n, fx, fx2))
#
#  Terminate.
#
    print('')
    print('SIN_POWER_INT_TEST')
    print('  Normal end of execution.')
    return


def sin_power_int_values(n_data):

    # *****************************************************************************80
    #
    # SIN_POWER_INT_VALUES returns some values of the sine power integral.
    #
    #  Discussion:
    #
    #    The function has the form
    #
    #      SIN_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( sin(T) )^N dt
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      Integrate [ ( Sin[x] )^n, { x, a, b } ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 February 2015
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
    #    Output, real A, B, the limits of integration.
    #
    #    Output, integer N, the power.
    #
    #    Output, real F, the value of the function.
    #
    import numpy as np

    n_max = 10

    a_vec = np.array((
        0.10E+02,
        0.00E+00,
        0.00E+00,
        0.00E+00,
        0.00E+00,
        0.00E+00,
        0.00E+00,
        0.10E+01,
        0.00E+00,
        0.00E+00))

    b_vec = np.array((
        0.20E+02,
        0.10E+01,
        0.10E+01,
        0.10E+01,
        0.10E+01,
        0.10E+01,
        0.20E+01,
        0.20E+01,
        0.10E+01,
        0.10E+01))

    f_vec = np.array((
        0.10000000000000000000E+02,
        0.45969769413186028260E+00,
        0.27267564329357957615E+00,
        0.17894056254885809051E+00,
        0.12402556531520681830E+00,
        0.88974396451575946519E-01,
        0.90393123848149944133E+00,
        0.81495684202992349481E+00,
        0.21887522421729849008E-01,
        0.17023439374069324596E-01))

    n_vec = np.array((
        0,
        1,
        2,
        3,
        4,
        5,
        5,
        5,
        10,
        11))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        a = 0.0
        b = 0.0
        f = 0.0
        n = 0
    else:
        a = a_vec[n_data]
        b = b_vec[n_data]
        f = f_vec[n_data]
        n = n_vec[n_data]
        n_data = n_data + 1

    return n_data, a, b, n, f


def sin_power_int_values_test():

    # *****************************************************************************80
    #
    # SIN_POWER_INT_VALUES_TEST tests SIN_POWER_INT_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('SIN_POWER_INT_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  SIN_POWER_INT_VALUES stores values of the cosine power integral.')
    print('')
    print('        A             B            N           F')
    print('')

    n_data = 0

    while (True):

        n_data, a, b, n, f = sin_power_int_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %12f  %6d  %24.16g' % (a, b, n, f))
#
#  Terminate.
#
    print('')
    print('SIN_POWER_INT_VALUES_TEST:')
    print('  Normal end of execution.')


def cos_power_int(a, b, n):

    # *****************************************************************************80
    #
    # COS_POWER_INT evaluates the cosine power integral.
    #
    #  Discussion:
    #
    #    The function is defined by
    #
    #      COS_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( cos ( t ))^n dt
    #
    #    The algorithm uses the following fact:
    #
    #      Integral cos^n ( t ) = -(1/n) * (
    #        cos^(n-1)(t) * sin(t) + ( n-1 ) * Integral cos^(n-2) ( t ) dt )
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters
    #
    #    Input, real A, B, the limits of integration.
    #
    #    Input, integer N, the power of the sine function.
    #
    #    Output, real VALUE, the value of the integral.
    #
    import numpy as np
    from sys import exit

    if (n < 0):
        print('')
        print('COS_POWER_INT - Fatal error!')
        print('  Power N < 0.')
        exit('COS_POWER_INT - Fatal error!')

    sa = np.sin(a)
    sb = np.sin(b)
    ca = np.cos(a)
    cb = np.cos(b)

    if ((n % 2) == 0):
        value = b - a
        mlo = 2
    else:
        value = sb - sa
        mlo = 3

    for m in range(mlo, n + 1, 2):
        value = ((m - 1) * value - ca ** (m - 1) * sa
                 + cb ** (m - 1) * sb) / float(m)

    return value


def cos_power_int_test():

    # *****************************************************************************80
    #
    # COS_POWER_INT_TEST tests COS_POWER_INT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform
    from cos_power_int_values import cos_power_int_values

    print('')
    print('COS_POWER_INT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  COS_POWER_INT returns values of')
    print('  the integral of COS(X)^N from A to B.')
    print('')
    print('      A         B          N      Exact           Computed')
    print('')

    n_data = 0

    while (True):

        n_data, a, b, n, fx = cos_power_int_values(n_data)

        if (n_data == 0):
            break

        fx2 = cos_power_int(a, b, n)

        print('  %8f  %8f  %6d  %14e  %14e' % (a, b, n, fx, fx2))
#
#  Terminate.
#
    print('')
    print('COS_POWER_INT_TEST')
    print('  Normal end of execution.')


def cos_power_int_values(n_data):

    # *****************************************************************************80
    #
    # COS_POWER_INT_VALUES returns some values of the cosine power integral.
    #
    #  Discussion:
    #
    #    The function has the form
    #
    #      COS_POWER_INT(A,B,N) = Integral ( A <= T <= B ) ( cos(T) )^N dt
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      Integrate [ ( Cos[x] )^n, { x, a, b } ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 January 2015
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
    #    Cambridge University Press, 1999,
    #    ISBN: 0-521-64314-7,
    #    LC: QA76.95.W65.
    #
    #  Parameters:
    #
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0
    #    before the first call.  On each call, the routine increments N_DATA by 1,
    #    and returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, real A, B, the limits of integration.
    #
    #    Output, integer N, the power.
    #
    #    Output, real F, the function value.
    #
    import numpy as np

    n_max = 11

    a_vec = np.array((
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00))

    b_vec = np.array((
        3.141592653589793,
        3.141592653589793,
        3.141592653589793,
        3.141592653589793,
        3.141592653589793,
        3.141592653589793,
        3.141592653589793,
        3.141592653589793,
        3.141592653589793,
        3.141592653589793,
        3.141592653589793))

    f_vec = np.array((
        3.141592653589793,
        0.0,
        1.570796326794897,
        0.0,
        1.178097245096172,
        0.0,
        0.9817477042468104,
        0.0,
        0.8590292412159591,
        0.0,
        0.7731263170943632))

    n_vec = np.array((
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        a = 0.0
        b = 0.0
        f = 0.0
        n = 0
    else:
        a = a_vec[n_data]
        b = b_vec[n_data]
        f = f_vec[n_data]
        n = n_vec[n_data]
        n_data = n_data + 1

    return n_data, a, b, n, f


def cos_power_int_values_test():

    # *****************************************************************************80
    #
    # COS_POWER_INT_VALUES_TEST tests COS_POWER_INT_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('COS_POWER_INT_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  COS_POWER_INT_VALUES stores values of the cosine power integral.')
    print('')
    print('        A             B            N           F')
    print('')

    n_data = 0

    while (True):

        n_data, a, b, n, f = cos_power_int_values(n_data)

        if (n_data == 0):
            break

        print('  %12f  %12f  %6d  %24.16g' % (a, b, n, f))
#
#  Terminate.
#
    print('')
    print('COS_POWER_INT_VALUES_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    sin_power_int_test()
    sin_power_int_values_test()
    cos_power_int_test()
    cos_power_int_values_test()
    timestamp()
