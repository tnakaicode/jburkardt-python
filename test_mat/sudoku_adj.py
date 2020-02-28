#! /usr/bin/env python
#
def sudoku_adj ( ):

#*****************************************************************************80
#
## SUDOKU_ADJ returns the Sudoku adjacency matrix.
#
#  Discussion:
#
#    A Sudoko is a 9x9 array, subdivided into 9 3x3 blocks.
#
#    Two elements of the 9x9 array are adjacent if they lie in the same
#    row, column, or 3x3 subblock.
#
#    The eigenvalues of the Sudoku adjacency matrix are all integers.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(81,81), the matrix.
#
  import numpy as np

  a = np.zeros ( [ 81, 81 ] )

  for i in range ( 0, 81 ):
    rowi = i // 9
    coli = i % 9
    browi = rowi // 3
    bcoli = coli // 3
    for j in range ( 0, 81 ):
      rowj = j // 9
      colj = j % 9
      browj = rowj // 3
      bcolj = colj // 3;
      if ( rowi == rowj or coli == colj or ( browi == browj and bcoli == bcolj ) ):
        a[i,j] = 1

  return a

def sudoku_adj_test ( ):

#*****************************************************************************80
#
## SUDOKU_ADJ_TEST tests SUDOKU_ADJ.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2018
#
#  Author:
#
#    John Burkardt
#
  import matplotlib.pyplot as plt
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'SUDOK_ADJ_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SUDOKU_ADJ computes the SUDOKU_ADJ matrix.' )

  a = sudoku_adj ( )
 
  plt.spy ( a )
  plt.show ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'SUDOKU_ADJ_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  sudoku_adj_test ( )
  timestamp ( )
