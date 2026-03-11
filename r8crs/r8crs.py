#! /usr/bin/env python3
#
def r8crs_test ( ):

#*****************************************************************************80
#
## r8crs_test() tests r8crs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8crs_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8crs().' )

  r8crs_dif2_test ( )
  r8crs_indicator_test ( )
  r8crs_mtv_test ( )
  r8crs_mv_test ( )
  r8crs_print_test ( )
  r8crs_print_some_test ( )
  r8crs_random_test ( )
  r8crs_to_r8ge_test ( )
  r8crs_zeros_test ( )

  r8ge_to_r8crs_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8crs_test():' )
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

def r8crs_dif2 ( n ):

#*****************************************************************************80
#
## r8crs_dif2() sets up an R8CRS second difference matrix.
#
#  Discussion:
#
#    The R8CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2022
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
#    integer ROW(N+1).  The nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), the column indices of the nonzero elements of A.
#
#    real VAL(NZ), the nonzero elements of A.
#
  import numpy as np

  nz = 3 * n - 2

  row = np.zeros ( n + 1, dtype = int )
  col = np.zeros ( nz, dtype = int )
  val = np.zeros ( nz, dtype = float )

  row[0] = 0
  k = 0

  for i in range ( 0, n ):

    if ( 0 < i ):

      col[k] = i - 1
      val[k] = -1.0
      k = k + 1

    col[k] = i
    val[k] = 2.0
    k = k + 1

    if ( i < n - 1 ):
      col[k] = i + 1
      val[k] = -1.0
      k = k + 1

    row[i+1] = k

  return row, col, val

def r8crs_dif2_test ( ):

#*****************************************************************************80
#
## r8crs_dif2_test() tests r8crs_dif2().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'r8crs_dif2_test():' )
  print ( '  r8crs_dif2() sets up a second difference matrix' )
  print ( '  using compressed row storage (CRS).' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  row, col, val = r8crs_dif2 ( n )

  r8crs_print ( n, row, col, val, '  The R8CRS second difference matrix:' )

  return

def r8crs_indicator ( n, nz, row, col ):

#*****************************************************************************80
#
## r8crs_indicator() sets up an R8CRS indicator matrix.
#
#  Discussion:
#
#    The R8CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of the matrix.
#
#    integer NZ: the number of nonzero elements.
#
#    integer ROW(N+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#  Output:
#
#    real VAL(NZ): the nonzero elements of A.
#
  import numpy as np

  nz = col.size
  val = np.zeros ( nz )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, n ):

    for k in range ( row[i], row[i+1] ):
      j = col[k]
      val[k] = fac * ( i + 1 ) + ( j + 1 )

  return val

def r8crs_indicator_test ( ):

#*****************************************************************************80
#
## r8crs_indicator_test() tests r8crs_indicator().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  nz = 12

  col = np.array ( [ \
    0, 1, 4, \
    1, 4, \
    0, 2, \
    0, 3, \
    1, 2, 4 ], dtype = int )

  row = np.array ( [ 0, 3, 5, 7, 9, 12 ], dtype = int )

  print ( '' )
  print ( 'r8crs_indicator_test():' )
  print ( '  r8crs_indicator() sets up an R8SR indicator matrix' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  val = r8crs_indicator ( n, nz, row, col )

  r8crs_print ( n, row, col, val, '  The R8CRS indicator matrix:' )

  return

def r8crs_mtv ( n, nz, row, col, val, x ):

#*****************************************************************************80
#
## r8crs_mtv() multiplies an R8CRS matrix, transposed, times a vector.
#
#  Discussion:
#
#    The R8SR storage format stores the diagonal of a sparse matrix in DIAG.
#    The off-diagonal entries of row I are stored in entries ROW(I)
#    through ROW(I+1)-1 of OFF.  COL(J) records the column index
#    of the entry in A(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of the matrix.
#
#    integer NZ: the number of nonzero elements.
#
#    integer ROW(N+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
#    real X(N): the vector to be multiplied by A.
#
#  Output:
#
#    real Y(N): the product A' * X.
#
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):
    for k in range ( row[i], row[i+1] ):
      j = col[k]
      y[j] = y[j] + val[k] * x[i]

  return y

def r8crs_mtv_test ( ):

#*****************************************************************************80
#
## r8crs_mtv_test() tests r8crs_mtv().
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

  n = 5
  nz = 12

  col = np.array ( [ \
    0, 1, 4, \
    1, 4, \
    0, 2, \
    0, 3, \
    1, 2, 4 ], dtype = int )

  row = np.array ( [ 0, 3, 5, 7, 9, 12 ], dtype = int )

  val = np.array ( [ \
    11.0, 12.0, 15.0, \
    22.0, 25.0, \
    31.0, 33.0, \
    41.0, 44.0, \
    52.0, 53.0, 55.0 ], dtype = float )

  print ( '' )
  print ( 'r8crs_mtv_test():' )
  print ( '  r8crs_mtv() multiplies an R8CRS matrix transposed times a vector.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Make a R8GE copy.
#
  A = r8crs_to_r8ge ( n, nz, row, col, val )

  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ], dtype = float )

  y1 = r8crs_mtv ( n, nz, row, col, val, x )
  y2 = np.dot ( np.transpose ( A ), x )

  r8vec2_print ( y1, y2, '  R8CRS and R8GE products:' )

  return

def r8crs_mv ( n, nz, row, col, val, x ):

#*****************************************************************************80
#
## r8crs_mv() multiplies an R8CRS matrix times a vector.
#
#  Discussion:
#
#    The R8CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    27 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of the matrix.
#
#    integer NZ: the number of nonzero elements.
#
#    integer ROW(N+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
#    real X(N): the vector to be multiplied by A.
#
#  Output:
#
#    real Y(N): the product A * X.
#  
  import numpy as np

  y = np.zeros ( n )

  for i in range ( 0, n ):
    for k in range ( row[i], row[i+1] ):
      j = col[k]
      y[i] = y[i] + val[k] * x[j]

  return y

def r8crs_mv_test ( ):

#*****************************************************************************80
#
## r8crs_mv_test() tests r8crs_mv().
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

  n = 5
  nz = 12
  col = np.array ( [ \
    0, 1, 4, \
    1, 4, \
    0, 2, \
    0, 3, \
    1, 2, 4 ], dtype = int )

  row = np.array ( [ 0, 3, 5, 7, 9, 12 ], dtype = int )

  val = np.array ( [ \
    11.0, 12.0, 15.0, \
    22.0, 25.0, \
    31.0, 33.0, \
    41.0, 44.0, \
    52.0, 53.0, 55.0 ], dtype = float )

  print ( '' )
  print ( 'r8crs_mv_test():' )
  print ( '  r8crs_mv() multiplies an R8CRS matrix by a vector' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Make a R8GE copy.
#
  A = r8crs_to_r8ge ( n, nz, row, col, val )

  x = np.array ( [ 1.0, 2.0, 3.0, 4.0, 5.0 ] )

  y1 = r8crs_mv ( n, nz, row, col, val, x )
  y2 = np.dot ( A, x )

  r8vec2_print ( y1, y2, '  R8CRS and R8GE products:' )

  return

def r8crs_print ( n, row, col, val, label ):

#*****************************************************************************80
#
## r8crs_print() prints an R8CRS matrix.
#
#  Discussion:
#
#    The R8CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), the column indices of the nonzero elements of A.
#
#    real VAL(NZ), the nonzero elements of A.
#
#    string label: a title.
#
  r8crs_print_some ( n, row, col, val, 0, 0, n, n, label )

  return

def r8crs_print_test ( ):

#*****************************************************************************80
#
## r8crs_print_test() tests r8crs_print().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 12
  col = np.array ( [ \
    0, 1, 4, \
    1, 4, \
    0, 2, \
    0, 3, \
    1, 2, 4 ] )
  row = np.array ( [ 0, 3, 5, 7, 9, 12 ] )
  val = np.array ( [ \
    11.0, 12.0, 15.0, \
    22.0, 25.0, \
    31.0, 33.0, \
    41.0, 44.0, \
    52.0, 53.0, 55.0 ] )

  print ( '' )
  print ( 'r8crs_print_test():' )
  print ( '  r8crs_print() prints a R8CRS matrix.' )
  print ( '  Matrix order N = ', n )
#
#  Print the matrix.
#
  r8crs_print ( n, row, col, val, '  The R8CRS matrix:' )

  return

def r8crs_print_some ( n, row, col, val, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## r8crs_print_some() prints some of a R8CRS matrix.
#
#  Discussion:
#
#    The R8CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
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
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), the column indices of the nonzero elements of A.
#
#    real VAL(NZ), the nonzero elements of A.
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
  for j2lo in range ( jlo, jhi, incx ):

    j2hi = j2lo + incx
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )

    inc = j2hi + 1 - j2lo

    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi ):
      print ( '%7d       ' % ( j ), end = '' )

    print ( '' )
    print ( '  Row' )
    print ( '  ---' )
#
#  Determine the range of the rows in this strip.
#
    i2lo = max ( ilo, 0 )
    i2hi = min ( ihi, n )

    for i in range ( i2lo, i2hi ):

      print ( '%4d  ' % ( i ), end = '' )
#
#  Print out (up to) 5 entries in row I, that lie in the current strip.
#
      for j in range ( j2lo, j2hi ):

        aij = 0.0

        for k in range ( row[i], row[i+1] ):
          if ( j == col[k] ):
            aij = val[k]

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8crs_print_some_test ( ):

#*****************************************************************************80
#
## r8crs_print_some_test() tests r8crs_print_some().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 12

  col = np.array ( [ \
    0, 1, 4, \
    1, 4, \
    0, 2, \
    0, 3, \
    1, 2, 4 ], dtype = int )

  row = np.array ( [ 0, 3, 5, 7, 9, 12 ], dtype = int )

  val = np.array ( [ \
    11.0, 12.0, 15.0, \
    22.0, 25.0, \
    31.0, 33.0, \
    41.0, 44.0, \
    52.0, 53.0, 55.0 ], dtype = float )

  print ( '' )
  print ( 'r8crs_print_some_test():' )
  print ( '  r8crs_print_some() prints some of a R8CRS matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Print the matrix.
#
  r8crs_print_some ( n, row, col, val, 0, 4, n, 5, '  Rows 0:N-1, column 4' )

  return

def r8crs_random ( n, nz, row, col ):

#*****************************************************************************80
#
## r8crs_random() randomizes a R8CRS matrix.
#
#  Discussion:
#
#    The R8CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of nonzero elements.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), the column indices of the nonzero elements of A.
#
#  Output:
#
#    real VALUE(NZ), the nonzero elements of A.
#
  from numpy.random import default_rng

  rng = default_rng ( )

  value = rng.standard_normal ( size = nz )

  return value

def r8crs_random_test ( ):

#*****************************************************************************80
#
## r8crs_random_test() tests r8crs_random().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    21 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 12
  col = np.array ( [ \
    0, 1, 4, \
    1, 4, \
    0, 2, \
    0, 3, \
    1, 2, 4 ] )
  row = np.array ( [ 0, 3, 5, 7, 9, 12 ] )

  print ( '' )
  print ( 'r8crs_random_test():' )
  print ( '  r8crs_random() randomizes a R8CRS matrix' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  val = r8crs_random ( n, nz, row, col )
#
#  Print the matrix.
#
  r8crs_print ( n, row, col, val, '  The R8CRS random matrix:' )

  return

def r8crs_to_r8ge ( n, nz, row, col, val ):

#*****************************************************************************80
#
## r8crs_to_r8ge() converts an R8CRS matrix to a R8GE matrix.
#
#  Discussion:
#
#    The R8CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 February 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N: the order of the matrix.
#
#    integer NZ: the number of nonzero elements.
#
#    integer ROW(N+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
#  Output:
#
#    real A(N,N): the R8GE matrix.
#
  import numpy as np

  A = np.zeros ( [ n, n ] )

  for i in range ( 0, n ):
    for j in range ( row[i], row[i+1] ):
      A[i,col[j]] = val[j]

  return A

def r8crs_to_r8ge_test ( ):

#*****************************************************************************80
#
## r8crs_to_r8ge_test() tests r8crs_to_r8ge().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  nz = 12

  col = np.array ( [ \
    0, 1, 4, \
    1, 4, \
    0, 2, \
    0, 3, \
    1, 2, 4 ] )

  row = np.array ( [ 0, 3, 5, 7, 9, 12 ] )

  val = np.array ( [ \
    11.0, 12.0, 15.0, \
    22.0, 25.0, \
    31.0, 33.0, \
    41.0, 44.0, \
    52.0, 53.0, 55.0 ] )

  print ( '' )
  print ( 'r8crs_to_r8ge_test():' )
  print ( '  r8crs_to_r8ge() converts an R8CRS matrix to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N =', n )
#
#  Print the matrix.
#
  r8crs_print ( n, row, col, val, '  The R8CRS matrix:' )
#
#  Convert the matrix.
#
  A = r8crs_to_r8ge ( n, nz, row, col, val )
#
#  Print the R8GE matrix.
#
  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( A )

  return

def r8crs_zeros ( n, nz, row, col ):

#*****************************************************************************80
#
## r8crs_zeros() zeros an R8SR matrix.
#
#  Discussion:
#
#    The R8CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of nonzero elements.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), the column indices of the nonzero elements of A.
#
#  Output:
#
#    real VAL(NZ), the nonzero elements of A.
#
  import numpy as np

  val = np.zeros ( nz )

  return val

def r8crs_zeros_test ( ):

#*****************************************************************************80
#
## r8crs_zeros_test() tests r8crs_zeros().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5

  nz = 12

  col = np.array ( [ \
    0, 1, 4, \
    1, 4, \
    0, 2, \
    0, 3, \
    1, 2, 4 ] )

  row = np.array ( [ 0, 3, 5, 7, 9, 12 ] )

  print ( '' )
  print ( 'r8crs_zeros_test():' )
  print ( '  r8crs_zeros() sets up a zero R8CRS matrix' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  val = r8crs_zeros ( n, nz, row, col )

  r8crs_print ( n, row, col, val, '  The R8CRS zero matrix:' )

  return

def r8ge_to_r8crs ( A ):

#*****************************************************************************80
#
## r8ge_to_r8crs() copies an R8GE matrix to R8CRS format.
#
#  Discussion:
#
#    The R8CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    25 August 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(N,N): the matrix.
#
#  Output:
#
#    integer N: the order of the matrix.
#
#    integer NZ: the number of nonzero elements.
#
#    integer ROW(N+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
  import numpy as np

  n = A.shape[0]

  nz = np.count_nonzero ( A )

  row = np.zeros ( n + 1, dtype = int )
  col = np.zeros ( nz, dtype = int  )
  val = np.zeros ( nz, dtype = float )

  row[0] = 0
  k = 0

  for i in range ( 0, n ):

    for j in range ( 0, n ):
      if ( A[i,j] != 0.0 ):

        col[k] = j
        val[k] = A[i,j]
        k = k + 1

    row[i+1] = k

  return n, nz, row, col, val

def r8ge_to_r8crs_test ( ):

#*****************************************************************************80
#
## r8ge_to_r8crs_test() tests r8ge_to_r8crs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    29 August 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'r8ge_to_r8crs_test():' )
  print ( '  r8ge_to_r8crs() converts an R8GE matrix to R8CRS format.' )

  A = np.array ( [ \
    [ 11.0, 12.0,  0.0,  0.0, 15.0 ], \
    [  0.0, 22.0,  0.0,  0.0, 25.0 ], \
    [ 31.0,  0.0, 33.0,  0.0,  0.0 ], \
    [ 41.0,  0.0,  0.0, 44.0,  0.0 ], \
    [  0.0, 52.0, 53.0,  0.0, 55.0 ] ] )
#
#  Print the R8GE matrix.
#
  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( A )
#
#  Convert the matrix.
#
  n, nz, row, col, val = r8ge_to_r8crs ( A )
#
#  Print the matrix.
#
  r8crs_print ( n, row, col, val, '  The R8CRS matrix:' )

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

def r8vec2_print ( a1, a2, title ):

#*****************************************************************************80
#
## r8vec2_print() prints an R8VEC2.
#
#  Discussion:
#
#    An R8VEC2 is a dataset consisting of N pairs of real values, stored
#    as two separate vectors A1 and A2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    20 June 2020
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the number of components of the vector.
#
#    real A1(N), A2(N), the vectors to be printed.
#
#    string TITLE, a title.
#
  n = len ( a1 )

  print ( '' )
  print ( title )
  print ( '' )
  for i in range ( 0, n ):
    print ( '  %6d:   %12g  %12g' % ( i, a1[i], a2[i] ) )

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
  r8crs_test ( )
  timestamp ( )

