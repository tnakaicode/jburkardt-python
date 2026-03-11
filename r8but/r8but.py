#! /usr/bin/env python3
#
def r8but_test ( ):

#*****************************************************************************80
#
## r8but_test() tests r8but().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    19 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8but_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8but().' )

  r8but_det_test ( )
  r8but_indicator_test ( )
  r8but_mtv_test ( )
  r8but_mv_test ( )
  r8but_print_test ( )
  r8but_print_some_test ( )
  r8but_random_test ( )
  r8but_sl_test ( )
  r8but_slt_test ( )
  r8but_to_r8ge_test ( )
  r8but_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8but_test():' )
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

def r8but_det ( n, mu, a ):

#*****************************************************************************80
#
## R8BUT_DET computes the determinant of an R8BUT matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer MU, the upper bandwidth.
#
#    real A(MU+1,N), the R8BUT matrix.
#
#  Output:
#
#    real DET, the determinant of A.
#
  det = 1.0
  for j in range ( 0, n ):
    i = j
    k = i - j + mu
    det = det * a[k,j]

  return det

def r8but_det_test ( ):

#*****************************************************************************80
#
## R8BUT_DET_TEST tests R8BUT_DET.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_DET_TEST' )
  print ( '  R8BUT_DET computes the determinant of an R8BUT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_random ( n, mu )
  r8but_print ( n, mu, a, '  The R8BUT matrix:' )
#
#  Compute the determinant.
#
  det = r8but_det ( n, mu, a )
  print ( '' )
  print ( '  Determinant = ', det )

  return

def r8but_indicator ( n, mu ):

#*****************************************************************************80
#
## R8BUT_INDICATOR sets up an R8BUT indicator matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
#
#    The indicator matrix is stored as:
#
#       0   0  13  24  35
#       0  12  23  34  45
#      11  22  33  44  55
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
#  Input:
#
#    integer N, the number of columns of the matrix.
#
#    integer MU, the upper bandwidth.
#
#  Output:
#
#    real A(MU+1,N), the R8BUT matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( [ mu + 1, n ] )

  for j in range ( 0, n ):
    ilo = max ( 0, j - mu )
    for i in range ( ilo, j + 1 ):
      k = i - j + mu
      a[k,j] = fac * ( i + 1 ) + ( j + 1 )

  return a

def r8but_indicator_test ( ):

#*****************************************************************************80
#
## R8BUT_INDICATOR_TEST tests R8BUT_INDICATOR.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_INDICATOR_TEST' )
  print ( '  R8BUT_INDICATOR sets up an R8BUT indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_indicator ( n, mu )

  r8but_print ( n, mu, a, '  The R8BUT matrix:' )

  return

def r8but_mtv ( n, mu, a, x ):

#*****************************************************************************80
#
## R8BUT_MTV multiplies a vector by an R8BUT matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer MU, the upper bandwidth.
#
#    real A(MU+1,N), the R8BUT matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product X*A.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    ilo = max ( 0, j - mu )
    for i in range ( ilo, j + 1 ):
      k = i - j + mu
      b[j] = b[j] + a[k,j] * x[i]

  return b

def r8but_mtv_test ( ):

#*****************************************************************************80
#
## R8BUT_MTV_TEST tests R8BUT_MTV.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_MTV_TEST' )
  print ( '  R8BUT_MTV computes b=A\'*x, where A is an R8BUT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_random ( n, mu )
  r8but_print ( n, mu, a, '  The R8BUT matrix:' )
#
#  Set x.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )
#
#  Compute b=A'*x.
#
  b = r8but_mtv ( n, mu, a, x )
  r8vec_print ( n, b, '  b=A\'*x:' )

  return

def r8but_mv ( n, mu, a, x ):

#*****************************************************************************80
#
## R8BUT_MV multiplies an R8BUT matrix times a vector.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer MU, the upper bandwidth.
#
#    real A(MU+1,N), the R8BUT matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  for j in range ( 0, n ):
    ilo = max ( 0, j - mu )
    for i in range ( ilo, j + 1 ):
      k = i - j + mu
      b[i] = b[i] + a[k,j] * x[j]

  return b

def r8but_mv_test ( ):

#*****************************************************************************80
#
## R8BUT_MV_TEST tests R8BUT_MV.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_MV_TEST' )
  print ( '  R8BUT_MV computes b=A*x, where A is an R8BUT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_random ( n, mu )
  r8but_print ( n, mu, a, '  The R8BUT matrix:' )
#
#  Set x.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )
#
#  Compute b=A*x.
#
  b = r8but_mv ( n, mu, a, x )
  r8vec_print ( n, b, '  b=A*x:' )

  return

def r8but_print ( n, mu, a, title ):

#*****************************************************************************80
#
## R8BUT_PRINT prints an R8BUT matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer MU, the upper bandwidth.
#
#    real A(MU+1,N), the R8BUT matrix.
#
#    string TITLE, a title to be printed.
#
  r8but_print_some ( n, mu, a, 0, 0, n - 1, n - 1, title )

  return

def r8but_print_test ( ):

#*****************************************************************************80
#
## R8BUT_PRINT_TEST tests R8BUT_PRINT.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_PRINT_TEST' )
  print ( '  R8BUT_PRINT prints an R8BUT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_indicator ( n, mu )
#
#  Print it.
#
  r8but_print ( n, mu, a, '  The R8BUT matrix:' )

  return

def r8but_print_some ( n, mu, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8BUT_PRINT_SOME prints some of an R8BUT matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer MU, the upper bandwidth.
#
#    real A(MU+1,N), the R8BUT matrix.
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
    i2hi = min ( i2hi, j2hi + mu )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%4d' % ( i ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j in range ( j2lo, j2hi + 1 ):

        if ( i <= j and j <= i + mu ):
          k = i - j + mu
          print ( '  %12g' % ( a[k,j] ), end = '' )
        else:
          print ( '              ', end = '' )

      print ( '' )

  return

def r8but_print_some_test ( ):

#*****************************************************************************80
#
## R8BUT_PRINT_SOME_TEST tests R8BUT_PRINT_SOME.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_PRINT_SOME_TEST' )
  print ( '  R8BUT_PRINT_SOME prints some of an R8BUT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_indicator ( n, mu )
#
#  Print some of it.
#
  r8but_print_some ( n, mu, a, 1, 2, 4, 4, '  Rows 1:4, Cols 2:4:' )

  return

def r8but_random ( n, mu ):

#*****************************************************************************80
#
## R8BUT_RANDOM randomizes an R8BUT matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the number of columns of the matrix.
#
#    integer MU, the upper bandwidth.
#
#  Output:
#
#    real A(MU+1,N), the R8BUT matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( [ mu + 1, n ] )

  for j in range ( 0, n ):
    ilo = max ( 0, j - mu )
    for i in range ( ilo, j + 1 ):
      k = i - j + mu
      a[k,j] = rng.uniform ( )

  return a

def r8but_random_test ( ):

#*****************************************************************************80
#
## r8but_random_test() tests r8but_random().
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_RANDOM_TEST' )
  print ( '  R8BUT_RANDOM randomizes an R8BUT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_random ( n, mu )

  r8but_print ( n, mu, a, '  The R8BUT matrix:' )

  return

def r8but_sl ( n, mu, a, b ):

#*****************************************************************************80
#
## R8BUT_SL solves A*x=b, where A is an R8BUT matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer MU, the upper bandwidth.
#
#    real A(MU+1,N), the R8BUT matrix.
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
    i = j
    k = i - j + mu
    x[j] = x[j] / a[k,j]
    ilo = max ( 0, j - mu )
    for i in range ( ilo, j ):
      k = i - j + mu
      x[i] = x[i] - a[k,j] * x[j]

  return x

def r8but_sl_test ( ):

#*****************************************************************************80
#
## R8BUT_SL_TEST tests R8BUT_SL.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_SL_TEST' )
  print ( '  R8BUT_SL solves A*x=b, where A is an R8BUT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_random ( n, mu )
  r8but_print ( n, mu, a, '  The R8BUT matrix:' )
#
#  Set x.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )
#
#  Compute b=A*x.
#
  b = r8but_mv ( n, mu, a, x )
  r8vec_print ( n, b, '  b=A*x:' )
#
#  Solve for x.
#
  x = r8but_sl ( n, mu, a, b )
  r8vec_print ( n, x, '  x:' )

  return

def r8but_slt ( n, mu, a, b ):

#*****************************************************************************80
#
## R8BUT_SLT solves A'*x=b, where A is an R8BUT matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer MU, the upper bandwidth.
#
#    real A(MU+1,N), the R8BUT matrix.
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
    i = j
    k = i - j + mu
    x[j] = x[j] / a[k,i]
    ihi = min ( n - 1, j + mu )
    for i in range ( j + 1, ihi + 1 ):
      k = j - i + mu
      x[i] = x[i] - a[k,i] * x[j]

  return x

def r8but_slt_test ( ):

#*****************************************************************************80
#
## R8BUT_SLT_TEST tests R8BUT_SLT.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_SLT_TEST' )
  print ( '  R8BUT_SLT solves A\'*x=b, where A is an R8BUT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_random ( n, mu )
  r8but_print ( n, mu, a, '  The R8BUT matrix:' )
#
#  Set x.
#
  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x:' )
#
#  Compute b=A'*x.
#
  b = r8but_mtv ( n, mu, a, x )
  r8vec_print ( n, b, '  b=A\'*x:' )
#
#  Solve for x.
#
  x = r8but_slt ( n, mu, a, b )
  r8vec_print ( n, x, '  x:' )

  return

def r8but_to_r8ge ( n, mu, a ):

#*****************************************************************************80
#
## R8BUT_TO_R8GE copies an R8BUT matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer MU, the upper bandwidth.
#
#    real A(MU+1,N), the R8BUT matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for j in range ( 0, n ):
    ilo = max ( 0, j - mu )
    for i in range ( ilo, j + 1 ):
       k = i - j + mu
       b[i,j] = a[k,j]

  return b

def r8but_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8BUT_TO_R8GE_TEST tests R8BUT_TO_R8GE.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_TO_R8GE_TEST' )
  print ( '  R8BUT_TO_R8GE converts a matrix from R8BUT to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a_r8but = r8but_random ( n, mu )
  r8but_print ( n, mu, a_r8but, '  The R8BUT matrix:' )
#
#  Convert the matrix.
#
  a_r8ge = r8but_to_r8ge ( n, mu, a_r8but );
#
#  Print the matrix.
#
  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8but_zeros ( n, mu ):

#*****************************************************************************80
#
## R8BUT_ZEROS zeros an R8BUT matrix.
#
#  Discussion:
#
#    The R8BUT storage format is used for a banded upper triangular matrix.
#    The matrix is assumed to be zero above the MU-th superdiagonal.
#    The matrix is stored in an MU+1 by N array.
#    Columns are preserved.
#
#    The diagonal is stored in row MU+1 of the array.
#    The first superdiagonal in row MU, columns 2 through N.
#    The second superdiagonal in row MU-1, columns 3 through N.
#    The MU-th superdiagonal in row 1, columns MU+1 through N.
#
#  Example:
#
#    N = 5, MU = 2
#
#    A11 A12 A13   0   0
#      0 A22 A23 A24   0
#      0   0 A33 A34 A35
#      0   0   0 A44 A45
#      0   0   0   0 A55
#                --- ---
#                    ---
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
#  Input:
#
#    integer N, the number of columns of the matrix.
#
#    integer MU, the upper bandwidth.
#
#  Output:
#
#    real A(MU+1,N), the R8BUT matrix.
#
  import numpy as np

  a = np.zeros ( [ mu + 1, n ] )

  return a

def r8but_zeros_test ( ):

#*****************************************************************************80
#
## R8BUT_ZEROS_TEST tests R8BUT_ZEROS.
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
  mu = 3

  print ( '' )
  print ( 'R8BUT_ZEROS_TEST' )
  print ( '  R8BUT_ZEROS zeros an R8BUT matrix.' )
  print ( '' )
  print ( '  Matrix order N     = ', n )
  print ( '  Upper bandwidth MU = ', mu )
#
#  Set the matrix.
#
  a = r8but_zeros ( n, mu )

  r8but_print ( n, mu, a, '  The R8BUT matrix:' )

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
  r8but_test ( )
  timestamp ( )
