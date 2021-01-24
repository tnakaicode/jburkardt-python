#! /usr/bin/env python
#
import numpy as np
import matplotlib.pyplot as plt
import platform
from lerch_values import lerch_values


def lerch(z, s, a):

    # *****************************************************************************80
    #
    # LERCH estimates the Lerch transcendent function.
    #
    #  Discussion:
    #
    #    The Lerch transcendent function is defined as:
    #
    #      LERCH ( Z, S, A ) = Sum ( 0 <= K < Infinity ) Z^K / ( A + K )^S
    #
    #    excluding any term with ( A + K ) = 0.
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
    #    23 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Eric Weisstein, editor,
    #    CRC Concise Encylopedia of Mathematics,
    #    CRC Press, 1998.
    #
    #  Thanks:
    #
    #    Oscar van Vlijmen
    #
    #  Parameters:
    #
    #    Input, real Z, integer S, real A,
    #    the parameters of the function.
    #
    #    Output, real VALUE, an approximation to the Lerch
    #    transcendent function.
    #
    value = 0.0

    if (z <= 0.0):
        return value

    eps = 1.0E-10
    k = 0
    z_k = 1.0

    while (True):

        if (a + k != 0.0):

            term = z_k / (a + k) ** s
            value = value + term

            if (abs(term) <= eps * (1.0 + abs(value))):
                break

        k = k + 1
        z_k = z_k * z

    return value


def lerch_test():

    # *****************************************************************************80
    #
    # LERCH_TEST tests LERCH.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 February 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('LERCH_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  LERCH evaluates the Lerch function;')
    print('')
    print('       Z       S       A         Lerch           Lerch')
    print('                             Tabulated        Computed')
    print('')

    data = []
    n_data = 0

    while (True):
        dat = [n_data]
        n_data, z, s, a, f = lerch_values(n_data)

        if (n_data == 0):
            break

        f2 = lerch(z, s, a)
        dat += [z, s, a, f, f2]
        data.append(dat)

        print('  %8g  %4d  %8g  %14g  %14g' % (z, s, a, f, f2))
    data = np.array(data)

    plt.figure()
    plt.plot(data[:, 1])
    plt.plot(data[:, 2])
    plt.plot(data[:, 3])
    plt.plot(data[:, 4])
    plt.plot(data[:, 5])
    plt.savefig("./lerch.png")

    print('')
    print('LERCH_TEST')
    print('  Normal end of execution.')
    return


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
    lerch_test()
    timestamp()
