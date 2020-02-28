#! /usr/bin/env python
#
def i4mat_row_swap ( m, n, a, i1, i2 ):

#*****************************************************************************80
#
## I4MAT_ROW_SWAP swaps rows in an I4MAT.
#
#  Discussion:
#
#    Because Python/Numpy makes it fiendishly difficult to do simple things.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 August 2018
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
#    Input, integer I1, I2, the indices of the rows.
#    0 <= I1, I2 < M.
#
#    Output, integer B(M,N), the flipped matrix.
#
  if ( i1 != i2 ):

    for j in range ( 0, n ):
      t       = a[i1,j]
      a[i1,j] = a[i2,j]
      a[i2,j] = t

  return a

def i4mat_row_swap_test ( ):

#*****************************************************************************80
#
## I4MAT_ROW_SWAP_TEST tests I4MAT_ROW_SWAP.
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
  print ( 'I4MAT_ROW_SWAP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_ROW_SWAP swaps two rows in an I4MAT.' )

  m = 6
  n = 5
  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  i4mat_print ( m, n, a, '  The original matrix:' )

  i1 = 1
  i2 = 4
  a2 = i4mat_row_swap ( m, n, a, i1, i2 )

  i4mat_print ( m, n, a2, '  After swapping rows 1 and 4:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_ROW_SWAP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_row_swap_test ( )
  timestamp ( )

