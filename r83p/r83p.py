#! /usr/bin/env python3
#
def r83p_test ( ):

#*****************************************************************************80
#
## r83p_test() tests r83p().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 August 2022
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform

  print ( '' )
  print ( 'r83p_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r83p().' )

  rng = default_rng ( )

  r83_np_sl_test ( rng )

  r83p_det_test ( )
  r83p_fa_test ( rng )
  r83p_indicator_test ( )
  r83p_ml_test ( rng )
  r83p_mtv_test ( )
  r83p_mv_test ( )
  r83p_print_test ( )
  r83p_print_some_test ( )
  r83p_random_test ( rng )
  r83p_sl_test ( rng )
  r83p_to_r8ge_test ( rng )
  r83p_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r83p_test():' )
  print ( '  Normal end of execution.' )

  return

def i4_log_10 ( i ):

#*****************************************************************************80
#
## i4_log_10() returns the integer part of the logarithm base 10 of ABS(X).
#
#  Example:
#
#        I  VALUE
#    -----  --------
#        0    0
#        1    0
#        2    0
#        9    0
#       10    1
#       11    1
#       99    1
#      100    2
#      101    2
#      999    2
#     1000    3
#     1001    3
#     9999    3
#    10000    4
#
#  Discussion:
#
#    i4_log_10 ( I ) + 1 is the number of decimal digits in I.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer I, the number whose logarithm base 10 is desired.
#
#  Output:
#
#    integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  import numpy as np

  i = np.floor ( i )

  if ( i == 0 ):

    value = 0

  else:

    value = 0
    ten_pow = 10

    i_abs = abs ( i )

    while ( ten_pow <= i_abs ):
      value = value + 1
      ten_pow = ten_pow * 10

  return value

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
#    real A_LU(3,N), the LU factors of R83_FA.
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

def r83_np_sl_test ( rng ):

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
#  Input:
#
#    rng: the current random number generator.
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
  a = r83_random ( n, n, rng )

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

def r83_random ( m, n, rng ):

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
#    rng: the current random number generator.
#
#  Output:
#
#    real A(3,N), the R83 matrix.
#
  import numpy as np

  a = np.zeros ( [ 3, n ] )

  for j in range ( 0, n ):
    for i in range ( max ( 0, j - 1 ), min ( m, j + 2 ) ):
      a[i-j+1,j] = rng.random ( )
 
  return a

def r83p_det ( n, a_lu, work4 ):

#*****************************************************************************80
#
## r83p_det() computes the determinant of a matrix factored by r83p_fa().
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as 
#    a 3 by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  The matrix value 
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 3.
#
#    real A_LU(3,N), the LU factors of R83P_FA.
#
#    real WORK4, factorization information of R83P_FA.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = work4

  for j in range ( 0, n - 1 ):
    det = det * a_lu[1,j]

  return det

def r83p_det_test ( ):

#*****************************************************************************80
#
## r83p_det_test() tests r83p_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r83p_det_test():' )
  print ( '  r83p_det() computes determinant of a tridiagonal periodic matrix.' )
#
#  Set the matrix.
#
  n = 5
  a = r83p_indicator ( n )

  r83p_print ( n, a, '  The periodic tridiagonal matrix:' )
#
#  Copy the matrix into a general array.
#
  b = r83p_to_r8ge ( n, a )
#
#  Factor the matrix.
#
  a_lu, work2, work3, work4, info = r83p_fa ( n, a )
#
#  Compute the determinant.
#
  det = r83p_det ( n, a_lu, work4 )

  print ( '' )
  print ( '  r83p_det() computes the determinant = ', det )
#
#  Factor the general matrix.
#
  b_lu, pivot, info = r8ge_fa ( n, b )
#
#  Compute the determinant.
#
  det = r8ge_det ( n, b_lu, pivot )

  print ( '  r8ge_det() computes the determinant = ', det )

  print ( '  np.linalg.det() computes            = ', np.linalg.det ( b ) )

  return

def r83p_fa ( n, a ):

#*****************************************************************************80
#
## r83p_fa() factors a R83P matrix.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as 
#    a 3 by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  The matrix value 
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#    Once the matrix has been factored by R83P_FA, R83P_SL may be called
#    to solve linear systems involving the matrix.
#
#    The logical matrix has a form which is suggested by this diagram:
#
#      D1 U1          L1
#      L2 D2 U2
#         L3 R83 U3
#            L4 D4 U4
#               L5 D5 U5
#      U6          L6 D6
#
#    The algorithm treats the matrix as a border banded matrix:
#
#      ( A1  A2 )
#      ( A3  A4 )
#
#    where:
#
#      D1 U1          | L1
#      L2 D2 U2       |  0
#         L3 R83 U3    |  0
#            L4 D4 U4 |  0
#               L5 D5 | U5
#      ---------------+---
#      U6  0  0  0 L6 | D6
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Method:
#
#    The algorithm rewrites the system as:
#
#         X1 + inverse(A1) A2 X2 = inverse(A1) B1
#
#      A3 X1 +             A4 X2 = B2
#
#    The first equation can be "solved" for X1 in terms of X2:
#
#         X1 = - inverse(A1) A2 X2 + inverse(A1) B1
#
#    allowing us to rewrite the second equation for X2 explicitly:
#
#      ( A4 - A3 inverse(A1) A2 ) X2 = B2 - A3 inverse(A1) B1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 3.
#
#    real A(3,N), the periodic tridiagonal matrix.  
#    On the arrays have been modified to hold information
#    defining the border-banded factorization of submatrices A1
#    and A3.
#
#  Output:
#
#    real A_LU(3,N), information defining the border-banded factorization 
#    of submatrices A1 and A3.
#
#    real WORK2(N-1), WORK3(N-1), WORK4, factorization information.
#
#    integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  import numpy as np
#
#  Factor A1:
#
  a1_lu, info = r83_np_fa ( n - 1, a )
  
  if ( info != 0 ):
    print ( '' )
    print ( 'R83P_FA - Fatal error!' )
    print ( '  R83_NP_FA returned INFO = ', info )
    print ( '  Factoring failed for column INFO.' )
    print ( '  The tridiagonal matrix A1 is singular.' )
    print ( '  This algorithm cannot continue!' )
    raise Exception ( 'R83P_FA - Fatal error!' )
#
#  WORK2 := inverse(A1) * A2.
#
  temp = np.zeros ( n - 1 )
  temp[0] = a[2,n-1]
  temp[n-2] = a[0,n-1]

  job = 0
  work2 = r83_np_sl ( n - 1, a1_lu, temp, job )
#
#  WORK3 := inverse ( A1' ) * A3'.
#
  temp = np.zeros ( n - 1 )
  temp[0] = a[0,0]
  temp[n-2] = a[2,n-2]

  job = 1
  work3 = r83_np_sl ( n - 1, a1_lu, temp, job )
#
#  A4 := ( A4 - A3 * inverse(A1) * A2 )
#
  work4 = a[1,n-1] - a[0,0] * work2[0] - a[2,n-2] * work2[n-2]

  if ( work4 == 0.0 ):
    info = n
    print ( '' )
    print ( 'r83p_fa(): Fatal error!' )
    print ( '  The factored A4 submatrix is zero.' )
    print ( '  This algorithm cannot continue!' )
    raise Exception ( 'r83p_fa(): Fatal error!' )
#
#  Pack up A_LU:
#
  a_lu = np.zeros ( [ 3, n ] )
  for i in range ( 0, 3 ):
    for j in range ( 0, n - 1 ):
      a_lu[i,j] = a1_lu[i,j]
  
  a_lu[0,0] = a[0,0]
  a_lu[2,n-2] = a[2,n-2]
  for i in range ( 0, 3 ):
    a_lu[i,n-1] = a[i,n-1]

  return a_lu, work2, work3, work4, info

def r83p_fa_test ( rng ):

#*****************************************************************************80
#
## r83p_fa_test() tests r83p_fa().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'r83p_fa_test():' )
  print ( '  r83p_fa() factors a tridiagonal periodic system' )
  print ( '  which then can be solved by R83P_SL.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83p_random ( n, rng )
#
#  Factor the matrix.
#
  a_lu, work2, work3, work4, info = r83p_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R83P_FA_TEST - Fatal error!' )
    print ( '  R83P_FA returns INFO = ', info )
    return

  for job in range ( 0, 2 ):
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    b = r83p_ml ( n, a_lu, x, job )
#
#  Solve the linear system.
#
    x = r83p_sl ( n, a_lu, b, job, work2, work3, work4 )

    if ( job == 0 ):
      r8vec_print ( n, x, '  Solution:' )
    else:
      r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r83p_indicator ( n ):

#*****************************************************************************80
#
## r83p_indicator() sets up a R83P indicator matrix.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as 
#    a 3 by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  The matrix value 
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#    Here are the values as stored in an indicator matrix:
#
#      51 12 23 34 45
#      11 22 33 44 55
#      21 32 43 54 15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
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
#  Output:
#
#    real A(3,N), the R83P indicator matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( [ 3, n ] )

  i = n - 1
  j = 0
  a[0,j] = fac * ( i + 1 ) + ( j + 1 )
  for j in range ( 1, n ):
    i = j - 1
    a[0,j] = fac * ( i + 1 ) + ( j + 1 )

  for j in range ( 0, n ):
    i = j
    a[1,j] = fac * ( i + 1 ) + ( j + 1 )

  for j in range ( 0, n - 1 ):
    i = j + 1
    a[2,j] = fac * ( i + 1 ) + ( j + 1 )

  i = 0
  j = n - 1
  a[2,j] = fac * ( i + 1 ) + ( j + 1 )

  return a

def r83p_indicator_test ( ):

#*****************************************************************************80
#
## r83p_indicator_test() tests r83p_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'R83P_INDICATOR_TEST' )
  print ( '  R83P_INDICATOR sets up an R83P indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83p_indicator ( n )

  r83p_print ( n, a, '  The R83P indicator matrix:' )

  return

def r83p_ml ( n, a_lu, x, job ):

#*****************************************************************************80
#
## r83p_ml() computes A * x or x * A, where A has been factored by R83P_FA.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as 
#    a 3 by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  The matrix value 
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 3.
#
#    real A_LU(3,N), the factors computed by R83P_FA.
#
#    real X(N), the vector to be multiplied by the matrix.
#
#    integer JOB, indicates what product should be computed.
#    0, compute A * x.
#    nonzero, compute A' * x.
#
#  Output:
#
#    real B(N), the result of the multiplication.
#
  import numpy as np
#
#  Multiply A(1:N-1,1:N-1) and X(1:N-1).
#
  a1_lu = np.zeros ( [ 3, n - 1 ] )
  for i in range ( 0, 3 ):
    for j in range ( 0, n - 1 ):
      a1_lu[i,j] = a_lu[i,j]

  b1 = r83_np_ml ( n - 1, a1_lu, x, job )

  b = np.zeros ( n )
  for i in range ( 0, n - 1 ):
    b[i] = b1[i]
#
#  Add border terms.
#
  if ( job == 0 ):
    b[0] = b[0] + a_lu[2,n-1] * x[n-1]
    b[n-2] = b[n-2] + a_lu[0,n-1] * x[n-1]
    b[n-1] = a_lu[0,0] * x[0] + a_lu[2,n-2] * x[n-2] + a_lu[1,n-1] * x[n-1]
  else:
    b[0] = b[0] + a_lu[0,0] * x[n-1]
    b[n-2] = b[n-2] + a_lu[2,n-2] * x[n-1]
    b[n-1] = a_lu[2,n-1] * x[0] + a_lu[0,n-1] * x[n-2] + a_lu[1,n-1] * x[n-1]

  return b

def r83p_ml_test ( rng ):

#*****************************************************************************80
#
## r83p_ml_test() tests r83p_ml().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'r83p_ml_test()' )
  print ( '  r83p_ml() computes A*x or A\'*X' )
  print ( '  where A has been factored by R83P_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  for job in range ( 0, 2 ):
#
#  Set the matrix.
#
    a = r83p_random ( n, rng )
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r83p_mv ( n, a, x )
    else:
      b = r83p_mtv ( n, a, x )
#
#  Factor the matrix.
#
    a_lu, work2, work3, work4, info = r83p_fa ( n, a )

    if ( info != 0 ):
      print ( '' )
      print ( 'R83P_ML_TEST - Fatal error!' )
      print ( '  R83P_FA declares the matrix is singular!' )
      print ( '  The value of INFO is ', info )
      return
#
#  Now multiply factored matrix times solution to get right hand side again.
#
    b2 = r83p_ml ( n, a_lu, x, job )

    if ( job == 0 ):
      r8vec2_print_some ( n, b, b2, 10, '  A*x and PLU*x' )
    else:
      r8vec2_print_some ( n, b, b2, 10, '  A\'*x and (PLU)\'*x' )

  return

def r83p_mtv ( n, a, x ):

#*****************************************************************************80
#
## r83p_mtv() multiplies a vector by a R83P matrix.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as
#    a 3 by N array, in which each row corresponds to a diagonal, and
#    column locations are preserved.  The matrix value
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 3.
#
#    real A(3,N), the R83P matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product X * A.
#
  import numpy as np

  b = np.zeros ( n )

  b[0] = a[0,0] * x[n-1] + a[1,0] * x[0] + a[2,0] * x[1]

  for i in range ( 1, n - 1 ):
    b[i] = a[0,i] * x[i-1] + a[1,i] * x[i] + a[2,i] * x[i+1]

  b[n-1] = a[0,n-1] * x[n-2] + a[1,n-1] * x[n-1] + a[2,n-1] * x[0]

  return b

def r83p_mtv_test ( ):

#*****************************************************************************80
#
## r83p_mtv_test() tests r83p_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R83P_MTV_TEST' )
  print ( '  R83P_MTV computes A\'*x=b for an R83P matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83p_indicator ( n )
  r83p_print ( n, a, '  The R83P matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  The vector X:' )

  b = r83p_mtv ( n, a, x )
  r8vec_print ( n, b, '  The product b = A\'*x:' )

  return

def r83p_mv ( n, a, x ):

#*****************************************************************************80
#
## r83p_mv() multiplies a R83P matrix times a vector.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as 
#    a 3 by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  The matrix value 
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 3.
#
#    real A(3,N), the R83P matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  b[0] = a[2,n-1] * x[n-1] + a[1,0] * x[0] + a[0,1] * x[1]

  for i in range ( 1, n - 1 ):
    b[i] = a[2,i-1] * x[i-1] + a[1,i] * x[i] + a[0,i+1] * x[i+1]

  b[n-1] = a[2,n-2] * x[n-2] + a[1,n-1] * x[n-1] + a[0,0] * x[0]

  return b

def r83p_mv_test ( ):

#*****************************************************************************80
#
## r83p_mv_test() tests r83p_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R83P_MV_TEST' )
  print ( '  R83P_MV computes A*x=b for an R83P matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83p_indicator ( n )
  r83p_print ( n, a, '  The R83P matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  The vector X:' )

  b = r83p_mv ( n, a, x )
  r8vec_print ( n, b, '  The product b = A*x:' )

  return

def r83p_print ( n, a, title ):

#*****************************************************************************80
#
## r83p_print() prints a R83P matrix.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as 
#    a 3 by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  The matrix value 
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A(3,N), the R83P matrix.
#
#    string TITLE, a title.
#
  r83p_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return

def r83p_print_test ( ):

#*****************************************************************************80
#
## r83p_print_test() tests r83p_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R83P_PRINT_TEST' )
  print ( '  R83P_PRINT prints an R83P matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83p_indicator ( n )

  r83p_print ( n, a, '  The R83P matrix:' )

  return

def r83p_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r83p_print_some() prints some of a R83P matrix.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as
#    a 3 by N array, in which each row corresponds to a diagonal, and
#    column locations are preserved.  The matrix value
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A(3,N), the R83P matrix.
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
#  Determine the column range of the rows in this strip.
#
    i2lo = max ( ilo, 0 )

    if ( 0 < i2lo or j2hi < n - 1 ):
      i2lo = max ( i2lo, j2lo - 1 )

    i2hi = min ( ihi, n - 1 )

    if ( i2hi < n - 1 or 0 < j2lo ):
      i2hi = min ( i2hi, j2hi + 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%5d: ' % ( i ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j2 in range ( 1, inc + 1 ):

        j = j2lo - 1 + j2

        if ( i == n - 1 and j == 0 ):
          print ( '%12g  ' % ( a[0,j] ), end = '' )
        elif ( i == 0 and j == n - 1 ):
          print ( '%12g  ' % ( a[2,j] ), end = '' )
        elif ( 1 < i - j or 1 < j - i ):
          print ( '              ', end = '' )
        elif ( j == i + 1 ):
          print ( '%12g  ' % ( a[0,j] ), end = '' )
        elif ( j == i ):
          print ( '%12g  ' % ( a[1,j] ), end = '' )
        elif ( j == i - 1 ):
          print ( '%12g  ' % ( a[2,j] ), end = '' )

      print ( '' )

  return

def r83p_print_some_test ( ):

#*****************************************************************************80
#
## r83p_print_some_test() tests r83p_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'R83P_PRINT_SOME_TEST' )
  print ( '  R83P_PRINT_SOME prints some of an R83P matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83p_indicator ( n )

  r83p_print_some ( n, a, 1, 1, n, 2, '  Rows 1:N, Cols 1:2:' )

  return

def r83p_random ( n, rng ):

#*****************************************************************************80
#
## r83p_random() randomizes a R83P matrix.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as
#    a 3 by N array, in which each row corresponds to a diagonal, and
#    column locations are preserved.  The matrix value
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 3.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(3,N), the R83P matrix.
#
  a = rng.random ( size = [ 3, n ] )

  return a

def r83p_random_test ( rng ):

#*****************************************************************************80
#
## r83p_random_test() tests r83p_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 5

  print ( '' )
  print ( 'r83p_random_test():' )
  print ( '  r83p_random() sets up a random R83P matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83p_random ( n, rng )

  r83p_print ( n, a, '  The R83P matrix:' )

  return

def r83p_sl ( n, a_lu, b, job, work2, work3, work4 ):

#*****************************************************************************80
#
## r83p_sl() solves a R83P system.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as
#    a 3 by N array, in which each row corresponds to a diagonal, and
#    column locations are preserved.  The matrix value
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#    The linear system must have been factored by R83P_FA.
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 3.
#
#    real A_LU(3,N), the LU factors of R83P_FA.
#
#    real B(N), the right hand side of the linear system.
#
#    integer JOB, specifies the system to solve.
#    0, solve A * x = b.
#    nonzero, solve A' * x = b.
#
#    real WORK2(N-1), WORK3(N-1), WORK4, factor data of R83P_FA.
#
#  Output:
#
#    real X(N), the solution to the linear system.
#
  import numpy as np

  x = b.copy();

  if ( job == 0 ):
#
#  Solve A1 * X1 = B1.
#
    x1 = r83_np_sl ( n - 1, a_lu, x, job )
#
#  X2 = B2 - A3 * X1
#
    x = np.zeros ( n )
    for i in range ( 0, n - 1 ):
      x[i] = x1[i]

    x[n-1] = b[n-1] - a_lu[0,0] * x[0] - a_lu[2,n-2] * x[n-2]
#
#  Solve A4 * X2 = X2
#
    x[n-1] = x[n-1] / work4
#
#  X1 := X1 - inverse ( A1 ) * A2 * X2.
#
    for i in range ( 0, n - 1 ):
      x[i] = x[i] - work2[i] * x[n-1]

  else:
#
#  Solve A1' * X1 = B1.
#
    x1 = r83_np_sl ( n - 1, a_lu, x, job )
#
#  X2 := X2 - A2' * B1
#
    x = np.zeros ( n )
    for i in range ( 0, n - 1 ):
      x[i] = x1[i]

    x[n-1] = b[n-1] - a_lu[2,n-1] * x[0] - a_lu[0,n-1] * x[n-2]
#
#  Solve A4 * X2 = X2.
#
    x[n-1] = x[n-1] / work4
#
#  X1 := X1 - transpose ( inverse ( A1 ) * A3 ) * X2.
#
    for i in range ( 0, n - 1 ):
      x[i] = x[i] - work3[i] * x[n-1]

  return x

def r83p_sl_test ( rng ):

#*****************************************************************************80
#
## r83p_sl_test() tests r83p_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 10

  print ( '' )
  print ( 'r83p_sl_test():' )
  print ( '  r83p_sl() solves a tridiagonal periodic system' )
  print ( '  after it has been factored by R83P_FA.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83p_random ( n, rng )
#
#  Factor the matrix.
#
  a_lu, work2, work3, work4, info = r83p_fa ( n, a )

  if ( info != 0 ):
    print ( '' )
    print ( 'R83P_SL_TEST - Fatal error!' )
    print ( '  R83P_FA returns INFO = ', info )
    return

  for job in range ( 0, 2 ):
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    b = r83p_ml ( n, a_lu, x, job )
#
#  Solve the linear system.
#
    x = r83p_sl ( n, a_lu, b, job, work2, work3, work4 )

    if ( job == 0 ):
      r8vec_print ( n, x, '  Solution:' )
    else:
      r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r83p_to_r8ge ( n, a ):

#*****************************************************************************80
#
## r83p_to_r8ge() copies a R83P matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as
#    a 3 by N array, in which each row corresponds to a diagonal, and
#    column locations are preserved.  The matrix value
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be at least 3.
#
#    real A(3,N), the R83P matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i == j ):
        b[i,j] = a[1,j]
      elif ( j == i - 1 ):
        b[i,j] = a[2,j]
      elif ( j == i + 1 ):
        b[i,j] = a[0,j]
      elif ( i == 0 and j == n - 1 ):
        b[i,j] = a[2,j]
      elif ( i == n - 1 and j == 0 ):
        b[i,j] = a[0,j]
      else:
        b[i,j] = 0.0

  return b

def r83p_to_r8ge_test ( rng ):

#*****************************************************************************80
#
## r83p_to_r8ge_test() tests r83p_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  n = 5

  print ( '' )
  print ( 'r83p_to_r8ge_test():' )
  print ( '  r83p_to_r8ge() converts an r83p matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a_r83p = r83p_random ( n, rng )
  r83p_print ( n, a_r83p, '  The R83P matrix:' )

  a_r8ge = r83p_to_r8ge ( n, a_r83p )
  r8ge_print ( n, n, a_r8ge, '  The R8GE matrix:' )

  return

def r83p_zeros ( n ):

#*****************************************************************************80
#
## r83p_zeros() sets up a zero R83P matrix.
#
#  Discussion:
#
#    The R83P storage format stores a periodic tridiagonal matrix as 
#    a 3 by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  The matrix value 
#    A(1,N) is stored as the array entry A(3,N), and the matrix value
#    A(N,1) is stored as the array entry A(1,1).
#
#  Example:
#
#    Here is how a R83P matrix of order 5 would be stored:
#
#      A51 A12 A23 A34 A45
#      A11 A22 A33 A44 A55
#      A21 A32 A43 A54 A15
#
#    Here are the values as stored in an indicator matrix:
#
#      51 12 23 34 45
#      11 22 33 44 55
#      21 32 43 54 15
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
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
#  Output:
#
#    real A(3,N), the R83P matrix.
#
  import numpy as np

  a = np.zeros ( [ 3, n ] )

  return a

def r83p_zeros_test ( ):

#*****************************************************************************80
#
## r83p_zeros_test() tests r83p_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 May 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R83P_ZEROS_TEST' )
  print ( '  R83P_ZEROS sets up a zero R83P matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r83p_zeros ( n )

  r83p_print ( n, a, '  The R83P matrix:' )

  return

def r8ge_det ( n, a_lu, pivot ):

#*****************************************************************************80
#
## r8ge_det(): determinant of a matrix factored by r8ge_fa() or r8ge_trf().
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
#
#    R8GE storage is used by LINPACK and LAPACK.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Jack Dongarra, Jim Bunch, Cleve Moler, Pete Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979,
#    ISBN13: 978-0-898711-72-1,
#    LC: QA214.L56.
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_LU(N,N), the LU factors of r8ge_fa() or r8ge_trf().
#
#    integer PIVOT(N), as computed by r8ge_fa or r8ge_trf.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  value = 1.0

  for i in range ( 0, n ):
    value = value * a_lu[i,i]
    if ( pivot[i] != i ):
      value = - value

  return value

def r8ge_fa ( n, a ):

#*****************************************************************************80
#
## r8ge_fa() performs a LINPACK style PLU factorization of a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_fa is a simplified version of the LINPACK routine R8GEFA.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Dongarra, Bunch, Moler, Stewart,
#    LINPACK User's Guide,
#    SIAM, 1979
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A(N,N), the matrix to be factored.
#
#  Output:
#
#    real A_LU(N,N), an upper triangular matrix and 
#    the multipliers used to obtain it.  The factorization 
#    can be written A = L * U, where L is a product of 
#    permutation and unit lower triangular matrices and U 
#    is upper triangular.
#
#    integer PIVOT(N), a vector of pivot indices.
#
#    integer INFO, singularity flag.
#    0, no singularity detected.
#    nonzero, the factorization failed on the INFO-th step.
#
  import numpy as np

  a_lu = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a_lu[i,j] = a[i,j]

  info = 0

  pivot = np.zeros ( n, dtype = np.int32 )

  for k in range ( 0, n - 1 ):
#
#  Find L, the index of the pivot row.
#
    l = k
    for i in range ( k + 1, n ):
      if ( abs ( a_lu[l,k] ) < abs ( a_lu[i,k] ) ):
        l = i

    pivot[k] = l
#
#  If the pivot index is zero, the algorithm has failed.
#
    if ( a_lu[l,k] == 0.0 ):
      info = k
      return a_lu, pivot, info
#
#  Interchange rows L and K if necessary.
#
    if ( l != k ):
      t         = a_lu[l,k]
      a_lu[l,k] = a_lu[k,k]
      a_lu[k,k] = t
#
#  Normalize the values that lie below the pivot entry A(K,K).
#
    for i in range ( k + 1, n ):
      a_lu[i,k] = - a_lu[i,k] / a_lu[k,k]
#
#  Row elimination with column indexing.
#
    for j in range ( k + 1, n ):

      if ( l != k ):
        t         = a_lu[l,j]
        a_lu[l,j] = a_lu[k,j]
        a_lu[k,j] = t

      for i in range ( k + 1, n ):
        a_lu[i,j] = a_lu[i,j] + a_lu[i,k] * a_lu[k,j]

  pivot[n-1] = n - 1

  if ( a_lu[n-1,n-1] == 0.0 ):
    info = n - 1

  return a_lu, pivot, info

def r8ge_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8ge_print() prints an R8GE matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
#    string TITLE, a title.
#
  r8ge_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ge_print_some() prints out a portion of an R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#    real A(M,N), an M by N matrix to be printed.
#
#    integer ILO, JLO, the first row and column to print.
#
#    integer IHI, JHI, the last row and column to print.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8ge_sl ( n, a_lu, pivot, b, job ):

#*****************************************************************************80
#
## r8ge_sl() solves a system factored by r8ge_fa().
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    r8ge_sl is a simplified version of the LINPACK routine R8GESL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#    N must be positive.
#
#    real A_LU(N,N), the LU factors from r8ge_fa.
#
#    integer PIVOT(N), the pivot vector from r8ge_fa.
#
#    real B(N), the right hand side vector.
#
#    integer JOB, specifies the operation.
#    0, solve A * x = b.
#    nonzero, solve A' * x = b.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]
#
#  Solve A * x = b.
#
  if ( job == 0 ):
#
#  Solve PL * Y = B.
#
    for k in range ( 0, n - 1 ):

      l = pivot[k]

      if ( l != k ):
        t    = x[l]
        x[l] = x[k]
        x[k] = t

      for i in range ( k + 1, n ):
        x[i] = x[i] + a_lu[i,k] * x[k]
#
#  Solve U * X = Y.
#
    for k in range ( n - 1, -1, -1 ):
      x[k] = x[k] / a_lu[k,k]
      for i in range ( 0, k ):
        x[i] = x[i] - a_lu[i,k] * x[k]
#
#  Solve A' * X = B.
#
  else:
#
#  Solve U' * Y = B.
#
    for k in range ( 0, n ):
      for i in range ( 0, k ):
        x[k] = x[k] - x[i] * a_lu[i,k]
      x[k] = x[k] / a_lu[k,k]
#
#  Solve ( PL )' * X = Y.
#
    for k in range ( n - 2, -1, -1 ):
      for i in range ( k + 1, n ):
        x[k] = x[k] + x[i] * a_lu[i,k]

      l = pivot[k]

      if ( l != k ):
        t    = x[l]
        x[l] = x[k]
        x[k] = t

  return x

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
  r83p_test ( )
  timestamp ( )
 
