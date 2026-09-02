#! /usr/bin/env python3
#
def st_to_ge_test ( ):

#*****************************************************************************80
#
## st_to_ge_test() tests st_to_ge.
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
  import numpy as np
  import platform

  print ( '' )
  print ( 'st_to_ge_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  Test st_to_ge().' )

  st_to_ge_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'st_to_ge_test():' )
  print ( '  Normal end of execution.' )

  return

def st_to_ge_test01 ( ):

#*****************************************************************************80
#
## st_to_ge_test01() tests st_to_ge() using a tiny matrix.
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
#    16 March 2026
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import pprint

  print ( '' )
  print ( 'st_to_ge_test01():' )
  print ( '  Convert a sparse matrix from ST to GE format.' )
  print ( '  ST: sparse triplet,    I, J,  AIJ.' )
  print ( '  GE: general,           A[1:M,1:N].' )
#
#  Set the ST matrix.
#
  m = 5
  n = 5
  nst = 12

  Ast = np.array ( [ \
    0.0,  1.0, \
   10.0,  12.0,  14.0, \
   21.0,  22.0,  23.0, \
   32.0, \
   41.0,  42.0,  44.0 ] )

  ist = np.array ( [ \
    0, 0, \
    1, 1, 1, \
    2, 2, 2, \
    3, \
    4, 4, 4 ] )

  jst = np.array ( [ \
    0, 1, \
    0, 2, 4, \
    1, 2, 3, \
    2, \
    1, 2, 4 ] )
#
#  Print the matrix.
#
  title = 'The ST matrix:'
  st_header_print ( ist, jst, title )
  st_print ( ist, jst, Ast, title )
#
#  Convert to GE format.
#
  Age = st_to_ge ( nst, ist, jst, Ast )

  print ( '' )
  print ( '  The GE matrix:' )
  pprint.pprint ( Age )

  return

def st_header_print ( ist, jst, title ):

#*****************************************************************************80
#
## st_header_print() prints the header of an ST file.
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
#    integer IST(NST), JST(NST), row and column indices of nonzeros.
#
  i_min = min ( ist )
  i_max = max ( ist )
  j_min = min ( jst )
  j_max = max ( jst )

  m = i_max - i_min + 1
  n = j_max - j_min + 1
  nst = len ( ist )

  print ( '' )
  print ( title )
  print ( '  Header information:' )
  print ( '  Minimum row index I_MIN = ', i_min )
  print ( '  Maximum row index I_MAX = ', i_max )
  print ( '  Minimum col index J_MIN = ', j_min )
  print ( '  Maximum col index J_MAX = ', j_max )
  print ( '  Number of rows        M = ', m )
  print ( '  Number of columns     N = ', n )
  print ( '  Number of nonzeros  NST = ', nst )

  return

def st_print ( ist, jst, ast, title ):

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
#    22 June 2022
#
#  Author:
#
#    John Burkardt
#
#  Input:
#
#    integer IST(NST), JST(NST), the row and column indices.
#
#    real AST(NST), the nonzero values.
#
#    string TITLE, a title.
#
  import numpy as np

  i_min = min ( ist )
  i_max = max ( ist )
  j_min = min ( jst )
  j_max = max ( jst )

  m = i_max - i_min + 1
  n = j_max - j_min + 1
  nst = len ( ist )

  print ( '' )
  print ( title )
  print ( '' )

  for k in range ( 0, nst ):
    print ( '  %8d  %8d  %8d  %16.8f' % ( k, ist[k], jst[k], ast[k] ) )

  return

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

if ( __name__ == "__main__" ):
  timestamp ( )
  st_to_ge_test ( )
  timestamp ( )

