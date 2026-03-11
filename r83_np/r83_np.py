#! /usr/bin/env python3
#
def r83_np_test ( ):

#*****************************************************************************80
#
## r83_np_test() tests r83_np().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    24 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r83_np_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r83_np().' )

  r83_np_det_test ( )
  r83_np_fa_test ( )
  r83_np_fs_test ( )
  r83_np_ml_test ( )
  r83_np_sl_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r83_np_test():' )
  print ( '  Normal end of execution.' )
  return

def r83_dif2 ( m, n ):

#*****************************************************************************80
#
## r83_dif2() returns the DIF2 matrix in R83 format.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)). 
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
#
#  Properties:
#
#    A is banded, with bandwidth 3.
#
#    A is tridiagonal.
#
#    Because A is tridiagonal, it has property A (bipartite).
#
#    A is a special case of the TRIS or tridiagonal scalar matrix.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is Toeplitz: constant along diagonals.
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
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Robert Gregory, David Karney,
#    A Collection of Matrices for Testing Computational Algorithms,
#    Wiley, 1969,
#    ISBN: 0882756494,
#    LC: QA263.68
#
#    Morris Newman, John Todd,
#    Example A8,
#    The evaluation of matrix inversion programs,
#    Journal of the Society for Industrial and Applied Mathematics,
#    Volume 6, Number 4, pages 466-476, 1958.
#
#    John Todd,
#    Basic Numerical Mathematics,
#    Volume 2: Numerical Algebra,
#    Birkhauser, 1980,
#    ISBN: 0817608117,
#    LC: QA297.T58.
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(3,N), the matrix.
#
  import numpy as np

  a = np.zeros( [ 3, n ] )

  for j in range ( 0, n):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      if ( i == j - 1 ):
        a[i-j+1,j] = -1.0
      elif ( i == j ):
        a[i-j+1,j] = +2.0
      elif ( i == j + 1 ):
        a[i-j+1,j] = -1.0
  
  return a

def r83_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r83_mtv() multiplies a vector by an R83 matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(3,N), the R83 matrix.
#
#    real X(N), the vector to be multiplied by A'.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      b[j] = b[j] + x[i] * a[i-j+1,j]

  return b

def r83_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r83_mv() multiplies a R83 matrix times a vector.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the linear system.
#
#    real A(3,N), the R83 matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      b[i] = b[i] + a[i-j+1,j] * x[j]

  return b

def r83_np_det ( n, a ):

#*****************************************************************************80
#
## r83_np_det() returns the determinant of a R83 system factored by r83_np_fa.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:N), the diagonal in
#    entries (2,1:N), and the subdiagonal in (3,1:N-1).  Thus, the
#    original matrix is "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R83 matrix of order 5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 2.
#
#    real A(3,N), the tridiagonal factor information computed
#    by r83_np_fa.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = 1.0
  for j in range ( 0, n ):
    det = det * a[1,j]

  return det

def r83_np_det_test ( ):

#*****************************************************************************80
#
## r83_np_det_test() tests r83_np_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'r83_np_det_test():' )
  print ( '  r83_np_det() computes the determinant of a tridiagonal' )
  print ( '  matrix factored by r83_np_fa.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83_dif2 ( n, n )
#
#  Factor the matrix.
#
  a_lu, info = r83_np_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r83_np_det_test(): Fatal error!' )
    print ( '  r83_np_fa() returns INFO = ', info )
    raise Exception ( 'r83_np_det_test(): Fatal error!' )

  r83_print ( n, n, a_lu, '  The factored R83 matrix:' )
#
#  Compute the determinant.
#
  det = r83_np_det ( n, a_lu )

  print ( '' )
  print ( '  r83_np_det() computes determinant = ', det )
  print ( '  Exact determinant is = ', n + 1  )

  return

def r83_np_fa ( n, a ):

#*****************************************************************************80
#
## r83_np_fa() factors a R83 matrix without pivoting.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:N), the diagonal in
#    entries (2,1:N), and the subdiagonal in (3,1:N-1).  Thus, the
#    original matrix is "collapsed" vertically into the array.
#
#    Because this routine does not use pivoting, it can fail even when
#    the matrix is not singular, and it is liable to make larger
#    errors.
#
#    r83_np_fa and R83_NP_SL may be preferable to the corresponding
#    LINPACK routine SGTSL for tridiagonal systems, which factors and solves
#    in one step, and does not save the factorization.
#
#  Example:
#
#    Here is how a R83 matrix of order 5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 2.
#
#    real A(3,N), the tridiagonal matrix.
#
#  Output:
#
#    integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
#    real A_LU(3,N), factorization information.
#
  info = 0

  a_lu = a.copy ( )

  for j in range ( 0, n - 1 ):

    if ( a_lu[1,j] == 0.0 ):
      info = i
      print ( '' )
      print ( 'r83_np_fa(): Fatal error!' )
      print ( '  Zero pivot on step ', info )
      raise Exception ( 'r83_np_fa(): Fatal error!' )
#
#  Store the multiplier in L.
#
    a_lu[2,j] = a_lu[2,j] / a_lu[1,j]
#
#  Modify the diagonal entry in the next column.
#
    a_lu[1,j+1] = a_lu[1,j+1] - a_lu[2,j] * a_lu[0,j+1]

  if ( a_lu[1,n-1] == 0.0 ):
    info = n - 1
    print ( '' )
    print ( 'r83_np_fa(): Fatal error!' )
    print ( '  Zero pivot on step ', info )
    raise Exception ( 'r83_np_fa(): Fatal error!' )

  return a_lu, info

def r83_np_fa_test ( ):

#*****************************************************************************80
#
## r83_np_fa_test() tests r83_np_fa().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r83_np_fa_test():' )
  print ( '  r83_np_fa() factors a tridiagonal matrix with no pivoting' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83_random ( n, n )

  r83_print ( n, n, a, '  The tridiagonal matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r83_mv ( n, n, a, x )
  x = np.zeros ( n )
#
#  Factor the matrix.
#
  a_lu, info = r83_np_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r83_np_fa_test(): Fatal error!' )
    print ( '  The test matrix is singular.' )
    raise Exception ( 'r83_np_fa_test(): Fatal error!' )
#
#  Solve the linear system.
#
  job = 0
  x = r83_np_sl ( n, a_lu, b, job )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side, using the factored matrix.
#
  job = 1
  b = r83_np_ml ( n, a_lu, x, job )
#
#  Solve the linear system.
#
  job = 1
  x = r83_np_sl ( n, a_lu, b, job )

  r8vec_print ( n, x, '  Solution to tranposed system:' )

  return

def r83_np_fs ( n, a, b ):

#*****************************************************************************80
#
## r83_np_fs() factors and solves a R83 system with no pivoting.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:N), the diagonal in
#    entries (2,1:N), and the subdiagonal in (3,1:N-1).  Thus, the
#    original matrix is "collapsed" vertically into the array.
#
#    This algorithm requires that each diagonal entry be nonzero.
#    It does not use pivoting, and so can fail on systems that
#    are actually nonsingular.
#
#  Example:
#
#    Here is how a R83 matrix of order 5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the linear system.
#
#    real A(3,N): the tridiagonal matrix.
#
#    real B(N), the right hand side of the linear system.
#
#  Output:
#
#    real A(3,N): input overwritten by factorization information.
#
#    real X(N), the solution of the linear system.
#

#
#  The diagonal entries can't be zero.
#
  for j in range ( 0, n ):
    if ( a[1,j] == 0.0 ):
      print ( '' )
      print ( 'r83_np_fs(): Fatal error!' )
      print ( '  A(2,%d) = 0.', j )
      raise Exception ( 'r83_np_fs(): Fatal error!' )

  x = b.copy ( )

  for i in range ( 1, n ):
    xmult = a[2,i-1] / a[1,i-1]
    a[1,i] = a[1,i] - xmult * a[0,i]
    x[i]   = x[i]   - xmult * x[i-1]

  x[n-1] = x[n-1] / a[1,n-1]
  for i in range ( n - 2, -1, -1 ):
    x[i] = ( x[i] - a[0,i+1] * x[i+1] ) / a[1,i]

  return x

def r83_np_fs_test ( ):

#*****************************************************************************80
#
## r83_np_fs_test() tests r83_np_fs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r83_np_fs_test():' )
  print ( '  r83_np_fs() factors and solves a tridiagonal linear system.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix elements.
#
  a = r83_random ( n, n )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute b = A * x.
#
  b = r83_mv ( n, n, a, x )
#
#  Solve the system.
#
  x = r83_np_fs ( n, a, b )

  r8vec_print ( n, x, '  Solution:' )

  return

def r83_np_ml ( n, a_lu, x, job ):

#*****************************************************************************80
#
## r83_np_ml() computes A * x or x * A, where A has been factored by r83_np_fa().
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:N), the diagonal in
#    entries (2,1:N), and the subdiagonal in (3,1:N-1).  Thus, the
#    original matrix is "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R83 matrix of order 5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 2.
#
#    real A_LU(3,N), the LU factors from R83_FA.
#
#    real X(N), the vector to be multiplied by A.
#
#    integer JOB, specifies the product to find.
#    0, compute A * x.
#    nonzero, compute A' * x.
#
#  Output:
#
#    real B(N), the product A*x or A'*x.
#
  b = x.copy ( )

  if ( job == 0 ):
#
#  Compute X := U * X
#
    for i in range ( 0, n):
      b[i] = a_lu[1,i] * b[i]
      if ( i < n - 1 ):
        b[i] = b[i] + a_lu[0,i+1] * b[i+1]
#
#  Compute X: = L * X.
#
    for i in range ( n - 1, 0, -1 ):
      b[i] = b[i] + a_lu[2,i-1] * b[i-1]

  else:
#
#  Compute X: = L' * X.
#
    for i in range ( 0, n - 1 ):
      b[i] = b[i] + a_lu[2,i] * b[i+1]
#
#  Compute X: = U' * X.
#
    for i in range ( n - 1, 0, -1 ):
      b[i] = a_lu[1,i] * b[i]
      b[i] = b[i] + a_lu[0,i] * b[i-1]
    b[0] = a_lu[1,0] * b[0]

  return b

def r83_np_ml_test ( ):

#*****************************************************************************80
#
## r83_np_ml_test() tests r83_np_ml().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'r83_np_ml_test():' )
  print ( '  r83_np_ml() computes A*x or A\'*x' )
  print ( '  where A has been factored by r83_fa().' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a = r83_random ( n, n )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r83_mv ( n, n, a, x )
    else:
      b = r83_mtv ( n, n, a, x )
#
#  Factor the matrix.
#
    a_lu, info = r83_np_fa ( n, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'r83_np_ml_test(): Fatal error!' )
      print ( '  r83_np_fa() declares the matrix is singular!' )
      print ( '  The value of INFO is ', info )
      raise Exception ( 'r83_np_ml_test(): Fatal error!' )
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    b2 = r83_np_ml ( n, a_lu, x, job )

    if ( job == 0 ):
      r8vec2_print_some ( n, b, b2, 10, '  A*x and PLU*x:' )
    else:
      r8vec2_print_some ( n, b, b2, 10, '  A\'*x and (PLU)\'*x' )

  return

def r83_np_sl ( n, a_lu, b, job ):

#*****************************************************************************80
#
## r83_np_sl() solves a R83 system factored by r83_np_fa().
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:N), the diagonal in
#    entries (2,1:N), and the subdiagonal in (3,1:N-1).  Thus, the
#    original matrix is "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R83 matrix of order 5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 2.
#
#    real A_LU(3,N), the LU factor information
#    returned by r83_np_fa.
#
#    real B(N), the right hand side of the linear system.
#
#    integer JOB, specifies the system to solve.
#    0, solve A * x = b.
#    nonzero, solve A' * x = b.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  x = b.copy ( )
  
  if ( job == 0 ):
#
#  Solve L * Y = B.
#
    for i in range ( 1, n ):
      x[i] = x[i] - a_lu[2,i-1] * x[i-1]
#
#  Solve U * X = Y.
#
    for i in range ( n - 1, -1, -1 ):
      x[i] = x[i] / a_lu[1,i]
      if ( 0 < i ):
        x[i-1] = x[i-1] - a_lu[0,i] * x[i]

  else:
#
#  Solve U' * Y = B
#
    for i in range ( 0, n ):
      x[i] = x[i] / a_lu[1,i]
      if ( i < n - 1 ):
        x[i+1] = x[i+1] - a_lu[0,i+1] * x[i]
#
#  Solve L' * X = Y.
#
    for i in range ( n - 2, -1, -1 ):
      x[i] = x[i] - a_lu[2,i] * x[i+1]

  return x

def r83_np_sl_test ( ):

#*****************************************************************************80
#
## r83_np_sl_test() tests r83_np_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 10

  print ( '' )
  print ( 'r83_np_sl_test():' )
  print ( '  r83_np_sl() solves a linear system after the tridiagonal' )
  print ( '  matrix has been factored by r83_np_fa().' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83_random ( n, n )

  r83_print ( n, n, a, '  The tridiagonal matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r83_mv ( n, n, a, x )
  x = np.zeros ( n )
#
#  Factor the matrix.
#
  [ a_lu, info ] = r83_np_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'r83_np_sl_test(): Fatal error!' )
    print ( '  The test matrix is singular.' )
    raise Exception ( 'r83_np_sl_test(): Fatal error!' )
#
#  Solve the linear system.
#
  job = 0
  x = r83_np_sl ( n, a_lu, b, job )

  r8vec_print ( n, x, '  Solution:' )
#
#  Set the desired solution
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side, using the factored matrix.
#
  job = 1
  b = r83_np_ml ( n, a_lu, x, job )
#
#  Solve the linear system.
#
  job = 1
  x = r83_np_sl ( n, a_lu, b, job )

  r8vec_print ( n, x, '  Solution to tranposed system:' )

  return

def r83_print ( m, n, a, title ):

#*****************************************************************************80
#
## r83_print() prints a R83 matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(3,N), the R83 matrix.
#
#    string TITLE, a title.
#
  r83_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r83_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r83_print_some() prints some of a R83 matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A(3,N), the R83 matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column, to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )

    inc = j2hi + 1 - j2lo

    print ( '' )
    print ( '  Col: ', end = '' )
    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )
    print ( '' )
    print ( '  Row' )
    print ( '  ---' )
#
#  Determine the range of the rows in this strip.
#
    i2lo = max ( ilo, 0 )
    i2lo = max ( i2lo, j2lo - 1 )
    i2hi = min ( ihi, m - 1 )
    i2hi = min ( i2hi, j2hi + 1 )

    for i in range ( i2lo, i2hi + 1 ):
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      print ( '%5d:' % ( i ), end = '' )

      for j2 in range ( 1, inc + 1 ):

        j = j2lo - 1 + j2

        if ( i - j + 1 < 0 or 2 < i - j + 1 ):
          print ( '              ', end = '' )
        else:
          print ( '%14g' % ( a[i-j+1,j] ), end = '' )

      print ( '' )

  return

def r83_random ( m, n ):

#*****************************************************************************80
#
## r83_random() randomizes a R83 matrix.
#
#  Discussion:
#
#    The R83 storage format is used for a tridiagonal matrix.
#    The superdiagonal is stored in entries (1,2:min(M+1,N)).
#    The diagonal in entries (2,1:min(M,N)).
#    The subdiagonal in (3,min(M-1,N)).  
#    R8GE A(I,J) = R83 A[I-J+1+J*3] (0 based indexing).
#
#  Example:
#
#    An R83 matrix of order 3x5 would be stored:
#
#       *  A12 A23 A34  *
#      A11 A22 A33  *   *
#      A21 A32  *   *   *
#
#    An R83 matrix of order 5x5 would be stored:
#
#       *  A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54  *
#
#    An R83 matrix of order 5x3 would be stored:
#
#       *  A12 A23
#      A11 A22 A33
#      A21 A32 A43
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the linear system.
#
#  Output:
#
#    real A(3,N), the R83 matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( [ 3, n ] )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      a[i-j+1,j] = rng.random ( )
 
  return a

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## r8vec_indicator1() sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements of the vector.
#
#  Output:
#
#    real A(N), the indicator array.
#
  import numpy as np

  a = np.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## r8vec_print() prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the dimension of the vector.
#
#    real A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def r8vec2_print_some ( n, x1, x2, max_print, title ):

#*****************************************************************************80
#
## r8vec2_print_some() prints "some" of an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is two R8VEC's.
#
#    An R8VEC is a vector of R8 values.
#
#    The user specifies MAX_print, the maximum number of lines to print.
#
#    If N, the size of the vectors, is no more than MAX_print, then
#    the entire vectors are printed, one entry of each per line.
#
#    Otherwise, if possible, the first MAX_print-2 entries are printed,
#    followed by a line of periods suggesting an omission,
#    and the last entry.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries of the vectors.
#
#    real X1(N), X2(N), the vector to be printed.
#
#    integer MAX_print, the maximum number of lines to print.
#
#    string TITLE, a title.
#
  if ( max_print <= 0 ):
    return

  if ( n <= 0 ):
    return

  print ( '' )
  print ( title )
  print ( '' )

  if ( n <= max_print ):

    for i in range ( 0, n ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  elif ( 3 <= max_print ):

    for i in range ( 0, max_print - 2 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    print ( '......  ..............  ..............' )
    i = n - 1
    print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )

  else:

    for i in range ( 0, max_print - 1 ):
      print ( '%6d: %14g  %14g' % ( i, x1[i], x2[i] ) )
    i = max_print - 1
    print ( '%6d: %14g  %14g  ...more entries...' % ( i, x1[i], x2[i] ) )

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
  r83_np_test ( )
  timestamp ( )
 
