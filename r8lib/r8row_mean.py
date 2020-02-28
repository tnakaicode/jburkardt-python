#! /usr/bin/env python
#
def r8row_mean ( m, n, a ):

#*****************************************************************************80
#
## R8ROW_MEAN returns the means of an R8ROW.
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
#    28 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the R8ROW
#
#    Output, real ROW_MEAN(M), the row means.
#
  import numpy as np

  mean = np.zeros ( m )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      mean[i] = mean[i] + a[i,j]
    mean[i] = mean[i] / float ( n )

  return mean

def r8row_mean_test ( ):

#*****************************************************************************80
#
## R8ROW_MEAN_TEST tests R8ROW_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 April 2016
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
  print ( 'R8ROW_MEAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8ROW_MEAN computes row means of an R8ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = float ( k )

  r8mat_print ( m, n, a, '  The matrix:' )

  means = r8row_mean ( m, n, a )

  r8vec_print ( m, means, '  The row means:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8ROW_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8row_mean_test ( )
  timestamp ( )
 
