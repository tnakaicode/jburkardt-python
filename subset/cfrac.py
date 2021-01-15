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


def cfrac_to_rat(n, a):

    # *****************************************************************************80
    #
    # CFRAC_TO_RAT converts a monic continued fraction to an ordinary fraction.
    #
    #  Discussion:
    #
    #    The routine is given the monic or "simple" continued fraction with
    #    integer coefficients:
    #
    #      A(1) + 1 / ( A(2) + 1 / ( A(3) ... + 1 / A(N) ) )
    #
    #    and returns the N successive approximants P(I)/Q(I)
    #    to the value of the rational number represented by the continued
    #    fraction, with the value exactly equal to the final ratio P(N)/Q(N).
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 May 2015
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
    #    Input, integer N, the number of continued fraction coefficients.
    #
    #    Input, integer A(N), the continued fraction coefficients.
    #
    #    Output, integer P(N), Q(N), the N successive approximations
    #    to the value of the continued fraction.
    #

    p = np.zeros(n)
    q = np.zeros(n)

    for i in range(0, n):

        if (i == 0):
            p[i] = a[i] * 1 + 0
            q[i] = a[i] * 0 + 1
        elif (i == 1):
            p[i] = a[i] * p[i - 1] + 1
            q[i] = a[i] * q[i - 1] + 0
        else:
            p[i] = a[i] * p[i - 1] + p[i - 2]
            q[i] = a[i] * q[i - 1] + q[i - 2]

    return p, q


def cfrac_to_rat_test():

    # *****************************************************************************80
    #
    # % CFRAC_TO_RAT_TEST tests CFRAC_TO_RAT.
    #
    #  Discussion:
    #
    #    Compute the continued fraction form of 4096/15625.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    28 May 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 10

    print('')
    print('CFRAC_TO_RAT_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CFRAC_TO_RAT continued fraction => fraction.')
    print('')

    top = 4096
    bot = 15625

    print('  Regular fraction is %6d / %6d' % (top, bot))

    n, a = rat_to_cfrac(top, bot)

    i4vec_print(n, a, '  Continued fraction coefficients:')

    p, q = cfrac_to_rat(n, a)

    print('')
    print('  The continued fraction convergents.')
    print('  The last row contains the value of the continued')
    print('  fraction, written as a common fraction.')
    print('')
    print('  I, P(I), Q(I), P(I)/Q(I)')
    print('')

    for i in range(0, n):
        print('  %3d  %6d  %6d  %14f' % (i, p[i], q[i], p[i] / q[i]))
    print('')
    print('CFRAC_TO_RAT_TEST')
    print('  Normal end of execution.')


def cfrac_to_rfrac(m, g, h):

    # *****************************************************************************80
    #
    # CFRAC_TO_RFRAC converts a polynomial fraction from continued to rational form.
    #
    #  Discussion:
    #
    #    The routine accepts a continued polynomial fraction:
    #
    #      G(1)     / ( H(1) +
    #      G(2) * X / ( H(2) +
    #      G(3) * X / ( H(3) + ...
    #      G(M) * X / ( H(M) )...) ) )
    #
    #    and returns the equivalent rational polynomial fraction:
    #
    #      P(1) + P(2) * X + ... + P(L1) * X^(L1)
    #      -------------------------------------------------------
    #      Q(1) + Q(2) * X + ... + Q(L2) * X^(L2-1)
    #
    #    where
    #
    #      L1 = (M+1)/2
    #      L2 = (M+2)/2.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 June 2015
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
    #    Input, integer M, the number of continued fraction polynomial coefficients.
    #
    #    Input, real G(M), H(M), the continued polynomial fraction coefficients.
    #
    #    Output, real P((M+1)/2), Q((M+2)/2), the rational polynomial fraction
    #    coefficients.
    #

    phi = (m + 1) // 2
    qhi = (m + 2) // 2

    p = np.zeros(phi)
    q = np.zeros(qhi)

    if (m == 1):
        p[0] = g[0]
        q[0] = h[0]
        return p, q

    #
    #  Solve for P's.
    #
    a = np.zeros([m, qhi])
    a[0, 0] = g[0]
    a[1, 0] = g[0] * h[1]

    for i in range(3, m + 1):
        a[i - 1, 0] = h[i - 1] * a[i - 2, 0]
        jhi = ((i + 1) // 2)
        for j in range(2, jhi + 1):
            a[i - 1, j - 1] = h[i - 1] * \
                a[i - 2, j - 1] + g[i - 1] * a[i - 3, j - 2]

    for j in range(1, phi + 1):
        p[j - 1] = a[m - 1, j - 1]

    #
    #  Solve for Q's.
    #
    a[0, 0] = h[0]
    a[1, 0] = h[0] * h[1]
    a[1, 1] = g[1]

    for i in range(3, m + 1):
        a[i - 1, 0] = h[i - 1] * a[i - 2, 0]
        jhi = ((i + 2) // 2)
        for j in range(2, jhi + 1):
            a[i - 1, j - 1] = h[i - 1] * \
                a[i - 2, j - 1] + g[i - 1] * a[i - 3, j - 2]

    for j in range(1, qhi + 1):
        q[j - 1] = a[m - 1, j - 1]

    return p, q


def cfrac_to_rfrac_test():

    # *****************************************************************************80
    #
    # CFRAC_TO_RFRAC_TEST tests CFRAC_TO_RFRAC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    maxm = 10
    m = 3

    p = np.array([1.0, 1.0, 2.0])
    q = np.array([1.0, 3.0, 1.0, 1.0])

    print('')
    print('CFRAC_TO_RFRAC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  CFRAC_TO_RFRAC: continued fraction to rational polynomial fraction.')

    r8vec_print(m, p, '  Rational polynomial numerator coefficients:')
    r8vec_print(m + 1, q, '  Rational polynomial numerator coefficients:')

    h = rfrac_to_cfrac(m, p, q)

    r8vec_print(2 * m, h, '  Continued fraction coefficients:')

    g = np.ones(2 * m)

    p2, q2 = cfrac_to_rfrac(2 * m, g, h)

    r8vec_print(m, p2, '  Recovered rational polynomial numerator coefficients:')
    r8vec_print(
        m + 1, q2, '  Recovered rational polynomial numerator coefficients:')

    print('')
    print('CFRAC_TO_RFRAC_TEST')
    print('  Normal end of execution.')


def rat_to_cfrac(p, q):

    # *****************************************************************************80
    #
    # RAT_TO_CFRAC converts a rational value to a continued fraction.
    #
    #  Discussion:
    #
    #    The routine is given a rational number represented by P/Q, and
    #    computes the monic or "simple" continued fraction representation
    #    with integer coefficients of the number:
    #
    #      A(1) + 1/ (A(2) + 1/ (A(3) + ... + 1/A(N) ...))
    #
    #    The user must dimension A to a value M which is "large enough".
    #    The actual number of terms needed in the continued fraction
    #    representation cannot be known beforehand.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    17 August 2004
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
    #    Input, integer P, Q, the numerator and denominator of the
    #    rational value whose continued fraction representation is
    #    desired.
    #
    #    Output, integer N, the number of entries in A.
    #
    #    Output, integer A(N), contains the continued fraction
    #    representation of the number.
    #

    b = []

    n = 0

    while (True):

        b.append(p // q)
        n = n + 1
        p = (p % q)

        if (p == 0):
            break

        b.append(q // p)
        n = n + 1
        q = (q % p)

        if (q == 0):
            break

    a = np.zeros(n)
    for i in range(0, n):
        a[i] = b[i]

    return n, a


def rat_to_cfrac_test():

    # *****************************************************************************80
    #
    # RAT_TO_CFRAC_TEST tests RAT_TO_CFRAC.
    #
    #  Discussion:
    #
    #    Compute the continued fraction form of 4096/15625.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 April 2009
    #
    #  Author:
    #
    #    John Burkardt
    #

    m = 10

    print('')
    print('RAT_TO_CFRAC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RAT_TO_CFRAC fraction => continued fraction,')
    print('')

    top = 4096
    bot = 15625

    print('  Regular fraction is %6d / %6d' % (top, bot))

    n, a = rat_to_cfrac(top, bot)

    i4vec_print(n, a, '  Continued fraction coefficients:')

    p, q = cfrac_to_rat(n, a)

    print('')
    print('  The continued fraction convergents.')
    print('  The last row contains the value of the continued')
    print('  fraction, written as a common fraction.')
    print('')
    print('  I, P(I), Q(I), P(I)/Q(I)')
    print('')

    for i in range(0, n):
        print('  %3d  %6d  %6d  %14f' % (i, p[i], q[i], p[i] / q[i]))

    print('')
    print('RAT_TO_CFRAC_TEST')
    print('  Normal end of execution.')


def rfrac_to_cfrac(m, p, q):

    # *****************************************************************************80
    #
    # RFRAC_TO_CFRAC converts a rational polynomial fraction to a continued fraction.
    #
    #  Discussion:
    #
    #    That is, it accepts
    #
    #      P(1) + P(2) * X + ... + P(M) * X^(M-1)
    #      -------------------------------------------------------
    #      Q(1) + Q(2) * X + ... + Q(M) * X^(M-1) + Q(M+1) * X^M
    #
    #    and returns the equivalent continued fraction:
    #
    #      1 / ( T(1) + X / ( T(2) + X / (...T(2*M-1) + X / ( T(2*M) ... )))
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 June 2015
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
    #    Input, integer M, defines the number of P coefficients,
    #    and is one less than the number of Q coefficients, and one
    #    half the number of T coefficients.
    #
    #    Input, real P(M), Q(M+1), the coefficients defining the rational
    #    polynomial fraction.
    #
    #    Output, real T(2*M), the coefficients defining the continued fraction.
    #

    a = np.zeros([m + 1, 2 * m + 1])
    t = np.zeros(2 * m)

    for i in range(0, m + 1):
        a[i, 0] = q[i]

    for i in range(0, m):
        a[i, 1] = p[i]

    t[0] = a[0, 0] / a[0, 1]
    ta = a[m, 0]

    for i in range(1, m + 1):
        a[m - i, 2 * i] = ta

    for k in range(1, 2 * m - 1):

        ihi = (2 * m - k) // 2

        for i in range(1, ihi + 1):
            a[i - 1, k + 1] = a[i, k - 1] - t[k - 1] * a[i, k]

        if (a[0, k + 1] == 0.0):
            print('')
            print('RFRAC_TO_CFRAC - Fatal error!')
            print('  A(1,K+2) is zero for K = %d' % (k))
            exit('RFRAC_TO_CFRAC - Fatal error!')

        t[k] = a[0, k] / a[0, k + 1]

    t[2 * m - 1] = a[0, 2 * m - 1] / a[0, 2 * m]

    return t


def rfrac_to_cfrac_test():

    # *****************************************************************************80
    #
    # RFRAC_TO_CFRAC_TEST tests RFRAC_TO_CFRAC.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    18 June 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    maxm = 10
    m = 3

    p = np.array([1.0, 1.0, 2.0])
    q = np.array([1.0, 3.0, 1.0, 1.0])

    print('')
    print('RFRAC_TO_CFRAC_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  RFRAC_TO_CFRAC: rational polynomial fraction to continued fraction.')

    r8vec_print(m, p, '  Rational polynomial numerator coefficients:')
    r8vec_print(m + 1, q, '  Rational polynomial numerator coefficients:')

    h = rfrac_to_cfrac(m, p, q)

    r8vec_print(2 * m, h, '  Continued fraction coefficients:')

    g = np.ones(2 * m)

    p2, q2 = cfrac_to_rfrac(2 * m, g, h)

    r8vec_print(m, p2, '  Recovered rational polynomial numerator coefficients:')
    r8vec_print(
        m + 1, q2, '  Recovered rational polynomial numerator coefficients:')

    print('')
    print('RFRAC_TO_CFRAC_TEST')
    print('  Normal end of execution.')


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

    print('')
    print('RFRAC_TO_JFRAC_TEST:')
    print('  Normal end of execution.')


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

    print('')
    print('JFRAC_TO_RFRAC_TEST:')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    cfrac_to_rat_test()
    cfrac_to_rfrac_test()
    jfrac_to_rfrac_test()
    rat_to_cfrac_test()
    rfrac_to_cfrac_test()
    rfrac_to_jfrac_test()
    timestamp()
