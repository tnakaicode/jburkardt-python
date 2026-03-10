#! /usr/bin/env python3
#
def eros_test ( ):

#*****************************************************************************80
#
## eros_test() tests eros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'eros_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test eros().' )

  gauss_test1 ( )
  gauss_test2 ( )
  gauss_det_test ( )
  gauss_inverse_test ( )
  gauss_plu_test ( )
  golub_matrix_test ( )
  ref_test ( )
  rref_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'eros_test():' )
  print ( '  Normal end of execution' )

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
#  Input:
#
#    integer N, the order of the matrix.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    if ( 0 <= i - 1 and i - 1 < n ):
      A[i,i-1] = -1.0
    if ( i < n ):
      A[i,i] = 2.0
    if ( i + 1 < n ):
      A[i,i+1] = -1.0

  return A

def elim ( Ab, i, j ):

#*****************************************************************************80
#
## elim() uses Ab(j,j) to eliminate Ab(i,j).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Ab(m,n+k), the augmented matrix.
#
#    integer i, j, the row and column indices of the entry to eliminate.
#
#  Output:
#
#    real Ab(m,n+k), the augmented matrix has been modified.
#
  if ( i == j ):
    print ( 'elim(): Ignoring this command' )
    print ( '  I and J must be distinct.' )
    return Ab

  if ( Ab[i,j] == 0.0 ):
    return Ab

  s = - Ab[i,j] / Ab[j,j]
  Ab[i,:] = Ab[i,:] + Ab[j,:] * s
  Ab[i,j] = 0.0

  return Ab

def gauss ( A, b, wait = 0 ):

#*****************************************************************************80
#
## gauss() uses Gauss elimination to solve a linear system A*x=b.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(m,n), the system matrix.
#
#    real b(m,k), the right hand side vectors.
#
#    integer wait:
#    0: no extra printout (default)
#    1: extra printout, but no pause.
#    2: extra printout, and pausing.
#
#  Output:
#
#    real x(m,k), the solution vectors.
#
  m, n = A.shape

  Ab = init ( A, b )

  if ( 0 < wait ):
    print ( '' )
    print ( '  Augmented matrix Ab, step 0' )
    print ( '' )
    print ( Ab )
    if ( 1 < wait ):
      input ( )

  for j in range ( 0, n ):

    Ab, p = pivot ( Ab, j )

    Ab = scale ( Ab, j )

    for i in range ( 0, n ):
      if ( i != j ):
        Ab = elim ( Ab, i, j )

    if ( 0 < wait ):
      print ( '' )
      print ( '  Augmented matrix Ab, after step ', j )
      print ( '' )
      print ( Ab )
      if ( 1 < wait ):
        input ( )

  x = solution ( Ab )

  if ( 0 < wait ):
    print ( '' )
    print ( '  Computed solution x' )
    print ( '' )
    print ( x )
    if ( 1 < wait ):
      input ( )

  return x

def gauss_test1 ( ):

#*****************************************************************************80
#
## gauss_test1() tests gauss().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'gauss_test1():' )
  print ( '  gauss() solves a 3x3 linear system with one right hand side.' )

  n = 3
  A = dif2_matrix ( n )
  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  print ( A )
  print ( '' )
  print ( '  Exact solution x:' )
  print ( '' )
  x = np.array ( [ [ 2.0 ], [ 1.0 ], [ 3.0 ] ] )
  print ( x )
  print ( '' )
  print ( '  Right hand side b:' )
  print ( '' )
  b = np.matmul ( A, x )
  print ( b )

  wait = 1
  gauss ( A, b, wait )

  return

def gauss_test2 ( ):

#*****************************************************************************80
#
## gauss_test2() tests gauss() with a random 3x3 system and two right hand sides.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  print ( '' )
  print ( 'gauss_test2():' )
  print ( '  gauss() solves a 3x3 linear system' )
  print ( '  with two right hand sides.' )

  A = golub_matrix ( 3, rng )
  print ( '' )
  print ( '  Random matrix A:' )
  print ( '' )
  print ( A )
  print ( '' )
  print ( '  Exact solution x:' )
  print ( '' )
  x = np.array ( [ \
    [ 2.0, 10.0 ], \
    [ 1.0,  1.5 ], \
    [ 3.0, -2.0 ] ] )
  print ( x )
  print ( '' )
  print ( '  Right hand side b:' )
  print ( '' )
  b = np.matmul ( A, x )
  print ( b )

  wait = 1
  gauss ( A, b, wait )

  return

def gauss_det ( A ):

#*****************************************************************************80
#
## gauss_det() uses Gauss elimination for the determinant of a matrix A.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(n,n), the system matrix.
#    The matrix A should be square.
#
#  Output:
#
#    real value, the determinant.
#
  import numpy as np

  m, n = A.shape
  k = 0
  b = np.zeros ( [ m, k ] )

  Ab = init ( A, b )

  value = 1.0

  for j in range ( 0, n ):

    Ab, p = pivot ( Ab, j )

    if ( p != j ):
      value = - value

    value = value * Ab[j,j]

    for i in range ( j + 1, n ):
      Ab = elim ( Ab, i, j )

  return value

def gauss_det_test ( ):

#*****************************************************************************80
#
## gauss_det_test() tests gauss_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'gauss_det_test():' )
  print ( '  gauss_det() uses Gauss elimination to find the determinant' )
  print ( '  of a matrix.' )

  rng = default_rng ( )

  A = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ], \
    [ 7, 8, 9 ] ] )
  value = gauss_det ( A )
  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  print ( A )
  print ( '' )
  print ( '  Computed determinant = ', value )
  print ( '  np.lingalg.det(A) =    ', np.linalg.det ( A ) )

  n = 5
  A = golub_matrix ( n, rng )
  value = gauss_det ( A )
  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  print ( A )
  print ( '' )
  print ( '  Computed determinant = ', value )
  print ( '  np.lingalg.det(A) =    ', np.linalg.det ( A ) )

  return

def gauss_inverse ( A ):

#*****************************************************************************80
#
## gauss_inverse() uses Gauss elimination for the inverse of a square matrix A.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(n,n), the matrix.
#
#  Output:
#
#    real B(n,n), the inverse matrix.
#
  import numpy as np

  m, n = A.shape

  if ( m != n ):
    print ( '' )
    print ( 'gauss_inverse(): Fatal error!' )
    print ( '  Input matrix is not square.' )
    raise Exception ( 'gauss_inverse(): Fatal error!' )

  I = np.identity ( n )

  B = gauss ( A, I )

  return B

def gauss_inverse_test ( ):

#*****************************************************************************80
#
## gauss_inverse_test() tests gauss_inverse().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'gauss_inverse_test():' )
  print ( '  gauss_inverse() uses Gauss elimination to find the' )
  print ( '  inverse of a matrix.' )

  rng = default_rng ( )

  A = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 8 ], \
    [ 7, 8, 9 ] ] )
  B = gauss_inverse ( A )
  I = np.identity ( A.shape[0] )
  AB = np.matmul ( A, B )
  r = np.linalg.norm ( AB - I )
  B2 = np.linalg.inv ( A )
  e = np.linalg.norm ( B2 - B )

  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  print ( A )
  print ( '' )
  print ( '  Computed inverse B:' )
  print ( '' )
  print ( B )
  print ( '' )
  print ( '  np.linalg.inv B2 = inv(A):' )
  print ( '' )
  print ( B2 )

  print ( '' )
  print ( '  Residual norm |A*B-I| = ', r )
  print ( '  Error norm    |B2-B|  = ', e )

  A = golub_matrix ( 5, rng )
  B = gauss_inverse ( A )
  I = np.identity ( A.shape[0] )
  AB = np.matmul ( A, B )
  r = np.linalg.norm ( AB - I )
  B2 = np.linalg.inv ( A )
  e = np.linalg.norm ( B2 - B )

  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  print ( A )
  print ( '' )
  print ( '  Computed inverse B:' )
  print ( '' )
  print ( B )
  print ( '' )
  print ( '  numpy linalg inverse: B2 = np.linalg.inv(A):' )
  print ( '' )
  print ( B2 )

  print ( '' )
  print ( '  Residual norm |A*B-I| = ', r )
  print ( '  Error norm    |B2-B| =  ', e )

  return

def gauss_plu ( A, wait = 0 ):

#*****************************************************************************80
#
## gauss_plu() uses Gauss eliminiation to find the PLU factors of a matrix.
#
#  Discussion:
#
#    The desired factorization is A = P' * L * U
#    * P is a permutation matrix
#    * L is a unit lower triangular matrix
#    * U is an upper triangular matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(m,n), the system matrix.
#
#    logical wait:
#    0: no extra printout
#    1: extra printout, but no pause.
#    2: extra printout, and pausing.
#
#  Output:
#
#    global real P(m,m), L(m,m), U(m,n), the PLU factors.
#
  import numpy as np

  m, n = A.shape
#
#  PLU initialize.
#
  P = np.identity ( m )
  L = np.identity ( m )
  U = A.copy()

  info = 0

  for j in range ( 0, n - 1 ):
#
#  Choose the pivot row P for variable J.
#
    p = np.argmax ( np.abs ( U[j:n,j] ) )
    p = p + j - 1

    if ( U[p,j] == 0.0 ):
      continue
#
#  Swap rows P and J.
#
    if ( p != j ):
      T      = P[j,:]
      P[j,:] = P[p,:]
      P[p,:] = T

      T      = U[j,:]
      U[j,:] = U[p,:]
      U[p,:] = T

      T        = L[j,1:j]
      L[j,1:j] = L[p,1:j]
      L[p,1:j] = T
#
#  Eliminate U(i,j), and store multiplier in L(i,j).
#
    for i in range ( j + 1, n ):
      s = U[i,j] / U[j,j]
      U[i,:] = U[i,:] - s * U[j,:]
      U[i,j] = 0.0
      L[i,j] = s
#
#  Show that it's still true that P' * L * U = A.
#
    if ( 0 < wait ):
      print ( '' )
      print ( '  After processing column ', j )
      print ( '' )
      print ( '  P:' )
      print ( '' )
      print ( P )
      print ( '' )
      print ( '  L:' )
      print ( '' )
      print ( L )
      print ( '' )
      print ( '  U:' )
      print ( '' )
      print ( U )
      t = np.linalg.norm ( A - np.matmul ( P.T, np.matmul ( L, U ) ) )
      print ( '  |A-P\'*L*U| = ', t )
      if ( 1 < wait ):
        input ( )

  return P, L, U

def gauss_plu_test ( ):

#*****************************************************************************80
#
## gauss_plu_test() tests gauss_plu().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np

  print ( '' )
  print ( 'gauss_plu_test():' )
  print ( '  gauss_plu() uses Gauss elimination to find the' )
  print ( '  PLU factors of a matrix.' )

  rng = default_rng ( )

  A = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 8 ], \
    [ 7, 8, 9 ] ] )
  P, L, U = gauss_plu ( A )
  PLU = np.matmul ( P.T, np.matmul ( L, U ) )
  r = np.linalg.norm ( A - PLU )

  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  print ( A )
  print ( '' )
  print ( '  Permutation matrix P:' )
  print ( '' )
  print ( P )
  print ( '' )
  print ( '  Unit lower triangular matrix L:' )
  print ( '' )
  print ( L )
  print ( '' )
  print ( '  Upper triangular matrix U:' )
  print ( '' )
  print ( U )
  print ( '' )
  print ( '  Residual norm |A-P\'*L*U| = ', r )

  A = golub_matrix ( 5, rng )
  P, L, U = gauss_plu ( A )
  PLU = np.matmul ( P.T, np.matmul ( L, U ) )
  r = np.linalg.norm ( A - PLU )

  print ( '' )
  print ( '  Matrix A:' )
  print ( '' )
  print ( A )
  print ( '' )
  print ( '  Permutation matrix P:' )
  print ( '' )
  print ( P )
  print ( '' )
  print ( '  Unit lower triangular matrix L:' )
  print ( '' )
  print ( L )
  print ( '' )
  print ( '  Upper triangular matrix U:' )
  print ( '' )
  print ( U )
  print ( '' )
  print ( '  Residual norm |A-P''*L*U| = ', r )

  return

def golub_matrix ( n, rng ):

#*****************************************************************************80
#
## golub_matrix() returns the golub matrix.
#
#  Discussion:
#
#    These matrices are the product of random unit lower and unit upper 
#    triangular matrices.
#
#    These matrices tend to be badly conditioned.
#
#  Properties:
#
#    A can be LU factored without pivoting.
#
#    det(A) = 1.
#
#    For values of n greater than 10, the determinant cannot may not be 
#    reliably computed.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Cleve Moler,
#    Numerical Computing with MATLAB,
#    SIAM, 2004,
#    ISBN13: 978-0-898716-60-3,
#    LC: QA297.M625
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    rng(): the current random number generator.
#
#  Output:
#
#    real A(N,N), the matrix.
#
  import numpy as np

  s = 10.0

  L = np.identity ( n )
  for i in range ( 0, n ):
    for j in range ( 0, i ):
      L[i,j] = s * rng.standard_normal ( )

  U = np.identity ( n )
  for i in range ( 0, n ):
    for j in range ( i + 1, n ):
      U[i,j] = s * rng.standard_normal ( )

  A = np.matmul ( L, U )

  return A

def golub_matrix_test ( ):

#*****************************************************************************80
#
## golub_matrix_test() tests golub_matrix().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    02 January 2024
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng

  print ( '' )
  print ( 'golub_matrix_test():' )
  print ( '  golub_matrix() evaluates a random Golub matrix of order N.' )

  rng = default_rng ( )

  n = 5
  A = golub_matrix ( n, rng )
  print ( '' )
  print ( '  The Golub matrix:' )
  print ( A )

  return

def init ( A, b ):

#*****************************************************************************80
#
## init() initializes the data.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(m,n): the matrix.
#
#    real b(m,k): the right hand sides.
#
#  Output:
#
#    real Ab(m,n+k), the augmented matrix.
#
  import numpy as np

  b = np.atleast_2d ( b )

  Ab = np.hstack ( [ A, b ] )

  return Ab

def pivot ( Ab, j ):

#*****************************************************************************80
#
## pivot() finds the pivot row for variable j.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Ab(m,n+k), the augmented matrix.
#
#    integer j, the variable for which a pivot is sought.
#
#  Output:
#
#    real Ab(m,n+k), the augmented matrix after pivoting.
#
#    integer p, the row that was chosen for the pivot.
#
  import numpy as np

  p = np.argmax ( np.abs ( Ab[j:,j] ) )

  p = p + j

  if ( Ab[p,j] == 0.0 ):
    print ( 'pivot(): Fatal error!' )
    print ( '  No nonzero pivot could be found.' )
    raise Exception ( 'pivot(): Fatal error!' )

  if ( p != j ):
    t       = Ab[j,:].copy()
    Ab[j,:] = Ab[p,:].copy()
    Ab[p,:] = t.copy()

  return Ab, p

def ref ( m, n, a ):

#*****************************************************************************80
#
## ref() computes the row echelon form of a matrix.
#
#  Discussion:
#
#    A matrix is in row echelon form if:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#  Example:
#
#    Input matrix:
#
#     1.0  3.0  0.0  2.0  6.0  3.0  1.0
#    -2.0 -6.0  0.0 -2.0 -8.0  3.0  1.0
#     3.0  9.0  0.0  0.0  6.0  6.0  2.0
#    -1.0 -3.0  0.0  1.0  0.0  9.0  3.0
#
#    Output matrix:
#
#     1.0  3.0  0.0  2.0  6.0  3.0  1.0
#     0.0  0.0  0.0  1.0  2.0  4.5  1.5
#     0.0  0.0  0.0  0.0  0.0  1.0  0.3
#     0.0  0.0  0.0  0.0  0.0  0.0  0.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Cullen,
#    An Introduction to Numerical Linear Algebra,
#    PWS Publishing Company, 1994,
#    ISBN: 978-0534936903,
#    LC: QA185.D37.C85.
#
#  Input:
#
#    integer M, N, the number of rows and columns of
#    the matrix A.
#
#    real A(M,N), the matrix to be analyzed.
#
#  Output:
#
#    real A(M,N), the REF form of the matrix.
#
#    real DET, the pseudo-determinant.
#
  import numpy as np

  tol = np.finfo(float).eps

  det = 1.0
  asum = 0.0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      asum = asum + abs ( a[i,j] )
  tol = tol * asum
  lead = 0

  for r in range ( 0, m ):

    if ( n < lead ):
      break

    i = r

    while ( abs ( a[i,lead] ) <= 0.0 ):

      i = i + 1

      if ( m <= i ):
        i = r
        lead = lead + 1
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break

    temp     = a[i,0:n]
    a[i,0:n] = a[r,0:n]
    a[r,0:n] = temp

    det = det * a[r,lead]
    a[r,0:n] = a[r,0:n] / a[r,lead]

    for i in range ( r + 1, m ):
      a[i,0:n] = a[i,0:n] - a[i,lead] * a[r,0:n]

    lead = lead + 1

  return a, det

def ref_test ( ):

#*****************************************************************************80
#
## ref_test() tests ref().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 7

  a = np.array( [ \
    [  1.0,  3.0,  0.0,  2.0,  6.0,  3.0,  1.0 ], \
    [ -2.0, -6.0,  0.0, -2.0, -8.0,  3.0,  1.0 ], \
    [  3.0,  9.0,  0.0,  0.0,  6.0,  6.0,  2.0 ], \
    [ -1.0, -3.0,  0.0,  1.0,  0.0,  9.0,  3.0 ] ] )

  print ( '' )
  print ( 'ref_test():' )
  print ( '  ref computes the row echelon form of a matrix.' )
  print ( '' )
  print ( '  Matrix A:' )
  print ( a )

  a, det = ref ( m, n, a )

  print ( '' )
  print ( '  Pseudo-determinat = ', det )

  print ( '' )
  print ( '  REF(A):' )
  print ( a )

  return

def rref ( m, n, a ):

#*****************************************************************************80
#
## rref() computes the reduced row echelon form of a matrix.
#
#  Discussion:
#
#    A matrix is in row echelon form if:
#
#    * The first nonzero entry in each row is 1.
#
#    * The leading 1 in a given row occurs in a column to
#      the right of the leading 1 in the previous row.
#
#    * Rows which are entirely zero must occur last.
#
#    The matrix is in reduced row echelon form if, in addition to
#    the first three conditions, it also satisfies:
#
#    * Each column containing a leading 1 has no other nonzero entries.
#
#  Example:
#
#    Input matrix:
#
#     1.0  3.0  0.0  2.0  6.0  3.0  1.0
#    -2.0 -6.0  0.0 -2.0 -8.0  3.0  1.0
#     3.0  9.0  0.0  0.0  6.0  6.0  2.0
#    -1.0 -3.0  0.0  1.0  0.0  9.0  3.0
#
#    Output matrix:
#
#     1.0  3.0  0.0  0.0  2.0  0.0  0.0
#     0.0  0.0  0.0  1.0  2.0  0.0  0.0
#     0.0  0.0  0.0  0.0  0.0  1.0  0.3
#     0.0  0.0  0.0  0.0  0.0  0.0  0.0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 July 2020
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Charles Cullen,
#    An Introduction to Numerical Linear Algebra,
#    PWS Publishing Company, 1994,
#    ISBN: 978-0534936903,
#    LC: QA185.D37.C85.
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix A.
#
#    real A(M,N), the matrix to be analyzed. 
#
#  Output:
#
#    real A(M,N), the RREF form of the matrix.
#
#    real DET, the pseudo-determinant.
#
  import numpy as np

  det = 1.0
  asum = 0.0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      asum = asum + abs ( a[i,j] )
  tol = asum * np.finfo(float).eps
  lead = 0

  for r in range ( 0, m ):

    if ( n <= lead ):
      break

    i = r

    while ( abs ( a[i,lead] ) <= tol ):

      i = i + 1

      if ( m <= i ):
        i = r
        lead = lead + 1
        if ( n <= lead ):
          lead = -1
          break

    if ( lead < 0 ):
      break

    for j in range ( 0, n ):
      t      = a[i,j]
      a[i,j] = a[r,j]
      a[r,j] = t

    det = det * a[r,lead]
    a[r,0:n] = a[r,0:n] / a[r,lead]

    for i in range ( 0, m ):
      if ( i != r ):
        a[i,0:n] = a[i,0:n] - a[i,lead] * a[r,0:n]

    lead = lead + 1

  return a, det

def rref_test ( ):

#*****************************************************************************80
#
## rref_test() tests rref().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 4
  n = 7

  a = np.array( [ \
    [  1.0,  3.0,  0.0,  2.0,  6.0,  3.0,  1.0 ], \
    [ -2.0, -6.0,  0.0, -2.0, -8.0,  3.0,  1.0 ], \
    [  3.0,  9.0,  0.0,  0.0,  6.0,  6.0,  2.0 ], \
    [ -1.0, -3.0,  0.0,  1.0,  0.0,  9.0,  3.0 ] ] )

  print ( '' )
  print ( 'rref_test():' )
  print ( '  rref computes the reduced row echelon form of a matrix.' )
  print ( '' )
  print ( '  Matrix A:' )
  print ( a )

  a, det = rref ( m, n, a )

  print ( '' )
  print ( '  Pseudo-determinant = ', det )

  print ( '' )
  print ( '  RREF(A):' )
  print ( a )

  return

def scale ( Ab, i, j = None ):

#*****************************************************************************80
#
## scale() scales row i so that Ab(i,j) = 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Ab(m,n+k), the augmented matrix.
#
#    integer i, j, the row and column indices of the entry whose value
#    is used to normalize row i.  Ab(i,j) must not be zero.
#    j defaults to i.
#
#  Output:
#
#    real Ab(m,n+k), the augmented matrix has been modified.
#    Row i was divided by Ab(i,j).
#
  if ( j == None ):
    j = i

  m, npk = Ab.shape

  if ( i < 0 or m <= i ):
    print ( 'scale(): Fatal error!' )
    print ( '  0 <= I < ', m, ' is required.' )
    raise Exception ( 'scale(): Fatal error!' )

  if ( j < 0 or npk <= j ):
    print ( 'scale(): Fatal error!' )
    print ( '  1 <= J <= ', npk, ' is required.' )
    raise Exception ( 'scale(): Fatal error!' )

  if ( Ab[i,j] == 0.0 ):
    print ( 'scale(): Fatal error!' )
    print ( '  Ab(',i,',',j,') = 0.' )
    raise Exception ( 'scale(): Fatal error!' )

  Ab[i,:] = Ab[i,:] / Ab[i,j]

  return Ab

def solution ( Ab ):

#*****************************************************************************80
#
## solution() returns the solution.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    15 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real Ab(m,n+k), the augmented matrix has been modified.
#
#  Output:
#
#    real x(m,k), the solution vectors.
#
  import numpy as np

  m, npk = Ab.shape

  I = np.identity ( m )

  norm_fro = np.linalg.norm ( Ab[0:m,0:m] - I, 'fro' )

  tol = np.finfo(float).eps

  if ( tol < norm_fro ):
    print ( 'solution(): Fatal error!' )
    print ( '  Augmented matrix Ab does not start with the identity.' )
    raise Exception ( 'solution(): Fatal error!' )

  x = Ab[0:m,m:]

  return x

def swap ( i1, i2 ):

#*****************************************************************************80
#
## swap() swaps rows i1 and i2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 September 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer i1, i2, the rows to be swapped.
#
#  Output:
#
#    real Ab(m,n+k), the augmented matrix has been modified.
#
  if ( i1 < 1 or m < i1 ):
    print ( 'swap(): Fatal error!' )
    print ( '  1 <= I1 <= #d is required.', m )
    raise Exception ( 'swap(): Fatal error!' )

  if ( i2 < 1 or m < i2 ):
    print ( 'swap(): Fatal error!' )
    print ( '  1 <= I2 <= #d is required.', m )
    raise Exception ( 'swap(): Fatal error!' )

  t        = Ab[i1,:]
  Ab[i1,:] = Ab[i2,:]
  Ab[i2,:] = t

  return Ab

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

if ( __name__ == "__main__" ):
  timestamp ( )
  eros_test ( )
  timestamp ( )

