#! /usr/bin/env python3
#
def r8ncf_test ( ):

#*****************************************************************************80
#
## r8ncf_test() tests r8ncf().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    24 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8ncf_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8ncf().' )

  r8ncf_dif2_test ( )
  r8ncf_indicator_test ( )
  r8ncf_mtv_test ( )
  r8ncf_mv_test ( )
  r8ncf_print_test ( )
  r8ncf_random_test ( )
  r8ncf_to_r8ge_test ( )
  r8ncf_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8ncf_test():' )
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

def r8ncf_dif2 ( m, n, nz_num, rowcol ):

#*****************************************************************************80
#
## R8NCF_DIF2 sets up an R8NCF second difference matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the number of rows and columns in
#    the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer ROWCOL(2,NZ_NUM), the coordinates of 
#    the nonzero entries.
#
#  Output:
#
#    real A(NZ_NUM), the matrix.
#
  import numpy as np

  a = np.zeros ( nz_num )

  for k in range ( 0, nz_num ):
    i = rowcol[0,k]
    j = rowcol[1,k]
    if ( j == i - 1 ):
      a[k] = -1.0
    elif ( j == i ):
      a[k] = 2.0
    elif ( j == i + 1 ):
      a[k] = -1.0

  return a

def r8ncf_dif2_nz_num ( m, n ):

#*****************************************************************************80
#
## R8NCF_DIF2_NZ_NUM counts nonzeros in an R8NCF second difference matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the number of rows and columns in
#    the matrix.
#
#  Output:
#
#    integer NZ_NUM, the number of nonzero entries.
#
  if ( m < n ):
    nz_num = 3 * m - 1
  elif ( m == n ):
    nz_num = 3 * n - 2
  else:
    nz_num = 3 * n - 1

  return nz_num

def r8ncf_dif2_rowcol ( m, n, nz_num ):

#*****************************************************************************80
#
## R8NCF_DIF2_ROWCOL sets indexing for an R8NCF second difference matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the number of rows and columns in
#    the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#  Output:
#
#    integer ROWCOL(2,NZ_NUM), the coordinates of 
#    the nonzero entries.
#
  import numpy as np

  rowcol = np.zeros ( [ 2, nz_num ], dtype = np.int32 )

  k = 0

  for i in range ( 0, m ):

    j = i - 1
    if ( 0 <= j and j < n ):
      rowcol[0,k] = i
      rowcol[1,k] = j
      k = k + 1

    j = i
    if ( j < n ):
      rowcol[0,k] = i
      rowcol[1,k] = j
      k = k + 1

    j = i + 1
    if ( j < n ):
      rowcol[0,k] = i
      rowcol[1,k] = j
      k = k + 1

  return rowcol

def r8ncf_dif2_test ( ):

#*****************************************************************************80
#
## R8NCF_DIF2_TEST tests R8NCF_DIF2.
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
#   John Burkardt
#
  m = 7
  n = 5

  print ( '' )
  print ( 'R8NCF_DIF2_TEST' )
  print ( '  R8NCF_DIF2 sets up a R8NCF second difference matrix' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )

  nz_num = r8ncf_dif2_nz_num ( m, n )

  print ( '  Matrix nonzeros =  ', nz_num )

  rowcol = r8ncf_dif2_rowcol ( m, n, nz_num )

  a = r8ncf_dif2 ( m, n, nz_num, rowcol )

  r8ncf_print ( m, n, nz_num, rowcol, a, '  The R8NCF matrix:' )

  return

def r8ncf_indicator ( m, n, nz_num, rowcol ):

#*****************************************************************************80
#
## R8NCF_INDICATOR sets up a R8NCF indicator matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROWCOL(2,NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#  Output:
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
  import numpy as np

  a = np.zeros ( nz_num )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for k in range ( 0, nz_num ):

    i = rowcol[0,k]
    j = rowcol[1,k]
    a[k] = float ( fac * ( i + 1 ) +  ( j + 1 ) )

  return a

def r8ncf_indicator_test ( ):

#*****************************************************************************80
#
## R8NCF_INDICATOR_TEST tests R8NCF_INDICATOR.
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
#   John Burkardt
#
  import numpy as np

  m = 5
  n = 7
  nz_num = 15

  rowcol = np.array ( [ \
    [ 0, 1, 2, 3, 4, 1, 4, 0, 4, 0, 1, 2, 3, 3, 0 ], \
    [ 0, 1, 2, 3, 4, 0, 0, 1, 1, 3, 3, 3, 4, 5, 6 ] ] )

  print ( '' )
  print ( 'R8NCF_INDICATOR_TEST' )
  print ( '  R8NCF_INDICATOR sets up a R8NCF indicator matrix' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
  print ( '  Matrix nonzeros =  ', nz_num )

  a = r8ncf_indicator ( m, n, nz_num, rowcol )

  r8ncf_print ( m, n, nz_num, rowcol, a, '  The R8NCF indicator matrix:' )

  return

def r8ncf_mtv ( m, n, nz_num, rowcol, a, x ):

#*****************************************************************************80
#
## R8NCF_MTV multiplies an R8VEC times an R8NCF matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in
#    the matrix.
#
#    integer ROWCOL(2,NZ_NUM), the row and column
#    indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    real X(M), the vector to be multiplied by A'.
#
#  Output:
#
#    real B(N), the product A' * x.
#
  import numpy as np

  b = np.zeros ( n )

  for k in range ( 0, nz_num ):
    i = rowcol[1,k]
    j = rowcol[0,k]
    b[i] = b[i] + a[k] * x[j]

  return b

def r8ncf_mtv_test ( ):

#*****************************************************************************80
#
## R8NCF_MTV_TEST tests R8NCF_MTV.
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
#   John Burkardt
#
  m = 5
  n = 7

  print ( '' )
  print ( 'R8NCF_MTV_TEST' )
  print ( '  R8NCF_MTV computes b=A\'*x, where A is an R8NCF matrix' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )

  nz_num = r8ncf_dif2_nz_num ( m, n )

  print ( '  Matrix nonzeros =  ', nz_num )

  rowcol = r8ncf_dif2_rowcol ( m, n, nz_num )

  a = r8ncf_dif2 ( m, n, nz_num, rowcol )

  r8ncf_print ( m, n, nz_num, rowcol, a, '  The R8NCF matrix:' )

  x = r8vec_indicator1 ( m )

  r8vec_print ( m, x, '  x:' )

  b = r8ncf_mtv ( m, n, nz_num, rowcol, a, x )

  r8vec_print ( n, b, '  b=A\'*x:' )

  return

def r8ncf_mv ( m, n, nz_num, rowcol, a, x ):

#*****************************************************************************80
#
## R8NCF_MV multiplies an R8NCF matrix by an R8VEC.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the order of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in 
#    the matrix.
#
#    integer ROWCOL(2,NZ_NUM), the row and column 
#    indices of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(M), the product A * x.
#
  import numpy as np

  b = np.zeros ( m )

  for k in range ( 0, nz_num ):
    i = rowcol[0,k]
    j = rowcol[1,k]
    b[i] = b[i] + a[k] * x[j]

  return b

def r8ncf_mv_test ( ):

#*****************************************************************************80
#
## R8NCF_MV_TEST tests R8NCF_MV.
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
#   John Burkardt
#
  m = 5
  n = 4

  print ( '' )
  print ( 'R8NCF_MV_TEST' )
  print ( '  R8NCF_MV computes b=A*x, where A is an R8NCF matrix' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )

  nz_num = r8ncf_dif2_nz_num ( m, n )

  print ( '  Matrix nonzeros =  ', nz_num )

  rowcol = r8ncf_dif2_rowcol ( m, n, nz_num )

  a = r8ncf_dif2 ( m, n, nz_num, rowcol )

  r8ncf_print ( m, n, nz_num, rowcol, a, '  The R8NCF matrix:' )

  x = r8vec_indicator1 ( n )

  r8vec_print ( n, x, '  x:' )

  b = r8ncf_mv ( m, n, nz_num, rowcol, a, x )

  r8vec_print ( m, b, '  b=A*x:' )

  return

def r8ncf_print ( m, n, nz_num, rowcol, a, title ):

#*****************************************************************************80
#
## R8NCF_PRINT prints a R8NCF matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROWCOL(2,NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    string TITLE, a title.
#
  r8ncf_print_some ( m, n, nz_num, rowcol, a, 0, 0, m - 1, n - 1, title )

  return

def r8ncf_print_test ( ):

#*****************************************************************************80
#
## R8NCF_PRINT_TEST tests R8NCF_PRINT.
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
#   John Burkardt
#
  import numpy as np

  m = 5
  n = 7
  nz_num = 15

  rowcol = np.array ( [ \
    [ 0, 1, 2, 3, 4, 1, 4, 0, 4, 0, 1, 2, 3, 3, 0 ], \
    [ 0, 1, 2, 3, 4, 0, 0, 1, 1, 3, 3, 3, 4, 5, 6 ] ] )

  print ( '' )
  print ( 'R8NCF_PRINT_TEST' )
  print ( '  R8NCF_PRINT prints an R8NCF matrix' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
  print ( '  Matrix nonzeros =  ', nz_num )

  a = r8ncf_indicator ( m, n, nz_num, rowcol )

  r8ncf_print ( m, n, nz_num, rowcol, a, '  The R8NCF indicator matrix:' )

  return

def r8ncf_print_some ( m, n, nz_num, rowcol, a, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8NCF_PRINT_SOME prints some of a R8NCF matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROWCOL(2,NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  import numpy as np

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

      arow = np.zeros ( n )

      for k in range ( 0, nz_num ):
        if ( rowcol[0,k] == i ):
          j = rowcol[1,k]
          arow[j] = arow[j] + a[k]

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):
        print ( '%12g  ' % ( arow[j] ), end = '' )

      print ( '' )

  return

def r8ncf_print_some_test ( ):

#*****************************************************************************80
#
## R8NCF_PRINT_SOME_TEST tests R8NCF_PRINT_SOME.
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
#   John Burkardt
#
  import numpy as np

  m = 5
  n = 7
  nz_num = 15

  rowcol = np.array ( [ \
    [ 0, 1, 2, 3, 4, 1, 4, 0, 4, 0, 1, 2, 3, 3, 0 ], \
    [ 0, 1, 2, 3, 4, 0, 0, 1, 1, 3, 3, 3, 4, 5, 6 ] ] )

  print ( '' )
  print ( 'R8NCF_PRINT_SOME_TEST' )
  print ( '  R8NCF_PRINT_SOME prints some of an R8NCF matrix' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
  print ( '  Matrix nonzeros =  ', nz_num )

  a = r8ncf_indicator ( m, n, nz_num, rowcol )

  r8ncf_print_some ( m, n, nz_num, rowcol, a, 0, 1, 4, 3, \
    '  Rows 0-4, Cols 1-3:' )

  return

def r8ncf_random ( m, n, nz_num, rowcol ):

#*****************************************************************************80
#
## R8NCF_RANDOM randomizes an R8NCF matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the number of rows and columns in
#    the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer ROWCOL(2,NZ_NUM), the coordinates of 
#    the nonzero entries.
#
#  Output:
#
#    real A(NZ_NUM), the indicator matrix.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  a = np.zeros ( nz_num )

  for k in range ( 0, nz_num ):
    i = rowcol[0,k]
    j = rowcol[1,k]
    a[k] = rng.random ( )

  return a

def r8ncf_random_test ( ):

#*****************************************************************************80
#
## r8ncf_random_test() tests r8ncf_random().
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
#   John Burkardt
#
  import numpy as np

  m = 5
  n = 7
  nz_num = 15

  rowcol = np.array ( [ \
    [ 0, 1, 2, 3, 4, 1, 4, 0, 4, 0, 1, 2, 3, 3, 0 ], \
    [ 0, 1, 2, 3, 4, 0, 0, 1, 1, 3, 3, 3, 4, 5, 6 ] ] )

  print ( '' )
  print ( 'R8NCF_RANDOM_TEST' )
  print ( '  R8NCF_RANDOM randomizes an R8NCF matrix' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
  print ( '  Matrix nonzeros =  ', nz_num )

  a = r8ncf_random ( m, n, nz_num, rowcol )

  r8ncf_print ( m, n, nz_num, rowcol, a, '  The R8NCF random matrix:' )

  return

def r8ncf_to_r8ge ( m, n, nz_num, rowcol, a ):

#*****************************************************************************80
#
## R8NCF_TO_R8GE converts an R8NCF matrix to R8GE format.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the number of rows and columns in
#    the matrix.
#
#    integer NZ_NUM, the number of nonzero entries.
#
#    integer ROWCOL(2,NZ_NUM), the coordinates of 
#    the nonzero entries.
#
#    real A(NZ_NUM), the matrix.
#
#  Output:
#
#    real A_R8GE(M,N), the R8GE matrix.
#
  import numpy as np

  a_r8ge = np.zeros ( [ m, n ] )

  for k in range ( 0, nz_num ):
    i = rowcol[0,k]
    j = rowcol[1,k]
    a_r8ge[i,j] = a_r8ge[i,j] + a[k]

  return a_r8ge

def r8ncf_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8NCF_TO_R8GE_TEST tests R8NCF_TO_R8GE.
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
#   John Burkardt
#
  import numpy as np

  m = 5
  n = 7
  nz_num = 15

  rowcol = np.array ( [ \
    [ 0, 1, 2, 3, 4, 1, 4, 0, 4, 0, 1, 2, 3, 3, 0 ], \
    [ 0, 1, 2, 3, 4, 0, 0, 1, 1, 3, 3, 3, 4, 5, 6 ] ] )

  print ( '' )
  print ( 'R8NCF_TO_R8GE_TEST' )
  print ( '  R8NCF_TO_R8GE converts an R8NCF matrix to R8GE format' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
  print ( '  Matrix nonzeros =  ', nz_num )

  a = r8ncf_indicator ( m, n, nz_num, rowcol )

  r8ncf_print ( m, n, nz_num, rowcol, a, '  The R8NCF matrix:' )

  a_r8ge = r8ncf_to_r8ge ( m, n, nz_num, rowcol, a )

  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8ncf_zeros ( m, n, nz_num, rowcol ):

#*****************************************************************************80
#
## R8NCF_ZEROS zeros an R8NCF matrix.
#
#  Discussion:
#
#    The R8NCF storage format stores NZ_NUM, the number of nonzeros, 
#    a real array containing the nonzero values, a 2 by NZ_NUM integer 
#    array storing the row and column of each nonzero entry.
#
#    The R8NCF format is used by NSPCG.  NSPCG requires that the information
#    for the diagonal entries of the matrix must come first.
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
#    integer M, N, the number of rows and columns of the matrix.
#
#    integer NZ_NUM, the number of nonzero elements in the matrix.
#
#    integer ROWCOL(2,NZ_NUM), the row and column indices
#    of the nonzero elements.
#
#  Output:
#
#    real A(NZ_NUM), the nonzero elements of the matrix.
#
  import numpy as np

  a = np.zeros ( nz_num )

  return a

def r8ncf_zeros_test ( ):

#*****************************************************************************80
#
## R8NCF_ZEROS_TEST tests R8NCF_ZEROS.
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
#   John Burkardt
#
  import numpy as np

  m = 5
  n = 7
  nz_num = 15

  rowcol = np.array ( [ \
    [ 0, 1, 2, 3, 4, 1, 4, 0, 4, 0, 1, 2, 3, 3, 0 ], \
    [ 0, 1, 2, 3, 4, 0, 0, 1, 1, 3, 3, 3, 4, 5, 6 ] ] )

  print ( '' )
  print ( 'R8NCF_ZEROS_TEST' )
  print ( '  R8NCF_ZEROS zeros an R8NCF matrix' )
  print ( '' )
  print ( '  Matrix rows M =    ', m )
  print ( '  Matrix columns N = ', n )
  print ( '  Matrix nonzeros =  ', nz_num )

  a = r8ncf_zeros ( m, n, nz_num, rowcol )

  r8ncf_print ( m, n, nz_num, rowcol, a, '  The R8NCF zero matrix:' )

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
  r8ncf_test ( )
  timestamp ( )

