#! /usr/bin/env python
#
def i4mat_row_reduce ( m, n, i, a ):

#*****************************************************************************80
#
## I4MAT_ROW_REDUCE divides out common factors in row I of an I4MAT.
#
#  Discussion:
#
#    An I4MAT is an MxN array of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 September 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows in the matrix.
#
#    Input, integer N, the number of columns in the matrix.
#
#    Input, integer I, the row to be reduced.  0 <= I < M.
#
#    Input, integer A[M,N], the matrix whose row is to be reduced.
#
#    Output, integer A[M,N], row I of the matrix has been reduced.
#
  from i4vec_red import i4vec_red

  a[i,:], common_factor = i4vec_red ( n, a[i,:], 1 )

  return a

def i4mat_row_reduce_test ( ):

#*****************************************************************************80
#
## I4MAT_ROW_REDUCE_TEST tests I4MAT_ROW_REDUCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 September 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  m = 5
  n = 3

  print ( '' )
  print ( 'I4MAT_ROW_REDUCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_ROW_REDUCE divides out any common factors in the' )
  print ( '  entries of a row of an I4MAT.' )

  a = np.array ( [ \
    [  12, 88,   9 ], \
    [   4,  8, 192 ], \
    [ -12, 99,  94 ], \
    [  30, 18,  42 ], \
    [   0,  4,   8 ] ] )

  i4mat_print ( m, n, a, '  Original matrix:' )

  for i in range ( m - 1, -1, -1 ):
    a = i4mat_row_reduce ( m, n, i, a )
    i4mat_print ( m, n, a, '  After reducing a row:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_ROW_REDUCE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_row_reduce_test ( )
  timestamp ( )

