#! /usr/bin/env python3
#

import numpy as np
import matplotlib.pyplot as plt
import platform
import time
import sys
import os
import math
from mpl_toolkits.mplot3d import Axes3D
from sys import exit

sys.path.append(os.path.join("../"))
from base import plot2d, plotocc
from timestamp.timestamp import timestamp

from i4lib.i4vec_print import i4vec_print
from i4lib.i4mat_print import i4mat_print, i4mat_print_some
from r8lib.r8vec_print import r8vec_print
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write

from i4lib.i4_gcd import i4_gcd
from i4lib.i4_huge import i4_huge


def frobenius_number_order2(c1, c2):

    # *****************************************************************************80
    #
    # FROBENIUS_NUMBER_ORDER2 returns the Frobenius number for order 2.
    #
    #  Discussion:
    #
    #    The Frobenius number of order N is the solution of the Frobenius
    #    coin sum problem for N coin denominations.
    #
    #    The Frobenius coin sum problem assumes the existence of
    #    N coin denominations, and asks for the largest value that cannot
    #    be formed by any combination of coins of these denominations.
    #
    #    The coin denominations are assumed to be distinct positive integers.
    #
    #    For general N, this problem is fairly difficult to handle.
    #
    #    For N = 2, it is known that:
    #
    #    * if C1 and C2 are not relatively prime, then
    #      there are infinitely large values that cannot be formed.
    #
    #    * otherwise, the largest value that cannot be formed is
    #      C1 * C2 - C1 - C2, and that exactly half the values between
    #      1 and C1 * C2 - C1 - C2 + 1 cannot be represented.
    #
    #    As a simple example, if C1 = 2 and C2 = 7, then the largest
    #    unrepresentable value is 5, and there are (5+1)/2 = 3
    #    unrepresentable values, namely 1, 3, and 5.
    #
    #    For a general N, and a set of coin denominations C1, C2, ..., CN,
    #    the Frobenius number F(N, C(1:N) ) is defined as the largest value
    #    B for which the equation
    #
    #      C1*X1 + C2*X2 + ... + CN*XN = B
    #
    #    has no nonnegative integer solution X(1:N).
    #
    #    In the Mathematica Package "NumberTheory", the Frobenius number
    #    can be determined by
    #
    #    <<NumberTheory`Frobenius`
    #    FrobeniusF[ {C1,...,CN} ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    James Sylvester,
    #    Question 7382,
    #    Mathematical Questions with their Solutions,
    #    Educational Times,
    #    Volume 41, page 21, 1884.
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
    #    Input, integer C1, C2, the coin denominations. C1 and C2
    #    should be positive and relatively prime.
    #
    #    Output, integer FROBENIUS_NUMBER_ORDER2, the Frobenius number of (C1,C2).
    #

    if (c1 <= 0):
        value = i4_huge()
    elif (c2 <= 0):
        value = i4_huge()
    elif (i4_gcd(c1, c2) != 1):
        value = i4_huge()
    else:
        value = c1 * c2 - c1 - c2

    return value


def frobenius_number_order2_test():

    # *****************************************************************************80
    #
    # FROBENIUS_NUMBER_ORDER2_TEST tests FROBENIUS_NUMBER_ORDER2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    08 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('FROBENIUS_NUMBER_ORDER2_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  FROBENIUS_NUMBER_ORDER2 computes Frobenius numbers of order 2.')
    print('')
    print('        C1        C1   exact F  computed F')
    print('')

    n_data = 0

    while (True):

        n_data, c1, c2, f1 = frobenius_number_order2_values(n_data)

        if (n_data == 0):
            break

        f2 = frobenius_number_order2(c1, c2)

        print('  %8d  %8d  %8d  %8d' % (c1, c2, f1, f2))

    print('')
    print('FROBENIUS_NUMBER_ORDER2_TEST:')
    print('  Normal end of execution.')
    return


def frobenius_number_order2_values(n_data):

    # *****************************************************************************80
    #
    # FROBENIUS_NUMBER_ORDER2_VALUES returns values of the order 2 Frobenius number.
    #
    #  Discussion:
    #
    #    The Frobenius number of order N is the solution of the Frobenius
    #    coin sum problem for N coin denominations.
    #
    #    The Frobenius coin sum problem assumes the existence of
    #    N coin denominations, and asks for the largest value that cannot
    #    be formed by any combination of coins of these denominations.
    #
    #    The coin denominations are assumed to be distinct positive integers.
    #
    #    For general N, this problem is fairly difficult to handle.
    #
    #    For N = 2, it is known that:
    #
    #    * if C1 and C2 are not relatively prime, then
    #      there are infinitely large values that cannot be formed.
    #
    #    * otherwise, the largest value that cannot be formed is
    #      C1 * C2 - C1 - C2, and that exactly half the values between
    #      1 and C1 * C2 - C1 - C2 + 1 cannot be represented.
    #
    #    As a simple example, if C1 = 2 and C2 = 7, then the largest
    #    unrepresentable value is 5, and there are (5+1)/2 = 3
    #    unrepresentable values, namely 1, 3, and 5.
    #
    #    For a general N, and a set of coin denominations C1, C2, ..., CN,
    #    the Frobenius number F(N, C(1:N) ) is defined as the largest value
    #    B for which the equation
    #
    #      C1*X1 + C2*X2 + ... + CN*XN = B
    #
    #    has no nonnegative integer solution X(1:N).
    #
    #    In Mathematica, the Frobenius number can be determined by
    #
    #      FrobeniusNumber[ {C1,...,CN} ]
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Gerard Cornuejols, Regina Urbaniak, Robert Weismantel, Laurence Wolsey,
    #    Decomposition of Integer Programs and of Generating Sets,
    #    in Algorithms - ESA '97,
    #    Lecture Notes in Computer Science 1284,
    #    edited by Rainer Burkard, G Woeginger,
    #    Springer, 1997, pages 92-103,
    #    LC: QA76.9.A43.E83.
    #
    #    Robert Owens,
    #    An Algorithm to Solve the Frobenius Problem,
    #    Mathematics Magazine,
    #    Volume 76, Number 4, October 2003, 264-275.
    #
    #    James Sylvester,
    #    Question 7382,
    #    Mathematical Questions with their Solutions,
    #    Educational Times,
    #    Volume 41, page 21, 1884.
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
    #    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
    #    first call.  On each call, the routine increments N_DATA by 1, and
    #    returns the corresponding data; when there is no more data, the
    #    output value of N_DATA will be 0 again.
    #
    #    Output, integer C1, C2, the parameters of the function.
    #
    #    Output, integer F, the value of the function.
    #

    n_max = 6

    c1_vec = np.array((2, 3, 4, 5, 12, 99))
    c2_vec = np.array((5, 17, 19, 13, 11, 100))
    f_vec = np.array((3, 31, 53, 47, 109, 9701))

    if (n_data < 0):
        n_data = 0

    if (n_max <= n_data):
        n_data = 0
        c1 = 0
        c2 = 0
        f = 0
    else:
        c1 = c1_vec[n_data]
        c2 = c2_vec[n_data]
        f = f_vec[n_data]
        n_data = n_data + 1

    return n_data, c1, c2, f


def frobenius_number_order2_values_test():

    # *****************************************************************************80
    #
    # FROBENIUS_NUMBER_ORDER2_VALUES_TEST tests FROBENIUS_NUMBER_ORDER2_VALUES.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    23 November 2014
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('FROBENIUS_NUMBER_ORDER2_VALUES_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  FROBENIUS_NUMBER_ORDER2_VALUES returns values of')
    print('  the Frobenius number of order 2.')
    print('')
    print('         C1        C2          F(C1,C2)')
    print('')

    n_data = 0

    while (True):

        n_data, c1, c2, f = frobenius_number_order2_values(n_data)

        if (n_data == 0):
            break

        print('  %8d  %8d  %8d' % (c1, c2, f))

    print('')
    print('FROBENIUS_NUMBER_ORDER2_VALUES_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    timestamp()
    frobenius_number_order2_values_test()
    frobenius_number_order2_test()
    timestamp()
