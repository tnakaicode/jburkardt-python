#! /usr/bin/env python3
#
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

def i4_log_10_test ( ) :

#*****************************************************************************80
#
## i4_log_10_test() tests i4_log_10().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'i4_log_10_test():' )
  print ( '  i4_log_10() returns the whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )

  return

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

def r8ge_print_test ( ):

#*****************************************************************************80
#
## r8ge_print_test() tests r8ge_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_print_test():' )
  print ( '  r8ge_print() prints an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print ( m, n, v, '  Here is an R8GE:' )

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

def r8ge_print_some_test ( ):

#*****************************************************************************80
#
## r8ge_print_some_test() tests r8ge_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_print_some_test():' )
  print ( '  r8ge_print_some() prints some of an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print_some ( m, n, v, 0, 3, 2, 5, '  Rows 0:2, Cols 3:5:' )

  return

def r8ge_to_r8ut ( m, n, a_ge ):

#*****************************************************************************80
#
## r8ge_to_r8ut() copies an R8GE matrix to an R8UT matrix.
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
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A_GE(M,N), the R8GE matrix.
#
#  Output:
#
#    real A_UT(M,N), the R8UT matrix.
#
  import numpy as np

  a_ut = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a_ut[i,j] = a_ge[i,j]

  return a_ut

def r8ge_to_r8ut_test ( rng ):

#*****************************************************************************80
#
## r8ge_to_r8ut_test() tests r8ge_to_r8ut().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2015
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

  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_to_r8ut_test():' )
  print ( '  r8ge_to_r8ut() converts an R8GE matrix to R8UT format.' )

  a_ge = rng.random ( size = [ m, n ] )

  r8ge_print ( m, n, a_ge, '  The random R8GE matrix:' )
 
  a_ut = r8ge_to_r8ut ( m, n, a_ge )

  r8ut_print ( m, n, a_ut, '  The R8UT matrix:' )

  return

def r8ut_det ( n, a ):

#*****************************************************************************80
#
## r8ut_det() computes the determinant of an R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 August 2015
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
#    real A(N,N), the R8UT matrix.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  det = 1.0
  for i in range ( 0, n ):
    det = det * a[i,i]

  return det

def r8ut_det_test ( rng ):

#*****************************************************************************80
#
## r8ut_det_test() tests r8ut_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 August 2015
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
  print ( 'r8ut_det_test():' )
  print ( '  r8ut_det() computes the determinant of an R8UT matrix.' )

  a = r8ut_random ( n, n, rng )

  r8ut_print ( n, n, a, '  The matrix A:' )
#
#  Compute the determinant.
#
  det = r8ut_det ( n, a )

  print ( '' )
  print ( '  Determinant is %g' % ( det ) )

  return

def r8ut_indicator ( m, n ):

#*****************************************************************************80
#
## r8ut_indicator() sets up a R8UT indicator matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#    M and N must be positive.
#
#  Output:
#
#    real A(M,N), the R8UT matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = r8ut_zeros ( m, n )
  for i in range ( 0, m ):
    for j in range ( i, n ):
      a[i,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r8ut_indicator_test ( ):

#*****************************************************************************80
#
## r8ut_indicator_test() tests r8ut_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_indicator_test():' )
  print ( '  r8ut_indicator() sets up an indicator matrix in R8UT format' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = r8ut_indicator ( m, n )

  r8ut_print ( m, n, a, '  The indicator matrix:' )

  return

def r8ut_inverse ( n, a ):

#*****************************************************************************80
#
## r8ut_inverse() computes the inverse of a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
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
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf,
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the matrix to be inverted.
#
#  Output:
#
#    real A_INV(N,N), the inverse matrix.
#
  import numpy as np
#
#  Check.
#
  for i in range ( 0, n ):
    if ( a[i,i] == 0.0 ):
      print ( '' )
      print ( 'r8ut_inverse - Fatal error!' )
      print ( '  Zero diagonal element.' )
      raise Exception ( 'r8ut_inverse - Fatal error!' )

  a_inv = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, n ):
      a_inv[i,j] = a[i,j]

  for j in range ( n - 1, -1, -1 ):

    for i in range ( n - 1, -1, -1 ):

      if ( j < i ):

        a_inv[i,j] = 0.0

      elif ( i == j ):

        a_inv[i,j] = 1.0 / a_inv[i,j]

      elif ( i < j ):

        t = 0.0
        for k in range ( i + 1, j + 1 ):
          t = t + a_inv[i,k] * a_inv[k,j]
        a_inv[i,j] = - t / a_inv[i,i]

  return a_inv

def r8ut_inverse_test ( rng ):

#*****************************************************************************80
#
## r8ut_inverse_test() tests r8ut_inverse().
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
#    rng: the current random number generator.
#
  n = 5

  print ( '' )
  print ( 'r8ut_inverse_test():' )
  print ( '  r8ut_inverse() computes the inverse of an R8UT matrix.' )

  a = r8ut_random ( n, n, rng )

  r8ut_print ( n, n, a, '  The matrix A:' )
#
#  Compute the inverse matrix B.
#
  b = r8ut_inverse ( n, a )

  r8ut_print ( n, n, b, '  The inverse matrix B:' )
#
#  Check
#
  c = r8ut_mm ( n, a, b )

  r8ut_print ( n, n, c, '  The product A * B:' )

  return

def r8ut_mm ( n, a, b ):

#*****************************************************************************80
#
## r8ut_mm() computes C = A * B, where A and B are R8UT matrices.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    The product C will also be an upper trangular matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
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
#    real A(N,N), B(N,N), the factors.
#
#  Output:
#
#    real C(N,N), the product.
#
  c = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( i, n ):
      for k in range ( i, j + 1 ):
        c[i,j] = c[i,j] + a[i,k] * b[k,j]

  return c

def r8ut_mm_test ( ):

#*****************************************************************************80
#
## r8ut_mm_test() tests r8ut_mm().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
 
  print ( '' )
  print ( 'r8ut_mm_test():' )
  print ( '  r8ut_mm() computes C = A * B for R8UT matrices.' )
 
  a = r8ut_zeros ( n, n )
  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = 1.0

  r8ut_print ( n, n, a, '  The matrix A:' )

  c = r8ut_mm ( n, a, a )
  r8ut_print ( n, n, c, '  The product C = A * A' )

  return

def r8ut_mtm ( n, a, b ):

#*****************************************************************************80
#
## r8ut_mtm() computes C = A' * B, where A and B are R8UT matrices.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    The product C will NOT be an R8UT matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
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
#    real A(N,N), B(N,N), the factors.
#
#  Output:
#
#    real C(N,N), the product.
#
  import numpy as np

  c = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      k_hi = min ( i + 1, j + 1 )
      for k in range ( 0, k_hi ):
        c[i,j] = c[i,j] + a[k,i] * b[k,j]

  return c

def r8ut_mtm_test ( ):

#*****************************************************************************80
#
## r8ut_mtm_test() tests r8ut_mtm().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
 
  print ( '' )
  print ( 'r8ut_mtm_test():' )
  print ( '  r8ut_mtm() computes C = A\' * B for R8UT matrices.' )
 
  a = r8ut_zeros ( n, n )
  for i in range ( 0, n ):
    for j in range ( i, n ):
      a[i,j] = 1.0

  r8ut_print ( n, n, a, '  The matrix A:' )

  c = r8ut_mtm ( n, a, a )
  r8ge_print ( n, n, c, '  The product C = A\' * A' )

  return

def r8ut_mtv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ut_mtv() multiplies a vector by a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8UT matrix.
#
#    real X(M), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    jhi = min ( i + 1, m )
    for j in range ( 0, jhi ):
      b[i] = b[i] + x[j] * a[j,i]

  return b

def r8ut_mtv_test ( ):

#*****************************************************************************80
#
## r8ut_mtv_test() tests r8ut_mtv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_mtv_test():' )
  print ( '  r8ut_mtv() computes a matrix product b=A\'*x for an R8UT matrix.' )

  a = r8ut_indicator ( m, n )
  r8ut_print ( m, n, a, '  The matrix A:' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  The vector X:' )

  b = r8ut_mtv ( m, n, a, x )
  r8vec_print ( n, b, '  The vector b=A\'*x:' )

  return

def r8ut_mv ( m, n, a, x ):

#*****************************************************************************80
#
## r8ut_mv() multiplies a R8UT matrix times a vector.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 February 2004
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8UT matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( i, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8ut_mv_test ( ):

#*****************************************************************************80
#
## r8ut_mv_test() tests r8ut_mv().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_mv_test():' )
  print ( '  r8ut_mv() computes a product b=A*x for an R8UT matrix.' )

  a = r8ut_indicator ( m, n )
  r8ut_print ( m, n, a, '  The R8UT matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  Vector x:' )

  b = r8ut_mv ( m, n, a, x )
  r8vec_print ( m, b, '  Vector b = A*x:' )

  return

def r8ut_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8ut_print() prints a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 April 2006
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8UT matrix.
#
#    string TITLE, a title to be printed.
#
  r8ut_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ut_print_test ( ):

#*****************************************************************************80
#
## r8ut_print_test() tests r8ut_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ut_print_test():' )
  print ( '  r8ut_print() prints an R8UT matrix.' )

  m = 6
  n = 4
  a = r8ut_indicator ( m, n )

  r8ut_print ( m, n, a, '  Here is an R8MAT:' )

  return

def r8ut_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8ut_print_some() prints some of a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows of the matrix.
#    M must be positive.
#
#    integer N, the number of columns of the matrix.
#    N must be positive.
#
#    real A(M,N), the R8UT matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
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
#
#  Determine the range of the rows in this strip.
#
    inc = j2hi + 1 - j2lo
    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( j < i ):
          print ( '              ', end = '' )
        else:
          print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

def r8ut_print_some_test ( ):

#*****************************************************************************80
#
## r8ut_print_some_test() tests r8ut_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ut_print_some_test():' )
  print ( '  r8ut_print_some() prints some of an R8UT matrix.' )

  m = 4
  n = 6
  a = r8ut_indicator ( m, n )

  r8ut_print_some ( m, n, a, 0, 3, 2, 5, '  Some of the matrix:' )

  return

def r8ut_random ( m, n, rng ):

#*****************************************************************************80
#
## r8ut_random() randomizes a R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
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
#    integer M, N, the number of rows and columns of the matrix.
#    M and N must be positive.
#
#    rng: the current random number generator.
#
#  Output:
#
#    real A(M,N), the R8UT matrix.
#
  import numpy as np
 
  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a[i,j] = rng.random ( )

  return a

def r8ut_random_test ( rng ):

#*****************************************************************************80
#
## r8ut_random_test() tests r8ut_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    rng: the current random number generator.
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_random_test():' )
  print ( '  r8ut_random() randomizes an R8UT matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8ut_random ( m, n, rng )

  r8ut_print ( m, n, a, '  Matrix A:' )

  return

def r8ut_sl ( n, a, b ):

#*****************************************************************************80
#
## r8ut_sl() solves a linear system A*x=b with an R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    No factorization of the upper triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8UT matrix.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )
  
  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( n - 1, -1, -1 ):
    x[j] = x[j] / a[j,j]
    for i in range ( 0, j ):
      x[i] = x[i] - a[i,j] * x[j]

  return x

def r8ut_sl_test ( ):

#*****************************************************************************80
#
## r8ut_sl_test() tests r8ut_sl().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8ut_sl_test():' )
  print ( '  r8ut_sl() solves a linear system A*x=b with R8UT matrix' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = float ( j + 1 )

  r8ut_print ( n, n, a, '  The upper triangular matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ut_mv ( n, n, a, x )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8ut_sl ( n, a, b )

  r8vec_print ( n, x, '  Solution:' )

  return

def r8ut_slt ( n, a, b ):

#*****************************************************************************80
#
## r8ut_slt() solves a linear system A'*x=b with an R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    No factorization of the upper triangular matrix is required.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N,N), the R8UT matrix.
#
#    real B(N), the right hand side.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = b[i]

  for j in range ( 0, n ):
    x[j] = x[j] / a[j,j]
    for i in range ( j + 1, n ):
      x[i] = x[i] - x[j] * a[j,i]

  return x

def r8ut_slt_test ( ):

#*****************************************************************************80
#
## r8ut_slt_test() tests r8ut_slt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8ut_slt_test():' )
  print ( '  r8ut_slt() solves a linear system A\'x=b with R8UT matrix' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )

  a = r8ut_zeros ( n, n )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
      if ( i <= j ):
        a[i,j] = float ( j + 1 )

  r8ut_print ( n, n, a, '  The upper triangular matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ut_mtv ( n, n, a, x )
  r8vec_print ( n, b, '  Right hand side b:' )
#
#  Solve the linear system.
#
  x = r8ut_slt ( n, a, b )

  r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8ut_to_r8ge ( m, n, a_ut ):

#*****************************************************************************80
#
## r8ut_to_r8ge() copies an R8UT matrix to an R8GE matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each entry.  The two dimensional logical
#    array can be thought of as a vector of M*N entries, starting with
#    the M entries in the column 1, then the M entries in column 2
#    and so on.  Considered as a vector, the entry A(I,J) is then stored
#    in vector location I+(J-1)*M.
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
#    integer M, N, the order of the matrix.
#
#    real A_UT(M,N), the R8UT matrix.
#
#  Output:
#
#    real A_GE(N,N), the R8GE matrix.
#
  import numpy as np

  a_ge = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a_ge[i,j] = a_ut[i,j]

  return a_ge

def r8ut_to_r8ge_test ( rng ):

#*****************************************************************************80
#
## r8ut_to_r8ge_test() tests r8ut_to_r8ge().
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
#    rng: the current random number generator.
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_to_r8ge_test():' )
  print ( '  r8ut_to_r8ge() converts an R8UT matrix to R8GE format.' )

  a_ut = r8ut_random ( m, n, rng )

  r8ut_print ( m, n, a_ut, '  The random R8UT matrix:' )
 
  a_ge = r8ut_to_r8ge ( m, n, a_ut )

  r8ge_print ( m, n, a_ge, '  The R8GE matrix:' )

  return

def r8ut_zeros ( m, n ):

#*****************************************************************************80
#
## r8ut_zeros() zeroes an R8UT matrix.
#
#  Discussion:
#
#    The R8UT storage format is used for an M by N upper triangular 
#    matrix.  The format stores all M*N entries, even those which are zero.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#  Output:
#
#    real A(M,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ m, n ] )

  return a

def r8ut_zeros_test ( ):

#*****************************************************************************80
#
## r8ut_zeros_test() tests r8ut_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    03 August 2015
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ut_zeros_test():' )
  print ( '  r8ut_zeros() zeros out space for an R8UT matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8ut_zeros ( m, n )

  r8ut_print ( m, n, a, '  Matrix A:' )

  return

def r8ut_test ( ):

#*****************************************************************************80
#
## r8ut_test() tests r8ut().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 January 2028
#
#  Author:
#
#    John Burkardt
#
  from numpy.random import default_rng
  import numpy as np
  import platform 

  print ( '' )
  print ( 'r8ut_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8ut().' )

  rng = default_rng ( )

  i4_log_10_test ( )

  r8ge_print_test ( )
  r8ge_print_some_test ( )
  r8ge_to_r8ut_test ( rng )

  r8ut_det_test ( rng )
  r8ut_indicator_test ( )
  r8ut_inverse_test ( rng )
  r8ut_mm_test ( )
  r8ut_mtm_test ( )
  r8ut_mtv_test ( )
  r8ut_mv_test ( )
  r8ut_print_test ( )
  r8ut_print_some_test ( )
  r8ut_random_test ( rng )
  r8ut_sl_test ( )
  r8ut_slt_test ( )
  r8ut_to_r8ge_test ( rng )
  r8ut_zeros_test ( )

  r8vec_indicator1_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8ut_test():' )
  print ( '  Normal end of execution.' )
  return

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
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## r8vec_indicator1_test() tests r8vec_indicator1().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8vec_indicator1_test():' )
  print ( '  r8vec_indicator1() returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )

  return

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
  r8ut_test ( )
  timestamp ( )

