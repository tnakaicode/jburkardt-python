#! /usr/bin/env python
#
def i4mat_flip_cols ( m, n, a ):

#*****************************************************************************80
#
## I4MAT_FLIP_COLS swaps the columns of an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an M by N array of I4's.
#
#    To "flip" the columns of an I4MAT is to start with something like
#
#      11 12 13 14 15
#      21 22 23 24 25
#      31 32 33 34 35
#      41 42 43 44 45
#      51 52 53 54 55
#
#    and return
#
#      15 14 13 12 11
#      25 24 23 22 21
#      35 34 33 32 31
#      45 44 43 42 41
#      55 54 53 52 51
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 April 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer A(M,N), the matrix to be flipped.
#
#    Output, integer B(M,N), the flipped matrix.
#
  import numpy as np

  b = np.zeros ( [ m, n ], dtype = np.int32 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[i,j] = a[i,n-1-j]

  return b

def i4mat_flip_cols_test ( ):

#*****************************************************************************80
#
## I4MAT_FLIP_COLS_TEST tests I4MAT_FLIP_COLS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  print ( '' )
  print ( 'I4MAT_FLIP_COLS_TEST:' )
  print ( '  I4MAT_FLIP_COLS reverses the order of matrix columns.' )

  m = 6
  n = 5
  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  i4mat_print ( m, n, a, '  The original matrix:' )

  b = i4mat_flip_cols ( m, n, a )

  i4mat_print ( m, n, b, '  The column-flipped matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_FLIP_COLS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_flip_cols_test ( )
  timestamp ( )

