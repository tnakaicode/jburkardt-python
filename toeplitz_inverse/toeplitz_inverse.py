#! /usr/bin/env python3
#
def exchange_matrix ( m, n ):

#*****************************************************************************80
#
## exchange_matrix() returns the EXCHANGE matrix.
#
#  Formula:
#
#    if ( I + J = N + 1 )
#      A(I,J) = 1
#    else
#      A(I,J) = 0
#
#  Example:
#
#    M = 4, N = 5
#
#    0 0 0 0 1
#    0 0 0 1 0
#    0 0 1 0 0
#    0 1 0 0 0
#
#    M = 5, N = 5
#
#    0 0 0 0 1
#    0 0 0 1 0
#    0 0 1 0 0
#    0 1 0 0 0
#    1 0 0 0 0
#
#  Rectangular properties:
#
#    A is integral: int ( A ) = A.
#
#    A is a zero/one matrix.
#
#  Square Properties:
#
#    A is nonsingular.
#
#    A is a permutation matrix.
#
#    A has property A.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A is a Hankel matrix: constant along anti-diagonals.
#
#    A is involutional: A * A = I.
#
#    A is a square root of the identity matrix.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    det ( A ) = ( -1 )^(N/2).
#
#    There are N/2 eigenvalues of -1, and (N+1)/2 eigenvalues of 1.
#
#    For each pair of distinct vector indices I1 and I2 that sum to N+1, there
#    is an eigenvector which has a 1 in the I1 and I2 positions and 0 elsewhere,
#    and there is an eigenvector for -1, with a 1 in the I1 position and a -1
#    in the I2 position.  If N is odd, then there is a single eigenvector
#    associated with the index I1 = (N+1)/2, having a 1 in that index and zero
#    elsewhere, associated with the eigenvalue 1.
#
#    The exchange matrix is also called the "counter-identity matrix".
#
#    A is not diagonally dominant.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2024
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      if ( i + j == n - 1 ):
        A[i,j] = 1.0

  return A

def hankel_matrix ( n, x ):

#*****************************************************************************80
#
## hankel_matrix() returns a HANKEL matrix.
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
#    18 January 2024
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

  A = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    A[0:n,j] = x[j:j+n]

  return A

def toeplitz_inverse ( n, x ):

#*****************************************************************************80
#
## toeplitz_inverse() computes the inverse of a Toeplitz matrix.
#
#  Discussion:
#
#    This function uses the fact that if T is a Toeplitz matrix,
#    and J is the "exchange" matrix, then H=J*T is a Hankel matrix.
#
#    By lucky chance, the vector x defining T is the same vector x
#    used to define J*T.
#
#    Hence, we can use a known algorithm for the inverse of a Hankel matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2024
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
#    integer N, the order of the matrix.
#
#    real X(2*N-1), the vector that defines the matrix.
#
#  Output:
#
#    real B(N,N), the inverse matrix.
#
  import numpy as np
#
#  Get the Exchange matrix J.
#
  J = exchange_matrix ( n, n )
#
#  Define the Toeplitz matrix A.
#
  A = toeplitz_matrix ( n, x )
#
#  Define the corresponding Hankel matrix H = J * A.
#
  H = np.matmul ( J, A )
#
#  Solve two linear systems.
#
  p = np.concatenate ( ( x[n:2*n-1], [ 0.0] ) )
  u = np.linalg.solve ( H, p )

  q = np.zeros ( n )
  q[n-1] = 1.0
  v = np.linalg.solve ( H, q )
#
#  Construct four matrices.
#
  z1 = np.zeros ( n )
  w1 = np.concatenate ( ( v[1:n], z1 ) )
  M1 = hankel_matrix ( n, w1 )

  z2 = np.zeros ( n-1 )
  w2 = np.concatenate ( ( z2, u ) )
  M2 = toeplitz_matrix ( n, w2 )

  z3 = np.zeros ( n )
  z3[0] = -1.0
  w3 = np.concatenate ( ( u[1:n], z3 ) )
  M3 = hankel_matrix ( n, w3 )

  z4 = np.zeros ( n-1 )
  w4 = np.concatenate ( ( z4, v ) )
  M4 = toeplitz_matrix ( n, w4 )
#
#  Construct K, the inverse of the Hankel matrix.
#
  K = np.matmul ( M1, M2 ) - np.matmul ( M3, M4 )
#
#  Compute B, the inverse of the Toeplitz matrix.
#
  B = np.matmul ( K, J )

  return B

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

def toeplitz_inverse_test ( ):

#*****************************************************************************80
#
## toeplitz_inverse_test() tests toeplitz_inverse()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'toeplitz_inverse_test()' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  toeplitz_inverse() computes the inverse of a Toeplitz matrix.' )

  rng = default_rng ( )

  print ( '' )
  print ( '     N      |A|      |C|      |I-AC|        |I-AB|' )
  print ( '' )

  for n in [ 5, 10, 20 ]:
    x = rng.normal ( size = 2 * n - 1 )
    A = toeplitz_matrix ( n, x )
    B = toeplitz_inverse ( n, x )
    C = np.linalg.inv ( A )
    I = np.eye ( n )
    error_ab = np.linalg.norm ( np.matmul ( B, A ) - I, 'fro' ) \
             + np.linalg.norm ( np.matmul ( A, B ) - I, 'fro' )
    error_ac = np.linalg.norm ( np.matmul ( C, A ) - I, 'fro' ) \
             + np.linalg.norm ( np.matmul ( A, C ) - I, 'fro' )
    norma_frobenius = np.linalg.norm ( A, 'fro' )
    normc_frobenius = np.linalg.norm ( C, 'fro' )
    print ( '  %4d  %10.2g  %10.2g  %14g  %14g'  \
      % ( n, norma_frobenius, normc_frobenius, error_ac, error_ab ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'toeplitz_inverse_test():' )
  print ( '  Normal end of execution.' )

  return

def toeplitz_matrix ( n, x ):

#*****************************************************************************80
#
## toeplitz_matrix() returns a TOEPLITZ matrix.
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
#    18 January 2024
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
      A[i,j] = x[n-1-i+j]

  return A

if ( __name__ == '__main__' ):
  timestamp ( )
  toeplitz_inverse_test ( )
  timestamp ( )

