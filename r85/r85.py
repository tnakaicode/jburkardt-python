#! /usr/bin/env python3
#
def r85_test ( ):

#*****************************************************************************80
#
## r85_test() tests r85().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r85_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r85().' )

  r85_dif2_test ( )
  r85_indicator_test ( )
  r85_mtv_test ( )
  r85_mv_test ( )
  r85_np_fs_test ( )
  r85_print_test ( )
  r85_print_some_test ( )
  r85_random_test ( )
  r85_to_r8ge_test ( )
  r85_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r85_test():' )
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

def r85_dif2 ( n ):

#*****************************************************************************80
#
## R85_DIF2 sets up an R85 second difference matrix.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how an R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 July 2016
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
#    real A(5,N), the matrix.
#
  import numpy as np

  a = np.zeros ( [ 5, n ] )

  a[1,1:n] = - 1.0
  a[2,0:n] = 2.0
  a[3,0:n-1] = - 1.0

  return a

def r85_dif2_test ( ):

#*****************************************************************************80
#
## R85_DIF2_TEST tests R85_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R85_DIF2_TEST' )
  print ( '  R85_DIF2 sets up a R85 second difference matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r85_dif2 ( n )

  r85_print ( n, a, '  The R85 second difference matrix:' )

  return

def r85_indicator ( n ):

#*****************************************************************************80
#
## R85_INDICATOR sets up a R85 indicator matrix.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#    Here are the values as stored in an indicator matrix:
#
#      00 00 13 24 35 46
#      00 12 23 34 45 56
#      11 22 33 44 55 66
#      21 32 43 54 65 00
#      31 42 53 64 00 00
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
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
#    real A(5,N), the R85 indicator matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( [ 5, n ] )

  for j in range ( 2, n ):
    i = j - 2
    a[0,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  for j in range ( 1, n ):
    i = j - 1
    a[1,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  for j in range ( 0, n ):
    i = j
    a[2,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  for j in range ( 0, n - 1 ):
    i = j + 1
    a[3,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  for j in range ( 0, n - 2 ):
    i = j + 2
    a[4,j] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return a

def r85_indicator_test ( ):

#*****************************************************************************80
#
## R85_INDICATOR_TEST tests R85_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R85_INDICATOR_TEST' )
  print ( '  R85_INDICATOR sets up a R85 indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r85_indicator ( n )

  r85_print ( n, a, '  The R85 indicator matrix:' )

  return

def r85_mtv ( n, a, x ):

#*****************************************************************************80
#
## R85_MTV multiplies a vector by a R85 matrix.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the linear system.
#
#    real A(5,N), the R85 matrix.
#
#    real X(N), the vector to be multiplied by A'.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  b[0:n]   =            a[2,0:n]   * x[0:n]
  b[1:n]   = b[1:n]   + a[3,0:n-1] * x[0:n-1]
  b[2:n]   = b[2:n]   + a[4,0:n-2] * x[0:n-2]
  b[0:n-1] = b[0:n-1] + a[1,1:n]   * x[1:n]
  b[0:n-2] = b[0:n-2] + a[0,2:n]   * x[2:n]

  return b

def r85_mtv_test ( ):

#*****************************************************************************80
#
## R85_MTV_TEST tests R85_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R85_MTV_TEST' )
  print ( '  R85_MTV computes b=A\'*x, where A is an R85 matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r85_indicator ( n )

  r85_print ( n, a, '  The R85 matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r85_mtv ( n, a, x )

  r8vec_print ( n, b, '  The product b=A\'*x:' )

  return

def r85_mv ( n, a, x ):

#*****************************************************************************80
#
## R85_MV multiplies a R85 matrix times a vector.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the linear system.
#
#    real A(5,N), the R85 matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    b[i] = a[2,i] * x[i]

  for i in range ( 2, n ):
    b[i] = b[i] + a[0,i] * x[i-2]

  for i in range ( 1, n ):
    b[i] = b[i] + a[1,i] * x[i-1]

  for i in range ( 0, n - 1 ):
    b[i] = b[i] + a[3,i] * x[i+1]

  for i in range ( 0, n - 2 ):
    b[i] = b[i] + a[4,i] * x[i+2]

  return b

def r85_mv_test ( ):

#*****************************************************************************80
#
## R85_MV_TEST tests R85_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R85_MV_TEST' )
  print ( '  R85_MV computes b=A*x, where A is an R85 matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r85_indicator ( n )

  r85_print ( n, a, '  The R85 matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  The vector x:' )

  b = r85_mv ( n, a, x )

  r8vec_print ( n, b, '  The product b=A*x:' )

  return

def r85_np_fs ( n, a, b ):

#*****************************************************************************80
#
## R85_NP_FS factors and solves a R85 linear system.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#    The factorization algorithm requires that each diagonal entry be nonzero.
#
#    No pivoting is performed, and therefore the algorithm may fail
#    in simple cases where the matrix is not singular.
#
#  Example:
#
#    Here is how a R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt.
#
#  Reference:
#
#    Cheney and Kincaid,
#    Numerical Mathematics and Computing,
#    1985, pages 233-236.
#
#  Input:
#
#    integer N, the order of the linear system.
#
#    real A(5,N): the pentadiagonal matrix.
#
#    real B(N), the right hand side of the linear system.
#
#  Output:
#
#    real A(5,N): input overwritten by factorization information.
#
#    real X(N), the solution of the linear system.
#
  import numpy as np

  for i in range ( 0, n ):
    if ( a[2,i] == 0.0 ):
      print ( '' )
      print ( 'R85_NP_FS - Fatal error!' )
      print ( '  A[2,',i,'] = 0.' )
      raise Exception ( 'r85_np_fs(): Fatal error!' )

  x = np.zeros ( n )

  for i in range ( 1, n - 1 ):

    xmult = a[1,i] / a[2,i-1]
    a[2,i] = a[2,i] - xmult * a[3,i-1]
    a[3,i] = a[3,i] - xmult * a[4,i-1]

    b[i] = b[i] - xmult * b[i-1]

    xmult = a[0,i+1] / a[2,i-1]
    a[1,i+1] = a[1,i+1] - xmult * a[3,i-1]
    a[2,i+1] = a[2,i+1] - xmult * a[4,i-1]

    b[i+1] = b[i+1] - xmult * b[i-1]

  xmult = a[1,n-1] / a[2,n-2]
  a[2,n-1] = a[2,n-1] - xmult * a[3,n-2]

  x[n-1] = ( b[n-1] - xmult * b[n-2] ) / a[2,n-1]
  x[n-2] = ( b[n-2] - a[3,n-2] * x[n-1] ) / a[2,n-2]

  for i in range ( n - 3, -1, -1 ):
    x[i] = ( b[i] - a[3,i] * x[i+1] - a[4,i] * x[i+2] ) / a[2,i]

  return x

def r85_np_fs_test ( ):

#*****************************************************************************80
#
## R85_NP_FS_TEST tests R85_NP_FS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'R85_NP_FS_TEST' )
  print ( '  R85_NP_FS factors and solves a pentadiagonal' )
  print ( '  linear system, with no pivoting.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix to a random value.
#
  a = r85_random ( n )

  r85_print ( n, a, '  The pentadiagonal matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute b = A * x.
#
  b = r85_mv ( n, a, x )

  r8vec_print ( n, b, '  The right hand side:' )
#
#  Solve the system.
#
  x = r85_np_fs ( n, a, b )

  r8vec_print ( n, x, '  Solution:' )

  return

def r85_print ( n, a, title ):

#*****************************************************************************80
#
## R85_PRINT prints a R85 matrix.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
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
#    real A(5,N), the R85 matrix.
#
#    string TITLE, a title to be printed.
#
  r85_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return

def r85_print_test ( ):

#*****************************************************************************80
#
## R85_PRINT_TEST tests R85_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R85_PRINT_TEST' )
  print ( '  R85_PRINT prints an R85 matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r85_indicator ( n )

  r85_print ( n, a, '  The R85 matrix:' )

  return

def r85_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R85_PRINT_SOME prints some of a R85 matrix.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(5,N), the R85 matrix.
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
    i2lo = max ( i2lo, j2lo - 2 )
    i2hi = min ( ihi, n - 1 )
    i2hi = min ( i2hi, j2hi + 2 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )

      for j in range ( j2lo, j2hi + 1 ):

        if ( 2 < i - j or 2 < j - i ):
          print ( '              ', end = '' )
        elif ( j == i + 2 ):
          print ( '%12g  ' % ( a[0,j] ), end = '' )
        elif ( j == i+1 ):
          print ( '%12g  ' % ( a[1,j] ), end = '' )
        elif ( j == i ):
          print ( '%12g  ' % ( a[2,j] ), end = '' )
        elif ( j == i-1 ):
          print ( '%12g  ' % ( a[3,j] ), end = '' )
        elif ( j == i-2 ):
          print ( '%12g  ' % ( a[4,j] ), end = '' )

      print ( '' )

  return

def r85_print_some_test ( ):

#*****************************************************************************80
#
## R85_PRINT_SOME_TEST tests R85_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 8

  print ( '' )
  print ( 'R85_PRINT_SOME_TEST' )
  print ( '  R85_PRINT_SOME prints some of an R85 matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r85_indicator ( n )

  r85_print_some ( n, a, 1, 2, 5, 4, '  Rows 1-5, Cols 2-4:' )

  return

def r85_random ( n ):

#*****************************************************************************80
#
## R85_RANDOM randomizes a R85 matrix.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the linear system.
#
#  Output:
#
#    real A(5,N), the R85 matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( [ 5, n ] )

  for j in range ( 2, n ):
    a[0,j] = rng.random ( )

  for j in range ( 1, n ):
    a[1,j] = rng.random ( )

  for j in range ( 0, n ):
    a[2,j] = rng.random ( )

  for j in range ( 0, n - 1 ):
    a[3,j] = rng.random ( )

  for j in range ( 0, n - 2 ):
    a[4,j] = rng.random ( )

  return a

def r85_random_test ( ):

#*****************************************************************************80
#
## r85_random_test() tests r85_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r85_random_test():' )
  print ( '  r85_random() sets up a random R85 matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r85_random ( n )

  r85_print ( n, a, '  The R85 random matrix:' )

  return

def r85_to_r8ge ( n, a ):

#*****************************************************************************80
#
## R85_TO_R8GE copies a R85 matrix into a R8GE matrix.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
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
#    real A(5,N), the R85 matrix.
#
#  Output:
#
#    real A(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):

      if ( j == i - 2 ):
        b[i,j] = a[0,i]
      elif ( j == i - 1 ):
        b[i,j] = a[1,i]
      elif ( i == j ):
        b[i,j] = a[2,i]
      elif ( j == i + 1 ):
        b[i,j] = a[3,i]
      elif ( j == i + 2 ):
        b[i,j] = a[4,i]

  return b

def r85_to_r8ge_test ( ):

#*****************************************************************************80
#
## R85_TO_R8GE_TEST tests R85_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R85_TO_R8GE_TEST' )
  print ( '  R85_TO_R8GE converts an R85 matrix to R8GE form.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r85_indicator ( n )

  r85_print ( n, a, '  The R85 matrix:' )

  a_r8ge = r85_to_r8ge ( n, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r85_zeros ( n ):

#*****************************************************************************80
#
## R85_ZEROS zeros an R85 matrix.
#
#  Discussion:
#
#    The R85 storage format represents a pentadiagonal matrix as a 5 
#    by N array, in which each row corresponds to a diagonal, and 
#    column locations are preserved.  Thus, the original matrix is 
#    "collapsed" vertically into the array.
#
#  Example:
#
#    Here is how a R85 matrix of order 6 would be stored:
#
#       *   *  A13 A24 A35 A46
#       *  A12 A23 A34 A45 A56
#      A11 A22 A33 A44 A55 A66
#      A21 A32 A43 A54 A65  *
#      A31 A42 A53 A64  *   *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the linear system.
#
#  Output:
#
#    real A(5,N), the R85 matrix.
#
  import numpy as np

  a = np.zeros ( [ 5, n ] )

  return a

def r85_zeros_test ( ):

#*****************************************************************************80
#
## R85_ZEROS_TEST tests R85_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 July 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R85_ZEROS_TEST' )
  print ( '  R85_ZEROS sets up a R85 zero matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r85_zeros ( n )

  r85_print ( n, a, '  The R85 zero matrix:' )

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
  r85_test ( )
  timestamp ( )
