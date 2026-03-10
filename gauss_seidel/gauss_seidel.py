#! /usr/bin/env python3
#
def gauss_seidel_test ( ):

#*****************************************************************************80
#
## gauss_seidel_test() tests gauss_seidel().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2025
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'gauss_seidel_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  gauss_seidel() solves a linear system using' )
  print ( '  a version of the Gauss-Seidel iteration.' )

  gauss_seidel1_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'gauss_seidel_test():' )
  print ( '  Normal end of execution.' )

  return

def dif2_matrix ( m, n ):

#*****************************************************************************80
#
## dif2_matrix() returns the second difference matrix.
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
#    This code is distributed under the MIT license.
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
#  Input:
#
#    integer M, N, the number of rows and columns of A.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    if ( 0 <= i - 1 and i - 1 < n ):
      a[i,i-1] = -1.0
    if ( i < n ):
      a[i,i] = 2.0
    if ( i + 1 < n ):
      a[i,i+1] = -1.0

  return a

def gauss_seidel1 ( kits, A, b, x ):

#*****************************************************************************80
#
## gauss_seidel1() carries out Gauss-Seidel iteration.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer KITS: the number of iterations to carry out.
#
#    real A(N,N): the matrix.
#
#    real B(N): the right hand side of the linear system.
#
#    real X(N): the solution estimate.
#
#  Output:
#
#    real X(N): the updated solution estimate.
#
  import numpy as np

  n = A.shape[0]

  for k in range ( 0, kits ):
    for i in range ( 0, n ):
      x[i] = x[i] + ( b[i] - np.dot ( A[i,:], x ) ) / A[i,i]

  return x

def gauss_seidel1_test ( ):

#*****************************************************************************80
#
## gauss_seidel1_test() tests gauss_seidel1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 February 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'gauss_seidel1_test():' )
  print ( '  gauss_seidel1() solves a linear system using' )
  print ( '  a for-loop version of the Gauss-Seidel iteration.' )

  n = 20
  A = dif2_matrix ( n, n )
  x_exact = np.arange ( 1, n + 1 )
  b = np.dot ( A, x_exact )

  print ( '' )
  print ( '  Iterations  ||Ax-b||' )
  print ( '' )

  for kits in [ 10, 20, 40, 80, 160, 320, 640, 1280, 2560 ]:
    x = np.zeros ( n )  
    x = gauss_seidel1 ( kits, A, b, x )
    l2error = np.linalg.norm ( np.dot ( A, x ) - b )
    print ( '  %4d        %g' % ( kits, l2error ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'gauss_seidel1_test():' )
  print ( '  Normal end of execution.' )

  return

def timestamp ( ):

#*****************************************************************************80
#
## timestamp() prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 August 2019
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return

if ( __name__ == '__main__' ):
  timestamp ( )
  gauss_seidel_test ( )
  timestamp ( )

