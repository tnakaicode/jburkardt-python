#! /usr/bin/env python3
#
def r8to_test ( ):

#*****************************************************************************80
#
## r8to_test() tests r8to().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    28 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8to_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8to().' )

  r8to_dif2_test ( )
  r8to_indicator_test ( )
  r8to_mtv_test ( )
  r8to_mv_test ( )
  r8to_print_test ( )
  r8to_print_some_test ( )
  r8to_random_test ( )
  r8to_sl_test ( )
  r8to_slt_test ( )
  r8to_to_r8ge_test ( )
  r8to_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8to_test():' )
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

def r8to_dif2 ( n ):

#*****************************************************************************80
#
## R8TO_DIF2 sets the second difference as an R8TO matrix.
#
#  Discussion:
#
#    The R8TO storage format is used for a real Toeplitz matrix, which 
#    is constant along diagonals.  Thus, in an N by N Toeplitz matrix, 
#    there are at most 2*N-1 distinct entries.  The format stores the 
#    N elements of the first row, followed by the N-1 elements of the 
#    first column (skipping the entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 September 2015
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
#    real A(2*N-1), the R8TO matrix.
#
  import numpy as np

  a = np.zeros ( 2 * n - 1 )

  a[0] = 2.0
  a[1] = -1.0
  a[n] = -1.0

  return a

def r8to_dif2_test ( ):

#*****************************************************************************80
#
## R8TO_DIF2_TEST tests R8TO_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8to_dif2_test():' )
  print ( '  r8to_dif2() sets up the second difference matrix in R8TO format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8to_dif2 ( n )

  r8to_print ( n, a, '  The matrix:' )

  return

def r8to_indicator ( n ):

#*****************************************************************************80
#
## R8TO_INDICATOR sets up a R8TO indicator matrix.
#
#  Discussion:
#
#    The R8TO storage format is used for a real Toeplitz matrix, which 
#    is constant along diagonals.  Thus, in an N by N Toeplitz matrix, 
#    there are at most 2*N-1 distinct entries.  The format stores the 
#    N elements of the first row, followed by the N-1 elements of the 
#    first column (skipping the entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
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
#  Output:
#
#    Output, real A(2*N-1), the R8TO matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = np.zeros ( 2 * n - 1 )

  i = 0
  k = 0
  for j in range ( 0, n ):
    a[k] = fac * ( i + 1 ) + ( j + 1 )
    k = k + 1

  j = 0
  for i in range ( 1, n ):
    a[k] = fac * ( i + 1 ) + ( j + 1 )
    k = k + 1
  
  return a

def r8to_indicator_test ( ):

#*****************************************************************************80
#
## R8TO_INDICATOR_TEST tests R8TO_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8TO_INDICATOR_TEST' )
  print ( '  R8TO_INDICATOR sets up a R8TO indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8to_indicator ( n )

  r8to_print ( n, a, '  The R8TO indicator matrix:' )

  return

def r8to_mtv ( n, a, x ):

#*****************************************************************************80
#
## R8TO_MTV multiplies a vector by a R8TO matrix.
#
#  Discussion:
#
#    The R8TO storage format is used for a Toeplitz matrix, which is constant
#    along diagonals.  Thus, in an N by N Toeplitz matrix, there are at most 
#    2*N-1 distinct entries.  The format stores the N elements of the first
#    row, followed by the N-1 elements of the first column (skipping the
#    entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(2*N-1), the R8TO matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A' * X.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 0, n ):

    for j in range ( 0, i + 1 ):
      b[i] = b[i] + a[i-j] * x[j]

    for j in range ( i + 1, n ):
      b[i] = b[i] + a[n-i+j-1] * x[j]

  return b

def r8to_mtv_test ( ):

#*****************************************************************************80
#
## R8TO_MTV_TEST tests R8TO_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8TO_MTV_TEST' )
  print ( '  R8TO_MTV computes b=A\'*x, where A is an R8TO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8to_random ( n )

  r8to_print ( n, a, '  The Toeplitz matrix:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x: ' )

  b = r8to_mtv ( n, a, x )
  r8vec_print ( n, b, '  b = A\'*x:' )

  return

def r8to_mv ( n, a, x ):

#*****************************************************************************80
#
## R8TO_MV multiplies a R8TO matrix times a vector.
#
#  Discussion:
#
#    The R8TO storage format is used for a Toeplitz matrix, which is constant
#    along diagonals.  Thus, in an N by N Toeplitz matrix, there are at most 
#    2*N-1 distinct entries.  The format stores the N elements of the first
#    row, followed by the N-1 elements of the first column (skipping the
#    entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(2*N-1), the R8TO matrix.
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
    b[0] = b[0] + a[i] * x[i]

  for i in range ( 1, n ):
    for j in range ( 0, i ):
      b[i] = b[i] + a[n+i-j-1] * x[j]
    for j in range ( i, n ):
      b[i] = b[i] + a[j-i] * x[j]

  return b

def r8to_mv_test ( ):

#*****************************************************************************80
#
## R8TO_MV_TEST tests R8TO_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8TO_MV_TEST' )
  print ( '  R8TO_MV computes b=A*x, where A is an R8TO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8to_random ( n )

  r8to_print ( n, a, '  The Toeplitz matrix:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  x: ' )

  b = r8to_mv ( n, a, x )
  r8vec_print ( n, b, '  b = A*x:' )

  return

def r8to_print ( n, a, title ):

#*****************************************************************************80
#
## R8TO_PRINT prints a R8TO matrix.
#
#  Discussion:
#
#    The R8TO storage format is used for a Toeplitz matrix, which is constant
#    along diagonals.  Thus, in an N by N Toeplitz matrix, there are at most 
#    2*N-1 distinct entries.  The format stores the N elements of the first
#    row, followed by the N-1 elements of the first column (skipping the
#    entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
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
#    real A(2*N-1), the R8TO matrix.
#
#    string TITLE, a title to be printed.
#
  r8to_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return

def r8to_print_test ( ):

#*****************************************************************************80
#
## R8TO_PRINT_TEST tests R8TO_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8TO_PRINT_TEST' )
  print ( '  R8TO_PRINT prints a R8TO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8to_indicator ( n )

  r8to_print ( n, a, '  The R8TO matrix:' )

  return

def r8to_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8TO_PRINT_SOME prints some of a R8TO matrix.
#
#  Discussion:
#
#    The R8TO storage format is used for a Toeplitz matrix, which is constant
#    along diagonals.  Thus, in an N by N Toeplitz matrix, there are at most 
#    2*N-1 distinct entries.  The format stores the N elements of the first
#    row, followed by the N-1 elements of the first column (skipping the
#    entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
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
#    real A(2*N-1), the R8TO matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
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
    i2hi = min ( ihi, n - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%4d  ' % ( i ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j in range ( j2lo, j2hi + 1 ):

        if ( i <= j ):
          aij = a[j-i]
        else:
          aij = a[n+i-j-1]

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8to_print_some_test ( ):

#*****************************************************************************80
#
## R8TO_PRINT_SOME_TEST tests R8TO_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'R8TO_PRINT_SOME_TEST' )
  print ( '  R8TO_PRINT_SOME prints some of a R8TO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8to_indicator ( n )

  r8to_print_some ( n, a, 2, 1, 5, 3, '  Rows2:5, Cols 1:3' )

  return

def r8to_random ( n ):

#*****************************************************************************80
#
## R8TO_RANDOM randomizes a R8TO matrix.
#
#  Discussion:
#
#    The R8TO storage format is used for a Toeplitz matrix, which is constant
#    along diagonals.  Thus, in an N by N Toeplitz matrix, there are at most 
#    2*N-1 distinct entries.  The format stores the N elements of the first
#    row, followed by the N-1 elements of the first column (skipping the
#    entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
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
#  Output:
#
#    real A(2*N-1), the R8TO matrix.
#
  from numpy.random import default_rng

  rng = default_rng ( )

  a = rng.random ( size = 2 * n - 1 )

  return a

def r8to_random_test ( ):

#*****************************************************************************80
#
## R8TO_RANDOM_TEST tests R8TO_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8TO_RANDOM_TEST' )
  print ( '  R8TO_RANDOM randomizes an R8TO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8to_random ( n )

  r8to_print ( n, a, '  The matrix:' )

  return

def r8to_sl ( n, a, b ):

#*****************************************************************************80
#
## R8TO_SL solves an R8TO system A*x=b.
#
#  Discussion:
#
#    The R8TO storage format is used for a Toeplitz matrix, which is constant
#    along diagonals.  Thus, in an N by N Toeplitz matrix, there are at most 
#    2*N-1 distinct entries.  The format stores the N elements of the first
#    row, followed by the N-1 elements of the first column (skipping the
#    entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(2*N-1), the R8TO matrix.
#
#    real B(N) the right hand side vector.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  c1 = np.zeros ( n - 1 )
  c2 = np.zeros ( n - 1 )
  x = np.zeros ( n )
#
#  Solve the system with the principal minor of order 1.
#
  r1 = a[0]
  x[0] = b[0] / r1

  if ( n == 1 ):
    return x
#
#  Recurrent process for solving the system with the Toeplitz matrix.
#
  for nsub in range ( 2, n + 1 ):
#
#  Compute multiples of the first and last columns of the inverse of
#  the principal minor of order NSUB.
#
    r5 = a[n+nsub-2]
    r6 = a[nsub-1]

    if ( 2 < nsub ):

      c1[nsub-2] = r2

      for i in range ( 1, nsub-1 ):
        r5 = r5 + a[n+i-1] * c1[nsub-i-1]
        r6 = r6 + a[i] * c2[i-1]

    r2 = - r5 / r1
    r3 = - r6 / r1
    r1 = r1 + r5 * r3

    if ( 2 < nsub ):

      r6 = c2[0]
      c2[nsub-2] = 0.0

      for i in range ( 2, nsub ):
        r5 = c2[i-1]
        c2[i-1] = c1[i-1] * r3 + r6
        c1[i-1] = c1[i-1] + r6 * r2
        r6 = r5

    c2[0] = r3
#
#  Compute the solution of the system with the principal minor of order NSUB.
#
    r5 = 0.0
    for i in range ( nsub - 1, 0, -1 ):
      r5 = r5 + a[n+nsub-i-1] * x[i-1]

    r6 = ( b[nsub-1] - r5 ) / r1

    for i in range ( 0, nsub - 1 ):
      x[i] = x[i] + c2[i] * r6
    x[nsub-1] = r6

  return x

def r8to_sl_test ( ):

#*****************************************************************************80
#
## R8TO_SL_TEST tests R8TO_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8TO_SL_TEST' )
  print ( '  R8TO_SL solves a A*x=b where A is an R8TO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8to_random ( n )

  r8to_print ( n, a, '  The Toeplitz matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8to_mv ( n, a, x )
#
#  Solve the linear system.
#
  x = r8to_sl ( n, a, b )

  r8vec_print ( n, x, '  Solution:' )

  return

def r8to_slt ( n, a, b ):

#*****************************************************************************80
#
## R8TO_SLT solves a R8TO system A'*x=b.
#
#  Discussion:
#
#    The R8TO storage format is used for a Toeplitz matrix, which is constant
#    along diagonals.  Thus, in an N by N Toeplitz matrix, there are at most 
#    2*N-1 distinct entries.  The format stores the N elements of the first
#    row, followed by the N-1 elements of the first column (skipping the
#    entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(2*N-1), the R8TO matrix.
#
#    real B(N) the right hand side vector.
#
#  Output:
#
#    real X(N), the solution vector.
#
  import numpy as np

  c1 = np.zeros ( n - 1 )
  c2 = np.zeros ( n - 1 )
  x = np.zeros ( n )
#
#  Solve the system with the principal minor of order 1.
#
  r1 = a[0]
  x[0] = b[0] / r1

  if ( n == 1 ):
    return x
#
#  Recurrent process for solving the system with the Toeplitz matrix.
#
  for nsub in range ( 2, n + 1 ):
#
#  Compute multiples of the first and last columns of the inverse of
#  the principal minor of order NSUB.
#
    r5 = a[nsub-1]
    r6 = a[n+nsub-2]
 
    if ( 2 < nsub ):

      c1[nsub-2] = r2

      for i in range ( 1, nsub - 1 ):
        r5 = r5 + a[i] * c1[nsub-i-1]
        r6 = r6 + a[n+i-1] * c2[i-1]

    r2 = - r5 / r1
    r3 = - r6 / r1
    r1 = r1 + r5 * r3

    if ( 2 < nsub ):

      r6 = c2[0]
      c2[nsub-2] = 0.0

      for i in range ( 2, nsub ):
        r5 = c2[i-1]
        c2[i-1] = c1[i-1] * r3 + r6
        c1[i-1] = c1[i-1] + r6 * r2
        r6 = r5

    c2[0] = r3
#
#  Compute the solution of the system with the principal minor of order NSUB.
#
    r5 = 0.0
    for i in range ( nsub - 1, 0, -1 ):
      r5 = r5 + a[nsub-i] * x[i-1]

    r6 = ( b[nsub-1] - r5 ) / r1

    for i in range ( 0, nsub - 1 ):
      x[i] = x[i] + c2[i] * r6
    x[nsub-1] = r6

  return x

def r8to_slt_test ( ):

#*****************************************************************************80
#
## r8to_slt_test() tests r8to_slt().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8to_slt_test' )
  print ( '  r8to_slt solves A\'*x=b where A is an R8TO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8to_random ( n )

  r8to_print ( n, a, '  The Toeplitz matrix:' )
#
#  Set the desired solution.
#
  x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
  b = r8to_mtv ( n, a, x )
#
#  Solve the linear system.
#
  x = r8to_slt ( n, a, b )

  r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8to_to_r8ge ( n, a ):

#*****************************************************************************80
#
## r8to_to_r8ge() copies a R8TO matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8TO storage format is used for a Toeplitz matrix, which is constant
#    along diagonals.  Thus, in an N by N Toeplitz matrix, there are at most 
#    2*N-1 distinct entries.  The format stores the N elements of the first
#    row, followed by the N-1 elements of the first column (skipping the
#    entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(2*N-1), the R8TO matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      b[i,j] = a[n+i-j-1]
    for j in range ( i, n ):
      b[i,j] = a[j-i]

  return b

def r8to_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8to_to_r8ge_test tests r8to_to_r8ge.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8to_to_r8ge_test' )
  print ( '  r8to_to_r8ge converts a matrix from R8TO to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a_r8to = r8to_random ( n )

  r8to_print ( n, a_r8to, '  The R8TO matrix:' )

  a_r8ge = r8to_to_r8ge ( n, a_r8to )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8to_zeros ( n ):

#*****************************************************************************80
#
## R8TO_ZEROS zeros an R8TO matrix.
#
#  Discussion:
#
#    The R8TO storage format is used for a Toeplitz matrix, which is constant
#    along diagonals.  Thus, in an N by N Toeplitz matrix, there are at most 
#    2*N-1 distinct entries.  The format stores the N elements of the first
#    row, followed by the N-1 elements of the first column (skipping the
#    entry in the first row).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
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
#  Output:
#
#    real A(2*N-1), the R8TO matrix.
#
  import numpy as np

  a = np.zeros ( 2 * n - 1 )

  return a

def r8to_zeros_test ( ):

#*****************************************************************************80
#
## R8TO_ZEROS_TEST tests R8TO_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    26 September 2015
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8TO_ZEROS_TEST' )
  print ( '  R8TO_ZEROS zeros an R8TO matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8to_zeros ( n )

  r8to_print ( n, a, '  The matrix:' )

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
  r8to_test ( )
  timestamp ( )

