#! /usr/bin/env python
#
def r8mat_scale_ab ( m, n, x, a, b ):

#*****************************************************************************80
#
## R8MAT_SCALE_AB scales the columns of an R8MAT to [A,B].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of entries in the vector.
#
#    Input, real X(M,N), the array to be scaled.
#
#    Input, real A, B, the new minimum and maximum.
#
#    Output, real XS(M,N), the scaled array.
#
  import numpy as np

  xmin = np.ndarray.min ( x, axis = 0 )
  xmax = np.ndarray.max ( x, axis = 0 )
  xs = np.zeros ( [ m, n ] )
  for j in range ( 0, n ):
    if ( 0.0 < xmax[j] - xmin[j] ):
      xs[0:m,j] = a + ( b - a ) * ( x[0:m,j] - xmin[j] ) / ( xmax[j] - xmin[j] )
    else:
      xs[0:m,j] = ( a + b ) / 2.0

  return xs

def r8mat_scale_ab_test ( ):

#*****************************************************************************80
#
## R8MAT_SCALE_AB_TEST tests R8MAT_SCALE_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    08 October 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8mat_uniform_ab import r8mat_uniform_ab
  from r8vec_transpose_print import r8vec_transpose_print

  print ( '' )
  print ( 'R8MAT_SCALE_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_SCALE_AB shifts and scales the columns of an R8MAT' )
  print ( '  so they each have min A and max B' )

  m = 5
  n = 3
  a = -5.0
  b = 15.0
  seed = 123456789

  x, seed = r8mat_uniform_ab ( m, n, a, b, seed )
 
  r8mat_print ( m, n, x, '  Array X:' )
  mu = np.mean ( x, axis = 0 )
  sigma = np.std ( x, axis = 0 )
  xmax = np.ndarray.max ( x, axis = 0 )
  xmin = np.ndarray.min ( x, axis = 0 )
  print ( '' )
  r8vec_transpose_print ( n, mu, '  mean(X):' )
  r8vec_transpose_print ( n, sigma, '  std(X):' )
  r8vec_transpose_print ( n, xmax, '  max(X):' )
  r8vec_transpose_print ( n, xmin, '  min(X):' )

  a = -1.0
  b = +1.0
  print ( '' )
  print ( '  Scaling data to [%g,%g]' % ( a, b ) )

  xs = r8mat_scale_ab ( m, n, x, a, b )

  r8mat_print ( m, n, xs, '  Array XS:' )
  mu = np.mean ( xs, axis = 0 )
  sigma = np.std ( xs, axis = 0 )
  xmax = np.ndarray.max ( xs, axis = 0 )
  xmin = np.ndarray.min ( xs, axis = 0 )
  print ( '' )
  r8vec_transpose_print ( n, mu, '  mean(XS):' )
  r8vec_transpose_print ( n, sigma, '  std(XS):' )
  r8vec_transpose_print ( n, xmax, '  max(XS):' )
  r8vec_transpose_print ( n, xmin, '  min(XS):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_SCALE_AB_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_scale_ab_test ( )
  timestamp ( )
 
