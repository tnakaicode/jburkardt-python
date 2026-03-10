#! /usr/bin/env python3
#
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

def ccs_to_st ( m, n, ncc, icc, ccc, acc ):

#*****************************************************************************80
#
## ccs_to_st() converts sparse matrix information from CCS to ST format.
#
#  Discussion:
#
#    Only JST actually needs to be computed.  The other three output 
#    quantities are simply copies.  
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
#    integer M, the number of rows.
#
#    integer N, the number of columns.
#
#    integer NCC, the number of elements.
#
#    integer ICC(NCC), the rows.
#
#    integer CCC(N+1), the compressed columns.
#
#    real ACC(NCC), the values.
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

  ist = np.copy ( icc )
  jst = np.zeros ( ncc, dtype = int )
  ast = np.copy ( acc )

  nst = 0

  if ( ccc[0] == 0 ):

    jlo = 0
    jhi = n - 1
  
    for j in range ( jlo, jhi + 1 ):

      klo = ccc[j]
      khi = ccc[j+1]

      for k in range ( klo, khi ):

        jst[nst] = j
        nst = nst + 1

  else:

    ist = ist - 1

    jlo = 0
    jhi = n - 1
  
    for j in range ( jlo, jhi + 1 ):

      klo = ccc[j] - 1
      khi = ccc[j+1] - 1

      for k in range ( klo, khi ):

        jst[nst] = j
        nst = nst + 1

  return nst, ist, jst, ast

def ccs_to_st_test01 ( ):

#*****************************************************************************80
#
## ccs_to_st_test01() tests ccs_to_st() using a 1-based matrix.
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
#    The 1-based CCS representation is
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
#    22 June 2022
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  m = 5
  n = 5
  ncc = 12

  acc = np.array ( [ \
    2.0,  3.0, \
    3.0, -1.0,  4.0, \
    4.0, -3.0,  1.0, 2.0, \
    2.0, \
    6.0, 1.0 ] )

  ccc = np.array ( [ \
    1, 3, 6, 10, 11, 13 ] )

  icc = np.array ( [ \
    1, 2, \
    1, 3, 5, \
    2, 3, 4, 5, \
    3, \
    2, 5 ] )

  print ( '' )
  print ( 'ccs_to_st_test01()' )
  print ( '  Convert a 1-based CCS matrix to ST format.' )
#
#  Print the CCS matrix.
#
  ccs_print ( m, n, ncc, icc, ccc, acc, '  The CCS matrix:' )
#
#  Convert it.
#
  nst, ist, jst, ast = ccs_to_st ( m, n, ncc, icc, ccc, acc )
#
#  Print the ST matrix.
#
  st_print ( m, n, nst, ist, jst, ast, '  The ST matrix:' )

  return

def ccs_to_st_test02 ( ):

#*****************************************************************************80
#
## ccs_to_st_test02() tests ccs_to_st() using a 0-based matrix.
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
#    The 0-based CCS representation is
#
#      #  ICC  CCC  ACC
#     --  ---  ---  ---
#      0    0    0    2
#      1    1         3
#
#      2    0    2    3
#      3    2        -1
#      4    4         4
#
#      5    1    5    4
#      6    2        -3
#      7    3         1
#      8    4         2
#
#      9    2    9    2
#
#     10    1   10    6
#     11    4         1
#
#     12    *   12
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
  import numpy as np

  m = 5
  n = 5
  ncc = 12

  acc = np.array ( [ \
    2.0,  3.0, \
    3.0, -1.0,  4.0, \
    4.0, -3.0,  1.0, 2.0, \
    2.0, \
    6.0, 1.0 ] )

  ccc = np.array ( [ \
    0, 2, 5, 9, 10, 12 ] )

  icc = np.array ( [ \
    0, 1, \
    0, 2, 4, \
    1, 2, 3, 4, \
    2, \
    1, 4  ] )

  print ( '' )
  print ( 'ccs_to_st_test02():' )
  print ( '  Convert a 0-based CCS matrix to ST format.' )
#
#  Print the CCS matrix.
#
  ccs_print ( m, n, ncc, icc, ccc, acc, '  The CCS matrix:' )
#
#  Convert it.
#
  nst, ist, jst, ast = ccs_to_st ( m, n, ncc, icc, ccc, acc )
#
#  Print the ST matrix.
#
  st_print ( m, n, nst, ist, jst, ast, '  The ST matrix:' )

  return

def ccs_to_st_test ( ):

#*****************************************************************************80
#
## ccs_to_st_test() tests ccs_to_st().
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'ccs_to_st_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test ccs_to_st().' )

  ccs_to_st_test01 ( )
  ccs_to_st_test02 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ccs_to_st_test():' )
  print ( '  Normal end of execution.' )

  return

def st_print ( m, n, nst, ist, jst, ast, title ):

#*****************************************************************************80
#
## st_print() prints an ST matrix.
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
  print ( '  %d rows by %d columns' % ( m, n ) )
  print ( '' );

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
  ccs_to_st_test ( )
  timestamp ( )
