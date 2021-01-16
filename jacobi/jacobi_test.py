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
from i4lib.i4mat_print import i4mat_print
from r8lib.r8vec_print import r8vec_print, r8vec_print_some
from r8lib.r8mat_print import r8mat_print, r8mat_print_some
from r8lib.r8mat_write import r8mat_write
from r8lib.r8mat_mm import r8mat_mm
from r8lib.r8mat_norm_fro import r8mat_norm_fro

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


def jacobi_eigenvalue(n, a, it_max):

    # *****************************************************************************80
    #
    # JACOBI_EIGENVALUE carries out the Jacobi eigenvalue iteration.
    #
    #  Discussion:
    #
    #    This function computes the eigenvalues and eigenvectors of a
    #    real symmetric matrix, using Rutishauser's modfications of the classical
    #    Jacobi rotation method with threshold pivoting.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, real A(N,N), the matrix, which must be square, real,
    #    and symmetric.
    #
    #    Input, integer IT_MAX, the maximum number of iterations.
    #
    #    Output, real V(N,N), the matrix of eigenvectors.
    #
    #    Output, real D(N), the eigenvalues, in descending order.
    #
    #    Output, integer IT_NUM, the total number of iterations.
    #
    #    Output, integer ROT_NUM, the total number of rotations.
    #

    v = np.zeros([n, n])
    d = np.zeros(n)

    for j in range(0, n):
        for i in range(0, n):
            v[i, j] = 0.0
        v[j, j] = 1.0

    for i in range(0, n):
        d[i] = a[i, i]

    bw = np.zeros(n)
    zw = np.zeros(n)
    w = np.zeros(n)

    for i in range(0, n):
        bw[i] = d[i]

    it_num = 0
    rot_num = 0

    while (it_num < it_max):

        it_num = it_num + 1
        #
        #  The convergence threshold is based on the size of the elements in
        #  the strict upper triangle of the matrix.
        #
        thresh = 0.0
        for j in range(0, n):
            for i in range(0, j):
                thresh = thresh + a[i, j] ** 2

        thresh = np.sqrt(thresh) / float(4 * n)

        if (thresh == 0.0):
            break

        for p in range(0, n):
            for q in range(p + 1, n):

                gapq = 10.0 * abs(a[p, q])
                termp = gapq + abs(d[p])
                termq = gapq + abs(d[q])

                #
                #  Annihilate tiny offdiagonal elements.
                #
                if (4 < it_num and termp == abs(d[p]) and termq == abs(d[q])):

                    a[p, q] = 0.0
                #
                #  Otherwise, apply a rotation.
                #
                elif (thresh <= abs(a[p, q])):

                    h = d[q] - d[p]
                    term = abs(h) + gapq

                    if (term == abs(h)):
                        t = a[p, q] / h
                    else:
                        theta = 0.5 * h / a[p, q]
                        t = 1.0 / (abs(theta) + np.sqrt(1.0 + theta * theta))
                        if (theta < 0.0):
                            t = - t

                    c = 1.0 / np.sqrt(1.0 + t * t)
                    s = t * c
                    tau = s / (1.0 + c)
                    h = t * a[p, q]
                    #
                    #  Accumulate corrections to diagonal elements.
                    #
                    zw[p] = zw[p] - h
                    zw[q] = zw[q] + h
                    d[p] = d[p] - h
                    d[q] = d[q] + h

                    a[p, q] = 0.0
                    #
                    #  Rotate, using information from the upper triangle of A only.
                    #
                    for j in range(0, p):
                        g = a[j, p]
                        h = a[j, q]
                        a[j, p] = g - s * (h + g * tau)
                        a[j, q] = h + s * (g - h * tau)

                    for j in range(p + 1, q):
                        g = a[p, j]
                        h = a[j, q]
                        a[p, j] = g - s * (h + g * tau)
                        a[j, q] = h + s * (g - h * tau)

                    for j in range(q + 1, n):
                        g = a[p, j]
                        h = a[q, j]
                        a[p, j] = g - s * (h + g * tau)
                        a[q, j] = h + s * (g - h * tau)

                    #
                    #  Accumulate information in the eigenvector matrix.
                    #
                    for j in range(0, n):
                        g = v[j, p]
                        h = v[j, q]
                        v[j, p] = g - s * (h + g * tau)
                        v[j, q] = h + s * (g - h * tau)

                    rot_num = rot_num + 1

        for i in range(0, n):
            bw[i] = bw[i] + zw[i]
            d[i] = bw[i]
            zw[i] = 0.0
    #
    #  Restore upper triangle of input matrix.
    #
    for j in range(0, n):
        for i in range(0, j):
            a[i, j] = a[j, i]

    #
    #  Ascending sort the eigenvalues and eigenvectors.
    #
    for k in range(0, n - 1):
        m = k
        for l in range(k + 1, n):
            if (d[l] < d[m]):
                m = l
        if (k != m):

            t = d[m]
            d[m] = d[k]
            d[k] = t

            for i in range(0, n):
                w[i] = v[i, m]
                v[i, m] = v[i, k]
                v[i, k] = w[i]

    return v, d, it_num, rot_num


def jacobi_eigenvalue_test01():

    # *****************************************************************************80
    #
    # JACOBI_EIGENVALUE_TEST01 uses a 4x4 test matrix.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4

    a = np.array([
        [4.0, -30.0, 60.0, -35.0, ],
        [-30.0, 300.0, -675.0, 420.0, ],
        [60.0, -675.0, 1620.0, -1050.0, ],
        [-35.0, 420.0, -1050.0, 700.0]])

    print('')
    print('JACOBI_EIGENVALUE_TEST01')
    print('  Python version: %s' % (platform.python_version()))
    print('  JACOBI_EIGENVALUE computes the eigenvalues D')
    print('  and eigenvectors V of a symmetric matrix A so that A * V = D * V.')

    r8mat_print(n, n, a, '  Input matrix A:')

    it_max = 100

    v, d, it_num, rot_num = jacobi_eigenvalue(n, a, it_max)

    print('')
    print('  Number of iterations = %d' % (it_num))
    print('  Number of rotations  = %d' % (rot_num))

    r8vec_print(n, d, '  Eigenvalues D:')

    r8mat_print(n, n, v, '  Eigenvector matrix V:')

    #
    #  Compute eigentest.
    #
    error_frobenius = r8mat_is_eigen_right(n, n, a, v, d)
    print('')
    print('  Frobenius norm error in eigensystem A*V-D*V = %g' %
          (error_frobenius))
    print('')
    print('JACOBI_EIGENVALUE_TEST01')
    print('  Normal end of execution.')
    return


def jacobi_eigenvalue_test02():

    # *****************************************************************************80
    #
    # JACOBI_EIGENVALUE_TEST02 uses a 4x4 test matrix.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 4

    a = np.array([
        [4.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 3.0, 0.0],
        [0.0, 0.0, 0.0, 2.0]])

    print('')
    print('JACOBI_EIGENVALUE_TEST02')
    print('  Python version: %s' % (platform.python_version()))
    print('  JACOBI_EIGENVALUE computes the eigenvalues D')
    print('  and eigenvectors V of a symmetric matrix so that A * V = D * V.')
    print('')
    print('  As a sanity check, input a diagonal matrix.')

    r8mat_print(n, n, a, '  Input matrix A:')

    it_max = 100

    [v, d, it_num, rot_num] = jacobi_eigenvalue(n, a, it_max)

    print('')
    print('  Number of iterations = %d' % (it_num))
    print('  Number of rotations  = %d' % (rot_num))

    r8vec_print(n, d, '  Eigenvalues D:')

    r8mat_print(n, n, v, '  Eigenvector matrix V:')

    #
    #  Compute eigentest.
    #
    error_frobenius = r8mat_is_eigen_right(n, n, a, v, d)
    print('')
    print('  Frobenius norm error in eigensystem A*V-D*V = %g' %
          (error_frobenius))
    print('')
    print('JACOBI_EIGENVALUE_TEST02')
    print('  Normal end of execution.')


def jacobi_eigenvalue_test03():

    # *****************************************************************************80
    #
    # JACOBI_EIGENVALUE_TEST03 uses a 5x5 test matrix.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    n = 5

    print('')
    print('JACOBI_EIGENVALUE_TEST03')
    print('  Python version: %s' % (platform.python_version()))
    print('  JACOBI_EIGENVALUE computes the eigenvalues D')
    print('  and eigenvectors V of a symmetric matrix so that A * V = D * V.')
    print('')
    print('  Use the discretized second derivative matrix.')

    a = np.zeros([n, n])

    for j in range(0, n):
        for i in range(0, n):
            if (i == j):
                a[i, j] = -2.0
            elif (i == j + 1 or i == j - 1):
                a[i, j] = 1.0

    r8mat_print(n, n, a, '  Input matrix A:')

    it_max = 100

    [v, d, it_num, rot_num] = jacobi_eigenvalue(n, a, it_max)

    print('')
    print('  Number of iterations = %d' % (it_num))
    print('  Number of rotations  = %d' % (rot_num))

    r8vec_print(n, d, '  Eigenvalues D:')

    r8mat_print(n, n, v, '  Eigenvector matrix V:')

    #
    #  Compute eigentest.
    #
    error_frobenius = r8mat_is_eigen_right(n, n, a, v, d)
    print('')
    print('  Frobenius norm error in eigensystem A*V-D*V = %g' %
          (error_frobenius))

    print('')
    print('JACOBI_EIGENVALUE_TEST03')
    print('  Normal end of execution.')


def jacobi_eigenvalue_test():

    # *****************************************************************************80
    #
    # JACOBI_EIGENVALUE_TEST tests the JACOBI_EIGENVALUE library.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    25 September 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    print('')
    print('JACOBI_EIGENVALUE_TEST')
    print('  Python version: %s' % (platform.python_version()))
    print('  Test the JACOBI_EIGENVALUE library.')

    jacobi_eigenvalue_test01()
    jacobi_eigenvalue_test02()
    jacobi_eigenvalue_test03()

    print('')
    print('JACOBI_EIGENVALUE_TEST:')
    print('  Normal end of execution.')


def r8mat_is_eigen_right(n, k, a, x, lam):

    # *****************************************************************************80
    #
    # R8MAT_IS_EIGEN_RIGHT determines the error in a right eigensystem.
    #
    #  Discussion:
    #
    #    An R8MAT is a matrix of real values.
    #
    #    This routine computes the Frobenius norm of
    #
    #      A * X - X * LAMBDA
    #
    #    where
    #
    #      A is an N by N matrix,
    #      X is an N by K matrix (each of K columns is an eigenvector)
    #      LAMBDA is a K by K diagonal matrix of eigenvalues.
    #
    #    This routine assumes that A, X and LAMBDA are all real.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer N, the order of the matrix.
    #
    #    Input, integer K, the number of eigenvectors.
    #    K is usually 1 or N.
    #
    #    Input, real A(N,N), the matrix.
    #
    #    Input, real X(N,K), the K eigenvectors.
    #
    #    Input, real LAM(K), the K eigenvalues.
    #
    #    Output, real VALUE, the Frobenius norm
    #    of the difference matrix A * X - X * LAM, which would be exactly zero
    #    if X and LAM were exact eigenvectors and eigenvalues of A.
    #
    c = r8mat_mm(n, n, k, a, x)

    for j in range(0, k):
        for i in range(0, n):
            c[i, j] = c[i, j] - lam[j] * x[i, j]

    value = r8mat_norm_fro(n, k, c)

    return value


def r8mat_is_eigen_right_test():

    # *****************************************************************************80
    #
    # R8MAT_IS_EIGEN_RIGHT_TEST tests R8MAT_IS_EIGEN_RIGHT.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    11 March 2015
    #
    #  Author:
    #
    #    John Burkardt
    #

    #
    #  This is the CARRY ( 4.0, 4 ) matrix.
    #
    m = 4
    n = m
    a = np.array([
        [0.13671875, 0.60546875, 0.25390625, 0.00390625],
        [0.05859375, 0.52734375, 0.39453125, 0.01953125],
        [0.01953125, 0.39453125, 0.52734375, 0.05859375],
        [0.00390625, 0.25390625, 0.60546875, 0.13671875]])

    k = 4
    x = np.array([
        [1.0, 6.0, 11.0, 6.0],
        [1.0, 2.0, -1.0, -2.0],
        [1.0, -2.0, -1.0, 2.0],
        [1.0, -6.0, 11.0, -6.0]])

    lam = np.array([
        1.000000000000000,
        0.250000000000000,
        0.062500000000000,
        0.015625000000000])

    print('')
    print('R8MAT_IS_EIGEN_RIGHT_TEST:')
    print('  Python version: %s' % (platform.python_version()))
    print('  R8MAT_IS_EIGEN_RIGHT tests the error in the right eigensystem')
    print('    A * X - X * LAMBDA = 0')

    r8mat_print(n, n, a, '  Matrix A:')
    r8mat_print(n, k, x, '  Eigenmatrix X:')
    r8vec_print(n, lam, '  Eigenvalues LAM:')

    value = r8mat_is_eigen_right(n, k, a, x, lam)

    print('')
    print('  Frobenius norm of A*X-X*LAMBDA is %g' % (value))
    print('')
    print('R8MAT_IS_EIGEN_RIGHT_TEST')
    print('  Normal end of execution.')


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
    jacobi_eigenvalue_test()
    jacobi_test()
    timestamp()
