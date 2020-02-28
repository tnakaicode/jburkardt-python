#! /usr/bin/env python
#
def i4row_min ( m, n, x ):

#*****************************************************************************80
#
## I4ROW_MIN returns the minimums of rows of an I4ROW.
#
#  Discussion:
#
#    An I4ROW is an M by N array of I4's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, integer X(M,N), the I4ROW.
#
#    Output, integer XMIN(M), the minimums of the rows of X.
#
  import numpy as np

  xmin = np.zeros ( m, dtype = np.int32 )

  for i in range ( 0, m ):
    xmin[i] = x[i,0]
    for j in range ( 1, n ):
      xmin[i] = min ( xmin[i], x[i,j] )

  return xmin

def i4row_min_test ( ):

#*****************************************************************************80
#
## I4ROW_MIN_TEST tests I4ROW_MIN
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print
  from i4vec_print import i4vec_print

  m = 3
  n = 4

  print ( '' )
  print ( 'I4ROW_MIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4ROW_MIN computes minimums of an I4ROW.' )

  a = np.zeros ( [ m, n ], dtype = np.int32 )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  amin = i4row_min ( m, n, a )

  i4vec_print ( m, amin, '  Row minimums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4ROW_MIN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4row_min_test ( )
  timestamp ( )
