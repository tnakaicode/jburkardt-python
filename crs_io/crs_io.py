#! /usr/bin/env python3
#
def crs_io_test ( ):

#*****************************************************************************80
#
## crs_io_test() tests crs_io().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'crs_io_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test crs_io().' )

  crs_write_test ( )
  crs_read_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'crs_io_test():' )
  print ( '  Normal end of execution.' )

  return

def crs_mv ( n, nz, row, col, val, x ):

#*****************************************************************************80
#
## crs_mv() multiplies a CRS matrix times a vector.
#
#  Discussion:
#
#    The CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
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

  n = len ( row ) - 1
  nz = len ( col )
 
  y = np.zeros ( n )

  for i in range ( 0, n ):
    for k in range ( row[i], row[i+1] ):
      j = col[k]
      y[i] = y[i] + val[k] * x[j]
 
  return y

def crs_print ( row, col, val, title ):

#*****************************************************************************80
#
## crs_print() prints a CRS matrix.
#
#  Discussion:
#
#    The CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer ROW(N+1).  The nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), the column indices of the nonzero elements of A.
#
#    real VAL(NZ), the nonzero elements of A.
#
#    string TITLE, a title.
#
  import numpy as np

  n = len ( row ) - 1

  crs_print_some ( row, col, val, 0, 0, n - 1, n - 1, title )

  return

def crs_print_some ( row, col, val, ilo, jlo, ihi, jhi, title ):

#*****************************************************************************80
#
## crs_print_some() prints some of a CRS matrix.
#
#  Discussion:
#
#    The CRS storage format stores the nonzero entries of row I in 
#    entries ROW(I) through ROW(I+1)-1 of VAL.  
#    COL(J) records the column index of the entry in VAL(J).
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
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
#    real VAL(NZ), the nonzero elements of A.
#
#    integer ILO, JLO, IHI, JHI, the first row and
#    column, and the last row and column to be printed.
#
#    string TITLE, a title.
#
  import numpy as np

  n = len ( row ) - 1
  nz = len ( col )

  print ( '' )
  print ( title )

  incx = 5
#
#  Print the columns of the matrix, in strips of 5.
#
  for j2lo in range ( jlo, jhi + 1, incx ):

    j2hi = j2lo + incx - 1
    j2hi = min ( j2hi, n )
    j2hi = min ( j2hi, jhi )

    inc = j2hi + 1 - j2lo

    print ( '' )
    print ( '  Col: ', end = '' )

    for j in range ( j2lo, j2hi + 1 ):
      print ( '%7d       ' % ( j ), end = '' )
    print ( '' )

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

        aij = 0.0
        for k in range ( row[i], row[i+1] ):
          if ( j == col[k] ):
            aij = val[k]

        print ( '%12g  ' % ( aij ), end = '' )

      print ( '' )

  return

def crs_read ( prefix ):

#*****************************************************************************80
#
## crs_read() reads data about a sparse matrix in CRS format.
#
#  Discussion:
#
#    Three files are presumed to exist:
#    * prefix_row.txt contains N+1 row start values
#    * prefix_col.txt contains NZ column indices
#    * prefix_val.txt contains NZ matrix entries
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string PREFIX, a common prefix for the filenames.
#
#  Output:
#
#    integer ROW(N+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
  import numpy as np

  filename = prefix + '_row.txt'
  row = np.loadtxt ( filename )
  row = row.astype ( int )

  filename = prefix + '_col.txt'
  col = np.loadtxt ( filename )
  col = col.astype ( int )

  filename = prefix + '_val.txt'
  val = np.loadtxt ( filename )

  return row, col, val

def crs_read_test ( ):

#*****************************************************************************80
#
## crs_read_test() tests crs_read()
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
#
#  Author:
#
#    John Burkardt
#
  print ( '' )
  print ( 'crs_read_test():' )
  print ( '  crs_read() reads a sparse matrix in CRS format from 3 files.' )
#
#  Read the matrix data.
#
  prefix = 'simple'
  row, col, val = crs_read ( prefix )
#
#  Print the matrix.
#
  crs_print ( row, col, val, '  The CRS matrix' )

  return

def crs_write ( prefix, row, col, val ):

#*****************************************************************************80
#
## crs_write() writes a CRS matrix to 3 files.
#
#  Discussion:
#
#    Three files will be created:
#    * prefix_row.txt contains N+1 row start values
#    * prefix_col.txt contains NZ column indices
#    * prefix_val.txt contains NZ matrix entries
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    string PREFIX, a common prefix for the filenames.
#
#    integer ROW(N+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
  import numpy as np

  filename = prefix + '_row.txt'
  np.savetxt ( filename, row )
  print ( '  Saved data as "' + filename + '"' )

  filename = prefix + '_col.txt'
  np.savetxt ( filename, col )
  print ( '  Saved data as "' + filename + '"' )

  filename = prefix + '_val.txt'
  np.savetxt ( filename, val )
  print ( '  Saved data as "' + filename + '"' )

  return

def crs_write_test ( ):

#*****************************************************************************80
#
## crs_write_test() tests crs_write() using a tiny matrix.
#
#  Discussion:
#
#    This test uses a trivial matrix whose full representation is:
#
#          2  3  0  0  0
#          3  0  4  0  6
#      A = 0 -1 -3  2  0
#          0  0  1  0  0
#          0  4  2  0  1
#
#    The 1-based CRS representation is
#
#      #  ROW  COL  VAL
#     --  ---  ---  ---
#      1    1    1    2
#      2         2    3
#
#      3    3    1    3
#      4         3    4
#      5         5    6
#
#      6    6    2   -1
#      7         3   -3
#      8         4    2
#
#      9    9    3    1
# 
#     10   10    2    4
#     11         3    2
#     12         5    1
#
#     13   13    *
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    16 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  row = np.array ( [ \
    0, 2, 5, 8, 9, 12 ] )

  col = np.array ( [ \
    0, 1, \
    0, 2, 4, \
    1, 2, 3, \
    2, \
    1, 2, 4 ] )

  val = np.array ( [ \
    2.0,  3.0, \
    3.0,  4.0,  6.0, \
   -1.0, -3.0,  2.0, \
    1.0, \
    4.0,  2.0,  1.0 ] )

  prefix = 'simple'

  print ( '' )
  print ( 'crs_write_test():' )
  print ( '  Write a CRS matrix to 3 files.' )
#
#  Print the matrix.
#
  crs_print ( row, col, val, '  The CRS matrix:' )
#
#  Write the matrix to 3 files.
#
  crs_write ( prefix, row, col, val )

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
  crs_io_test ( )
  timestamp ( )


