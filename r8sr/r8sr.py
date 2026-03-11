#! /usr/bin/env python3
#
def r8sr_test ( ):

#*****************************************************************************80
#
## r8sr_test() tests r8sr().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'r8sr_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test r8sr().' )

  r8sr_dif2_test ( )
  r8sr_indicator_test ( )
  r8sr_mtv_test ( )
  r8sr_mv_test ( )
  r8sr_print_test ( )
  r8sr_print_some_test ( )
  r8sr_random_test ( )
  r8sr_to_r8ge_test ( )
  r8sr_zeros_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8sr_test():' )
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

def r8sr_dif2 ( n ):

#*****************************************************************************80
#
## R8SR_DIF2 sets up an R8SR second difference matrix.
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
#    12 June 2016
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
#    integer NZ, the number of offdiagonal nonzero elements
#    in the matrix.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), contains the column index of the 
#    element in the corresponding position in A.
#
#    real DIAG(N), the diagonal elements of A.
#
#    real OFF(NZ), the off-diagonal elements of A.
#
  import numpy as np

  nz = 2 * n - 2

  row = np.zeros ( n + 1, dtype = np.int32 )
  col = np.zeros ( nz, dtype = np.int32 )
  diag = np.zeros ( n, dtype = np.float64 )
  off = np.zeros ( nz, dtype = np.float64 )

  for i in range ( 0, n ):
    diag[i] = - 2.0

  row[0] = 0
  nz2 = 0

  for i in range ( 0, n ):

    if ( i == 0 ):

      col[nz2] = i + 1
      off[nz2] = 1.0
      nz2 = nz2 + 1

      row[i+1] = row[i] + 1

    elif ( i < n - 1 ):

      col[nz2] = i - 1
      off[nz2] = 1.0
      nz2 = nz2 + 1

      col[nz2] = i + 1
      off[nz2] = 1.0
      nz2 = nz2 + 1

      row[i+1] = row[i] + 2

    else:

      col[nz2] = i - 1
      off[nz2] = 1.0
      nz2 = nz2 + 1

      row[i+1] = row[i] + 1

  return nz, row, col, diag, off

def r8sr_dif2_test ( ):

#*****************************************************************************80
#
## R8SR_DIF2_TEST tests R8SR_DIF2.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 June 2016
#
#  Author:
#
#    John Burkardt
#
  n = 5

  print ( '' )
  print ( 'R8SR_DIF2_TEST' )
  print ( '  R8SR_DIF2 sets up an R8SR second difference matrix' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  nz, row, col, diag, off = r8sr_dif2 ( n )

  r8sr_print ( n, nz, row, col, diag, off, '  The R8SR second difference matrix:' )

  return

def r8sr_indicator ( n, nz, row, col ):

#*****************************************************************************80
#
## R8SR_INDICATOR sets up a R8SR indicator matrix.
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
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of offdiagonal nonzero elements in A.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements of row I of A
#    are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), contains the column index of the element
#    in the corresponding position in A.
#
#  Output:
#
#    real DIAG(N), the diagonal elements of A.
#
#    real OFF(NZ), the off-diagonal elements of A.
#
  import numpy as np

  diag = np.zeros ( n, dtype = np.float64 )
  off = np.zeros ( nz, dtype = np.float64 )

  fac = 10 ** ( i4_log_10 ( n ) + 1 )

  for i in range ( 0, n ):

    j = i
    diag[i] = float ( fac * ( i + 1 ) + ( j + 1 ) )

    for k in range ( row[i], row[i+1] ):
      j = col[k]
      off[k] = float ( fac * ( i + 1 ) + ( j + 1 ) )

  return diag, off

def r8sr_indicator_test ( ):

#*****************************************************************************80
#
## R8SR_INDICATOR_TEST tests R8SR_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 7
  col = np.array ( [ 1, 4, 4, 0, 0, 1, 2 ] )
  row = np.array ( [ 0, 2, 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'R8SR_INDICATOR_TEST' )
  print ( '  R8SR_INDICATOR sets up a R8SR indicator matrix' )
  print ( '' )
  print ( '  Matrix order N = ', n )

  diag, off = r8sr_indicator ( n, nz, row, col )

  r8sr_print ( n, nz, row, col, diag, off, '  The R8SR indicator matrix:' )

  return

def r8sr_mtv ( n, nz, row, col, diag, off, x ):

#*****************************************************************************80
#
## R8SR_MTV multiplies a vector times a R8SR matrix.
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
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of offdiagonal nonzero elements in A.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements of row I of A
#    are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), contains the column index of the element
#    in the corresponding position in A.
#
#    real DIAG(N), the diagonal elements of A.
#
#    real OFF(NZ), the off-diagonal elements of A.
#
#    real X(N), the vector to be multiplies by A.
#
#  Output:
#
#    real B(N), the product A' * X.
#
  import numpy as np

  b = np.zeros ( n, dtype = np.float64 )

  for i in range ( 0, n ):
    b[i] = b[i] + diag[i] * x[i]
    for k in range ( row[i], row[i+1] ):
      j = col[k]
      b[j] = b[j] + off[k] * x[i]

  return b

def r8sr_mtv_test ( ):

#*****************************************************************************80
#
#% R8SR_MTV_TEST tests R8SR_MTV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    14 March 2009
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 7
  col = np.array ( [ 1, 4, 4, 0, 0, 1, 2 ] )
  row = np.array ( [ 0, 2, 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'R8SR_MTV_TEST' )
  print ( '  R8SR_MTV multiplies a vector by a R8SR matrix' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  diag, off = r8sr_random ( n, nz, row, col )
#
#  Make a R8GE copy.
#
  c = r8sr_to_r8ge ( n, nz, row, col, diag, off )
#
#  Print the R8GE copy.
#
  print ( '' )
  print ( '  The R8SR matrix, in R8GE form:' )
  print ( c )

  x = np.zeros ( n, dtype = np.float64 )
  x[0] = 1.0
  x[n-1] = -1.0

  r8vec_print ( n, x, '  The vector x:' )

  b = r8sr_mtv ( n, nz, row, col, diag, off, x )

  r8vec_print ( n, b, '  The product A'' * x:' )

  return

def r8sr_mv ( n, nz, row, col, diag, off, x ):

#*****************************************************************************80
#
## R8SR_MV multiplies a R8SR matrix times a vector.
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
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of offdiagonal nonzero elements in A.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements of row I of A
#    are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), contains the column index of the element
#    in the corresponding position in A.
#
#    real DIAG(N), the diagonal elements of A.
#
#    real OFF(NZ), the off-diagonal elements of A.
#
#    real X(N), the vector to be multiplied by A.
#
#  Output:
#
#    real B(N), the product A * X.
#
  import numpy as np

  b = np.zeros ( n, dtype = np.float64 )

  for i in range ( 0, n ):
    b[i] = b[i] + diag[i] * x[i]
    for k in range ( row[i], row[i+1] ):
      j = col[k]
      b[i] = b[i] + off[k] * x[j]

  return b

def r8sr_mv_test ( ):

#*****************************************************************************80
#
## R8SR_MV_TEST tests R8SR_MV.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 7
  col = np.array ( [ 1, 4, 4, 0, 0, 1, 2 ] )
  row = np.array ( [ 0, 2, 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'R8SR_MV_TEST' )
  print ( '  R8SR_MV multiplies a R8SR matrix by a vector' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  diag, off = r8sr_random ( n, nz, row, col )
#
#  Make a R8GE copy.
#
  c = r8sr_to_r8ge ( n, nz, row, col, diag, off )
#
#  Print the R8GE copy.
#
  print ( '' )
  print ( '  The R8SR matrix, in R8GE form:' )
  print ( c )

  x = np.zeros ( n, dtype = np.float64 )
  x[0] = 1.0
  x[n-1] = -1.0

  r8vec_print ( n, x, '  The vector x:' )

  b = r8sr_mv ( n, nz, row, col, diag, off, x )

  r8vec_print ( n, b, '  The product A * x:' )

  return

def r8sr_print ( n, nz, row, col, diag, off, title ):

#*****************************************************************************80
#
##  R8SR_PRINT prints a R8SR matrix.
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
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of offdiagonal nonzero elements in A.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements of row I of A
#    are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), contains the column index of the element
#    in the corresponding position in A.
#
#    real DIAG(N), the diagonal elements of A.
#
#    real OFF(NZ), the off-diagonal elements of A.
#
#    string TITLE, a title.
#
  r8sr_print_some ( n, nz, row, col, diag, off, 0, 0, n - 1, n - 1, title )

  return

def r8sr_print_test ( ):

#*****************************************************************************80
#
## R8SR_PRINT_TEST tests R8SR_PRINT.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 7
  col = np.array ( [ 1, 4, 4, 0, 0, 1, 2 ] )
  row = np.array ( [ 0, 2, 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'R8SR_PRINT_TEST' )
  print ( '  R8SR_PRINT prints a R8SR matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  diag, off = r8sr_random ( n, nz, row, col )
#
#  Print the matrix.
#
  r8sr_print ( n, nz, row, col, diag, off, '  The R8SR matrix:' )

  return

def r8sr_print_some ( n, nz, row, col, diag, off, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## R8SR_PRINT_SOME prints some of a R8SR matrix.
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
#    13 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of offdiagonal nonzero elements in A.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements of row I of A
#    are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), contains the column index of the element
#    in the corresponding position in A.
#
#    real DIAG(N), the diagonal elements of A.
#
#    real OFF(NZ), the off-diagonal elements of A.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  incx = 5

  print ( '' )
  print ( title )

  if ( n <= 0 ):
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
    i2hi = min ( ihi, n - 1 )

    for i in range ( i2lo, i2hi + 1 ):

      print ( '%7d :' % ( i ), end = '' )
      
      for j in range ( j2lo, j2hi + 1 ):

        aij = 0.0

        if ( j == i ):
          aij = diag[i]
        else:
          for k in range ( row[i], row[i+1] ):
            if ( j == col[k] ):
              aij = off[k]

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def r8sr_print_some_test ( ):

#*****************************************************************************80
#
## R8SR_PRINT_SOME_TEST tests R8SR_PRINT_SOME.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 7

  col = np.array ( [ 1, 4, 4, 0, 0, 1, 2 ] )
  row = np.array ( [ 0, 2, 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'R8SR_PRINT_SOME_TEST' )
  print ( '  R8SR_PRINT_SOME prints some of an R8SR matrix.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  diag, off = r8sr_random ( n, nz, row, col )
#
#  Print the matrix.
#
  r8sr_print_some ( n, nz, row, col, diag, off, 0, 4, n - 1, 4, \
    '  Rows 0:N-1, column 4' )

  return

def r8sr_random ( n, nz, row, col ):

#*****************************************************************************80
#
## R8SR_RANDOM randomizes a R8SR matrix.
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
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of offdiagonal nonzero elements in A.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements of row I of A
#    are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), contains the column index of the element
#    in the corresponding position in A.
#
#  Output:
#
#    real DIAG(N), the diagonal elements of A.
#
#    real OFF(NZ), the off-diagonal elements of A.
#
  from numpy.random import default_rng
  import numpy as np

  rng = default_rng ( )

  diag = np.zeros ( n, dtype = np.float64 )
  off = np.zeros ( nz, dtype = np.float64 )

  for i in range ( 0, n ):
    diag[i] = rng.random ( )
    for j in range ( row[i], row[i+1] ):
      off[j] = rng.random ( )

  return diag, off

def r8sr_random_test ( ):

#*****************************************************************************80
#
## R8SR_RANDOM_TEST tests R8SR_RANDOM.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 7
  col = np.array ( [ 1, 4, 4, 0, 0, 1, 2 ] )
  row = np.array ( [ 0, 2, 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'R8SR_RANDOM_TEST' )
  print ( '  R8SR_RANDOM randomizes a R8SR matrix' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  diag, off = r8sr_random ( n, nz, row, col )
#
#  Print the R8GE copy.
#
  r8sr_print ( n, nz, row, col, diag, off, '  The R8SR matrix:' )

  return

def r8sr_to_r8ge ( n, nz, row, col, diag, off ):

#*****************************************************************************80
#
## R8SR_TO_R8GE converts a R8SR matrix to a R8GE matrix.
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
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of offdiagonal nonzero elements in A.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements of row I of A
#    are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), contains the column index of the element
#    in the corresponding position in A.
#
#    real DIAG(N), the diagonal elements of A.
#
#    real OFF(NZ), the off-diagonal elements of A.
#
#  Output:
#
#    real B(N,N), the R8GE matrix.
#
  import numpy as np

  b = np.zeros ( [ n, n ], dtype = np.float64 )

  for i in range ( 0, n ):
    b[i,i] = diag[i]

  for i in range ( 0, n ):
    for j in range ( row[i], row[i+1] ):
      b[i,col[j]] = off[j]

  return b

def r8sr_to_r8ge_test ( ):

#*****************************************************************************80
#
## R8SR_TO_R8GE_TEST tests R8SR_TO_R8GE.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    15 October 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 7

  col = np.array ( [ 1, 4, 4, 0, 0, 1, 2 ] )
  row = np.array ( [ 0, 2, 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'R8SR_TO_R8GE_TEST' )
  print ( '  R8SR_TO_R8GE converts a matrix from R8SR to R8GE format.' )
  print ( '' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  diag, off = r8sr_random ( n, nz, row, col )
#
#  Print the matrix.
#
  r8sr_print ( n, nz, row, col, diag, off, '  The R8SR matrix:' )
#
#  Convert the matrix.
#
  a_r8ge = r8sr_to_r8ge ( n, nz, row, col, diag, off )
#
#  Print the R8GE matrix.
#
  print ( '' )
  print ( '  The R8GE matrix:' )
  print ( a_r8ge )

  return

def r8sr_zeros ( n, nz, row, col ):

#*****************************************************************************80
#
## R8SR_ZEROS zeros an R8SR matrix.
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
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer N, the order of the matrix.
#
#    integer NZ, the number of offdiagonal nonzero elements in A.
#
#    integer ROW(N+1).  The nonzero offdiagonal elements of row I of A
#    are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), contains the column index of the element
#    in the corresponding position in A.
#
#  Output:
#
#    real DIAG(N), the diagonal elements of A.
#
#    real OFF(NZ), the off-diagonal elements of A.
#
  import numpy as np

  diag = np.zeros ( n, dtype = np.float64 )
  off = np.zeros ( nz, dtype = np.float64 )

  return diag, off

def r8sr_zeros_test ( ):

#*****************************************************************************80
#
## R8SR_ZEROS_TEST tests R8SR_ZEROS.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    12 June 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  n = 5
  nz = 7

  col = np.array ( [ 1, 4, 4, 0, 0, 1, 2 ] )
  row = np.array ( [ 0, 2, 3, 4, 5, 7 ] )

  print ( '' )
  print ( 'R8SR_ZEROS_TEST' )
  print ( '  R8SR_ZEROS zeros an R8SR matrix' )
  print ( ' ' )
  print ( '  Matrix order N = ', n )
#
#  Set the matrix.
#
  diag, off = r8sr_zeros ( n, nz, row, col )
#
#  Print the matrix.
#
  r8sr_print ( n, nz, row, col, diag, off, '  The R8SR matrix:' )

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
  r8sr_test ( )
  timestamp ( )
 
