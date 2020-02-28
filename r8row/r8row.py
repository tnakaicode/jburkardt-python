#! /usr/bin/env python3
#
def i4_log_10 ( i ):

#*****************************************************************************80
#
## I4_LOG_10 returns the integer part of the logarithm base 10 of ABS(X).
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
#    I4_LOG_10 ( I ) + 1 is the number of decimal digits in I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the number whose logarithm base 10 is desired.
#
#    Output, integer VALUE, the integer part of the logarithm base 10 of
#    the absolute value of X.
#
  from math import floor

  i = floor ( i )

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
## I4_LOG_10_TEST tests I4_LOG_10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 May 2013
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 13

  x = [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ]

  print ( '' )
  print ( 'I4_LOG_10_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4_LOG_10: whole part of log base 10,' )
  print ( '' )
  print ( '  X, I4_LOG_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4_LOG_10_TEST' )
  print ( '  Normal end of execution.' )
  return

def i4mat_print ( m, n, a, title ):

#*****************************************************************************80
#
## I4MAT_PRINT prints an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 October 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, integer A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  i4mat_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

def i4mat_print_test ( ):

#*****************************************************************************80
#
## I4MAT_PRINT_TEST tests I4MAT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 May 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4MAT_PRINT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test I4MAT_PRINT, which prints an I4MAT.' )

  m = 5
  n = 6
  a = np.array ( ( \
    ( 11, 12, 13, 14, 15, 16 ), \
    ( 21, 22, 23, 24, 25, 26 ), \
    ( 31, 32, 33, 34, 35, 36 ), \
    ( 41, 42, 43, 44, 45, 46 ), \
    ( 51, 52, 53, 54, 55, 56 ) ) )
  title = '  A 5 x 6 integer matrix:'
  i4mat_print ( m, n, a, title )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def i4mat_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## I4MAT_PRINT_SOME prints out a portion of an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, integer A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 10

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for j2lo in range ( max ( jlo, 0 ), min ( jhi + 1, n ), incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d  ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( ' %4d: ' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%7d  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def i4mat_print_some_test ( ):

#*****************************************************************************80
#
## I4MAT_PRINT_SOME_TEST tests I4MAT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'I4MAT_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_PRINT_SOME prints some of an I4MAT.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11, 12, 13, 14, 15, 16 ], 
    [ 21, 22, 23, 24, 25, 26 ], 
    [ 31, 32, 33, 34, 35, 36 ], 
    [ 41, 42, 43, 44, 45, 46 ] ], dtype = np.int32 )
  i4mat_print_some ( m, n, v, 0, 3, 2, 5, '  Here is I4MAT, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_compare ( m, n, a, i, j ):

#*****************************************************************************80
#
## R8ROW_COMPARE compares rows in an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Example:
#
#    Input:
#
#      M = 4, N = 3, I = 2, J = 4
#
#      A = (
#        1  5  9
#        2  6 10
#        3  7 11
#        4  8 12 )
#
#    Output:
#
#      VALUE = -1
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the M by N array.
#
#    Input, integer I, J, the rows to be compared.
#    I and J must be between 0 and M-1.
#
#    Output, integer VALUE, the results of the comparison:
#    -1, row I < row J,
#     0, row I = row J,
#    +1, row J < row I.
#
  from sys import exit
#
#  Check.
#
  if ( i < 0 or m <= i ):
    print ( '' )
    print ( 'R8ROW_COMPARE - Fatal error!' )
    print ( '  Row index I is out of bounds.' )
    print ( '  I = %d' % ( i ) )
    exit ( 'R8ROW_COMPARE - Fatal error!' )

  if ( j < 0 or m <= j ):
    print ( '' )
    print ( 'R8ROW_COMPARE - Fatal error!' )
    print ( '  Row index J is out of bounds.' )
    print ( '  J = %d' % ( j ) )
    exit ( 'R8ROW_COMPARE - Fatal error!' )

  value = 0

  if ( i == j ):
    return value

  k = 0

  while ( k < n ):

    if ( a[i,k] < a[j,k] ):
      value = -1
      return value
    elif ( a[j,k] < a[i,k] ):
      value = +1
      return value

    k = k + 1

  return value

def r8row_compare_test ( ):

#*****************************************************************************80
#
## R8ROW_COMPARE_TEST tests R8ROW_COMPARE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R8ROW_COMPARE_TEST' )
  print ( '  R8ROW_COMPARE compares rows of an R8ROW,' )
  print ( '  returning -1, 0 or +1 for comparison.' )

  m = 6
  n = 5
 
  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = ( ( i + j ) % 3 )

  r8row_print ( m, n, a, '  Matrix A:' )

  c = np.zeros ( [ m, m ] )

  for j in range ( 0, m ):
    for i in range ( 0, m ):
      c[i,j] = r8row_compare ( m, n, a, i, j )

  i4mat_print ( m, m, c, '  C(I,J) = Row I compare Row J:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_COMPARE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_indicator ( m, n ):

#*****************************************************************************80
#
## R8ROW_INDICATOR sets up an indicator R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#    The value of each entry suggests its location, as in:
#
#      11  12  13  14
#      21  22  23  24
#      31  32  33  34
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows of the matrix.
#    M must be positive.
#
#    Input, integer N, the number of columns of the matrix.
#    N must be positive.
#
#    Output, real A(M,N), the indicator table.
#
  import numpy as np

  a = np.zeros ( ( m, n ), dtype = np.float64 )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = fac * ( i + 1 ) + ( j + 1 )

  return a

def r8row_indicator_test ( ):

#*****************************************************************************80
#
## R8ROW_INDICATOR_TEST tests R8ROW_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8ROW_INDICATOR_TEST' )
  print ( '  R8ROW_INDICATOR creates an "indicator" R8ROW.' )

  m = 5
  n = 4
  a = r8row_indicator ( m, n )
  r8row_print ( m, n, a, '  The indicator matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_INDICATOR_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8row_max ( m, n, x ):

#*****************************************************************************80
#
## R8ROW_MAX returns the maximums of rows of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real X(M,N), the R8ROW.
#
#    Output, real XMAX(M), the maximums of the rows of X.
#
  import numpy as np

  xmax = np.zeros ( m )

  for i in range ( 0, m ):
    xmax[i] = x[i,0]
    for j in range ( 1, n ):
      xmax[i] = max ( xmax[i], x[i,j] )

  return xmax

def r8row_max_test ( ):

#*****************************************************************************80
#
## R8ROW_MAX_TEST tests R8ROW_MAX
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'R8ROW_MAX_TEST' )
  print ( '  R8ROW_MAX computes maximums of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8row_print ( m, n, a, '  The matrix:' )

  amax = r8row_max ( m, n, a )

  r8vec_print ( m, amax, '  Row maximums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_MAX_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_mean ( m, n, a ):

#*****************************************************************************80
#
## R8ROW_MEAN returns the means of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the R8ROW
#
#    Output, real ROW_MEAN(M), the row means.
#
  import numpy as np

  mean = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      mean[i] = mean[i] + a[i,j]
    mean[i] = mean[i] / float ( n )

  return mean

def r8row_mean_test ( ):

#*****************************************************************************80
#
## R8ROW_MEAN_TEST tests R8ROW_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'R8ROW_MEAN_TEST' )
  print ( '  R8ROW_MEAN computes row means of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8row_print ( m, n, a, '  The matrix:' )

  means = r8row_sum ( m, n, a )

  r8vec_print ( m, means, '  The row means:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_min ( m, n, x ):

#*****************************************************************************80
#
## R8ROW_MIN returns the minimums of rows of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real X(M,N), the R8ROW.
#
#    Output, real XMIN(M), the minimums of the rows of X.
#
  import numpy as np

  xmin = np.zeros ( m )

  for i in range ( 0, m ):
    xmin[i] = x[i,0]
    for j in range ( 1, n ):
      xmin[i] = min ( xmin[i], x[i,j] )

  return xmin

def r8row_min_test ( ):

#*****************************************************************************80
#
## R8ROW_MIN_TEST tests R8ROW_MIN
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'R8ROW_MIN_TEST' )
  print ( '  R8ROW_MIN computes minimums of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8row_print ( m, n, a, '  The matrix:' )

  amin = r8row_min ( m, n, a )

  r8vec_print ( m, amin, '  Row minimums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_MIN_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8ROW_PRINT prints an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8row_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8row_print_test ( ):

#*****************************************************************************80
#
## R8ROW_PRINT_TEST tests R8ROW_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R8ROW_PRINT_TEST' )
  print ( '  R8ROW_PRINT prints an R8ROW.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8row_print ( m, n, v, '  Here is an R8ROW:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8ROW_PRINT_SOME prints out a portion of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
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
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8row_print_some_test ( ):

#*****************************************************************************80
#
## R8ROW_PRINT_SOME_TEST tests R8ROW_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R8ROW_PRINT_SOME_TEST' )
  print ( '  R8ROW_PRINT_SOME prints some of an R8ROW.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8row_print_some ( m, n, v, 0, 3, 2, 5, '  Here is an R8ROW:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_test ( ):

#*****************************************************************************80
#
## R8ROW_TEST tests the R8ROW library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 March 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8ROW_TEST' )
  print ( '  Python version:' )
  print ( '  Test the R8ROW library.' )

  i4_log_10_test ( )

  i4mat_print_test ( )
  i4mat_print_some_test ( )

  r8row_compare_test ( )
  r8row_indicator_test ( )
  r8row_max_test ( )
  r8row_mean_test ( )
  r8row_min_test ( )
  r8row_print_test ( )
  r8row_print_some_test ( )
  r8row_running_average_test ( )
  r8row_running_sum_test ( )
  r8row_sum_test ( )
  r8row_swap_test ( )
  r8row_to_r8vec_test ( )
  r8row_transpose_print_test ( )
  r8row_transpose_print_some_test ( )
  r8row_uniform_ab_test ( )
  r8row_variance_test ( )

  r8vec_print_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_running_average ( m, n, v ):

#*****************************************************************************80
#
## R8ROW_RUNNING_AVERAGE computes the running averages of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows.
#
#    Input, integer N, the number of items in each row.
#
#    Input, real V(M,N), the data.
#
#    Output, real A(M,N+1), the running average.  A(I,J) is the average value
#    of V(I,1:J-1).
#
  import numpy as np

  a = np.zeros ( [ m, n + 1 ] )
#
#  Sum.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 0, m ):
      a[i,j] = a[i,j-1] + v[i,j-1]
#
#  Average.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 0, m ):
      a[i,j] = a[i,j] / float ( j )

  return a

def r8row_running_average_test ( ):

#*****************************************************************************80
#
## R8ROW_RUNNING_AVERAGE_TEST tests R8ROW_RUNNING_AVERAGE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8ROW_RUNNING_AVERAGE_TEST' )
  print ( '  R8ROW_RUNNING_AVERAGE returns M sets of running averages' )
  print ( '  of an MxN R8ROW.' )

  m = 5
  n = 10
  a = -5.0
  b = +10.0
  seed = 123456789

  r, seed = r8row_uniform_ab ( m, n, a, b, seed )

  r8row_print ( m, n, r, '  Random R8ROW:' )

  s = r8row_running_average ( m, n, r )

  r8row_print ( m, n + 1, s, '  Running averages:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_RUNNING_AVERAGE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_running_sum ( m, n, v ):

#*****************************************************************************80
#
## R8ROW_RUNNING_SUM computes the running sum of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows.
#
#    Input, integer N, the number of items in each row.
#
#    Input, real V(M,N), the data.
#
#    Output, real S(M,N+1), the running sums.  S(I,J) is the sum
#    of V(i,1:J-1).
#
  import numpy as np

  s = np.zeros ( [ m, n + 1 ] )
#
#  Sum.
#
  for j in range ( 1, n + 1 ):
    for i in range ( 0, m ):
      s[i,j] = s[i,j-1] + v[i,j-1]

  return s

def r8row_running_sum_test ( ):

#*****************************************************************************80
#
## R8ROW_RUNNING_SUM_TEST tests R8ROW_RUNNING_SUM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'R8ROW_RUNNING_SUM_TEST' )
  print ( '  R8ROW_RUNNING_SUM returns the M running sums of an R8ROW.' )

  m = 5
  n = 10
  a = -5.0
  b = +10.0
  seed = 123456789

  r, seed = r8row_uniform_ab ( m, n, a, b, seed )

  r8row_print ( m, n, r, '  Random R8ROW:' )

  s = r8row_running_sum ( m, n, r )

  r8row_print ( m, n + 1, s, '  Running sums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_RUNNING_SUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_sum ( m, n, a ):

#*****************************************************************************80
#
## R8ROW_SUM returns the sums of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the R8ROW
#
#    Output, real ROW_SUM(M), the sum of the entries of 
#    each row.
#
  import numpy as np

  row_sum = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      row_sum[i] = row_sum[i] + a[i,j]

  return row_sum

def r8row_sum_test ( ):

#*****************************************************************************80
#
## R8ROW_SUM_TEST tests R8ROW_SUM
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'R8ROW_SUM_TEST' )
  print ( '  R8ROW_SUM computes sums of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8row_print ( m, n, a, '  The matrix:' )

  rowsum = r8row_sum ( m, n, a )

  r8vec_print ( m, rowsum, '  The row sums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_SUM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_swap ( m, n, a, irow1, irow2 ):

#*****************************************************************************80
#
## R8ROW_SWAP swaps two rows of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the R8ROW.
#
#    Input, integer IROW1, IROW2, the two rows to swap.
#    0 <= IROW1, IROW2 < M.
#
#    Output, real A(M,N), the array after row swapping.
#
  from sys import exit

  if ( irow1 < 0 or m <= irow1 ):
    print ( '' )
    print ( 'R8ROW_SWAP - Fatal error!' )
    print ( '  IROW1 is out of range.' )
    exit ( 'R8ROW_SWAP - Fatal error!' )

  if ( irow2 < 0 or m <= irow2 ):
    print ( '' )
    print ( 'R8ROW_SWAP - Fatal error!' )
    print ( '  IROW2 is out of range.' )
    exit ( 'R8ROW_SWAP - Fatal error!' )

  if ( irow1 == irow2 ):
    return a

  for j in range ( 0, n ):
    t          = a[irow1,j]
    a[irow1,j] = a[irow2,j]
    a[irow2,j] = t

  return a

def r8row_swap_test ( ):

#*****************************************************************************80
#
## R8ROW_SWAP_TEST tests R8ROW_SWAP
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'R8ROW_SWAP_TEST' )
  print ( '  R8ROW_SWAP swaps two rows of an R8ROW.' )

  a = np.zeros ( [ m, n ] )

  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  r8row_print ( m, n, a, '  The original matrix:' )

  row1 = 0
  row2 = 2

  print ( '' )
  print ( '  Swap rows %d and %d' % ( row1, row2 ) )

  a = r8row_swap ( m, n, a, row1, row2 )

  r8row_print ( m, n, a, '  The modified matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_SWAP_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_to_r8vec ( m, n, a ):

#*****************************************************************************80
#
## R8ROW_TO_R8VEC converts an R8ROW into an R8VEC.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Example:
#
#    M = 3, N = 4
#
#    A =
#      11 12 13 14
#      21 22 23 24
#      31 32 33 34
#
#    X = ( 11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the R8ROW.
#
#    Output, real X(M*N), a vector containing the M rows of A.
#
  import numpy as np

  x = np.zeros ( m * n )

  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      x[k] = a[i,j]
      k = k + 1

  return x

def r8row_to_r8vec_test ( ):

#*****************************************************************************80
#
## R8ROW_TO_R8VEC_TEST tests R8ROW_TO_R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 February 2016
#
#  Author:
#
#    John Burkardt
#
  m = 3
  n = 4

  print ( '' )
  print ( 'R8ROW_TO_R8VEC_TEST' )
  print ( '  R8ROW_TO_R8VEC converts an R8ROW to an R8VEC.' )
 
  a = r8row_indicator ( m, n )

  r8row_print ( m, n, a, '  The array of rows:' )
 
  x = r8row_to_r8vec ( m, n, a )
 
  r8vec_print ( m * n, x, '  The resulting vector of rows:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_TO_R8VEC_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_transpose_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8ROW_TRANSPOSE_PRINT prints an R8ROW, transposed.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in A.
#
#    Input, integer N, the number of columns in A.
#
#    Input, real A(M,N), the matrix.
#
#    Input, string TITLE, a title.
#
  r8row_transpose_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8row_transpose_print_test ( ):

#*****************************************************************************80
#
## R8ROW_TRANSPOSE_PRINT_TEST tests R8ROW_TRANSPOSE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R8ROW_TRANSPOSE_PRINT_TEST' )
  print ( '  R8ROW_TRANSPOSE_PRINT prints an R8ROW.' )

  m = 4
  n = 3
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0 ], 
    [ 21.0, 22.0, 23.0 ], 
    [ 31.0, 32.0, 33.0 ], 
    [ 41.0, 42.0, 43.0 ] ], dtype = np.float64 )
  r8row_transpose_print ( m, n, v, '  Here is an R8ROW, transposed:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_TRANSPOSE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_transpose_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8ROW_TRANSPOSE_PRINT_SOME prints a portion of an R8ROW, transposed.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 November 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns of the matrix.
#
#    Input, real A(M,N), an M by N matrix to be printed.
#
#    Input, integer ILO, JLO, the first row and column to print.
#
#    Input, integer IHI, JHI, the last row and column to print.
#
#    Input, string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( m <= 0 or n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  for i2lo in range ( max ( ilo, 0 ), min ( ihi, m - 1 ), incx ):

    i2hi = i2lo + incx - 1
    i2hi = min ( i2hi, m - 1 )
    i2hi = min ( i2hi, ihi )
    
    print ( '' )
    print ( '  Row: ', end = '' )

    for i in range ( i2lo, i2hi + 1 ):
      print ( '%7d       ' % ( i ), end = '' )

    print ( '' )
    print ( '  Col' )

    j2lo = max ( jlo, 0 )
    j2hi = min ( jhi, n - 1 )

    for j in range ( j2lo, j2hi + 1 ):

      print ( '%7d :' % ( j ), end = '' )
      
      for i in range ( i2lo, i2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ), end = '' )

      print ( '' )

  return

def r8row_transpose_print_some_test ( ):

#*****************************************************************************80
#
## R8ROW_TRANSPOSE_PRINT_SOME_TEST tests R8ROW_TRANSPOSE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'R8ROW_TRANSPOSE_PRINT_SOME_TEST' )
  print ( '  R8ROW_TRANSPOSE_PRINT_SOME prints some of an R8ROW, transposed.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )
  r8row_transpose_print_some ( m, n, v, 0, 3, 2, 5, '  R8ROW, rows 0:2, cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_TRANSPOSE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_uniform_ab ( m, n, a, b, seed ):

#*****************************************************************************80
#
## R8ROW_UNIFORM_AB returns a scaled pseudorandom R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Paul Bratley, Bennett Fox, Linus Schrage,
#    A Guide to Simulation,
#    Second Edition,
#    Springer, 1987,
#    ISBN: 0387964673,
#    LC: QA76.9.C65.B73.
#
#    Bennett Fox,
#    Algorithm 647:
#    Implementation and Relative Efficiency of Quasirandom
#    Sequence Generators,
#    ACM Transactions on Mathematical Software,
#    Volume 12, Number 4, December 1986, pages 362-376.
#
#    Pierre L'Ecuyer,
#    Random Number Generation,
#    in Handbook of Simulation,
#    edited by Jerry Banks,
#    Wiley, 1998,
#    ISBN: 0471134031,
#    LC: T57.62.H37.
#
#    Peter Lewis, Allen Goodman, James Miller,
#    A Pseudo-Random Number Generator for the System/360,
#    IBM Systems Journal,
#    Volume 8, Number 2, 1969, pages 136-143.
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real A, B, the range of the pseudorandom values.
#
#    Input, integer SEED, the integer "seed" used to generate
#    the output random number.
#
#    Output, real R(M,N), an array of random values between 0 and 1.
#
#    Output, integer SEED, the updated seed.  This would
#    normally be used as the input seed on the next call.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = np.floor ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8ROW_UNIFORM_AB - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8ROW_UNIFORM_AB - Fatal error!' )

  r = np.zeros ( ( m, n ) )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = np.floor ( seed )

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = a + ( b - a ) * seed * 4.656612875E-10

  return r, seed

def r8row_uniform_ab_test ( ):

#*****************************************************************************80
#
## R8ROW_UNIFORM_AB_TEST tests r8row_UNIFORM_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 4
  a = -1.0
  b = +5.0
  seed = 123456789

  print ( '' )
  print ( 'R8ROW_UNIFORM_AB_TEST' )
  print ( '  R8ROW_UNIFORM_AB computes a random R8ROW.' )
  print ( '' )
  print ( '  %g <= X <= %g' % ( a, b ) )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8row_uniform_ab ( m, n, a, b, seed )

  r8row_print ( m, n, v, '  Random R8ROW:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_UNIFORM_AB_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8row_variance ( m, n, x ):

#*****************************************************************************80
#
## R8ROW_VARIANCE returns the variances of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real X(M,N), the R8ROW whose row means are desired.
#
#    Output, real VARIANCE(M), the variances of the rows of X.
#
  import numpy as np

  variance = np.zeros ( m )

  for i in range ( 0, m ):

    mean = 0.0
    for j in range ( 0, n ):
      mean = mean + x[i,j]
    mean = mean / float ( n )

    for j in range ( 0, n ):
      variance[i] = variance[i] + ( x[i,j] - mean ) ** 2

    if ( 1 < n ):
      variance[i] = variance[i] / float ( n - 1 )
    else:
      variance[i] = 0.0 

  return variance

def r8row_variance_test ( ):

#*****************************************************************************80
#
## R8ROW_VARIANCE_TEST tests R8ROW_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 3
  n = 4

  print ( '' )
  print ( 'R8ROW_VARIANCE_TEST' )
  print ( '  R8ROW_VARIANCE computes variances of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8row_print ( m, n, a, '  The matrix:' )

  variance = r8row_variance ( m, n, a )

  r8vec_print ( m, variance, '  The row variances:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_VARIANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_print ( n, a, title ):

#*****************************************************************************80
#
## R8VEC_PRINT prints an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the vector.
#
#    Input, real A(N), the vector to be printed.
#
#    Input, string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d:  %12g' % ( i, a[i] ) )

  return

def r8vec_print_test ( ):

#*****************************************************************************80
#
## R8VEC_PRINT_TEST tests R8VEC_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 October 2014
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'R8VEC_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_PRINT prints an R8VEC.' )

  n = 4
  v = np.array ( [ 123.456, 0.000005, -1.0E+06, 3.14159265 ], dtype = np.float64 )
  r8vec_print ( n, v, '  Here is an R8VEC:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version:' )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )

if ( __name__ == '__main__' ):
  timestamp ( )
  r8row_test ( )
  timestamp ( )

