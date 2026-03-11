#! /usr/bin/env python3
#
def r8utp_test ( ):

#*****************************************************************************80
#
## r8utp_test() tests r8utp().
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN)  
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8utp_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  r8utp() handles real upper triangular packed matrices.' )

  r8ge_to_r8utp_test ( )
  r8utp_det_test ( )
  r8utp_indicator_test ( )
  r8utp_print_test ( )
  r8utp_print_some_test ( )
  r8utp_random_test ( )
  r8utp_size_test ( )
  r8utp_to_r8ge_test ( )
  r8utp_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8utp_test():' )
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
  import numpy as np

  n = 13

  x = np.array ( [ 0, 1, 2, 3, 9, 10, 11, 99, 101, -1, -2, -3, -9 ] )

  print ( '' )
  print ( 'i4_log_10_test():' )
  print ( '  i4_log_10(): whole part of log base 10,' )
  print ( '' )
  print ( '  X, i4_log_10' )
  print ( '' )

  for i in range ( 0, n ):
    j = i4_log_10 ( x[i] )
    print ( '%6d  %12d' % ( x[i], j ) )

  return

def r8ge_to_r8utp ( m, n, a_ge ):

#*****************************************************************************80
#
## r8ge_to_r8utp() copies an R8GE matrix to an R8UTP matrix.
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
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
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
#    real A_UTP(*), the R8UTP matrix.
#
  import numpy as np

  a_utp = r8utp_zeros ( m, n )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a_utp[k] = a_ge[i,j]
      k = k + 1

  return a_utp

def r8ge_to_r8utp_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8utp_test() tests r8ge_to_r8utp().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
 
  m = 5
  n = 4

  print ( '' )
  print ( 'r8ge_to_r8utp_test():' )
  print ( '  r8ge_to_r8utp() converts an R8GE matrix to R8UTP format.' )

  a_ge = np.zeros ( [ m, n ] )
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      a_ge[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_ge )
 
  a_utp = r8ge_to_r8utp ( m, n, a_ge )

  r8utp_print ( m, n, a_utp, '  The R8UTP matrix:' )

  return

def r8utp_det ( m, n, a ):

#*****************************************************************************80
#
## r8utp_det() computes the determinant of an R8UTP matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN).
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
#    It must be the case that M = N.
#
#    real A(*), the R8UTP matrix.
#
#  Output:
#
#    real DET, the determinant of the matrix.
#
  if ( m != n ):
    raise Exception ( 'r8utp_det(): M != N' )

  det = 1.0
  k = 0
  for j in range ( 0, n ):
    det = det * a[k]
    k = k + j + 2

  return det

def r8utp_det_test ( ):

#*****************************************************************************80
#
## r8utp_det_test() tests r8utp_det().
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 5

  print ( '' )
  print ( 'r8utp_det_test():' )
  print ( '  r8utp_det() computes the determinant of an R8UTP matrix.' )

  a = r8utp_zeros ( m, n )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a[k] = k + 1
      k = k + 1

  r8utp_print ( m, n, a, '  The matrix A:' )
#
#  Compute the determinant.
#
  det = r8utp_det ( m, n, a )

  print ( '' )
  print ( '  Determinant is %g' % ( det ) )

  return

def r8utp_indicator ( m, n ):

#*****************************************************************************80
#
## r8utp_indicator() sets up a R8UTP indicator matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#  Output:
#
#    real A(*), the R8UTP matrix.
#
  import numpy as np

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  a = r8utp_zeros ( m, n )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a[k] = float ( fac * ( i + 1 ) + ( j + 1 ) )
      k = k + 1

  return a

def r8utp_indicator_test ( ):

#*****************************************************************************80
#
## r8utp_indicator_test() tests r8utp_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8utp_indicator_test():' )
  print ( '  r8utp_indicator() sets up an indicator matrix in R8UTP format' )
  print ( '' )
  print ( '  Matrix rows M =    %d' % ( m ) )
  print ( '  Matrix columns N = %d' % ( n ) )

  a = r8utp_indicator ( m, n )

  r8utp_print ( m, n, a, '  The indicator matrix:' )

  return

def r8utp_print ( m, n, a, title ):

#*****************************************************************************80
#
## r8utp_print() prints a R8UTP matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N: the number of rows and columns of the matrix.
#
#    real A(*), the matrix.
#
#    string TITLE, a title to be printed.
#
  r8utp_print_some ( m, n, a, 1, 1, m, n, title )

  return

def r8utp_print_test ( ):

#*****************************************************************************80
#
## r8utp_print_test() tests r8utp_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
  m = 6
  n = 4

  print ( '' )
  print ( 'r8utp_print_test():' )
  print ( '  r8utp_print() prints an R8UTP matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )

  a = r8utp_indicator ( m, n )

  r8utp_print ( m, n, a, '  The R8UTP matrix:' )

  return

def r8utp_print_some ( m, n, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8utp_print_some() prints some of an R8UTP matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N: the number of rows and columns of the matrix.
#
#    real A(*), the matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )

  if ( n <= 0 ):
    print ( '' )
    print ( '  (None)' )
    return

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
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
    i2lo = max ( ilo, 1 )
    i2hi = min ( ihi, m )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        if ( j < i ):
          print ( '              ', end = '' )
        else:
          print ( '%12g  ' % ( a[i-1+(j*(j-1))//2] ), end = '' )

      print ( '' )
      
  return

def r8utp_print_some_test ( ):

#*****************************************************************************80
#
## r8utp_print_some_test() tests r8utp_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 August 2022
#
#  Author:
#
#    John Burkardt
#
  m = 4
  n = 6

  print ( '' )
  print ( 'r8utp_print_some_test():' )
  print ( '  r8utp_print_some() prints some of an R8UTP matrix.' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )

  a = r8utp_indicator ( m, n )

  r8utp_print_some ( m, n, a, 1, 4, 3, 6, '  Some of the matrix:' )

  return

def r8utp_random ( m, n ):

#*****************************************************************************80
#
## r8utp_random() randomizes a R8UTP matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the number of rows and columns of the matrix.
#
#  Output:
#
#    real A(*), the R8UTP matrix.
#
  from numpy.random import default_rng
  import numpy as np
 
  rng = default_rng ( )

  mn = r8utp_size ( m, n )

  a = np.zeros ( mn )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a[k] = rng.random ( )
      k = k + 1

  return a

def r8utp_random_test ( ):

#*****************************************************************************80
#
## r8utp_random_test() tests r8utp_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8utp_random_test():' )
  print ( '  r8utp_random() randomizes an R8UTP matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8utp_random ( m, n )

  r8utp_print ( m, n, a, '  Matrix A:' )

  return

def r8utp_size ( m, n ):

#*****************************************************************************80
#
## r8utp_size() returns the size of an M x N R8UTP matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N: the number of rows and columns.
#
#  Output:
#
#    integer VALUE: the length of the array needed to store the matrix.
#
  if ( m > n ):
    value = n * ( n + 1 ) // 2
  elif ( m == n ):
    value = m * ( m + 1 ) // 2
  else:
    value = m * ( m + 1 ) // 2 + ( n - m ) * m

  return value

def r8utp_size_test ( ):

#*****************************************************************************80
#
## r8utp_size_test() tests r8utp_size().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'r8utp_size_test ( ):' )
  print ( '  r8utp_size() determines the size of an m x n r8utp matrix.' )
  print ( '' )
  print ( '   M   N   Size  Size(check)' )
  print ( '' )

  for m, n in ( [4, 3 ], [4, 4 ], [4, 6 ] ):
    value1 = r8utp_size ( m, n )
    value2 = 0
    for j in range ( 0, n ):
      for i in range ( 0, min ( j + 1, m ) ):
        value2 = value2 + 1
    print ( '  %2d  %2d  %2d  %2d' % ( m, n, value1, value2 ) )

  return

def r8utp_to_r8ge ( m, n, a_utp ):

#*****************************************************************************80
#
## r8utp_to_r8ge() copies an R8UTP matrix to an R8GE matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN).
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
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    real A_UTP(*), the R8UTP matrix.
#
#  Output:
#
#    real A_GE(N,N), the R8GE matrix.
#
  import numpy as np

  a_ge = np.zeros ( [ m, n ] )

  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, min ( j + 1, m ) ):
      a_ge[i,j] = a_utp[k]
      k = k + 1

  return a_ge

def r8utp_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8utp_to_r8ge_test() tests r8utp_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8utp_to_r8ge_test():' )
  print ( '  r8utp_to_r8ge() converts an R8UTP matrix to R8GE format.' )

  a_utp = r8utp_random ( m, n )

  r8utp_print ( m, n, a_utp, '  The random R8UTP matrix:' )
 
  a_ge = r8utp_to_r8ge ( m, n, a_utp )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_ge )

  return

def r8utp_zeros ( m, n ):

#*****************************************************************************80
#
## r8utp_zeros() zeroes an R8UTP matrix.
#
#  Discussion:
#
#    The R8UTP storage format is appropriate for an upper triangular
#    matrix.  Only the upper triangle of the matrix is stored,
#    by successive partial columns, in an array which contains
#    (A11,A12,A22,A13,A23,A33,A14,...,AMN).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    13 August 2022
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
#    real A(*), the matrix.
#
  import numpy as np

  value = r8utp_size ( m, n )

  a = np.zeros ( value )

  return a

def r8utp_zeros_test ( ):

#*****************************************************************************80
#
## r8utp_zeros_test() tests r8utp_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    13 August 2022
#
#  Author:
#
#    John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'r8utp_zeros_test():' )
  print ( '  r8utp_zeros() zeros out space for an R8UTP matrix.' )
  print ( '' )
  print ( '  Matrix order M, N = %d, %d' % ( m, n ) )

  a = r8utp_zeros ( m, n )

  r8utp_print ( m, n, a, '  Matrix A:' )

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

if ( __name__ == "__main__" ):
  timestamp ( )
  r8utp_test ( )
  timestamp ( )

