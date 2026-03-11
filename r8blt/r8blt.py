#! /usr/bin/env python3
#
def r8blt_test ( ):

#*****************************************************************************80
#
## r8blt_test() tests r8blt().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    18 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8blt_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8blt().' )

  r8blt_det_test ( )
  r8blt_indicator_test ( )
  r8blt_mtv_test ( )
  r8blt_mv_test ( )
  r8blt_print_test ( )
  r8blt_print_some_test ( )
  r8blt_random_test ( )
  r8blt_sl_test ( )
  r8blt_slt_test ( )
  r8blt_to_r8ge_test ( )
  r8blt_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8blt_test():' )
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

def r8blt_det ( n, ml, a ):

#*****************************************************************************80
#
## R8BLT_DET computes the determinant of a R8BLT matrix.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ML, the lower bandwidth.
#
#    real A(ML+1,N), the R8BLT matrix.
#
#  Output:
#
#    real DET, the determinant of A.
#
  det = 1.0
  for j in range ( 0, n ):
    det = det * a[0,j]

  return det

def r8blt_det_test ( ):

#*****************************************************************************80
#
## R8BLT_DET_TEST tests R8BLT_DET.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'R8BLT_DET_TEST' )
  print ( '  R8BLT_DET computes the determinant of an R8BLT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_random ( n, ml )
  r8blt_print ( n, ml, a, '  The R8BLT matrix:' )
#
#  Compute the determinant.
#
  det = r8blt_det ( n, ml, a )
  print ( '' )
  print ( '  Determinant = ', det )

  return

def r8blt_indicator ( n, ml ):

#*****************************************************************************80
#
## R8BLT_INDICATOR sets up a R8BLT indicator matrix.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#    The indicator matrix is stored as:
#
#      11  22  33  44  55
#      21  32  43  54   0
#      31  42  53   0   0
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of columns of the matrix.
#
#    integer ML, the lower bandwidth.
#
#  Output:
#
#    real A(ML+1,N), the R8BLT matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( [ ml + 1, n ] )

  for i in range ( 0, n ):
    jlo = max ( 0, i - ml )
    for j in range ( jlo, i + 1 ):
      a[i-j,j] = fac * ( i + 1 ) + ( j + 1 )

  return a

def r8blt_indicator_test ( ):

#*****************************************************************************80
#
## R8BLT_INDICATOR_TEST tests R8BLT_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'R8BLT_INDICATOR_TEST' )
  print ( '  R8BLT_INDICATOR sets up an R8BLT indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_indicator ( n, ml )

  r8blt_print ( n, ml, a, '  The R8BLT matrix:' )

  return

def r8blt_mtv ( n, ml, a, x ):

#*****************************************************************************80
#
## R8BLT_MTV multiplies a vector by a R8BLT matrix.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ML, the lower bandwidth.
#
#    real A(ML+1,N), the R8BLT matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product X*A.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):
    jlo = max ( 0, i - ml )
    for j in range ( jlo, i + 1 ):
      b[j] = b[j] + x[i] * a[i-j,j]

  return b

def r8blt_mtv_test ( ):

#*****************************************************************************80
#
## R8BLT_MTV_TEST tests R8BLT_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'R8BLT_MTV_TEST' )
  print ( '  R8BLT_MTV computes b=A\'*x, where A is an R8BLT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_random ( n, ml )
  r8blt_print ( n, ml, a, '  The R8BLT matrix:' )
#
#  Set x.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )
#
#  Compute b=A'*x.
#
  b = r8blt_mtv ( n, ml, a, x )
  r8vec_print ( n, b, '  b=A\'*x:' )

  return

def r8blt_mv ( n, ml, a, x ):

#*****************************************************************************80
#
## R8BLT_MV multiplies a R8BLT matrix times a vector.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ML, the lower bandwidth.
#
#    real A(ML+1,N), the R8BLT matrix.
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
    jlo = max ( 0, i - ml )
    for j in range ( jlo, i + 1 ):
      b[i] = b[i] + a[i-j,j] * x[j]

  return b

def r8blt_mv_test ( ):

#*****************************************************************************80
#
## R8BLT_MV_TEST tests R8BLT_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'R8BLT_MV_TEST' )
  print ( '  R8BLT_MV computes b=A*x, where A is an R8BLT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_random ( n, ml )
  r8blt_print ( n, ml, a, '  The R8BLT matrix:' )
#
#  Set x.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )
#
#  Compute b=A*x.
#
  b = r8blt_mv ( n, ml, a, x )
  r8vec_print ( n, b, '  b=A*x:' )

  return

def r8blt_print ( n, ml, a, title ):

#*****************************************************************************80
#
## R8BLT_PRINT prints a R8BLT matrix.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ML, the lower bandwidth.
#
#    real A(ML+1,N), the R8BLT matrix.
#
#    string TITLE, a title to be printed.
#
  r8blt_print_some ( n, ml, a, 0, 0, n - 1, n - 1, title )

  return

def r8blt_print_test ( ):

#*****************************************************************************80
#
## R8BLT_PRINT_TEST tests R8BLT_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'R8BLT_PRINT_TEST' )
  print ( '  R8BLT_PRINT prints an R8BLT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_indicator ( n, ml )
#
#  Print it.
#
  r8blt_print ( n, ml, a, '  The R8BLT matrix:' )

  return

def r8blt_print_some ( n, ml, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8BLT_PRINT_SOME prints some of a R8BLT matrix.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ML, the lower bandwidth.
#
#    real A(ML+1,N), the R8BLT matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n - 1 )
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
    i2lo = max ( i2lo, j2lo )
    i2hi = min ( ihi, n - 1 )
    i2hi = min ( i2hi, j2hi + ml )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%4d' % ( i ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j in range ( j2lo, j2hi + 1 ):

        if ( 0 <= i - j and i - j <= ml ):
          print ( '  %12g' % ( a[i-j,j] ), end = '' )
        else:
          print ( '              ', end = '' )

      print ( '' )

  return

def r8blt_print_some_test ( ):

#*****************************************************************************80
#
## R8BLT_PRINT_SOME_TEST tests R8BLT_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 10
  ml = 3

  print ( '' )
  print ( 'R8BLT_PRINT_SOME_TEST' )
  print ( '  R8BLT_PRINT_SOME prints some of an R8BLT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_indicator ( n, ml )
#
#  Print some of it.
#
  r8blt_print_some ( n, ml, a, 0, 1, 2, 2, '  Rows 0:3, Cols 1:3:' )

  return

def r8blt_random ( n, ml ):

#*****************************************************************************80
#
## R8BLT_RANDOM randomizes a R8BLT matrix.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of columns of the matrix.
#
#    integer ML, the lower bandwidth.
#
#  Output:
#
#    real A(ML+1,N), the R8BLT matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( [ ml + 1, n ] )

  for i in range ( 0, n ):
    jlo = max ( 0, i - ml )
    for j in range ( jlo, i + 1 ):
      a[i-j,j] = rng.random ( )

  return a

def r8blt_random_test ( ):

#*****************************************************************************80
#
## r8blt_random_test() tests r8blt_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'r8blt_random_test():' )
  print ( '  r8blt_random() randomizes an R8BLT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_random ( n, ml )

  r8blt_print ( n, ml, a, '  The R8BLT matrix:' )

  return

def r8blt_sl ( n, ml, a, b ):

#*****************************************************************************80
#
## R8BLT_SL solves A*x=b, where A is an R8BLT matrix.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#    No factorization of the lower triangular matrix is required.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ML, the lower bandwidth.
#
#    real A(ML+1,N), the R8BLT matrix.
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
    x[j] = x[j] / a[0,j]
    ihi = min ( j + ml, n - 1 )
    for i in range ( j + 1, ihi + 1 ):
      x[i] = x[i] - a[i-j,j] * x[j]

  return x

def r8blt_sl_test ( ):

#*****************************************************************************80
#
## R8BLT_SL_TEST tests R8BLT_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'R8BLT_SL_TEST' )
  print ( '  R8BLT_SL solves A*x=b, where A is an R8BLT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_random ( n, ml )
  r8blt_print ( n, ml, a, '  The R8BLT matrix:' )
#
#  Set x.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )
#
#  Compute b=A*x.
#
  b = r8blt_mv ( n, ml, a, x )
  r8vec_print ( n, b, '  b=A*x:' )
#
#  Solve for x.
#
  x = r8blt_sl ( n, ml, a, b )
  r8vec_print ( n, x, '  x:' )

  return

def r8blt_slt ( n, ml, a, b ):

#*****************************************************************************80
#
## R8BLT_SLT solves A'*x=b, where A is an R8BLT matrix.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#    No factorization of the lower triangular matrix is required.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ML, the lower bandwidth.
#
#    real A(ML+1,N), the R8BLT matrix.
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
    x[j] = x[j] / a[0,j]
    ilo = max ( j - ml, 0 )
    for i in range ( ilo, j ):
      x[i] = x[i] - a[j-i,i] * x[j]

  return x

def r8blt_slt_test ( ):

#*****************************************************************************80
#
## R8BLT_SLT_TEST tests R8BLT_SLT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'R8BLT_SLT_TEST' )
  print ( '  R8BLT_SLT solves A\'*x=b, where A is an R8BLT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_random ( n, ml )
  r8blt_print ( n, ml, a, '  The R8BLT matrix:' )
#
#  Set x.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )
#
#  Compute b=A'*x.
#
  b = r8blt_mtv ( n, ml, a, x )
  r8vec_print ( n, b, '  b=A\'*x:' )
#
#  Solve for x.
#
  x = r8blt_slt ( n, ml, a, b )
  r8vec_print ( n, x, '  x:' )

  return

def r8blt_to_r8ge ( n, ml, a ):

#*****************************************************************************80
#
## R8BLT_TO_R8GE copies a R8BLT matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8BLT storage format is used for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ML, the lower bandwidth.
#
#    real A(ML+1,N), the R8BLT matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, n ):
       if ( j <= i and i <= j + ml ):
          b[i,j] = a[i-j,j]

  return b

def r8blt_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8BLT_TO_R8GE_TEST tests R8BLT_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'R8BLT_TO_R8GE_TEST' )
  print ( '  R8BLT_TO_R8GE converts a matrix from R8BLT to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a_r8blt = r8blt_random ( n, ml )
  r8blt_print ( n, ml, a_r8blt, '  The R8BLT matrix:' )
#
#  Convert the matrix.
#
  a_r8ge = r8blt_to_r8ge ( n, ml, a_r8blt );
#
#  Print the matrix.
#
  r8ge_print ( n, n, a_r8ge, '  The R8GE matrix:' )

  return

def r8blt_zeros ( n, ml ):

#*****************************************************************************80
#
## R8BLT_ZEROS zeros an R8BLT matrix.
#
#  Discussion:
#
#    The R8BLT storage format is appropriate for a banded lower triangular matrix.
#    The matrix is assumed to be zero below the ML-th subdiagonal.
#    The matrix is stored in an ML+1 by N array, in which the diagonal
#    appears in the first row, followed by successive subdiagonals.
#    Columns are preserved.
#
#  Example:
#
#    N = 5, ML = 2
#
#    A11   0   0   0   0
#    A21 A22   0   0   0
#    A31 A32 A33   0   0
#      0 A42 A43 A44   0
#      0   0 A53 A54 A55
#                --- ---
#                    ---
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    06 October 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of columns of the matrix.
#
#    integer ML, the lower bandwidth.
#
#  Output:
#
#    real A(ML+1,N), the R8BLT matrix.
#
  import numpy as np

  a = np.zeros ( [ ml + 1, n ] )

  return a

def r8blt_zeros_test ( ):

#*****************************************************************************80
#
## R8BLT_ZEROS_TEST tests R8BLT_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    07 October 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5
  ml = 3

  print ( '' )
  print ( 'R8BLT_ZEROS_TEST' )
  print ( '  R8BLT_ZEROS zeros an R8BLT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Lower bandwidth ML = ', ml )
#
#  Set the matrix.
#
  a = r8blt_zeros ( n, ml )

  r8blt_print ( n, ml, a, '  The R8BLT matrix:' )
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
  r8blt_test ( )
  timestamp ( )
