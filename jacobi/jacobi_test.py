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

obj = plot2d()


def dif2(m, n):

    # *****************************************************************************80
    #
    # DIF2 returns the second difference matrix.
    #
    #  Example:
    #
    #    N = 5
    #
    #    2 -1  .  .  .
    #   -1  2 -1  .  .
    #    . -1  2 -1  .
    #    .  . -1  2 -1
    #    .  .  . -1  2
    #
    #  Rectangular Properties:
    #
    #    A is banded, with bandwidth 3.
    #
    #    A is tridiagonal.
    #
    #    Because A is tridiagonal, it has property A (bipartite).
    #
    #    A is integral: int ( A ) = A.
    #
    #    A is Toeplitz: constant along diagonals.
    #
    #  Square Properties:
    #
    #    A is symmetric: A' = A.
    #
    #    Because A is symmetric, it is normal.
    #
    #    Because A is normal, it is diagonalizable.
    #
    #    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
    #
    #    A is positive definite.
    #
    #    A is an M matrix.
    #
    #    A is weakly diagonally dominant, but not strictly diagonally dominant.
    #
    #    A has an LU factorization A = L * U, without pivoting.
    #
    #      The matrix L is lower bidiagonal with subdiagonal elements:
    #
    #        L(I+1,I) = -I/(I+1)
    #
    #      The matrix U is upper bidiagonal, with diagonal elements
    #
    #        U(I,I) = (I+1)/I
    #
    #      and superdiagonal elements which are all -1.
    #
    #    A has a Cholesky factorization A = L * L', with L lower bidiagonal.
    #
    #      L(I,I) =    sqrt ( (I+1) / I )
    #      L(I,I-1) = -sqrt ( (I-1) / I )
    #
    #    The eigenvalues are
    #
    #      LAMBDA(I) = 2 + 2 * COS(I*PI/(N+1))
    #                = 4 SIN^2(I*PI/(2*N+2))
    #
    #    The corresponding eigenvector X(I) has entries
    #
    #       X(I)(J) = sqrt(2/(N+1)) * sin ( I*J*PI/(N+1) ).
    #
    #    Simple linear systems:
    #
    #      x = (1,1,1,...,1,1),   A*x=(1,0,0,...,0,1)
    #
    #      x = (1,2,3,...,n-1,n), A*x=(0,0,0,...,0,n+1)
    #
    #    det ( A ) = N + 1.
    #
    #    The value of the determinant can be seen by induction,
    #    and expanding the determinant across the first row:
    #
    #      det ( A(N) ) = 2 * det ( A(N-1) ) - (-1) * (-1) * det ( A(N-2) )
    #                = 2 * N - (N-1)
    #                = N + 1
    #
    #    The family of matrices is nested as a function of N.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    21 January 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Reference:
    #
    #    Robert Gregory, David Karney,
    #    Example 3.18,
    #    A Collection of Matrices for Testing Computational Algorithms,
    #    Wiley, New York, 1969, page 45,
    #    LC: QA263.G68.
    #
    #    Morris Newman, John Todd,
    #    Example A8,
    #    The evaluation of matrix inversion programs,
    #    Journal of the Society for Industrial and Applied Mathematics,
    #    Volume 6, Number 4, pages 466-476, 1958.
    #
    #    John Todd,
    #    Example A8,
    #    Basic Numerical Mathematics,
    #    Volume 2: Numerical Algebra,
    #    Academic Press, 1977, page 1.
    #
    #    Joan Westlake,
    #    Test Matrix A15,
    #    A Handbook of Numerical Matrix Inversion and Solution of Linear Equations,
    #    John Wiley, 1968.
    #
    #  Parameters:
    #
    #    Input, integer M, N, the number of rows and columns of A.
    #
    #    Output, real A(M,N), the matrix.
    #

    a = np.zeros([m, n])

    for i in range(0, m):
        if (0 <= i - 1 and i - 1 < n):
            a[i, i - 1] = -1.0
        if (i < n):
            a[i, i] = 2.0
        if (i + 1 < n):
            a[i, i + 1] = -1.0

    return a


def jacobi1(n, a, b, x):

    # *****************************************************************************80
    #
    # JACOBI1 carries out one step of the Jacobi iteration.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 March 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the number of equations.
    #
    #    Input, real A(N,N), the matrix.
    #
    #    Input, real B(N), the right hand side.
    #
    #    Input, real X(N), the estimated solution.
    #
    #    Output, real X_NEW(N), the improved estimate of the solution.
    #

    x_new = np.zeros(n)

    for i in range(0, n):
        x_new[i] = b[i]
        for j in range(0, n):
            if (j != i):
                x_new[i] = x_new[i] - a[i, j] * x[j]
        x_new[i] = x_new[i] / a[i, i]

    return x_new


def jacobi_test01():

    # *****************************************************************************80
    #
    # JACOBI_TEST01 tests JACOBI1.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 March 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('JACOBI_TEST01:')

    it_num = 400
    n = 20

    x_exact = np.zeros(n)
    for i in range(0, n):
        x_exact[i] = float(i + 1)

    a = dif2(n, n)

    b = np.dot(a, x_exact)

    x = np.zeros(n)

    x_plot = np.zeros([n, it_num + 1])
    for i in range(0, n):
        x_plot[i, 0] = x[i]

    step = np.zeros(it_num + 1)
    for i in range(0, it_num + 1):
        step[i] = i + 1

    r = np.zeros(it_num + 1, dtype=np.float)
    r.fill(np.nan)
    r[0] = residual_norm(a, x, b)
    r_log = np.zeros(it_num + 1, dtype=np.float)
    r_log.fill(np.nan)
    r_log[0] = 0.0

    xm = np.zeros(it_num + 1, dtype=np.float)
    xm.fill(np.nan)
    xm[0] = 0.0
    xm_log = np.zeros(it_num + 1, dtype=np.float)
    xm_log.fill(np.nan)
    xm_log[0] = 0.0

    for it in range(1, it_num + 1):

        x_new = jacobi1(n, a, b, x)
        for i in range(0, n):
            x_plot[i, it] = x_new[i]

        #
        #  Display the residual.
        #
        r[it] = residual_norm(a, x, b)
        r_log[it] = np.log(r[it])

        #
        #  Display the motion.
        #
        xm[it] = np.linalg.norm(x_new - x) / n
        xm_log[it] = np.log(xm[it])

        #
        #  Update the solution
        #
        x = x_new.copy()

    #
    #  1: Display the residuals.
    #
    filename = 'jacobi_residual.png'
    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(step, r_log, linewidth=2, color='m')
    obj.axs.set_xlabel('<-- Step -->')
    obj.axs.set_ylabel('<-- Residual -->')
    obj.axs.set_title('Log (Residual)')
    obj.SavePng(filename)

    #
    #  2: Display the motions.
    #
    filename = 'jacobi_motion.png'
    obj.new_2Dfig(aspect="auto")
    obj.axs.plot(step, xm_log, linewidth=2, color='m')
    obj.axs.set_xlabel('<-- Step -->')
    obj.axs.set_ylabel('<-- Motion -->')
    obj.axs.set_title('Log (Average generator motion)')
    obj.SavePng(filename)

    #
    #  3: Plot the evolution of the locations of the generators.
    #
    filename = 'jacobi_evolution.png'
    obj.new_2Dfig(aspect="auto")
    for k in range(0, n):
        obj.axs.plot(x_plot[k, :], step)
    obj.axs.set_xlabel('<-- Generator position -->')
    obj.axs.set_ylabel('<-- Iteration -->')
    obj.axs.set_title('Generator evolution')
    obj.SavePng(filename)


def residual_norm(a, x, b):

    # *****************************************************************************80
    #
    # RESIDUAL_NORM returns the norm of the residual A*x-b.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 March 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real A(N,N), the matrix.
    #
    #    Input, real B(N), the right hand side.
    #
    #    Input, real X(N), the estimated solution.
    #
    #    Output, real VALUE, the norm of A*x-b.
    #

    residual = np.dot(a, x) - b
    value = np.linalg.norm(residual)

    return value


def jacobi_test():

    # *****************************************************************************80
    #
    # JACOBI_TEST tests the JACOBI library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    20 March 2018
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('JACOBI_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the JACOBI library.')

    jacobi_test01()

    print('')
    print('JACOBI_TEST')
    print('  Normal end of execution.')


if (__name__ == '__main__'):
    timestamp()
    jacobi_test()
    timestamp()
