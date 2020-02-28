#! /usr/bin/env python
#
def i4row_variance ( m, n, x ):

#*****************************************************************************80
#
## I4ROW_VARIANCE returns the variances of an I4ROW.
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
#    Input, integer X(M,N), the I4ROW whose row means are desired.
#
#    Output, real VARIANCE(M), the variances of the rows of X.
#
  import numpy as np

  variance = np.zeros ( m, dtype = np.float32 )

  for i in range ( 0, m ):

    mean = 0.0
    for j in range ( 0, n ):
      mean = mean + x[i,j]
    mean = mean / float ( n )

    for j in range ( 0, n ):
      variance[i] = variance[i] + ( x[i,j] - mean ) ** 2

    if ( 1 < n ):
      variance[i] = variance[i] / float ( n - 1 )
    else:
      variance[i] = 0.0 

  return variance

def i4row_variance_test ( ):

#*****************************************************************************80
#
## I4ROW_VARIANCE_TEST tests I4ROW_VARIANCE.
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
  from i4mat_print import i4mat_print
  from r8vec_print import r8vec_print

  m = 3
  n = 4

  print ( '' )
  print ( 'I4ROW_VARIANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4ROW_VARIANCE computes variances of an I4ROW.' )

  a = np.zeros ( [ m, n ], dtype = np.int32 )
  k = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      k = k + 1
      a[i,j] = k

  i4mat_print ( m, n, a, '  The matrix:' )

  variance = i4row_variance ( m, n, a )

  r8vec_print ( m, variance, '  The row variances:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4ROW_VARIANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4row_variance_test ( )
  timestamp ( )
