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

from subset.rfrac_to_cfrac import rfrac_to_cfrac


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
    import numpy as np

    phi = (m + 1) // 2
    qhi = (m + 2) // 2

    p = np.zeros(phi)
    q = np.zeros(qhi)

    if (m == 1):
        p[0] = g[0]
        q[0] = h[0]
        return p, q

    a = np.zeros([m, qhi])
#
#  Solve for P's.
#
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
#
#  Terminate.
#
    print('')
    print('CFRAC_TO_RFRAC_TEST')
    print('  Normal end of execution.')
    return


if (__name__ == '__main__'):
    from timestamp import timestamp
    timestamp()
    cfrac_to_rfrac_test()
    timestamp()
