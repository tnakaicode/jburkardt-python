#! /usr/bin/env python3
#
def crs_to_ccs_test ( ):

#*****************************************************************************80
#
## crs_to_ccs_test() tests crs_to_ccs() converts a CRS matrix to CCS format.
#
#  Discussion:
#
#    Consider the following small matrix.
#
#          2  3  0  0  0
#          3  0  4  0  6
#      A = 0 -1 -3  2  0
#          0  0  1  0  0
#          0  4  2  0  1
#
#    In CRS format, this would be:
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
#    In CCS format, the matrix would be:
#
#      #  ICC  CCC  ACC
#     --  ---  ---  ---
#      1    1    1    2
#      2    2         3
#
#      3    1    3    3
#      4    3        -1
#      5    5         4
#
#      6    2    6    4
#      7    3        -3
#      8    4         1
#      9    5         2
#
#     10    3   10    2
#
#     11    2   11    6
#     12    5         1
#
#     13    *   13
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'crs_to_ccs_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test crs_to_ccs().' )

  crs_to_ccs_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'crs_to_ccs_test():' )
  print ( '  Normal end of execution.' )

  return

def crs_to_ccs_test01 ( ):

#*****************************************************************************80
#
## crs_to_ccs_test01() tests crs_to_ccs() using a 1-based CRS matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  print ( '' )
  print ( 'crs_to_ccs_test01()' )
  print ( '  Convert a 1-based CRS matrix to CCS format.' )

  m = 5
  n = 5
  ncrs = 12

  icrs = np.array ( [ \
    1, 3, 6, 9, 10, 13 ], dtype = int )

  ccrs = np.array ( [ \
    1, 2, \
    1, 3, 5, \
    2, 3, 4, \
    3, \
    2, 3, 5 ], dtype = int )

  Acrs = np.array ( [ \
    2.0,  3.0, \
    3.0,  4.0,  6.0, \
   -1.0, -3.0,  2.0, \
    1.0, \
    4.0,  2.0,  1.0 ] )
#
#  Print the CRS matrix.
#
  crs_print ( m, n, ncrs, icrs, ccrs, Acrs, '  The CRS matrix:' )
#
#  Convert CRS to CCS.
#
  m, n, ncc, icc, ccc, Acc = crs_to_ccs ( m, n, ncrs, icrs, ccrs, Acrs )
#
#  Print the CCS matrix.
#
  ccs_print ( m, n, ncc, icc, ccc, Acc, '  The CCS matrix:' )

  return

def crs_to_ccs ( m, n, nz, row, col, val ):

#*****************************************************************************80
#
## crs_to_ccs() converts a CRS matrix to CCS format.
#
#  Discussion:
#
#    A sparse mxn matrix with nz nonzeros can be set in compressed 
#    row storage (CRS) format.
#
#    A sparse mxn matrix with ncc nonzeros can be set in compressed 
#    column storage (CCS) format.
#
#    This function converts from CRS to CCS format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    12 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N: the number of rows and columns.
#
#    integer NZ: the number of nonzero elements.
#
#    integer ROW(M+1): the nonzero elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
#  Output:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NCC, the number of values.
#
#    integer ICC(NCC), the rows.
#
#    integer CCC(N+1), the compressed columns
#
#    real ACC(NCC), the values.
#
  import numpy as np
#
#  Allocate space.
#
  column_length = np.zeros ( n, dtype = int )

  ncc = nz
  icc = np.zeros ( ncc, dtype = int )
  ccc = np.zeros ( n + 1, dtype = int )
  acc = np.zeros ( ncc )
#
#  Try to handle 0-based and 1-based indexing.
#
  base = row[0]
#
#  Compute the number of nonzeros in each column.
#
  for k in range ( 0, nz ):
    j = col[k] - base
    column_length[j] = column_length[j] + 1
#
#  Construct the column pointer array.
#
  ccc[0] = 0 + base
  for j in range ( 0, n ):
    ccc[j+1] = ccc[j] + column_length[j]
#
#  Record the first open position in each column.
#
  column_free = np.zeros ( n, dtype = int )
#
#  For each matrix entry, determine its column j, and place
#  the row i and value v in the next free spot for that column.
#
  for i in range ( 0, m ):
    for c in range ( row[i] - base, row[i+1] - base ):
      v = val[c]
      j = col[c] - base
      k = ccc[j] - base + column_free[j]
      acc[k] = v
      icc[k] = i + base
      column_free[j] = column_free[j] + 1

  return m, n, ncc, icc, ccc, acc

def ccs_print ( m, n, ncc, icc, ccc, acc, title ):

#*****************************************************************************80
#
## ccs_print() prints a sparse matrix in CCS format.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    22 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows in the matrix.
#
#    integer N, the number of columns in the matrix.
#
#    integer NCC, the number of elements.
#
#    integer ICC(NCC), the rows.
#
#    integer CCC(N+1), the compressed columns.
#
#    real ACC(NCC), the values.
#
#    character TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '     #     I     J       A' )
  print ( '  ----  ----  ----  --------------' )
  print ( '' )

  if ( ccc[0] == 0 ):

    j = 0
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j+1] <= k ):
        j = j + 1
      print ( '  %4d  %4d  %4d  %16.8g' % ( k, i, j, acc[k] ) )
#
#  Matrix uses 1-based indexing.
#
  else:

    j = 1
    for k in range ( 0, ncc ):
      i = icc[k]
      while ( ccc[j] <= k + 1 ):
        j = j + 1
      print ( '  %4d  %4d  %4d  %16.8g' % ( k + 1, i, j, acc[k] ) )

  return

def crs_print ( m, n, nz, row, col, val, title ):

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
#    19 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N, the order of the matrix.
#
#    integer NZ: the number of nonzero values.
#
#    integer ROW(M+1).  The nonzero elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ), the column indices of the nonzero elements of A.
#
#    real VAL(NZ), the nonzero elements of A.
#
#    string title: a title.
#
  print ( '' )
  print ( title )
  print ( '     #     I     J       A' )
  print ( '  ----  ----  ----  --------------' )
  print ( '' )
  
  if ( row[0] == 0 ):

    i = 0
    k = 0
    while ( i < m ):
      for c in range ( row[i], row[i+1] ):
        j = col[c];
        print ( '  %4d  %4d  %4d  %16.8g' % ( k, i, j, val[k] ) )
        k = k + 1
      i = i + 1;

  else:

    i = 1
    k = 0
    while ( i <= m ):
      for c in range ( row[i-1] - 1, row[i] - 1 ):
        j = col[c]
        print ( '  %4d  %4d  %4d  %16.8g' % ( k + 1, i, j, val[k] ) )
        k = k + 1
      i = i + 1

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
  crs_to_ccs_test ( )
  timestamp ( )

