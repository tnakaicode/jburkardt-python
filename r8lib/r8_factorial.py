#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpi4py import MPI
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp


def r8_factorial(n):

    # *****************************************************************************80
    #
    # R8_FACTORIAL returns N factorial.
    #
    #  Discussion:
    #
    #    factorial ( N ) = Product ( 1 <= I <= N ) I
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    03 June 2013
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the argument of the function.
    #    0 <= N.
    #
    #    Output, real VALUE, the factorial of N.
    #
    from sys import exit

    if (n < 0):
        print('')
        print('R8_FACTORIAL - Fatal error!')
        print('  N < 0.')
        exit('R8_FACTORIAL - Fatal error!')

    value = 1.0

    for i in range(2, n + 1):
        value = value * i

    return value


def r8_factorial_test():

    # *****************************************************************************80
    #
    # R8_FACTORIAL_TEST tests R8_FACTORIAL.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('R8_FACTORIAL_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_FACTORIAL evaluates the factorial function.')
    print('')
    print('      N                     Exact                  Computed')

    n_data = 0

    while (True):

        n_data, n, f1 = r8_factorial_values(n_data)

        if (n_data == 0):
            break

        f2 = r8_factorial(n)

        print('  %4d  %24.16g  %24.16g' % (n, f1, f2))
#
#  Terminate.
#
    print('')
    print('R8_FACTORIAL_TEST')
    print('  Normal end of execution.')
    return


def r8_factorial_values(n_data):

    # *****************************************************************************80
    #
    # R8_FACTORIAL_VALUES returns values of the real factorial function.
    #
    #  Discussion:
    #
    #    0! = 1
    #    I! = Product ( 1 <= J <= I ) J
    #
    #    Although the factorial is an integer valued function, it quickly
    #    becomes too large for an integer to hold.  This routine still accepts
    #    an integer as the input argument, but returns the function value
    #    as a real number.
    #
    #    In Mathematica, the function can be evaluated by:
    #
    #      n!
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
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
    #    Output, integer N, the argument of the function.
    #
    #    Output, real FN, the value of the function.
    #
    import numpy as np

    n_max = 25

    fn_vec = np.array([
        0.1000000000000000E+01,
        0.1000000000000000E+01,
        0.2000000000000000E+01,
        0.6000000000000000E+01,
        0.2400000000000000E+02,
        0.1200000000000000E+03,
        0.7200000000000000E+03,
        0.5040000000000000E+04,
        0.4032000000000000E+05,
        0.3628800000000000E+06,
        0.3628800000000000E+07,
        0.3991680000000000E+08,
        0.4790016000000000E+09,
        0.6227020800000000E+10,
        0.8717829120000000E+11,
        0.1307674368000000E+13,
        0.2092278988800000E+14,
        0.3556874280960000E+15,
        0.6402373705728000E+16,
        0.1216451004088320E+18,
        0.2432902008176640E+19,
        0.1551121004333099E+26,
        0.3041409320171338E+65,
        0.9332621544394415E+158,
        0.5713383956445855E+263])

    n_vec = np.array([
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
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        25,
        50,
        100,
        150])

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        n = 0
        fn = 0
    else:
        n = n_vec[n_data]
        fn = fn_vec[n_data]
        n_data = n_data + 1

    return n_data, n, fn


def r8_factorial_values_test():

    # *****************************************************************************80
    #
    # R8_FACTORIAL_VALUES_TEST tests R8_FACTORIAL_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    27 December 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_FACTORIAL_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_FACTORIAL_VALUES returns values of the real factorial function.')
    print('')
    print('          N          R8_FACTORIAL(N)')
    print('')

    n_data = 0

    while (True):

        n_data, n, fn = r8_factorial_values(n_data)

        if (n_data == 0):
            break

        print('  %8d  %14.6g' % (n, fn))
#
#  Terminate.
#
    print('')
    print('R8_FACTORIAL_VALUES_TEST:')
    print('  Normal end of execution.')
    return


def r8_factorial_stirling(n):

    # *****************************************************************************80
    #
    # R8_FACTORIAL_STIRLING computes Stirling's approximation to N!.
    #
    #  Discussion:
    #
    #    N! = Product ( 1 <= I <= N ) I
    #
    #    Stirling ( N ) = sqrt ( 2 * PI * N ) * ( N / E )^N * E^(1/(12*N) )
    #
    #    This routine returns the raw approximation for all nonnegative
    #    values of N.  If N is less than 0, the value is returned as 0,
    #    and if N is 0, the value of 1 is returned.  In all other cases,
    #    Stirling's formula is used.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the argument of the function.
    #
    #    Output, real R8_FACTORIAL_STIRLING, an approximation to N!.
    #
    import numpy as np

    r8_e = 2.71828182845904523

    if (n < 0):

        value = 0.0

    elif (n == 0):

        value = 1.0

    else:

        value = np.sqrt(2.0 * np.pi * n) * (n / r8_e) ** n \
            * np.exp(1.0 / (12 * n))

    return value


def r8_factorial_stirling_test():

    # *****************************************************************************80
    #
    # R8_FACTORIAL_STIRLING_TEST tests R8_FACTORIAL_STIRLING
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    07 April 2016
    #
    #  Author:
    #
    #    John Burkardt
    #
    import platform

    print('')
    print('R8_FACTORIAL_STIRLING_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8_FACTORIAL_STIRLING computes Stirling\'s')
    print('  approximate factorial function')
    print('')
    print('  N      Factorial    Factorial')
    print('         Stirling')
    print('')

    f2 = 1.0
    for i in range(1, 21):
        f1 = r8_factorial_stirling(i)
        f2 = f2 * i
        print('  %6d  %14g  %14g' % (i, f1, f2))

    print('')
    print('R8_FACTORIAL_STIRLING_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    r8_factorial_test()
    timestamp()
