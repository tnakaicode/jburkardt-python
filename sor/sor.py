#! /usr/bin/env python3
#
def sor_test ( ):

#*****************************************************************************80
#
## sor_test() tests sor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'sor_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test sor().' )

  w = 1.5
  sor_test01 ( w )
#
#  Terminate.
#
  print ( '' )
  print ( 'sor_test():' )
  print ( '  Normal end of execution.' )

  return

def dif2_matrix ( n ):

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
#    06 February 2025
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
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):

    if ( 0 < i and i - 1 < n ):
      A[i,i-1] = -1.0

    if ( i < n ):
      A[i,i] = 2.0

    if ( i + 1 < n ):
      A[i,i+1] = -1.0

  return A

def sor ( n, A, b, x, w ):

#*****************************************************************************80
#
## sor() carries out one step of the SOR iteration.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer n: the order of the matrix.
#
#    real A(n,n): the matrix.
#
#    real b(n): the right hand side.
#
#    real x(n): the current solution estimate.
#
#    real w: the SOR parameter, between 0 and 2.
#
#  Output:
#
#    real x_new(n): the solution estimate updated by one SOR step.
#
  import numpy as np

  x_new = np.zeros ( n )

  for i in range ( 0, n ):

    x_new[i] = b[i]
    x_new[i] = x_new[i] - np.dot ( A[i,0:i], x_new[0:i] )
    x_new[i] = x_new[i] - np.dot ( A[i,i+1:n], x[i+1:n] )
    x_new[i] = x_new[i] / A[i,i]

    x_new[i] = ( 1.0 - w ) * x[i] + w * x_new[i]

  return x_new

def sor_test01 ( w ):

#*****************************************************************************80
#
## sor_test01() tests sor().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 February 2026
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import numpy as np

  print ( '' )
  print ( 'sor_test01():' )
  print ( '  sor() is an iterative solver of a linear system.' )

  it_num = 400
  n = 20

  x_exact = np.arange ( 1, n + 1 )
  A = dif2_matrix ( n )
  b = np.matmul ( A, x_exact )

  x = np.zeros ( n )  

  x_plot = np.zeros ( [ it_num + 1, n ] )
  x_plot[0,:] = x.copy ( )

  step = np.arange ( 0, it_num + 1 )
  e = np.nan * np.ones ( it_num + 1 )
  xm = np.nan * np.ones ( it_num + 1 )

  e[0] = ( np.linalg.norm ( np.matmul ( A, x ) - b ) )**2

  for it in range ( 1, it_num + 1 ):

    x_new = sor ( n, A, b, x, w )

    e[it] = ( np.linalg.norm ( np.matmul ( A, x_new ) - b ) )**2
    x_plot[it,:] = x_new.copy ( )
    xm[it] = ( np.linalg.norm ( x_new - x ) )**2 / n
#
#  Update the solution
#
    x = x_new.copy ( )
#
#  Display the error.
#
  plt.clf ( )
  plt.plot ( step, np.log ( e ), 'm-*' )
  plt.title ( 'Log (Error^2)' )
  plt.xlabel ( 'Step' )
  plt.ylabel ( 'Error' )
  plt.grid ( True )
  filename = 'error.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Display the motion.
#
  plt.clf ( )
  plt.plot ( step, np.log ( xm ), 'm-*' )
  plt.title ( 'Log (Average generator motion)' )
  plt.xlabel ( 'Step' )
  plt.ylabel ( 'Energy' )
  plt.grid ( True )
  filename = 'motion.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )
#
#  Plot the evolution of the locations of the generators.
#
  plt.clf ( )
  y = np.arange ( 0, it_num + 1 )
  for k in range ( 0, n ):
    plt.plot ( x_plot[:,k], y )
  plt.grid ( True )
  plt.title ( 'Generator evolution.' )
  plt.xlabel ( 'Generator positions' )
  plt.ylabel ( 'Iterations' ) 
  filename = 'generators.png'
  plt.savefig ( filename )
  print ( '  Graphics saved as "' + filename + '"' )
  plt.close ( )

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
  sor_test ( )
  timestamp ( )

