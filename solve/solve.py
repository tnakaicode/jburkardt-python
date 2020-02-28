#! /usr/bin/env python
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
  i = int ( i )

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
  import numpy as np
  import platform

  n = 13

  x = np.array ( [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ] )

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

def r8ge_fs ( n, a, b ):

#*****************************************************************************80
#
## R8GE_FS factors and solves a R8GE system.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#    R8GE_FS does not save the LU factors of the matrix, and hence cannot
#    be used to efficiently solve multiple linear systems, or even to
#    factor A at one time, and solve a single linear system at a later time.
#
#    R8GE_FS uses partial pivoting, but no pivot vector is required.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be positive.
#
#    Input, real A(N,N), the coefficient matrix of the linear system.
#
#    Input, real B(N), the right hand side of the linear system.
#
#    Output, real X(N), the solution of the linear system.
#
  import numpy as np

  info = 0
  x = b.copy ( )

  for jcol in range ( 0, n ):
#
#  Find the maximum element in column I.
#
    piv = abs ( a[jcol,jcol] )
    ipiv = jcol
    for i in range ( jcol + 1, n ):
      if ( piv < abs ( a[i,jcol] ) ):
        piv = abs ( a[i,jcol] )
        ipiv = i

    if ( piv == 0.0 ):
      info = jcol
      return
#
#  Switch rows JCOL and IPIV, and B.
#
    if ( jcol != ipiv ):

      for j in range ( 0, n ):
        t         = a[jcol,j]
        a[jcol,j] = a[ipiv,j]
        a[ipiv,j] = t

      t       = x[jcol]
      x[jcol] = x[ipiv]
      x[ipiv] = t
#
#  Scale the pivot row.
#
    t = a[jcol,jcol]
    a[jcol,jcol] = 1.0
    for k in range ( jcol + 1, n ):
      a[jcol,k] = a[jcol,k] / t
    x[jcol] = x[jcol] / t
#
#  Use the pivot row to eliminate lower entries in that column.
#
    for i in range ( jcol + 1, n ):
      if ( a[i,jcol] != 0.0 ):
        t = - a[i,jcol]
        a[i,jcol] = 0.0
        for k in range ( jcol + 1, n ):
          a[i,k] = a[i,k] + t * a[jcol,k]
        x[i] = x[i] + t * x[jcol]
#
#  Back solve.
#
  for jcol in range ( n - 1, 0, -1 ):
    for k in range ( 0, jcol ):
      x[k] = x[k] - a[k,jcol] * x[jcol]

  return x

def r8ge_fs_test ( ):

#*****************************************************************************80
#
## R8GE_FS_TEST tests R8GE_FS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  n = 10
  seed = 123456789

  print ( '' )
  print ( 'R8GE_FS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_FS factors and solves a linear system involving' )
  print ( '  an R8GE matrix.' )
  print ( '' )
  print ( '  Matrix order N = %d' % ( n ) )
#
#  Set the matrix.
#
  a, seed = r8ge_random ( n, n, seed )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8ge_mv ( n, n, a, x )
#
#  Factor and solve the system.
#
  x = r8ge_fs ( n, a, b )
 
  r8vec_print ( n, x, '  Solution:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_FS_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_indicator ( m, n ):

#*****************************************************************************80
#
## R8GE_INDICATOR sets an R8GE indicator matrix.
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
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of A.
#
#    Output, real A(M,N), the matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a[i,j] = fac * ( i + 1 ) +  ( j + 1 )

  return a

def r8ge_indicator_test ( ):

#*****************************************************************************80
#
## R8GE_INDICATOR_TEST tests R8GE_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_INDICATOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_INDICATOR returns the indicator matrix.' )

  a = r8ge_indicator ( m, n )

  r8ge_print ( m, n, a, '  Indicator matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_INDICATOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_mv ( m, n, a, x ):

#*****************************************************************************80
#
## R8GE_MV multiplies an R8GE matrix times a vector.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
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
#    Input, real A(M,N), the R8GE matrix.
#
#    Input, real X(N), the vector to be multiplied by A.
#
#    Output, real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i] = b[i] + a[i,j] * x[j]

  return b

def r8ge_mv_test ( ):

#*****************************************************************************80
#
## R8GE_MV_TEST tests R8GE_MV.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 September 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  m = 5
  n = 4

  print ( '' )
  print ( 'R8GE_MV_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_MV computes a matrix product b=A*x for an R8GE matrix.' )

  a = r8ge_indicator ( m, n )
  r8ge_print ( m, n, a, '  The matrix A:' )

  x = r8vec_indicator1 ( m )
  r8vec_print ( m, x, '  The vector X:' )

  b = r8ge_mv ( m, n, a, x )
  r8vec_print ( n, b, '  The vector b=A*x:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_MV_TEST' )
  print ( '  Normal end of execution.' )
  return

def r8ge_print ( m, n, a, title ):

#*****************************************************************************80
#
## R8GE_PRINT prints an R8GE matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
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
  r8ge_print_some ( m, n, a, 0, 0, m - 1, n - 1, title )

  return

def r8ge_print_test ( ):

#*****************************************************************************80
#
## R8GE_PRINT_TEST tests R8GE_PRINT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8GE_PRINT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_PRINT prints an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print ( m, n, v, '  Here is an R8GE:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_PRINT_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8GE_PRINT_SOME prints out a portion of an R8GE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 February 2015
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
    j2hi = min ( j2hi, n - 1 )
    j2hi = min ( j2hi, jhi )
    
    print ( '' )
    print ( '  Col: ' ),

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ) ),

    print ( '' )
    print ( '  Row' )

    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, m - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ) ),
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( a[i,j] ) ),

      print ( '' )

  return

def r8ge_print_some_test ( ):

#*****************************************************************************80
#
## R8GE_PRINT_SOME_TEST tests R8GE_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8GE_PRINT_SOME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_PRINT_SOME prints some of an R8GE matrix.' )

  m = 4
  n = 6
  v = np.array ( [ \
    [ 11.0, 12.0, 13.0, 14.0, 15.0, 16.0 ], 
    [ 21.0, 22.0, 23.0, 24.0, 25.0, 26.0 ], 
    [ 31.0, 32.0, 33.0, 34.0, 35.0, 36.0 ], 
    [ 41.0, 42.0, 43.0, 44.0, 45.0, 46.0 ] ], dtype = np.float64 )

  r8ge_print_some ( m, n, v, 0, 3, 2, 5, '  Rows 0:2, Cols 3:5:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_PRINT_SOME_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8ge_random ( m, n, seed ):

#*****************************************************************************80
#
## R8GE_RANDOM randomizes a R8GE matrix.
#
#  Discussion:
#
#    The R8GE storage format is used for a general M by N matrix.  A storage 
#    space is made for each logical entry.  The two dimensional logical
#    array is mapped to a vector, in which storage is by columns.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
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
#    Input, integer SEED, a seed for the random number generator.
#
#    Output, real A(M,N), the R8GE matrix.
#
#    Output, integer SEED, an updated seed for the random number generator.
#
  import numpy as np
  from sys import exit

  i4_huge = 2147483647

  seed = int ( seed )

  if ( seed < 0 ):
    seed = seed + i4_huge

  if ( seed == 0 ):
    print ( '' )
    print ( 'R8GE_RANDOM - Fatal error!' )
    print ( '  Input SEED = 0!' )
    exit ( 'R8GE_RANDOM - Fatal error!' )

  r = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):

      k = ( seed // 127773 )

      seed = 16807 * ( seed - k * 127773 ) - k * 2836

      seed = ( seed % i4_huge )

      if ( seed < 0 ):
        seed = seed + i4_huge

      r[i,j] = seed * 4.656612875E-10

  return r, seed

def r8ge_random_test ( ):

#*****************************************************************************80
#
## R8GE_RANDOM_TEST tests R8GE_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  m = 5
  n = 4
  seed = 123456789

  print ( '' )
  print ( 'R8GE_RANDOM_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8GE_RANDOM computes a random R8GE.' )
  print ( '' )
  print ( '  0 <= X <= 1' )
  print ( '  Initial seed is %d' % ( seed ) )

  v, seed = r8ge_random ( m, n, seed )

  r8ge_print ( m, n, v, '  Random R8GE:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8GE_RANDOM_TEST:' )
  print ( '  Normal end of execution.' )
  return

def r8vec_indicator1 ( n ):

#*****************************************************************************80
#
## R8VEC_INDICATOR1 sets an R8VEC to the indicator vector (1,2,3,...).
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 September 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements of the vector.
#
#    Output, real A(N), the indicator array.
#
  import numpy

  a = numpy.zeros ( n );

  for i in range ( 0, n ):
    a[i] = i + 1

  return a

def r8vec_indicator1_test ( ):

#*****************************************************************************80
#
## R8VEC_INDICATOR1_TEST tests R8VEC_INDICATOR1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
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
  import platform

  print ( '' )
  print ( 'R8VEC_INDICATOR1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_INDICATOR1 returns the 1-based indicator matrix.' )

  n = 10
  a = r8vec_indicator1 ( n )

  r8vec_print ( n, a, '  The 1-based indicator vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_INDICATOR1_TEST' )
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

def solve_test ( ):

#*****************************************************************************80
#
## SOLVE_TEST tests the SOLVE library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    08 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SOLVE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the SOLVE library.' )

  i4_log_10_test ( )

  r8ge_fs_test ( )
  r8ge_indicator_test ( )
  r8ge_mv_test ( )
  r8ge_print_test ( )
  r8ge_print_some_test ( )
  r8ge_random_test ( )

  r8vec_indicator1_test ( )
  r8vec_print_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'SOLVE_TEST:' )
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
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  solve_test ( )
  timestamp ( )

