#! /usr/bin/env python
#
def r8col_flip ( m, n, a ):

#*****************************************************************************80
#
## R8COL_FLIP flips the entries in each column of an R8COL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the array to be examined.
#
#    Output, real B(M,N), the flipped array.
#
  import numpy as np

  b = np.zeros ( [ m, n ] )

  for j in range ( 0, n ):
    for i in range ( 0, m ):
      b[i,j] = a[m-1-i,j]

  return b

def r8col_flip_test ( ):

#*****************************************************************************80
#
## R8COL_FLIP_TEST tests R8COL_FLIP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 May 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8COL_FLIP_TEST:' )
  print ( '  R8COL_FLIP flips the columns of an R8COL.' )

  m = 5
  n = 4
  a = np.random.random ( [ m, n ] )

  r8mat_print ( m, n, a, '  Matrix A:' )

  b = r8col_flip ( m, n, a )

  r8mat_print ( m, n, b, '  Matrix after column flipping:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8COL_FLIP_TEST:' )
  print ( '  Normale end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8col_flip_test ( )
  timestamp ( )