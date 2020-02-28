#! /usr/bin/env python
#
def i4mat_transpose ( m, n, a ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE transposes an I4MAT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 April 2018
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
#    Output, integer B(N,M), the transposed matrix.
#
  import numpy as np

  b = np.zeros ( [ n, m ], dtype = np.int32 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      b[j,i] = a[i,j]

  return b

def i4mat_transpose_test ( ):

#*****************************************************************************80
#
## I4MAT_TRANSPOSE_TEST tests I4MAT_TRANSPOSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 April 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  print ( '' )
  print ( 'I4MAT_TRANSPOSE_TEST:' )
  print ( '  I4MAT_TRANSPOSE transposes an I4MAT.' )

  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      a[i,j] = 10 * ( i + 1 ) + ( j + 1 )

  i4mat_print ( m, n, a, '  The original matrix:' )

  b = i4mat_transpose ( m, n, a )

  i4mat_print ( n, m, b, '  The transposed matrix:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_TRANSPOSE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_transpose_test ( )
  timestamp ( )
