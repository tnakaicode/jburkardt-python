#! /usr/bin/env python3
#
def r8pbl_test ( ):

#*****************************************************************************80
#
## r8pbl_test() tests r8pbl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8pbl_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8pbl().' )

  r8pbl_dif2_test ( )
  r8pbl_indicator_test ( )
  r8pbl_mv_test ( )
  r8pbl_print_test ( )
  r8pbl_print_some_test ( )
  r8pbl_random_test ( )
  r8pbl_to_r8ge_test ( )
  r8pbl_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8pbl_test():' )
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

def r8pbl_dif2 ( n, ml ):

#*****************************************************************************80
#
## R8PBL_DIF2 returns the DIF2 matrix in R8PBL format.
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
#    23 July 2016
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
#    integer N, the number of rows and columns.
#
#    integer ML, the number of subdiagonals.
#    ML must be at least 0, and no more than N-1.
#
#  Output:
#
#    real A(ML+1,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ ml + 1, n ] )

  a[0,0:n]   = +2.0
  a[1,0:n-1] = -1.0
 
  return a

def r8pbl_dif2_test ( ):

#*****************************************************************************80
#
## R8PBL_DIF2_TEST tests R8PBL_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 1

  print ( '' )
  print ( 'R8PBL_DIF2_TEST' )
  print ( '  R8PBL_DIF2 sets an R8PBL second difference matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth ML = ', ml )

  a = r8pbl_dif2 ( n, ml )

  r8pbl_print ( n, ml, a, '  The R8PBL second difference matrix:' )

  return

def r8pbl_indicator ( n, ml ):

#*****************************************************************************80
#
## R8PBL_INDICATOR sets up a R8PBL indicator matrix.
#
#  Discussion:
#
#    The R8PBL storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and lower triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row 1 of the array.
#    The first subdiagonal in row 2, columns 1 through ML.
#    The second subdiagonal in row 3, columns 1 through ML-1.
#    The ML-th subdiagonal in row ML+1, columns 1 through 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 February 2004
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
#    integer ML, the number of subdiagonals in the matrix.
#    ML must be at least 0 and no more than N-1.
#
#  Output:
#
#    real A(ML+1,N), the R8PBL matrix.
#
  import numpy as np

  a = np.zeros ( [ ml + 1, n ] )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, n ):
    for j in range ( max ( 0, i - ml ), i + 1 ):
      a[i-j,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8pbl_indicator_test ( ):

#*****************************************************************************80
#
## R8PBL_INDICATOR_TEST tests R8PBL_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2003
#
#  Author:
#
#    John Burkardt
#
  n = 9
  ml = 3

  print ( '' )
  print ( 'R8PBL_INDICATOR_TEST' )
  print ( '  R8PBL_INDICATOR sets up a R8PBL indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth ML = ', ml )

  a = r8pbl_indicator ( n, ml )

  r8pbl_print ( n, ml, a, '  The R8PBL indicator matrix:' )

  return

def r8pbl_mv ( n, ml, a, x ):

#*****************************************************************************80
#
## R8PBL_MV multiplies an R8PBL matrix by an R8VEC.
#
#  Discussion:
#
#    The R8PBL storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and lower triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row 1 of the array.
#    The first subdiagonal in row 2, columns 1 through ML.
#    The second subdiagonal in row 3, columns 1 through ML-1.
#    The ML-th subdiagonal in row ML+1, columns 1 through 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ML, the number of subdiagonals in the matrix.
#    ML must be at least 0 and no more than N-1.
#
#    real A(ML+1,N), the R8PBL matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the result vector A * x.
#
  import numpy as np

  b = np.zeros ( n )
#
#  Multiply X by the diagonal of the matrix.
#
  for i in range ( 0, n ):
    b[i] = a[0,i] * x[i]
#
#  Multiply X by the subdiagonals of the matrix.
#
  for k in range ( 0, ml ):
    for j in range ( 0, n - k ):
      i = j + k
      aij = a[k+1,j]
      b[i] = b[i] + aij * x[j]
      b[j] = b[j] + aij * x[i]

  return b

def r8pbl_mv_test ( ):

#*****************************************************************************80
#
## R8PBL_MV_TEST tests R8PBL_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 2

  print ( '' )
  print ( 'R8PBL_MV_TEST' )
  print ( '  R8PBL_MV computes A*x, where A is an R8PBL matrix.' )
  print ( '' )
  print ( '  Matrix order N =     ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8pbl_random ( n, ml )

  r8pbl_print ( n, ml, a, '  Matrix A:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  Vector x:' )
#
#  Compute the corresponding right hand side.
#
  b = r8pbl_mv ( n, ml, a, x )

  r8vec_print ( n, b, '  Product b=A*x' )

  return

def r8pbl_print ( n, ml, a, title ):

#*****************************************************************************80
#
## R8PBL_PRINT prints a R8PBL matrix.
#
#  Discussion:
#
#    The R8PBL storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and lower triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row 1 of the array.
#    The first subdiagonal in row 2, columns 1 through ML.
#    The second subdiagonal in row 3, columns 1 through ML-1.
#    The ML-th subdiagonal in row ML+1, columns 1 through 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2016
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
#    integer ML, the upper (and lower) bandwidth.
#    ML must be nonnegative, and no greater than N-1.
#
#    real A(ML+1,N), the R8PBL matrix.
#
#    string TITLE, a title to be printed.
#
  r8pbl_print_some ( n, ml, a, 0, 0, n - 1, n - 1, title )

  return

def r8pbl_print_test ( ):

#*****************************************************************************80
#
## R8PBL_PRINT_TEST tests R8PBL_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 9
  ml = 3

  print ( '' )
  print ( 'R8PBL_PRINT_TEST' )
  print ( '  R8PBL_PRINT prints an R8PBL matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth ML = ', ml )

  a = r8pbl_indicator ( n, ml )

  r8pbl_print ( n, ml, a, '  The R8PBL matrix:' )

  return

def r8pbl_print_some ( n, ml, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8PBL_PRINT_SOME prints some of a R8PBL matrix.
#
#  Discussion:
#
#    The R8PBL storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and lower triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row 1 of the array.
#    The first subdiagonal in row 2, columns 1 through ML.
#    The second subdiagonal in row 3, columns 1 through ML-1.
#    The ML-th subdiagonal in row ML+1, columns 1 through 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2016
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
#    integer ML, the upper (and lower) bandwidth.
#    ML must be nonnegative, and no greater than N-1.
#
#    real A(ML+1,N), the R8PBL matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

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
    i2lo = max ( i2lo, j2lo - ml )
    i2hi = min ( ihi, n - 1 )
    i2hi = min ( i2hi, j2hi + ml )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%4d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):

        if ( j < i - ml or i + ml < j ):
          print ( '              ', end = '' )
        elif ( i <= j and j <= i + ml ):
          print ( '%12g  ' % ( a[j-i,i] ), end = '' )
        elif ( j <= i and i <= j + ml ):
          print ( '%12g  ' % ( a[i-j,j] ), end = '' )
 
      print ( '' )

  return

def r8pbl_print_some_test ( ):

#*****************************************************************************80
#
## R8PBL_PRINT_SOME_TEST tests R8PBL_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 9
  ml = 4

  print ( '' )
  print ( 'R8PBL_PRINT_SOME_TEST' )
  print ( '  R8PBL_PRINT_SOME prints some of an R8PBL matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth ML = ', ml )

  a = r8pbl_indicator ( n, ml )

  r8pbl_print_some ( n, ml, a, 3, 4, 7, 8, '  Row(3:7), Col(4:8):' )

  return

def r8pbl_random ( n, ml ):

#*****************************************************************************80
#
## R8PBL_RANDOM randomizes a R8PBL matrix.
#
#  Discussion:
#
#    The R8PBL storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and lower triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row 1 of the array.
#    The first subdiagonal in row 2, columns 1 through ML.
#    The second subdiagonal in row 3, columns 1 through ML-1.
#    The ML-th subdiagonal in row ML+1, columns 1 through 1.
#
#    The matrix returned will be positive definite, but of limited
#    randomness.  The off diagonal elements are random values between
#    0 and 1, and the diagonal element of each row is selected to
#    ensure strict diagonal dominance.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 February 2005
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
#    integer ML, the number of subdiagonals in the matrix.
#    ML must be at least 0 and no more than N-1.
#
#  Output:
#
#    real A(ML+1,N), the R8PBL matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( [ ml + 1, n ] )
#
#  Set the off diagonal values.
#
  for i in range ( 0, n ):
    for j in range ( max ( 0, i - ml ), i ):
      a[i-j,j] = rng.random ( )
#
#  Set the diagonal values.
#
  for i in range ( 0, n ):

    sum2 = 0.0

    jlo = max ( 0, i - ml )
    for j in range ( jlo, i ):
      sum2 = sum2 + abs ( a[i-j,j] )

    jhi = min ( i + ml, n - 1 )
    for j in range ( i + 1, jhi + 1 ):
      sum2 = sum2 + abs ( a[j-i,i] )

    r = rng.random ( )

    a[0,i] = ( 1.0 + r ) * ( sum2 + 0.01 )

  return a

def r8pbl_random_test ( ):

#*****************************************************************************80
#
## r8pbl_random_test() tests r8pbl_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 2

  print ( '' )
  print ( 'R8PBL_RANDOM_TEST' )
  print ( '  R8PBL_RANDOM randomizes an R8PBL matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth ML = ', ml )

  a = r8pbl_random ( n, ml )

  r8pbl_print ( n, ml, a, '  The R8PBL random matrix:' )

  return

def r8pbl_to_r8ge ( n, ml, a ):

#*****************************************************************************80
#
## R8PBL_TO_R8GE copies a R8PBL matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8PBL storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and lower triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row 1 of the array.
#    The first subdiagonal in row 2, columns 1 through ML.
#    The second subdiagonal in row 3, columns 1 through ML-1.
#    The ML-th subdiagonal in row ML+1, columns 1 through 1.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    23 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrices.
#    N must be positive.
#
#    integer ML, the upper bandwidth of A.
#    ML must be nonnegative, and no greater than N-1.
#
#    real A(ML+1,N), the R8PBL matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j and j <= i + ml ):
        b[i,j] = a[j-i,i]
      elif ( i - ml <= j and j < i ):
        b[i,j] = a[i-j,j]

  return b

def r8pbl_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8PBL_TO_R8GE_TEST tests R8PBL_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 2

  print ( '' )
  print ( 'R8PBL_TO_R8GE_TEST' )
  print ( '  R8PBL_TO_R8GE converts an R8PBL matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth ML = ', ml )

  a = r8pbl_random ( n, ml )

  r8pbl_print ( n, ml, a, '  The R8PBL matrix:' )

  a_r8ge = r8pbl_to_r8ge ( n, ml, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8pbl_zeros ( n, ml ):

#*****************************************************************************80
#
## R8PBL_ZEROS zeros an R8PBL matrix.
#
#  Discussion:
#
#    The R8PBL storage format is for a symmetric positive definite band matrix.
#
#    To save storage, only the diagonal and lower triangle of A is stored,
#    in a compact diagonal format that preserves columns.
#
#    The diagonal is stored in row 1 of the array.
#    The first subdiagonal in row 2, columns 1 through ML.
#    The second subdiagonal in row 3, columns 1 through ML-1.
#    The ML-th subdiagonal in row ML+1, columns 1 through 1.
#
#    The matrix returned will be positive definite, but of limited
#    randomness.  The off diagonal elements are random values between
#    0 and 1, and the diagonal element of each row is selected to
#    ensure strict diagonal dominance.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 August 2015
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
#    integer ML, the number of subdiagonals in the matrix.
#    ML must be at least 0 and no more than N-1.
#
#  Output:
#
#    real A(ML+1,N), the R8PBL matrix.
#
  import numpy as np

  a = np.zeros ( [ ml + 1, n ] )

  return a

def r8pbl_zeros_test ( ):

#*****************************************************************************80
#
## R8PBL_ZEROS_TEST tests R8PBL_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 2

  print ( '' )
  print ( 'R8PBL_ZEROS_TEST' )
  print ( '  R8PBL_ZEROS zeros an R8PBL matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
  print ( '  Bandwidth ML = ', ml )

  a = r8pbl_zeros ( n, ml )

  r8pbl_print ( n, ml, a, '  The R8PBL zero matrix:' )

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
  r8pbl_test ( )
  timestamp ( )
