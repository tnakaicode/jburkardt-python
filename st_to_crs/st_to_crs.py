#! /usr/bin/env python3
#
def st_to_crs_test ( ):

#*****************************************************************************80
#
## st_to_crs_test() tests st_to_crs().
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform

  print ( '' )
  print ( 'st_to_crs_test():' )
  print ( '  numpy version:      ' + np.version.version )
  print ( '  python version:     ' + platform.python_version ( ) )
  print ( '  Test st_to_crs().' )

  st_to_crs_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'st_to_crs_test():' )
  print ( '  Normal end of execution.' )

  return

def st_to_crs_test01 ( ):

#*****************************************************************************80
#
## st_to_crs_test01() tests st_to_crs() using a tiny matrix.
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
#    A (1-based) ST representation, reading in order by rows is:
#
#      I  J   A
#     -- --  --
#      1  1   2
#      1  2   3
#
#      2  1   3
#      2  3   4
#      2  5   6
#
#      3  2  -1
#      3  3  -3
#      3  4   2
#
#      4  3   1
#
#      5  2   4
#      5  3   2
#      5  5   1
#
#  Licensing:
#
#    This code is distributed under the MIT license.
#
#  Modified:
#
#    11 May 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  nst = 12

  ast = np.array ( [ \
   -1.0, -3.0,  2.0, \
    3.0,  4.0,  6.0, \
    1.0, \
    2.0,  3.0, \
    4.0,  2.0,  1.0 ] )

  ist = np.array ( [ \
    3, 3, 3, \
    2, 2, 2, \
    4, \
    1, 1, \
    5, 5, 5 ], dtype = int )

  jst = np.array ( [ \
    2, 3, 4, \
    1, 3, 5, \
    3, \
    1, 2, \
    2, 3, 5 ], dtype = int )

  m = 5
  n = 5

  print ( '' )
  print ( 'st_to_crs_test01():' )
  print ( '  Convert a sparse matrix from st to crs format.' )
  print ( '  st:  sparse triplet,    I,  J, A.' )
  print ( '  crs: compressed row   , RR, J, A.' )
#
#  Print the ST matrix.
#
  title = 'The ST matrix:'
  st_print ( m, n, nst, ist, jst, ast, title )
#
#  Convert from ST to CRS format.
#
  row, col, val = st_to_crs ( nst, ist, jst, ast )
#
#  Print the crs matrix.
#
  title = 'The crs matrix:'
  crs_print ( row, col, val, title )

  return

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
#    11 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
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
  
  m = row.shape[0] - 1

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

def ge_to_crs ( A ):

#*****************************************************************************80
#
## ge_to_crs() copies a GE matrix to CRS format.
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
#    15 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    real A(M,N): the matrix.
#
#  Output:
#
#    integer ROW(M+1): the nonzero offdiagonal elements 
#    of row I of A are contained in A(ROW(I)) through A(ROW(I+1)-1).
#
#    integer COL(NZ): the column indices of the nonzero elements of A.
#
#    real VAL(NZ): the nonzero elements of A.
#
  import numpy as np

  m, n = A.shape
  nz = np.count_nonzero ( A )
  row = np.zeros ( m + 1, dtype = int )
  col = np.zeros ( nz, dtype = int )
  val = np.zeros ( nz, dtype = float )

  row[0] = 0
  k = 0

  for i in range ( 0, m ):
    for j in range ( 0, n):
      if ( A[i,j] != 0.0 ):
        col[k] = j
        val[k] = A[i,j]
        k = k + 1

    row[i+1] = k

  return row, col, val

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

def st_to_crs ( nst, ist, jst, Ast ):

#*****************************************************************************80
#
## st_to_crs() copies an ST matrix to CRS format.
#
#  Discussion:
#
#    The ST storage format stores, for each nonzero entry of a matrix,
#    the values I, J, and AIJ in separate vectors.
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
#    11 May 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NST, the number of ST elements.
#
#    integer IST(NST), JST(NST), the ST rows and columns.
#
#    real Ast(NST), the ST values.
#
#  Output:
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
  Age = st_to_ge ( nst, ist, jst, Ast )

  row, col, val = ge_to_crs ( Age )

  return row, col, val

def st_to_ge ( nst, ist, jst, Ast ):

#*****************************************************************************80
#
## st_to_ge() converts ST matrix data to GE format.
#
#  Licensing:
#
#    This code is distributed under the MIT license. 
#
#  Modified:
#
#    16 March 2026
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer NST: the number of values.
#
#    integer IST(NST), JST(NST), the ST rows and columns.
#
#    real Ast(NST), the ST values.
#
#  Output:
#
#    real Age[M,N], the GE matrix.
#
  import numpy as np

  if ( ist[0] == 0 ):
    offset = 0
    m = np.max ( ist ) + 1
    n = np.max ( jst ) + 1
  else:
    offset = 1
    m = np.max ( ist )
    n = np.max ( jst )

  Age = np.zeros ( [ m, n ] )

  for kst in range ( 0, nst ):

    i = ist[kst] - offset
    j = jst[kst] - offset
    Age[i,j] = Age[i,j] + Ast[kst]

  return Age

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
  st_to_crs_test ( )
  timestamp ( )

