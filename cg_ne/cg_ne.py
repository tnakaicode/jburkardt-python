#! /usr/bin/env python3
#
def cg_ne_test ( ):

#*****************************************************************************80
#
## cg_ne_test() tests cg_ne().
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
  print ( 'cg_ne_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test cg_ne().' )

  n = 10
  cg_ne_helmert_test ( n )

  n = 100
  cg_ne_lesp_test ( n )

  n = 20
  cg_ne_involutory_test ( n )
#
#  Terminate.
#
  print ( '' )
  print ( 'cg_ne_test():' )
  print ( '  Normal end of execution.' )

  return

def cg_ne_helmert_test ( n ):

#*****************************************************************************80
#
## cg_ne_helmert_test() tests cg_ne() for the Helmert matrix.
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
#    integer N, the size of the system.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'cg_ne_helmert_test()' )
  print ( '  Test cg_ne() on the Helmert matrix.' )
  print ( '  Number of variables N =', n )
#
#  Get the matrix.
#
  A = helmert_matrix ( n )
  print ( '  Estimated condition number = ', np.linalg.cond ( A ) )
#
#  Choose a random solution.
#
  x1 = rng.standard_normal ( n )
#
#  Compute the corresponding right hand side.
#
  b = np.matmul ( A, x1 )
#
#  Call cg_ne ( )
#
  x2 = np.ones ( n )
  x2 = cg_ne ( A, b, x2 )
#
#  Compute the residual.
#
  r = b - np.matmul ( A, x2 )
  r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
  e_norm = np.linalg.norm ( x1 - x2 )
#
#  Report.
#
  print ( '' )
  print ( '  Norm of residual |Ax-b| = ', r_norm )
  print ( '  Norm of error |x1-x2| = ', e_norm )

  return

def cg_ne_involutory_test ( n ):

#*****************************************************************************80
#
## cg_ne_involutory_test() tests cg_ne() for the involutory matrix.
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
#    integer N, the size of the system.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'cg_ne_involutory_test():' )
  print ( '  Test cg_ne() on the involutory matrix.' )
  print ( '  Number of variables N =', n )
#
#  Get the matrix.
#
  A = involutory_matrix ( n )
  print ( '  Estimated condition number =', np.linalg.cond ( A ) )
#
#  Choose a random solution.
#
  x1 = rng.standard_normal ( n )
#
#  Compute the corresponding right hand side.
#
  b = np.matmul ( A, x1 )
#
#  Call cg_ne ( )
#
  x2 = np.ones ( n )

  for it in range ( 1, 5 ):

    x2 = cg_ne ( A, b, x2 )
#
#  Compute the residual.
#
    r = b - np.matmul ( A, x2 )
    r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
    e_norm = np.linalg.norm ( x1 - x2 )
#
#  Report.
#
    print ( '' )
    print ( '  Full iteration number = ', it )
    print ( '  Norm of residual |Ax-b| = ', r_norm )
    print ( '  Norm of error |x1-x2| = ', e_norm )

  return

def cg_ne_lesp_test ( n ):

#*****************************************************************************80
#
## cg_ne_lesp_test() tests cg_ne() for the Lesp matrix.
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
#    integer N, the size of the system.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'cg_ne_lesp_test():' )
  print ( '  Test cg_ne() on the Lesp matrix.' )
  print ( '  Number of variables N = ', n )
#
#  Get the matrix.
#
  A = lesp_matrix ( n )
  print ( '  Estimated condition number = ', np.linalg.cond ( A ) )
#
#  Choose a random solution.
#
  x1 = rng.standard_normal ( n )
#
#  Compute the corresponding right hand side.
#
  b = np.matmul ( A, x1 )
#
#  Call cg_ne ( )
#
  x2 = np.ones ( n )

  for it in range ( 1, 5 ):

    x2 = cg_ne ( A, b, x2 )
#
#  Compute the residual.
#
    r = b - np.matmul ( A, x2 )
    r_norm = np.linalg.norm ( r )
#
#  Compute the error.
#
    e_norm = np.linalg.norm ( x1 - x2 )
#
#  Report.
#
    print ( '' )
    print ( '  Full iteration number = ', it )
    print ( '  Norm of residual |Ax-b| = ', r_norm )
    print ( '  Norm of error |x1-x2| = ', e_norm )

  return

def cg_ne ( A, b, x ):

#*****************************************************************************80
#
## cg_ne() carries out the conjugate gradient method for the normal equations.
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
#    real A(n,n): the matrix.
#
#    real B(n): the right hand side.
#
#    real X(n): an initial guess for the solution.
#
#  Output:
#
#    real X(n): an improved solution estimate.
#
  import numpy as np

  n = A.shape[0]

  r = b - np.matmul ( A, x )
  z = np.matmul ( A.T, r )
  d = z.copy ( )

  for i in range ( 0, n ):

    alpha = np.linalg.norm ( z ) / ( np.linalg.norm ( np.matmul ( A, d ) ) )
    alpha = alpha**2

    x = x + alpha * d

    r = b - np.matmul ( A, x )

    if ( np.linalg.norm ( r ) == 0.0 ):
      print ( '  Early finish on step ', i )
      break

    zold = z.copy ( )
    z = np.matmul ( A.T, r )

    beta = np.linalg.norm ( z ) / np.linalg.norm ( zold )
    beta = beta**2

    d = z + beta * d

  return x

def helmert_matrix ( n ):

#*****************************************************************************80
#
## helmert_matrix() returns the HELMERT matrix.
#
#  Formula:
#
#    If I == 0 then
#      A(I,J) = 1 / sqrt ( N )
#    else if J < I then
#      A(I,J) = 1 / sqrt ( I * ( I + 1 ) )
#    else if J == I then
#      A(I,J) = -I / sqrt ( I * ( I + 1 ) )
#    else
#      A(I,J) = 0
#
#  Discussion:
#
#    The matrix given above by Helmert is the classic example of
#    a family of matrices which are now called Helmertian or
#    Helmert matrices.
#
#    A matrix is a (standard) Helmert matrix if it is orthogonal,
#    and the elements which are above the diagonal and below the
#    first row are zero.
#
#    If the elements of the first row are all strictly positive,
#    then the matrix is a strictly Helmertian matrix.
#
#    It is possible to require in addition that all elements below
#    the diagonal be strictly positive, but in the reference, this
#    condition is discarded as being cumbersome and not useful.
#
#    A Helmert matrix can be regarded as a change of basis matrix
#    between a pair of orthonormal coordinate bases.  The first row
#    gives the coordinates of the first new basis vector in the old
#    basis.  Each later row describes combinations of (an increasingly
#    extensive set of) old basis vectors that constitute the new
#    basis vectors.
#
#    Helmert matrices have important applications in statistics.
#
#  Example:
#
#    N = 5
#
#    0.4472    0.4472    0.4472    0.4472    0.4472
#    0.7071   -0.7071         0         0         0
#    0.4082    0.4082   -0.8165         0         0
#    0.2887    0.2887    0.2887   -0.8660         0
#    0.2236    0.2236    0.2236    0.2236   -0.8944
#
#  Properties:
#
#    A is generally not symmetric: A' ~= A.
#
#    A is orthogonal: A' * A = A * A' = I.
#
#    Because A is orthogonal, it is normal: A' * A = A * A'.
#
#    A is not symmetric: A' ~= A.
#
#    det ( A ) = (-1)^(N+1)
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    HO Lancaster,
#    The Helmert Matrices,
#    American Mathematical Monthly,
#    Volume 72, 1965, pages 4-12.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )
#
#  A begins with the first row, diagonal, and lower triangle set to 1.
#
  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i == 0 ):
        a[i,j] = 1.0 / np.sqrt ( n )
      elif ( j < i ):
        a[i,j] = 1.0 / np.sqrt ( float ( i * ( i + 1 ) ) )
      elif ( i == j ):
        a[i,j] = float ( - i ) / np.sqrt ( float ( i * ( i + 1 ) ) )

  return a

def involutory_matrix ( n ):

#*****************************************************************************80
#
## involutory_matrix() returns the involutory matrix.
#
#  Formula:
#
#    A(I,J) = 1 / ( I + J - 1 )
#
#    Set D = -N
#
#    Multiply column 1 of A by D.
#
#    For I = 1 to N-1
#      D = -(N+I)*(N-I)*D/(I*I)
#      Multiply row I + 1 by D.
#    End
#
#  Example:
#
#    N = 5
#
#       -5     0.5     0.33     0.25    0.2
#     -300    40.0    30.00    24.00   20.0
#     1050  -157.5  -126.00  -105.00  -90.0
#    -1400   224.0   186.66   160.00  140.0
#      630  -105.0   -90.00   -78.75  -70.0
#
#  Properties:
#
#    A is generally not symmetric: A' /= A.
#
#    A is involutory: A * A = I.
#
#    det ( A ) = +1 or -1.
#
#    A is unimodular.
#
#    The matrices:
#      B = 1/2 ( I - A )
#    and
#      C = 1/2 ( I + A )
#    are idempotent, that is, B * B = B, and C * C = C.
#
#    A is ill-conditioned.
#
#    A is a diagonally scaled version of the Hilbert matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Alston Householder, John Carpenter,
#    The singular values of involutory and of idempotent matrices,
#    Numerische Mathematik,
#    Volume 5, 1963, pages 234-237.
#
#  Input:
#
#    integer N, the order of A.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      a[i,j] = 1.0 / float ( i + j + 1 )
 
  for i in range ( 0, n ):
    a[i,0] = - n * a[i,0]

  d = - float ( n )
  for i in range ( 1, n ):
    d = - float ( n + i ) * float ( n - i ) * d  / float ( i * i )
    for j in range ( 0, n ):
      a[i,j] = d * a[i,j]

  return a

def lesp_matrix ( n ):

#*****************************************************************************80
#
## lesp_matrix() returns the LESP matrix.
#
#  Formula:
#
#    if ( I - J == 1 )
#      A(I,J) = 1 / I
#    else if ( I - J == 0 )
#      A(I,J) = - ( 2*I+3 )
#    else if ( I - J == 1 )
#      A(I,J) = J
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    M = 5, N = 5
#
#     -5    2    .    .     .
#     1/2  -7    3    .     .
#      .   1/3  -9    4     .
#      .    .   1/4 -11     5
#      .    .    .   1/5  -13
#
#
#  Properties:
#
#    The matrix is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is generally not symmetric: A' /= A.
#
#    The eigenvalues are real, and smoothly distributed in [-2*N-3.5, -4.5].
#
#    The eigenvalues are sensitive.
#
#    The matrix is similar to the symmetric tridiagonal matrix with
#    the same diagonal entries and with off-diagonal entries 1,
#    via a similarity transformation using the diagonal matrix
#    D = diagonal ( 1!, 2!, ..., N! ).
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Wim Lenferink, MN Spijker,
#    On the use of stability regions in the numerical analysis of initial
#    value problems,
#    Mathematics of Computation,
#    Volume 57, 1991, pages 221-237.
#
#    Lloyd Trefethen,
#    Pseudospectra of matrices,
#    in Numerical Analysis 1991,
#    Proceedings of the 14th Dundee Conference,
#    D F Griffiths and G A Watson, editors,
#    Pitman Research Notes in Mathematics, volume 260,
#    Longman Scientific and Technical, Essex, UK, 1992, pages 234-266.
#
#  Input:
#
#    integer N, the number of rows and columns of A.
#
#  Output:
#
#    real A(N), the matrix.
#
  import numpy as np

  a = np.zeros ( ( n, n ) )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( i - j == 1 ):
        a[i,j] = 1.0 / float ( i + 1 )
      elif ( i - j == 0 ):
        a[i,j] = - float ( 2 * i + 5 )
      elif ( i - j == -1 ):
        a[i,j] = float ( j + 1 )

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
  cg_ne_test ( )
  timestamp ( )

