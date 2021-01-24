#! /usr/bin/env python
#
def sigma(n):

    # *****************************************************************************80
    #
    # SIGMA returns the value of SIGMA(N), the divisor sum.
    #
    #  Definition:
    #
    #    SIGMA(N) is the sum of the distinct divisors of N, including 1 and N.
    #
    #  First values:
    #
    #     N  SIGMA(N)
    #
    #     1    1
    #     2    3
    #     3    4
    #     4    7
    #     5    6
    #     6   12
    #     7    8
    #     8   15
    #     9   13
    #    10   18
    #    11   12
    #    12   28
    #    13   14
    #    14   24
    #    15   24
    #    16   31
    #    17   18
    #    18   39
    #    19   20
    #    20   42
    #
    #  Formula:
    #
    #    SIGMA(U*V) = SIGMA(U) * SIGMA(V) if U and V are relatively prime.
    #
    #    SIGMA(P^K) = ( P^(K+1) - 1 ) / ( P - 1 ) if P is prime.
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
    #  Parameters:
    #
    #    Input, integer N, the value to be analyzed.
    #
    #    Output, integer VALUE, the value of SIGMA(N).  If N is less than
    #    or equal to 0, VALUE will be returned as 0.  If there is not
    #    enough room for factoring N, VALUE is returned as -1.
    #
    from i4_factor import i4_factor

    maxfactor = 20

    if (n <= 0):
        value = 0
        return value

    if (n == 1):
        value = 1
        return value
#
#  Factor N.
#
    nfactor, factor, power, nleft = i4_factor(n)

    if (nleft != 1):
        print('')
        print('SIGMA - Fatal error!')
        print('  Not enough factorization space.')

    value = 1
    for i in range(0, nfactor):
        value = (value * (factor[i] ** (power[i] + 1) - 1)) \
            / (factor[i] - 1)

    return value


def sigma_test():

    # *****************************************************************************80
    #
    # SIGMA_TEST tests SIGMA.
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
    from sigma_values import sigma_values

    print('')
    print('SIGMA_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  SIGMA computes the SIGMA function.')
    print('')
    print('         N      Exact         SIGMA(N)')

    n_data = 0

    while (True):

        n_data, n, c1 = sigma_values(n_data)

        if (n_data == 0):
            break

        c2 = sigma(n)

        print('  %8d  %12d  %12d' % (n, c1, c2))
#
#  Terminate.
#
    print('')
    print('SIGMA_TEST')
    print('  Normal end of execution.')
    return


def sigma_values(n_data):

    # *****************************************************************************80
    #
    # SIGMA_VALUES returns some values of the Sigma function.
    #
    #  Discussion:
    #
    #    SIGMA(N) is the sum of the distinct divisors of N, including 1 and N.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      DivisorSigma[1,n]
    #
    #  First values:
    #
    #     N  SIGMA(N)
    #
    #     1    1
    #     2    3
    #     3    4
    #     4    7
    #     5    6
    #     6   12
    #     7    8
    #     8   15
    #     9   13
    #    10   18
    #    11   12
    #    12   28
    #    13   14
    #    14   24
    #    15   24
    #    16   31
    #    17   18
    #    18   39
    #    19   20
    #    20   42
    #
    #  Formula:
    #
    #    SIGMA(U*V) = SIGMA(U) * SIGMA(V) if U and V are relatively prime.
    #
    #    SIGMA(P^K) = ( P^(K+1) - 1 ) / ( P - 1 ) if P is prime.
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
    #    Output, integer N, the argument of the Sigma function.
    #
    #    Output, integer C, the value of the Sigma function.
    #
    import numpy as np

    n_max = 20

    c_vec = np.array((
        1, 3, 4, 7, 6, 12, 8, 15, 13, 18,
        72, 128, 255, 176, 576, 1170, 618, 984, 2232, 2340))

    n_vec = np.array((
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        30, 127, 128, 129, 210, 360, 617, 815, 816, 1000))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        n = 0
        c = 0
    else:
        n = n_vec[n_data]
        c = c_vec[n_data]
        n_data = n_data + 1

    return n_data, n, c


def sigma_values_test():

    # *****************************************************************************80
    #
    # SIGMA_VALUES_TEST demonstrates the use of SIGMA_VALUES.
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
    print('SIGMA_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  SIGMA_VALUES stores values of the SIGMA function.')
    print('')
    print('             N    SIGMA(N)')
    print('')

    n_data = 0

    while (True):

        n_data, n, c = sigma_values(n_data)

        if (n_data == 0):
            break

        print('  %12d  %12d' % (n, c))
    print('')
    print('SIGMA_VALUES_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    sigma_test()
    timestamp()
