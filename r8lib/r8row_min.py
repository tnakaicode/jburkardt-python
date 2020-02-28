#! /usr/bin/env python
#
def r8row_min ( m, n, x ):

#*****************************************************************************80
#
## R8ROW_MIN returns the minimums of rows of an R8ROW.
#
#  Discussion:
#
#    An R8ROW is an M by N array of R8's, regarded as an array of M rows,
#    each of length N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns in the array.
#
#    Input, real X(M,N), the R8ROW.
#
#    Output, real XMIN(M), the minimums of the rows of X.
#
  import numpy as np

  xmin = np.zeros ( m )

  for i in range ( 0, m ):
    xmin[i] = x[i,0]
    for j in range ( 1, n ):
      xmin[i] = min ( xmin[i], x[i,j] )

  return xmin

def r8row_min_test ( ):

#*****************************************************************************80
#
## R8ROW_MIN_TEST tests R8ROW_MIN
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    27 February 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  m = 3
  n = 4

  print ( '' )
  print ( 'R8ROW_MIN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8ROW_MIN computes minimums of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  amin = r8row_min ( m, n, a )

  r8vec_print ( m, amin, '  Row minimums:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_MIN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8row_min_test ( )
  timestamp ( )
