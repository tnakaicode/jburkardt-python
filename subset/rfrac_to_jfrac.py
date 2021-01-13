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

from r8lib.r8vec_uniform_01 import r8vec_uniform_01


def rfrac_to_jfrac(m, p, q):

    # *****************************************************************************80
    #
    # % RFRAC_TO_JFRAC converts a rational polynomial fraction to a J fraction.
    #
    #  Discussion:
    #
    #    The routine accepts
    #
    #    P(1) + P(2) * X + ... + P(M) * X^(M-1)
    #    -------------------------------------------------------
    #    Q(1) + Q(2) * X + ... + Q(M) * X^(M-1) + Q(M+1) * X^M
    #
    #    and returns the equivalent J-fraction:
    #
    #    R(1) / ( X + S(1) +
    #    R(2) / ( X + S(2) +
    #    R(3) / ...        +
    #    R(M) / ( X + S(M) )... ))
    #
    #    Thanks to Henry Amuasi for noticing and correcting an error in a
    #    previous formulation of this routine, 02 October 2010.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt.
    #
    #  Reference:
    #
    #    John Hart, Ward Cheney, Charles Lawson, Hans Maehly, Charles Mesztenyi,
    #    John Rice, Henry Thatcher, Christoph Witzgall,
    #    Computer Approximations,
    #    Wiley, 1968.
    #
    #  Parameters:
    #
    #    Input, integer M, defines the number of P, R, and S coefficients,
    #    and is one less than the number of Q coefficients.
    #    1 <= M.
    #
    #    Input, real P(M), Q(M+1), the coefficients defining the rational
    #    polynomial fraction.
    #
    #    Output, real R(M), S(M), the coefficients defining the
    #    J-fraction.
    #

    if (m < 1):
        print('')
        print('RFRAC_TO_JFRAC - Fatal error!')
        print('  M < 1')
        exit('RFRAC_TO_JFRAC - Fatal error!')

    a = np.zeros([m + 1, m + 1])

    for i in range(0, m + 1):
        a[i, 0] = q[i]

    for i in range(0, m):
        a[i, 1] = p[i]

    r = np.zeros(m)
    s = np.zeros(m)

    if (1 < m):

        r[0] = a[m - 1, 1] / a[m, 0]
        s[0] = (r[0] * a[m - 1, 0] - a[m - 2, 1]) / a[m - 1, 1]

        for k in range(0, m - 2):

            a[0, k + 2] = r[k] * a[0, k] - s[k] * a[0, k + 1]

            for i in range(1, m - k - 1):
                a[i, k + 2] = r[k] * a[i, k] - \
                    a[i - 1, k + 1] - s[k] * a[i, k + 1]

            if (a[m - k - 2, k + 2] == 0.0):
                print('')
                print('RFRAC_TO_JFRAC - Fatal error!')
                print('  A(M-K-2,K+2) = 0 for K = %d' % (k))
                exit('RFRAC_TO_JFRAC - Fatal error!')

            r[k + 1] = a[m - k - 2, k + 2] / a[m - k - 1, k + 1]
            s[k + 1] = (r[k + 1] * a[m - k - 2, k + 1] -
                        a[m - k - 3, k + 2]) / a[m - k - 2, k + 2]

        a[0, m] = r[m - 2] * a[0, m - 2] - s[m - 2] * a[0, m - 1]

    r[m - 1] = a[0, m] / a[1, m - 1]
    s[m - 1] = a[0, m - 1] / a[1, m - 1]

    return r, s


def rfrac_to_jfrac_test():

    # *****************************************************************************80
    #
    # RFRAC_TO_JFRAC_TEST tests RFRAC_TO_JFRAC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    #
    #  Generate the data, but force Q(M+1) to be 1.
    #  That will make it easier to see that the two operations are inverses
    #  of each other.  JFRAC_TO_RFRAC is free to scale its output, and chooses
    #  a scaling in which Q(M+1) is 1.
    #
    seed = 123456789
    m = 6
    p, seed = r8vec_uniform_01(m, seed)
    q, seed = r8vec_uniform_01(m + 1, seed)

    t = q[m]
    for i in range(0, m + 1):
        q[i] = q[i] / t

    print('')
    print('RFRAC_TO_JFRAC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RFRAC_TO_JFRAC converts a rational polynomial')
    print('  fraction to a J fraction.')

    r8vec_print(m, p, '  RFRAC P:')
    r8vec_print(m + 1, q, '  RFRAC Q:')

    r, s = rfrac_to_jfrac(m, p, q)

    r8vec_print(m, r, '  JFRAC R:')
    r8vec_print(m, s, '  JFRAC S:')

    p2, q2 = jfrac_to_rfrac(m, r, s)

    r8vec_print(m, p2, '  Recovered RFRAC P:')
    r8vec_print(m + 1, q2, '  Recovered RFRAC Q:')
#
#  Terminate.
#
    print('')
    print('RFRAC_TO_JFRAC_TEST:')
    print('  Normal end of execution.')

    return


def jfrac_to_rfrac(m, r, s):

    # *****************************************************************************80
    #
    # JFRAC_TO_RFRAC converts a J-fraction into a rational polynomial fraction.
    #
    #  Discussion:
    #
    #    The routine accepts a J-fraction:
    #
    #        R(1) / ( X + S(1)
    #      + R(2) / ( X + S(2)
    #      + R(3) / ...
    #      + R(M) / ( X + S(M) )... ))
    #
    #    and returns the equivalent rational polynomial fraction:
    #
    #      P(1) + P(2) * X + ... + P(M) * X^(M-1)
    #      -------------------------------------------------------
    #      Q(1) + Q(2) * X + ... + Q(M) * X^(M-1) + Q(M+1) * X^M
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Hart, Cheney, Lawson, Maehly, Mesztenyi, Rice, Thacher, Witzgall,
    #    Computer Approximations,
    #    Wiley, 1968.
    #
    #  Parameters:
    #
    #    Input, integer M, defines the number of P, R, and S
    #    coefficients, and is one less than the number of Q
    #    coefficients.
    #
    #    Input, real R(M), S(M), the coefficients defining the J-fraction.
    #
    #    Output, real P(M), Q(M+1), the coefficients defining the rational
    #    polynomial fraction.  The algorithm used normalizes the coefficients
    #    so that Q(M+1) = 1.0.
    #

    a = np.zeros([m, m])
    b = np.zeros([m, m])

    a[0, 0] = r[0]
    b[0, 0] = s[0]

    if (1 < m):

        for k in range(1, m):
            a[k, k] = r[0]
            b[k, k] = b[k - 1, k - 1] + s[k]

        a[0, 1] = r[0] * s[1]
        b[0, 1] = r[1] + s[0] * s[1]

        for k in range(2, m):
            a[0, k] = s[k] * a[0, k - 1] + r[k] * a[0, k - 2]
            a[k - 1, k] = a[k - 2, k - 1] + s[k] * r[0]
            b[0, k] = s[k] * b[0, k - 1] + r[k] * b[0, k - 2]
            b[k - 1, k] = b[k - 2, k - 1] + s[k] * b[k - 1, k - 1] + r[k]

        for k in range(3, m):
            for i in range(1, k - 1):
                a[i, k] = a[i - 1, k - 1] + s[k] * \
                    a[i, k - 1] + r[k] * a[i, k - 2]
                b[i, k] = b[i - 1, k - 1] + s[k] * \
                    b[i, k - 1] + r[k] * b[i, k - 2]

    p = np.zeros(m)
    for i in range(0, m):
        p[i] = a[i, m - 1]

    q = np.zeros(m + 1)
    for i in range(0, m):
        q[i] = b[i, m - 1]
    q[m] = 1.0

    return p, q


def jfrac_to_rfrac_test():

    # *****************************************************************************80
    #
    # JFRAC_TO_RFRAC_TEST tests JFRAC_TO_RFRAC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    12 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    #
    #  Generate the data, but force Q(M+1) to be 1.
    #  That will make it easier to see that the two operations are inverses
    #  of each other.  JFRAC_TO_RFRAC is free to scale its output, and chooses
    #  a scaling in which Q(M+1) is 1.
    #
    seed = 123456789
    m = 6
    p, seed = r8vec_uniform_01(m, seed)
    q, seed = r8vec_uniform_01(m + 1, seed)

    t = q[m]
    for i in range(0, m + 1):
        q[i] = q[i] / t

    print('')
    print('JFRAC_TO_RFRAC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  JFRAC_TO_RFRAC converts a J fraction')
    print('  to a rational polynomial fraction.')

    r8vec_print(m, p, '  RFRAC P:')
    r8vec_print(m + 1, q, '  RFRAC Q:')

    r, s = rfrac_to_jfrac(m, p, q)

    r8vec_print(m, r, '  JFRAC R:')
    r8vec_print(m, s, '  JFRAC S:')

    p2, q2 = jfrac_to_rfrac(m, r, s)

    r8vec_print(m, p2, '  Recovered RFRAC P:')
    r8vec_print(m + 1, q2, '  Recovered RFRAC Q:')
#
#  Terminate.
#
    print('')
    print('JFRAC_TO_RFRAC_TEST:')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    rfrac_to_jfrac_test()
    timestamp()
