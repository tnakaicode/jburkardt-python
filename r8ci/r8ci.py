#! /usr/bin/env python3
#
def r8ci_test ( ):

#*****************************************************************************80
#
## r8ci_test() tests r8ci().
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
  print ( 'r8ci_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8ci().' )

  r8ci_det_test ( )
  r8ci_dif2_test ( )
  r8ci_eval_test ( )
  r8ci_indicator_test ( )
  r8ci_mtv_test ( )
  r8ci_mv_test ( )
  r8ci_print_test ( )
  r8ci_print_some_test ( )
  r8ci_random_test ( )
  r8ci_sl_test ( )
  r8ci_to_r8ge_test ( )
  r8ci_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8ci_test():' )
  print ( '  Normal end of execution.' )
  return

def c8_le_l2 ( c1, c2 ):

#*****************************************************************************80
#
## c8_le_l2() := C1 <= C1 for C8's, and the L2 norm.
#
#  Discussion:
#
#    The L2 norm can be defined here as:
#
#      c8_norm_l2(C) = sqrt ( ( real (C) ) ^ 2 + abs ( imag (C) ) ^ 2 )
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
#  Input:
#
#    complex C1, C2, the values to be compared.
#
#  Output:
#
#    bool VALUE, is TRUE if C1 <= C2.
#
  if ( c1.real ** 2 + c1.imag ** 2 <= c2.real ** 2 + c2.imag ** 2 ) :
    value = True
  else:
    value = False

  return value

def c8vec_print ( n, a, title ):

#*****************************************************************************80
#
## c8vec_print() prints a C8VEC.
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
#  Input:
#
#    integer N, the dimension of the vector.
#
#    complex A(N), the vector to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '%6d  %12g  %12g' % ( i, a.real[i], a.imag[i] ) )

  return

def c8vec_sort_a_l2 ( n, x ):

#*****************************************************************************80
#
## c8vec_sort_a_l2() ascending sorts a C8VEC by L2 norm.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    28 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of entries in the array.
#
#    complex X(N), an unsorted array.
#
#  Output:
#
#    complex X(N), the sorted array.
#
  if ( 1 < n ):

    i = 0
    indx = 0
    isgn = 0
    j = 0
    i_save = 0
    j_save = 0
    k_save = 0
    l_save = 0
    n_save = 0

    while ( True ):

      [ indx, i, j, i_save, j_save, k_save, l_save, n_save ] = sort_safe_rc ( \
        n, indx, isgn, i_save, j_save, k_save, l_save, n_save )

      if ( 0 < indx ):

        temp = x[i-1]
        x[i-1] = x[j-1]
        x[j-1] = temp

      elif ( indx < 0 ):

        if ( c8_le_l2 ( x[i-1], x[j-1] ) ):
          isgn = -1
        else:
          isgn = +1

      elif ( indx == 0 ):

        break

  return x

def c8vec_unity ( n ):

#*****************************************************************************80
#
## c8vec_unity() returns the N roots of unity.
#
#  Discussion:
#
#    X(1:N) = exp ( 2 * PI * (0:N-1) / N )
#
#    X(1:N)^N = ( (1,0), (1,0), ..., (1,0) ).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of elements.
#
#  Output:
#
#    complex A(N), the array.
#
  import numpy as np

  a = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    t = 2.0 * np.pi * float ( i ) / float ( n )
    a[i] = np.cos ( t ) + 1j * np.sin ( t )

  return a

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

def r8ci_det ( n, a ):

#*****************************************************************************80
#
## R8CI_DET returns the determinant of an R8CI matrix.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8CI matrix.
#
#  Output:
#
#    real DET, the determinant.
#
  import numpy as np

  w = c8vec_unity ( n )

  lam = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    lam[i] = a[n-1]

  for i in range ( n - 2, -1, -1 ):
    for j in range ( 0, n ):
      lam[j] = lam[j] * w[j] + a[i]

  detc = 1.0 + 0j
  for i in range ( 0, n ):
    detc = detc * lam[i]
#
#  DETC should be real, but we need to copy it into a real variable.
#
  det = detc.real

  return det

def r8ci_det_test ( ):

#*****************************************************************************80
#
## R8CI_DET_TEST tests R8CI_DET.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8CI_DET_TEST' )
  print ( '  R8CI_DET finds the determinant of a real circulant system.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8ci_random ( n )

  r8ci_print ( n, a, '  The circulant matrix:' )

  det = r8ci_det ( n, a )

  print ( '' )
  print ( '  Computed determinant = ', det )

  return

def r8ci_dif2 ( n ):

#*****************************************************************************80
#
## R8CI_DIF2 sets up a R8CI second difference matrix.
#
#  Discussion:
#
#    This is actually a periodic second difference matrix.
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
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
#    real A(N), the R8CI matrix.
#
  import numpy as np

  a = np.zeros ( n )

  a[0] = 2.0
  a[1] = -1.0
  a[n-1] = -1.0

  return a

def r8ci_dif2_test ( ):

#*****************************************************************************80
#
## R8CI_DIF2_TEST tests R8CI_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8CI_DIF2_TEST' )
  print ( '  R8CI_DIF2 sets up an R8CI periodic second difference matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8ci_dif2 ( n )

  r8ci_print ( n, a, '  The R8CI periodic second difference matrix:' )

  return

def r8ci_eval ( n, a ):

#*****************************************************************************80
#
## R8CI_EVAL returns the eigenvalues of a R8CI matrix.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Philip Davis,
#    Circulant Matrices,
#    Wiley, 1979.
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8CI matrix.
#
#  Output:
#
#    complex LAMBDA(N), the eigenvalues.
#
  import numpy as np

  w = c8vec_unity ( n )

  lam = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    lam[i] = a[n-1]

  for i in range ( n - 2, -1, -1 ):
    for j in range ( 0, n ):
      lam[j] = lam[j] * w[j] + a[i]

  lam = c8vec_sort_a_l2 ( n, lam )

  return lam

def r8ci_eval_test ( ):

#*****************************************************************************80
#
## R8CI_EVAL_TEST tests R8CI_EVAL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8CI_EVAL_TEST' )
  print ( '  R8CI_EVAL finds the eigenvalues of' )
  print ( '  a real circulant system.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8ci_random ( n )

  r8ci_print ( n, a, '  The circulant matrix:' )

  lam = r8ci_eval ( n, a )

  c8vec_print ( n, lam, '  The eigenvalues:' )

  return

def r8ci_indicator ( n ):

#*****************************************************************************80
#
## R8CI_INDICATOR sets up a R8CI indicator matrix.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
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
#    real A(N), the R8CI matrix.
#
  import numpy as np

  a = np.zeros ( n )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for j in range ( 0, n ):
    a[j] = float ( fac * 1 + j + 1 )

  return a

def r8ci_indicator_test ( ):

#*****************************************************************************80
#
## R8CI_INDICATOR_TEST tests R8CI_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8CI_INDICATOR_TEST' )
  print ( '  R8CI_INDICATOR sets up a R8CI indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8ci_indicator ( n )

  r8ci_print ( n, a, '  The R8CI indicator matrix:' )

  return

def r8ci_mtv ( n, a, x ):

#*****************************************************************************80
#
## R8CI_MTV multiplies a vector by a R8CI matrix.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The R8CI format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8CI matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A' * X.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 1, n + 1 ):
    for j in range ( 1, i + 1 ):
      b[i-1] = b[i-1] + a[i+1-j-1] * x[j-1]
    for j in range ( i + 1, n + 1 ):
      b[i-1] = b[i-1] + a[n+i+1-j-1] * x[j-1]

  return b

def r8ci_mtv_test ( ):

#*****************************************************************************80
#
## R8CI_MTV_TEST tests R8CI_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8CI_MTV_TEST' )
  print ( '  R8CI_MTV computes b=A''*x where A is an R8CI indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8ci_indicator ( n )
  r8ci_print ( n, a, '  The R8CI matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  The vector x:' )

  b = r8ci_mtv ( n, a, x )
  r8vec_print ( n, b, '  The product b=A''*x:' )

  return

def r8ci_mv ( n, a, x ):

#*****************************************************************************80
#
## R8CI_MV multiplies a R8CI matrix times a vector.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8CI matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * x.
#
  import numpy as np

  b = np.zeros ( n )

  for i in range ( 1, n + 1 ):
    for j in range ( 1, i ):
      b[i-1] = b[i-1] + a[n+j+1-i-1] * x[j-1]
    for j in range ( i, n + 1 ):
      b[i-1] = b[i-1] + a[j+1-i-1] * x[j-1]

  return b

def r8ci_mv_test ( ):

#*****************************************************************************80
#
## R8CI_MV_TEST tests R8CI_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8CI_MV_TEST' )
  print ( '  R8CI_MV computes b=A*x where A is an R8CI indicator matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8ci_indicator ( n )
  r8ci_print ( n, a, '  The R8CI matrix A:' )

  x = r8vec_indicator1 ( n )
  r8vec_print ( n, x, '  The vector x:' )

  b = r8ci_mv ( n, a, x )
  r8vec_print ( n, b, '  The product b=A*x:' )

  return

def r8ci_print ( n, a, title ):

#*****************************************************************************80
#
## R8CI_PRINT prints a R8CI matrix.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The R8CI format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
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
#    real A(N), the R8CI matrix.
#
#    string TITLE, a title to be printed.
#
  r8ci_print_some ( n, a, 0, 0, n - 1, n - 1, title )

  return

def r8ci_print_test ( ):

#*****************************************************************************80
#
## R8CI_PRINT_TEST tests R8CI_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8CI_PRINT_TEST' )
  print ( '  R8CI_PRINT prints an R8CI matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8ci_indicator ( n )

  r8ci_print ( n, a, '  The R8CI matrix:' )

  return

def r8ci_print_some ( n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8CI_PRINT_SOME prints some of a R8CI matrix.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
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
#    real A(N), the R8CI matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  incx = 5

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
    i2hi = min ( ihi, n - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):

        if ( i <= j ):
          aij = a[j-i]
        else:
          aij = a[n+j-i]
 
        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8ci_print_some_test ( ):

#*****************************************************************************80
#
## R8CI_PRINTS_SOME_TEST tests R8CI_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'R8CI_PRINT_SOME_TEST' )
  print ( '  R8CI_PRINT_SOME prints some of an R8CI matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8ci_indicator ( n )

  r8ci_print_some ( n, a, 2, 3, 6, 5, '  Rows 2-6, Cols 3-5:' )

  return

def r8ci_random ( n ):

#*****************************************************************************80
#
## r8ci_random() randomizes a R8CI matrix.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The R8CI format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
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
#    real A(N), the R8CI matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( n )

  for i in range ( 0, n ):
    a[i] = rng.uniform ( )

  return a

def r8ci_random_test ( ):

#*****************************************************************************80
#
## r8ci_random_test() tests r8ci_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8ci_random_test():' )
  print ( '  r8ci_random() computes a random R8CI matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8ci_random ( n )

  r8ci_print ( n, a, '  The random R8CI matrix:' )

  return

def r8ci_sl ( n, a, b, job ):

#*****************************************************************************80
#
## R8CI_SL solves a R8CI system.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The R8CI format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8CI matrix.
#
#    real B(N), the right hand side.
#
#    integer JOB, specifies the system to solve.
#    0, solve A * x = b.
#    nonzero, solve A' * x = b.
#
#  Output:
#
#    real X(N), the solution of the linear system.
#
  import numpy as np

  x = np.zeros ( n )
  work = np.zeros ( 2 * n - 2 )

  if ( job == 0 ):
#
#  Solve the system with the principal minor of order 1.
#
    r1 = a[0]
    x[0] = b[0] / r1

    r2 = 0.0
#
#  Recurrent process for solving the system.
#
    for nsub in range ( 2, n + 1 ):
#
#  Compute multiples of the first and last columns of
#  the inverse of the principal minor of order N.
#
      r5 = a[n+2-nsub-1]
      r6 = a[nsub-1]

      if ( 2 < nsub ):

        work[nsub-2] = r2

        for i in range ( 1, nsub - 1 ):
          r5 = r5 + a[n-i] * work[nsub-i-1]
          r6 = r6 + a[i] * work[n-2+i]

      r2 = - r5 / r1
      r3 = - r6 / r1
      r1 = r1 + r5 * r3

      if ( 2 < nsub ):

        r6 = work[n-1]
        work[n+nsub-3] = 0.0
        for i in range ( 2, nsub ):
          r5 = work[n-2+i]
          work[n-2+i] = work[i-1] * r3 + r6
          work[i-1] = work[i-1] + r6 * r2
          r6 = r5

      work[n-1] = r3
#
#  Compute the solution of the system with the principal minor of order NSUB.
#
      r5 = 0.0
      for i in range ( 1, nsub ):
        r5 = r5 + a[n-i] * x[nsub-i-1]

      r6 = ( b[nsub-1] - r5 ) / r1
      for i in range ( 1, nsub ):
        x[i-1] = x[i-1] + work[n+i-2] * r6
      x[nsub-1] = r6

  else:
#
#  Solve the system with the principal minor of order 1.
#
    r1 = a[0]
    x[0] = b[0] / r1

    r2 = 0.0
#
#  Recurrent process for solving the system.
#
    for nsub in range ( 2, n + 1 ):
#
#  Compute multiples of the first and last columns of
#  the inverse of the principal minor of order N.
#
      r5 = a[nsub-1]
      r6 = a[n+1-nsub]

      if ( 2 < nsub ):

        work[nsub-2] = r2

        for i in range ( 1, nsub - 1 ):
          r5 = r5 + a[i] * work[nsub-i-1]
          r6 = r6 + a[n-i] * work[n-2+i]

      r2 = - r5 / r1
      r3 = - r6 / r1
      r1 = r1 + r5 * r3

      if ( 2 < nsub ):

        r6 = work[n-1]
        work[n+nsub-3] = 0.0
        for i in range ( 2, nsub ):
          r5 = work[n-2+i]
          work[n-2+i] = work[i-1] * r3 + r6
          work[i-1] = work[i-1] + r6 * r2
          r6 = r5

      work[n-1] = r3
#
#  Compute the solution of the system with the principal minor of order NSUB.
#
      r5 = 0.0
      for i in range ( 1, nsub ):
        r5 = r5 + a[i] * x[nsub-i-1]

      r6 = ( b[nsub-1] - r5 ) / r1
      for i in range ( 1, nsub ):
        x[i-1] = x[i-1] + work[n-2+i] * r6

      x[nsub-1] = r6

  return x

def r8ci_sl_test ( ):

#*****************************************************************************80
#
## R8CI_SL_TEST tests R8CI_SL.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 10

  print ( '' )
  print ( 'R8CI_SL_TEST' )
  print ( '  R8CI_SL solves a circulant system.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  a = r8ci_random ( n )

  r8ci_print ( n, a, '  The circulant matrix:' )

  for job in range ( 0, 2 ):
#
#  Set the desired solution.
#
    x = r8vec_indicator1 ( n )
#
#  Compute the corresponding right hand side.
#
    if ( job == 0 ):
      b = r8ci_mv ( n, a, x )
    else:
      b = r8ci_mtv ( n, a, x )
#
#  Solve the linear system.
#
    x = r8ci_sl ( n, a, b, job )

    if ( job == 0 ):
      r8vec_print ( n, x, '  Solution:' )
    else:
      r8vec_print ( n, x, '  Solution to transposed system:' )

  return

def r8ci_to_r8ge ( n, a ):

#*****************************************************************************80
#
## R8CI_TO_R8GE copies a R8CI matrix into a R8GE matrix.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The R8CI format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    real A(N), the R8CI matrix.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( 0, i ):
      b[i,j] = a[n+j-i]
    for j in range ( i, n ):
      b[i,j] = a[j-i]

  return b

def r8ci_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8CI_TO_R8GE_TEST tests R8CI_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8CI_TO_R8GE_TEST' )
  print ( '  R8CI_TO_R8GE converts an R8CI matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8ci_indicator ( n )
  r8ci_print ( n, a, '  The R8CI matrix:' )

  a_r8ge = r8ci_to_r8ge ( n, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8ci_zeros ( n ):

#*****************************************************************************80
#
## R8CI_ZEROS zeros an R8CI matrix.
#
#  Discussion:
#
#    The R8CI storage format is used for an N by N circulant matrix.
#    An N by N circulant matrix A has the property that the entries on
#    row I appear again on row I+1, shifted one position to the right,
#    with the final entry of row I appearing as the first of row I+1.
#    The R8CI format simply records the first row of the matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
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
#    real A(N), the R8CI matrix.
#
  import numpy as np

  a = np.zeros ( n )

  return a

def r8ci_zeros_test ( ):

#*****************************************************************************80
#
## R8CI_ZEROS_TEST tests R8CI_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    18 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8CI_ZEROS_TEST' )
  print ( '  R8CI_ZEROS zeros an R8CI matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  a = r8ci_zeros ( n )

  r8ci_print ( n, a, '  The zero R8CI matrix:' )

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

def sort_safe_rc ( n, indx, isgn, i_save, j_save, k_save, l_save, n_save ):

#*****************************************************************************80
#
## sort_safe_rc() externally sorts a list of items into ascending order.
#
#  Discussion:
#
#    This is a version of SORT_RC which does not rely on
#    storing certain work variables internally to the function.  This makes
#    the function somewhat more awkward to call, but easier to program
#    in a variety of languages, and safe to use in a parallel programming
#    environment, or in cases where the sorting of several vectors is to
#    be carried out at more or less the same time.
#
#    The actual list of data is not passed to the routine.  Hence this
#    routine may be used to sort integers, reals, numbers, names,
#    dates, shoe sizes, and so on.  After each call, the routine asks
#    the user to compare or interchange two items, until a special
#    return value signals that the sorting is completed.
#
#  Example:
#
#    n = 100
#    indx = 0
#    isgn = 0
#    i_save = 0
#    j_save = 0
#    k_save = 0
#    l_save = 0
#    n_save = 0
#
#    while ( 1 )
#
#      indx, i, j, i_save, j_save, k_save, l_save, n_save = 
#        sort_safe_rc ( n, indx, isgn, i_save, j_save, k_save, l_save, n_save )
#
#      if ( indx < 0 )
#
#        isgn = 1
#        if ( a(i) <= a(j) )
#          isgn = -1
#        end
#
#      elseif ( 0 < indx )
#
#        k    = a(i)
#        a(i) = a(j)
#        a(j) = k
#
#      else
#
#        break
#
#      end
#
#    end
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    Original FORTRAN77 version by Albert Nijenhuis, Herbert Wilf.
#    This version by John Burkardt
#
#  Reference:
#
#    Albert Nijenhuis, Herbert Wilf.
#    Combinatorial Algorithms,
#    Academic Press, 1978, second edition,
#    ISBN 0-12-519260-6.
#
#  Input:
#
#    integer N, the number of items to be sorted.
#
#    integer INDX, the main communication signal.
#    The user must set INDX to 0 before the first call.
#    Thereafter, the user should set the input value of INDX
#    to the output value from the previous call.
#
#    integer ISGN, results of comparison of elements I and J.
#    (Used only when the previous call returned INDX less than 0).
#    ISGN <= 0 means I is less than or equal to J
#    0 <= ISGN means I is greater than or equal to J.
#
#    integer I_SAVE, J_SAVE, K_SAVE, L_SAVE, N_SAVE, workspace 
#    needed by the routine.  Before calling the function,
#    the user should declare variables to hold these values, but should
#    not change them, and need not ever examine them.
#
#  Output:
#
#    integer INDX, the main communication signal.
#    If INDX is
#    * greater than 0, the user should:
#      interchange items I and J
#      call again.
#    * less than 0, the user should:
#      compare items I and J
#      set ISGN = -1 if I < J, ISGN = +1 if J < I
#      call again.
#    * equal to 0, the sorting is done.
#
#    integer I, J, the indices of two items.
#    On return with INDX positive, elements I and J should be interchanged.
#    On return with INDX negative, elements I and J should be compared, and
#    the result reported in ISGN on the next call.
#
#    integer I_SAVE, J_SAVE, K_SAVE, L_SAVE, N_SAVE, updated information.
#

#
#  INDX = 0: This is the first call.
#
  if ( indx == 0 ):
      
    k_save = ( n // 2 )
    l_save = k_save
    n_save = n
#
#  INDX < 0: The user is returning the results of a comparison.
#
  elif ( indx < 0 ):

    if ( indx == -2 ):

      if ( isgn < 0 ):
        i_save = i_save + 1

      j_save = l_save
      l_save = i_save
      indx = -1
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save
 
    if ( 0 < isgn ):
      indx = 2
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save

    if ( k_save <= 1 ):

      if ( n_save == 1 ):
        i_save = 0
        j_save = 0
        indx = 0
      else:
        i_save = n_save
        n_save = n_save - 1
        j_save = 1
        indx = 1

      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save

    k_save = k_save - 1
    l_save = k_save
#
#  0 < INDX, the user was asked to make an interchange.
#
  elif ( indx == 1 ):

    l_save = k_save

  while ( True ):

    i_save = 2 * l_save

    if ( i_save == n_save ):
      j_save = l_save
      l_save = i_save
      indx = -1
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save
    elif ( i_save <= n_save ):
      j_save = i_save + 1
      indx = -2
      i = i_save
      j = j_save
      return indx, i, j, i_save, j_save, k_save, l_save, n_save

    if ( k_save <= 1 ):
      break

    k_save = k_save - 1
    l_save = k_save

  if ( n_save == 1 ):
    i_save = 0
    j_save = 0
    indx = 0
    i = i_save
    j = j_save
  else:
    i_save = n_save
    n_save = n_save - 1
    j_save = 1
    indx = 1
    i = i_save
    j = j_save

  return indx, i, j, i_save, j_save, k_save, l_save, n_save

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
  r8ci_test ( )
  timestamp ( )
 
