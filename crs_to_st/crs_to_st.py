#! /usr/bin/env python3
#
def crs_to_st_test ( ):

#*****************************************************************************80
#
## crs_to_st_test() tests crs_to_st().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'crs_to_st_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test crs_to_st(), converting compressed row storage (CRS)' )
  print ( '  sparse matrix files to sparse triplet (ST) format.' )

  crs_to_st_test01 ( )
  crs_to_st_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'crs_to_st_test():' )
  print ( '  Normal end of execution.' )

  return

def crs_to_st_test01 ( ):

#*****************************************************************************80
#
## crs_to_st_test01() tests crs_to_st() using a 1-based CRS matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 5
  ncrs = 12
  ccrs = np.array ( [ \
    1, 2, 5, \
    2, 5, \
    1, 3, \
    1, 4, \
    2, 3, 5 ], dtype = int )
  icrs = np.array ( \
    [ 1, 4, 6, 8, 10, 13 ], dtype = int )
  Acrs = np.array ( \
    [ 11.0, 12.0, 15.0, 22.0, 25.0, 31.0, 33.0, 41.0, 44.0, 52.0, 53.0, 55.0 ] )

  print ( '' )
  print ( 'crs_to_st_test01()' )
  print ( '  Convert a 1-based CRS matrix to ST format.' )
#
#  Print the CRS matrix.
#
  crs_print ( m, n, ncrs, icrs, ccrs, Acrs, '  The CRS matrix:' )
#
#  Convert it.
#
  nst, ist, jst, Ast = crs_to_st ( m, n, ncrs, icrs, ccrs, Acrs )
#
#  Print the ST matrix.
#
  st_print ( m, n, nst, ist, jst, Ast, '  The ST matrix:' )

  return

def crs_to_st_test02 ( ):

#*****************************************************************************80
#
## crs_to_st_test02() tests crs_to_st() using a 0-based CRS matrix.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 5
  ncrs = 12
  ccrs = np.array ( [ \
    0, 1, 4, \
    1, 4, \
    0, 2, \
    0, 3, \
    1, 2, 4 ], dtype = int )
  icrs = np.array ( [ \
    0, 3, 5, 7, 9, 12 ], dtype = int )
  Acrs = np.array ( [ \
    11.0, 12.0, 15.0, 22.0, 25.0, 31.0, 33.0, 41.0, 44.0, 52.0, 53.0, 55.0 ] )

  print ( '' )
  print ( 'crs_to_st_test02():' )
  print ( '  Convert a 0-based CRS matrix to ST format.' )
#
#  Print the CRS matrix.
#
  crs_print ( m, n, ncrs, icrs, ccrs, Acrs, '  The CRS matrix:' )
#
#  Convert it.
#
  nst, ist, jst, Ast = crs_to_st ( m, n, ncrs, icrs, ccrs, Acrs )
#
#  Print the ST matrix.
#
  st_print ( m, n, nst, ist, jst, Ast, '  The ST matrix:' )

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

def crs_to_st (  m, n, nz, row, col, val ):

#*****************************************************************************80
#
## crs_to_st() converts from compressed row storage (CRS) to sparse triplet (ST).
# 
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    10 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, N: the order of the matrix.
#
#    integer NZ: the number of nonzero elements.
#
#    integer ROW(M+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
#  Output:
#
#    integer NST, the number of ST elements.
#
#    integer IST(NST), JST(NST), the ST rows and columns.
#
#    real AST(NST), the ST values.
#
  import numpy as np

  nst = 0
  ist = np.zeros ( nz, dtype = int )
  jst = np.zeros ( nz, dtype = int )
  Ast = np.zeros ( nz )
#
#  Handle 0-based indexing.
#
  if ( row[0] == 0 ):
    for i in range ( 0, m ):
      for j in range ( row[i], row[i+1] ):
        ist[nst] = i + 1
        jst[nst] = col[j] + 1
        Ast[nst] = val[j]
        nst = nst + 1
#
#  Handle 1-based indexing.
#
  else:
    for i in range ( 0, m ):
      for j in range ( row[i] - 1, row[i+1] - 1 ):
        ist[nst] = i + 1
        jst[nst] = col[j]
        Ast[nst] = val[j]
        nst = nst + 1

  return nst, ist, jst, Ast

def st_print ( m, n, nst, ist, jst, ast, title ):

#*****************************************************************************80
#
## st_print() prints an ST file.
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    10 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NST, the number of nonzeros.
#
#    integer IST(NST), JST(NST), the row and column indices.
#
#    real AST(NST), the nonzero values.
#
#    string TITLE, a title.
#
  print ( '' )
  print ( title )
  print ( '' )

  for k in range ( 0, nst ):
    print ( '  %8d  %8d  %8d  %16.8f' % ( k, ist[k], jst[k], ast[k] ) )

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
  crs_to_st_test ( )
  timestamp ( )

