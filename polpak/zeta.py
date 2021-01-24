#! /usr/bin/env python
#
def zeta_m1(p, tol):

    # *****************************************************************************80
    #
    # ZETA_M1 estimates the Riemann Zeta function minus 1.
    #
    #  Discussion:
    #
    #    This function includes the Euler-McLaurin correction.
    #
    #    ZETA_M1 ( P ) = ZETA ( P ) - 1
    #
    #    ZETA(P) has the form 1 + small terms.  Computing ZETA(P)-1
    #    allows for greater accuracy in the small terms.
    #
    #  Definition:
    #
    #    For 1 < P, the Riemann Zeta function is defined as:
    #
    #      ZETA ( P ) = Sum ( 1 <= N < Infinity ) 1 / N^P
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    William Thompson,
    #    Atlas for Computing Mathematical Functions,
    #    Wiley, 1997,
    #    ISBN: 0471181714,
    #    LC: QA331 T385
    #
    #  Parameters:
    #
    #    Input, real P, the power to which the integers are raised.
    #    P must be greater than 1.
    #
    #    Input, real TOL, the requested relative tolerance.
    #
    #    Output, real VALUE, an approximation to the Riemann
    #    Zeta function minus 1.
    #
    if (p <= 1.0):
        print('')
        print('ZETA_M1 - Fatal error!')
        print('  Exponent P <= 1.0.')

    nsterm = p * (p + 1.0) * (p + 2.0) * (p + 3.0) * (p + 4.0) \
        / 30240.0

    base = nsterm * (2.0 ** p) / tol

    n = int(base ** (1.0 / (p + 5.0)))
    n = max(n, 10)
    negp = - p
    t = 0.0
    for k in range(2, n):
        base = float(k)
        t = t + base ** negp
#
#  Euler-McLaurin correction.
#
    base = float(n)
    t = t + base ** negp \
        * (0.5 + float(n) / (p - 1.0)
           + p * (1.0 -
                  (p + 1.0) * (p + 2.0) / float(60 * n * n)) / float(12 * n)
           + nsterm / base ** (p + 5.0))

    return t


def zeta_m1_test():

    # *****************************************************************************80
    #
    # ZETA_M1_TEST tests ZETA_M1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    tol = 1.0E-10

    print('')
    print('ZETA_M1_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  ZETA_M1 evaluates the Riemann Zeta function minus 1.')
    print('  Relative accuracy requested is TOL = %g' % (tol))
    print('')
    print('         P                ZETA_M1(P)                ZETA_M1(P)')
    print('                          tabulated                 computed')
    print('')

    n_data = 0

    while (True):

        n_data, p, z1 = zeta_m1_values(n_data)

        if (n_data == 0):
            break

        z2 = zeta_m1(p, tol)

        print('  %8.4g  %24.16e  %24.16e' % (p, z1, z2))
#
#  Terminate.
#
    print('')
    print('ZETA_M1_TEST')
    print('  Normal end of execution.')
    return


def zeta_m1_values(n_data):

    # *****************************************************************************80
    #
    # ZETA_M1_VALUES returns some values of the Riemann Zeta function minus 1.
    #
    #  Discussion:
    #
    #    ZETA_M1(N) = ZETA(N) - 1
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Milton Abramowitz and Irene Stegun,
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
    #    Output, real P, the argument.
    #
    #    Output, real F, the value.
    #
    import numpy as np

    n_max = 17

    p_vec = np.array((
        2.0,
        2.5,
        3.0,
        3.5,
        4.0,
        5.0,
        6.0,
        7.0,
        8.0,
        9.0,
        10.0,
        11.0,
        12.0,
        16.0,
        20.0,
        30.0,
        40.0))

    f_vec = np.array((
        0.64493406684822643647E+00,
        0.3414872573E+00,
        0.20205690315959428540E+00,
        0.1267338673E+00,
        0.8232323371113819152E-01,
        0.3692775514336992633E-01,
        0.1734306198444913971E-01,
        0.834927738192282684E-02,
        0.407735619794433939E-02,
        0.200839292608221442E-02,
        0.99457512781808534E-03,
        0.49418860411946456E-03,
        0.24608655330804830E-03,
        0.1528225940865187E-04,
        0.95396203387280E-06,
        0.93132743242E-10,
        0.90949478E-12))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        p = 0.0
        f = 0.0
    else:
        p = p_vec[n_data]
        f = f_vec[n_data]
        n_data = n_data + 1

    return n_data, p, f


def zeta_naive(p):

    # *****************************************************************************80
    #
    # ZETA_NAIVE estimates the Riemann Zeta function.
    #
    #  Definition:
    #
    #    For 1 < P, the Riemann Zeta function is defined as:
    #
    #      ZETA ( P ) = Sum ( 1 <= N < Infinity ) 1 / N^P
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
    #  Reference:
    #
    #    Daniel Zwillinger, editor,
    #    CRC Standard Mathematical Tables and Formulae,
    #    30th Edition,
    #    CRC Press, 1996.
    #
    #  Parameters:
    #
    #    Input, real P, the power to which the integers are raised.
    #    P must be greater than 1.
    #
    #    Output, real VALUE, an approximation to the Riemann
    #    Zeta function.
    #
    if (p <= 1.0):
        print('')
        print('ZETA - Fatal error!')
        print('  Exponent P <= 1.0.')

    value = 0.0
    n = 0

    while (True):

        n = n + 1
        value_old = value
        value = value + 1.0 / n ** p

        if (value <= value_old or 10000 <= n):
            break

    return value


def zeta_naive_test():

    # *****************************************************************************80
    #
    # ZETA_NAIVE_TEST tests ZETA_NAIVE.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    15 January 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('ZETA_NAIVE_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  ZETA evaluates the Riemann Zeta function using a naive approach.')
    print('')
    print('      N                   ZETA(N)             ZETA_NAIVE(N)')
    print('                          tabulate            computed')
    print('')

    n_data = 0

    while (True):

        n_data, n, z1 = zeta_values(n_data)

        if (n_data == 0):
            break

        n_real = float(n)
        z2 = zeta_naive(n_real)

        print('  %5d  %24.16g  %24.16g' % (n, z1, z2))
#
#  Terminate.
#
    print('')
    print('ZETA_NAIVE_TEST')
    print('  Normal end of execution.')
    return


def zeta_values(n_data):

    # *****************************************************************************80
    #
    # ZETA_VALUES returns some values of the Riemann Zeta function.
    #
    #  Discussion:
    #
    #    ZETA(N) = sum ( 1 <= I < Infinity ) 1 / I^N
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      Zeta[n]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    22 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Milton Abramowitz and Irene Stegun,
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
    #    Output, integer N, the argument of the Zeta function.
    #
    #    Output, real F, the value of the Zeta function.
    #
    import numpy as np

    n_max = 15

    n_vec = np.array((
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        16,
        20,
        30,
        40))

    f_vec = np.array((
        0.164493406684822643647E+01,
        0.120205690315959428540E+01,
        0.108232323371113819152E+01,
        0.103692775514336992633E+01,
        0.101734306198444913971E+01,
        0.100834927738192282684E+01,
        0.100407735619794433939E+01,
        0.100200839292608221442E+01,
        0.100099457512781808534E+01,
        0.100049418860411946456E+01,
        0.100024608655330804830E+01,
        0.100001528225940865187E+01,
        0.100000095396203387280E+01,
        0.100000000093132743242E+01,
        0.100000000000090949478E+01))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        n = 0
        f = 0.0
    else:
        n = n_vec[n_data]
        f = f_vec[n_data]
        n_data = n_data + 1

    return n_data, n, f


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    zeta_naive_test()
    zeta_m1_test()
    timestamp()
