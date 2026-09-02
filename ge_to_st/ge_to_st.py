#! /usr/bin/env python3
#
def ge_to_st_test ( ):

#*****************************************************************************80
#
## ge_to_st_test() tests ge_to_st().
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
  print ( 'ge_to_st_test():' )
  print ( '  python version: ' + platform.python_version ( ) )
  print ( '  numpy version:  ' + np.version.version )
  print ( '  ge_to_st() converts a matrix from GE to ST format.' )

  ge_to_st_test01 ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'ge_to_st_test():' )
  print ( '  Normal end of execution.' )

  return

def ge_to_st ( Age ):

#*****************************************************************************80
#
## ge_to_st() converts a GE matrix to Sparse Triplet (ST) format.
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
#    real Age(M,N), the GE matrix.
#
#  Output:
#
#    integer nst, the number of nonzero elements.
#
#    integer ist(nst), jst(nst), the row and column indices
#    of the nonzero elements.
#
#    real Ast(nst), the values of the nonzero elements.
#
  import numpy as np

  m, n = Age.shape
  nst = np.count_nonzero ( Age )
  ist = np.zeros ( nst, dtype = int )
  jst = np.zeros ( nst, dtype = int )
  Ast = np.zeros ( nst, dtype = float )
  
  k = 0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( Age[i,j] != 0.0 ):
        ist[k] = i
        jst[k] = j
        Ast[k] = Age[i,j]
        k = k + 1;

  return nst, ist, jst, Ast

def ge_to_st_test01 ( ):

#*****************************************************************************80
#
## ge_to_st_test01() converts a matrix from GE to ST format.
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

  print ( '' )
  print ( 'ge_to_st_test01():' )
  print ( '  Convert a matrx from GE to ST format.' )
#
#  Set GE data.
#
  m = 5
  n = 5
  Age = np.array ( [ \
    [ 2,  3,  0,  0,  0 ], \
    [ 3,  0,  4,  0,  6 ], \
    [ 0, -1, -3,  2,  0 ], \
    [ 0,  0,  1,  0,  0 ], \
    [ 0,  4,  2,  0,  1 ] ] )
#
#  Convert from GE to ST format.
#
  nst, ist, jst, Ast = ge_to_st ( Age )
#
#  Print the ST data.
#
  st_print ( m, n, nst, ist, jst, Ast, '  The ST matrix:' )

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
#    26 September 2018
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
  ge_to_st_test ( )
  timestamp ( )

