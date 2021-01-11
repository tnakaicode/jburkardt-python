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

from r8lib.r8vec_print import r8vec_print
from r8lib.r8vec_uniform_01 import r8vec_uniform_01
from r8lib.r8mat_print import r8mat_print
from r8lib.r8mat_uniform_01 import r8mat_uniform_01
from r8lib.r8mat_diff_frobenius import r8mat_diff_frobenius


def haar_1d(n, x):

    # *****************************************************************************80
    #
    # HAAR_1D computes the Haar transform of a vector.
    #
    #  Discussion:
    #
    #    For the classical Haar transform, N should be a power of 2.
    #    However, this is not required here.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, int N, the dimension of the vector.
    #
    #    Input, double X[N], the vector to be transformed.
    #
    #    Output, double U[N], the transformed vector.
    #

    u = x.copy()
    s = np.sqrt(2.0)
    v = np.zeros(n, dtype=np.float64)

    #
    #  Determine K, the largest power of 2 such that K <= N.
    #
    k = 1
    while (k * 2 <= n):
        k = k * 2

    while (1 < k):
        k = k // 2
        v[0:k] = (u[0:2 * k - 1:2] + u[1:2 * k:2]) / s
        v[k:2 * k] = (u[0:2 * k - 1:2] - u[1:2 * k:2]) / s
        u[0:2 * k] = v[0:2 * k].copy()

    return u


def haar_1d_inverse(n, x):

    # *****************************************************************************80
    #
    # HAAR_1D_INVERSE computes the inverse Haar transform of a vector.
    #
    #  Discussion:
    #
    #    For the classical Haar transform, N should be a power of 2.
    #    However, this is not required here.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, int N, the dimension of the vector.
    #
    #    Input, double X[N], the vector to be transformed.
    #
    #    Output, double U[N], the transformed vector.
    #

    u = x.copy()
    s = np.sqrt(2.0)
    v = np.zeros(n)
    k = 1
    while (k * 2 <= n):
        v[0:2 * k - 1:2] = (u[0:k] + u[0 + k:k + k]) / s
        v[1:2 * k:2] = (u[0:k] - u[0 + k:k + k]) / s
        u[0:2 * k] = v[0:2 * k].copy()
        k = k * 2

    return u


def haar_1d_test():

    # *****************************************************************************80
    #
    # HAAR_1D_TEST tests HAAR_1D.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('HAAR_1D_TEST')
    print('  HAAR_1D computes the Haar transform of a vector.')

    #
    #  Random data.
    #
    n = 16
    seed = 123456789
    u, seed = r8vec_uniform_01(n, seed)
    v = haar_1d(n, u)
    w = haar_1d_inverse(n, v)

    print('')
    print('   i      U(i)        H(U)(i)  Hinv(H(U))(i)')
    print('')
    for i in range(0, n):
        print('  %2d  %10f  %10f  %10f' % (i, u[i], v[i], w[i]))

    #
    #  Constant signal.
    #
    n = 8
    u = np.ones(n)
    v = haar_1d(n, u)
    w = haar_1d_inverse(n, v)

    print('')
    print('   i      U(i)        H(U)(i)  Hinv(H(U))(i)')
    print('')
    for i in range(0, n):
        print('  %2d  %10f  %10f  %10f' % (i, u[i], v[i], w[i]))

    #
    #  Linear signal.
    #
    n = 16
    u = np.linspace(1, n, n)
    v = haar_1d(n, u)
    w = haar_1d_inverse(n, v)

    print('')
    print('   i      U(i)        H(U)(i)  Hinv(H(U))(i)')
    print('')
    for i in range(0, n):
        print('  %2d  %10f  %10f  %10f' % (i, u[i], v[i], w[i]))

    #
    #  Quadratic data.
    #
    n = 8
    u = np.array([
        25.0, 16.0, 9.0, 4.0, 1.0,
        0.0, 1.0, 4.0])
    v = haar_1d(n, u)
    w = haar_1d_inverse(n, v)

    print('')
    print('   i      U(i)        H(U)(i)  Hinv(H(U))(i)')
    print('')
    for i in range(0, n):
        print('  %2d  %10f  %10f  %10f' % (i, u[i], v[i], w[i]))

    #
    #  N not a power of 2.
    #
    n = 99
    seed = 123456789
    u, seed = r8vec_uniform_01(n, seed)
    v = haar_1d(n, u)
    w = haar_1d_inverse(n, v)

    print('')
    print('   i      U(i)        H(U)(i)  Hinv(H(U))(i)')
    print('')
    for i in range(0, n):
        print('  %2d  %10f  %10f  %10f' % (i, u[i], v[i], w[i]))


def haar_2d(m, n, x):

    # *****************************************************************************80
    #
    # HAAR_2D computes the Haar transform of an array.
    #
    #  Discussion:
    #
    #    For the classical Haar transform, M and N should be a power of 2.
    #    However, this is not required here.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, int M, N, the dimensions of the array.
    #
    #    Input, double X[M*N], the array to be transformed.
    #
    #    Output, double U[M*N], the transformed array.
    #

    u = x.copy()
    s = np.sqrt(2.0)
    v = u.copy()

    #
    #  Determine K, the largest power of 2 such that K <= M.
    #
    k = 1
    while (k * 2 <= m):
        k = k * 2

    #
    #  Transform all columns.
    #
    while (1 < k):
        k = k // 2
        v[0: k, 0:n] = (u[0:2 * k - 1:2, 0:n] + u[1:2 * k:2, 0:n]) / s
        v[k + 0:k + k, 0:n] = (u[0:2 * k - 1:2, 0:n] - u[1:2 * k:2, 0:n]) / s
        u[0:2 * k, 0:n] = v[0:2 * k, 0:n].copy()

    #
    #  Determine K, the largest power of 2 such that K <= N.
    #
    k = 1
    while (k * 2 <= n):
        k = k * 2

    #
    #  Transform all rows.
    #
    while (1 < k):
        k = k // 2
        v[0:m, 0: k] = (u[0:m, 0:2 * k - 1:2] + u[0:m, 1:2 * k:2]) / s
        v[0:m, k + 0:k + k] = (u[0:m, 0:2 * k - 1:2] - u[0:m, 1:2 * k:2]) / s
        u[0:m, 0:2 * k] = v[0:m, 0:2 * k].copy()

    return u


def haar_2d_inverse(m, n, x):

    # *****************************************************************************80
    #
    # HAAR_2D_INVERSE inverts the Haar transform of an array.
    #
    #  Discussion:
    #
    #    For the classical Haar transform, M and N should be a power of 2.
    #    However, this is not required here.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, int M, N, the dimensions of the array.
    #
    #    Input, double X[M*N], the array to be transformed.
    #
    #    Output, double U[M*N], the transformed array.
    #

    u = x.copy()
    s = np.sqrt(2.0)
    v = u.copy()
    #
    #  Inverse transform of all rows.
    #
    k = 1
    while (k * 2 <= n):
        v[0:m, 0:2 * k - 1:2] = (u[0:m, 0:k] + u[0:m, 0 + k:k + k]) / s
        v[0:m, 1:2 * k:2] = (u[0:m, 0:k] - u[0:m, 0 + k:k + k]) / s
        u[0:m, 0:2 * k] = v[0:m, 0:2 * k].copy()
        k = k * 2

    #
    #  Inverse transform of all columns.
    #
    k = 1
    while (k * 2 <= m):
        v[0:2 * k - 1:2, 0:n] = (u[0:k, 0:n] + u[0 + k:k + k, 0:n]) / s
        v[1:2 * k:2, 0:n] = (u[0:k, 0:n] - u[0 + k:k + k, 0:n]) / s
        u[0:2 * k, 0:n] = v[0:2 * k, 0:n].copy()
        k = k * 2

    return u


def haar_2d_test():

    # *****************************************************************************80
    #
    # HAAR_2D_TEST tests HAAR_2D..
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #
    print('')
    print('HAAR_2D_TEST')
    print('  HAAR_2D computes the Haar transform of an array.')
    print('  HAAR_2D_INVERSE inverts the transform.')

    #
    #  Demonstrate successful inversion.
    #
    m = 16
    n = 4
    seed = 123456789
    u, seed = r8mat_uniform_01(m, n, seed)
    r8mat_print(m, n, u, '  Input array U:')

    v = haar_2d(m, n, u)
    r8mat_print(m, n, v, '  Transformed array V:')

    w = haar_2d_inverse(m, n, v)
    r8mat_print(m, n, w, '  Recovered array W:')

    #
    #  M, N not powers of 2.
    #
    m = 37
    n = 53
    seed = 123456789
    u, seed = r8mat_uniform_01(m, n, seed)
    v = haar_2d(m, n, u)
    w = haar_2d_inverse(m, n, v)
    err = r8mat_diff_frobenius(m, n, u, w)

    print('')
    print('  M = %d, N = %d, ||haar_2d_inverse(haar_2d(u))-u|| = %g'
          % (m, n, err))


def haar_test():

    # *****************************************************************************80
    #
    # HAAR_TEST tests the HAAR library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 August 2017
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('HAAR_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the HAAR library.')

    haar_1d_test()
    haar_2d_test()

    print('')
    print('HAAR_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    haar_test()
    timestamp()
