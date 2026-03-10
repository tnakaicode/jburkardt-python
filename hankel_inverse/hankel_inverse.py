#! /usr/bin/env python3
#
def hankel_inverse ( n, x ):

#*****************************************************************************80
#
## hankel_inverse() computes the inverse of a Hankel matrix.
#
#  Discussion:
#
#    An NxN Hankel matrix is defined by a vector X of length 2*N-1
#    containing the first row and (most of) the last column.
#
#    If X = ( 1, 2, 3, 4, 5, 6, 7, 8, 9 )
#
#    then the Hankel matrix A is:
#
#      1  2  3  4  5
#      2  3  4  5  6
#      3  4  5  6  7
#      4  5  6  7  8
#      5  6  7  8  9
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Miroslav Fiedler,
#    Hankel and Loewner Matrices
#
#  Input:
#
#    integer N, the order of the Hankel matrix.
#
#    real X(2*N-1), the vector that defines the matrix.
#
#  Output:
#
#    real B(N,N), the inverse matrix.
#
  import numpy as np
#
#  Define the matrix.
#
  A = hankel_matrix ( n, x )
#
#  Solve two linear systems.
#
  p = np.zeros ( n )
  p[0:n-1] = x[n:2*n-1]
  p[n-1] = 0.0
# p = np.concatenate ( [ x[n:2*n-1], 0.0 ] )
  A.shape
  p.shape
  u = np.linalg.solve ( A, p )

  q = np.zeros ( n )
  q[n-1] = 1.0
  v = np.linalg.solve ( A, q )
#
#  Construct four matrices.
#
  z1 = np.zeros ( n )
  w1 = np.concatenate ( [ v[1:n], z1 ] )
  M1 = hankel_matrix ( n, w1 )

  z2 = np.zeros ( n-1 )
  w2 = np.concatenate ( [ z2, u ] )
  M2 = toeplitz_matrix ( n, w2 )

  z3 = np.zeros ( n )
  z3[0] = -1.0
  w3 = np.concatenate ( [ u[1:n], z3 ] )
  M3 = hankel_matrix ( n, w3 )

  z4 = np.zeros ( n-1 )
  w4 = np.concatenate ( [ z4, v ] )
  M4 = toeplitz_matrix ( n, w4 )
#
#  Construct the inverse matrix.
#
  B = np.matmul ( M1, M2 ) - np.matmul ( M3, M4 )

  return B

def hankel_inverse_test ( ):

#*****************************************************************************80
#
## hankel_inverse_test() tests hankel_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2020
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy.linalg
  import numpy as np
  import platform

  rng = default_rng ( )

  print ( '' )
  print ( 'hankel_inverse_test():\n' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  hankel_inverse() computes the inverse of a Hankel matrix.' )
  print ( '' )
  print ( '     N      ||A||      ||C||      ||I-AC||        ||I-AB||' )
  print ( '' )

  for n in [ 5, 10, 20 ]:
    x = rng.standard_normal ( size = ( 2 * n - 1 ) )
    A = hankel_matrix ( n, x )
    B = hankel_inverse ( n, x )
    C = np.linalg.inv ( A )
    I = np.identity ( n )
    error_ab = np.linalg.norm ( np.matmul ( B, A ) - I, 'fro' ) \
             + np.linalg.norm ( np.matmul ( A, B ) - I, 'fro' )
    error_ac = np.linalg.norm ( np.matmul ( C, A ) - I, 'fro' ) \
             + np.linalg.norm ( np.matmul ( A, C ) - I, 'fro' )
    norma_frobenius = np.linalg.norm ( A, 'fro' )
    normc_frobenius = np.linalg.norm ( C, 'fro' )
    print ( '  %4d  %10.2g  %10.2g  %14g  %14g' \
      % ( n, norma_frobenius, normc_frobenius, error_ac, error_ab ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'hankel_inverse_test():' )
  print ( '  Normal end of execution.' )

  return

def hankel_matrix ( n, x ):

#*****************************************************************************80
#
## hankel_matrix() returns a Hankel matrix.
#
#  Formula:
#
#    A(I,J) = X(I+J-1)
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3, 4, 5, 6, 7, 8, 9 )
#
#    1  2  3  4  5
#    2  3  4  5  6
#    3  4  5  6  7
#    4  5  6  7  8
#    5  6  7  8  9
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    The family of matrices is nested as a function of N.
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(2*N-1), the vector that defines A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a[i,j] = x[j+i]

  return a

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
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def toeplitz_matrix ( n, x ):

#*****************************************************************************80
#
## toeplitz_matrix() returns a Toeplitz matrix.
#
#  Formula:
#
#    A(I,J) = X(N+J-I)
#
#  Example:
#
#    N = 5, X = ( 1, 2, 3, 4, 5, 6, 7, 8, 9 )
#
#    5  6  7  8  9
#    4  5  6  7  8
#    3  4  5  6  7
#    2  3  4  5  6
#    1  2  3  4  5
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is Toeplitz: constant along diagonals.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 May 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of A.
#
#    real X(2*N-1), the diagonals of A, with X(1) being
#    the A(N,1) entry, X(N) being the main diagonal value of A,
#    and X(2*N-1) being the A(1,N) entry.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      A[i,j] = x[n-i+j-1]

  return A

if ( __name__ == '__main__' ):
  timestamp ( )
  hankel_inverse_test ( )
  timestamp ( )
 
