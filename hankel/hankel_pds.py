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

from r8lib.r8mat_print import r8mat_print
from r8lib.r8vec_uniform_01 import r8vec_uniform_01
from r8lib.r8mat_cholesky_factor import r8mat_cholesky_factor


def hankel_pds_cholesky_lower(n, lii, liim1):

    # *****************************************************************************80
    #
    # HANKEL_PDS_CHOLESKY_LOWER returns L such that L*L' is Hankel PDS.
    #
    #  Discussion:
    #
    #    In other words, H = L * L' is a positive definite symmetric matrix
    #    with the property that H is constant along antidiagonals, so that
    #
    #      H(I+J) = h(k-1), for 1 <= I, J <= N, 1 <= K <= 2*N-1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 January 2017
    #
    #  Author:
    #
    #    S Al-Homidan, M Alshahrani.
    #    Python implementation by John Burkardt.
    #
    #  Reference:
    #
    #    S Al-Homidan, M Alshahrani,
    #    Positive Definite Hankel Matrices Using Cholesky Factorization,
    #    Computational Methods in Applied Mathematics,
    #    Volume 9, Number 3, pages 221-225, 2009.
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real LII(N), values to be used in L(I,I), for 1 <= I <= N.
    #
    #    Input, real LIIM1(N-1), values to be used in L(I+1,I) for 1 <= I <= N-1.
    #
    #    Output, real L(N,N), the lower Cholesky factor.
    #

    l = np.zeros([n, n])

    for i in range(0, n):
        l[i, i] = lii[i]

    for i in range(0, n - 1):
        l[i + 1, i] = liim1[i]

    for i in range(2, n):
        for j in range(0, i - 1):

            if (((i + j) % 2) == 0):
                q = int((i + j) / 2)
                r = q
            else:
                q = int((i + j - 1) / 2)
                r = q + 1

            alpha = 0.0
            for s in range(0, q + 1):
                alpha = alpha + l[q, s] * l[r, s]

            beta = 0.0
            for t in range(0, j):
                beta = beta + l[i, t] * l[j, t]

            l[i, j] = (alpha - beta) / l[j, j]

    return l


def hankel_pds_cholesky_lower_test01():

    # *****************************************************************************80
    #
    # HANKEL_PDS_CHOLESKY_LOWER_TEST01 tests HANKEL_PDS_CHOLESKY_LOWER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('HANKEL_PDS_CHOLESKY_LOWER_TEST01')
    print('  HANKEL_PDS_CHOLESKY_LOWER computes a lower Cholesky')
    print('  matrix L such that the matrix H = L * L\' is a')
    print('  positive definite (symmetric) Hankel matrix.')

    n = 5
    lii = np.ones(n)
    liim1 = np.ones(n - 1)

    l = hankel_pds_cholesky_lower(n, lii, liim1)

    r8mat_print(n, n, l, '  The Cholesky factor L:')

    h = np.dot(l, l.transpose())

    r8mat_print(n, n, h, '  The Hankel matrix H = L * L\':')

    n = 5
    lii = np.zeros(n)
    for i in range(0, n):
        lii[i] = float(i + 1)

    liim1 = np.zeros(n - 1)
    for i in range(0, n - 1):
        liim1[i] = n - float(i + 1)

    l = hankel_pds_cholesky_lower(n, lii, liim1)

    r8mat_print(n, n, l, '  The Cholesky factor L:')

    h = np.dot(l, l.transpose())

    r8mat_print(n, n, h, '  The Hankel matrix H = L * L\':')

    n = 5
    seed = 123456789
    lii, seed = r8vec_uniform_01(n, seed)
    liim1, seed = r8vec_uniform_01(n - 1, seed)

    l = hankel_pds_cholesky_lower(n, lii, liim1)

    r8mat_print(n, n, l, '  The Cholesky factor L:')

    h = np.dot(l, l.transpose())

    r8mat_print(n, n, h, '  The Hankel matrix H = L * L\':')


def hankel_pds_cholesky_lower_test02():

    # *****************************************************************************80
    #
    # HANKEL_PDS_CHOLESKY_LOWER_TEST02 tests HANKEL_PDS_CHOLESKY_LOWER.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('HANKEL_PDS_CHOLESKY_LOWER_TEST02')
    print('  HANKEL_PDS_CHOLESKY_LOWER computes a lower Cholesky')
    print('  matrix L such that the matrix H = L * L\' is a')
    print('  positive definite (symmetric) Hankel matrix.')

    n = 5
    lii = np.ones(n)
    liim1 = np.ones(n - 1)

    l = hankel_pds_cholesky_lower(n, lii, liim1)

    r8mat_print(n, n, l, '  The Cholesky factor L:')

    h = np.dot(l, l.transpose())

    r8mat_print(n, n, h, '  The Hankel matrix H = L * L\':')

    l2, flag = r8mat_cholesky_factor(n, h)

    r8mat_print(n, n, l2, '  The Cholesky factor L2 of H:')

    h2 = np.dot(l2, l2.transpose())

    r8mat_print(n, n, h2, '  The Hankel matrix H2 = L2 * L2\':')


def hankel_pds_test():

    # *****************************************************************************80
    #
    # HANKEL_PDS_TEST tests HANKEL_PDS.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    26 January 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('HANKEL_PDS_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the HANKEL_PDS library.')

    hankel_pds_cholesky_lower_test01()
    hankel_pds_cholesky_lower_test02()

    print('')
    print('HANKEL_PDS_TEST')
    print('  Normal end of execution.')
    print('')


if (__name__ == '__main__'):
    timestamp()
    hankel_pds_test()
    timestamp()
