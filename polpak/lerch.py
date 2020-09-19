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


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    lerch_test()
    timestamp()
