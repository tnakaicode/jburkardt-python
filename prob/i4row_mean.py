#! /usr/bin/env python
#
def i4row_mean ( m, n, a ):

#*****************************************************************************80
#
## I4ROW_MEAN returns the means of an I4ROW.
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
#    Input, integer M, N, the number of rows and columns.
#
#    Input, integer A(M,N), the I4ROW
#
#    Output, real ROW_MEAN(M), the row means.
#
  import numpy as np

  mean = np.zeros ( m, dtype = np.float64 )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      mean[i] = mean[i] + a[i,j]
    mean[i] = mean[i] / float ( n )

  return mean

def i4row_mean_test ( ):

#*****************************************************************************80
#
## I4ROW_MEAN_TEST tests I4ROW_MEAN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print
  from r8vec_print import r8vec_print

  m = 3
  n = 4

  print ( '' )
  print ( 'I4ROW_MEAN_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4ROW_MEAN computes row means of an I4ROW.' )

  a = np.zeros ( [ m, n ] )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  means = i4row_mean ( m, n, a )

  r8vec_print ( m, means, '  The row means:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4ROW_MEAN_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4row_mean_test ( )
  timestamp ( )
 
