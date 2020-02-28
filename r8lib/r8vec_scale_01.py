#! /usr/bin/env python
#
def r8vec_scale_01 ( n, x ):

#*****************************************************************************80
#
## R8VEC_SCALE_01 scales an R8VEC to [0,1].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 October 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real X(N), the vector to be scaled.
#
#    Output, real XS(N), the scaled vector.
#
  import numpy as np

  xs = x.copy ( )
  xmin = np.ndarray.min ( xs )
  xmax = np.ndarray.max ( xs )
  if ( 0.0 < xmax - xmin ):
    xs = ( xs - xmin ) / ( xmax - xmin )
  else:
    xs = 0.5

  return xs

def r8vec_scale_01_test ( ):

#*****************************************************************************80
#
## R8VEC_SCALE_01_TEST tests R8VEC_SCALE_01.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 October 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'R8VEC_SCALE_01_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SCALE_01 shifts and scales an R8VEC so that' )
  print ( '  it has min 0 and max 1' )

  n = 10
  a = -5.0
  b = 15.0
  seed = 123456789

  x, seed = r8vec_uniform_ab ( n, a, b, seed )
 
  r8vec_print ( n, x, '  Vector X:' )
  mu = np.mean ( x )
  sigma = np.std ( x )
  xmin = np.ndarray.min ( x )
  xmax = np.ndarray.max ( x )
  print ( '' )
  print ( '  mean(X) = %g' % ( mu ) )
  print ( '  std(X)  = %g' % ( sigma ) )
  print ( '  max(X)  = %g' % ( xmax ) )
  print ( '  min(X)  = %g' % ( xmin ) )

  xs = r8vec_scale_01 ( n, x )

  r8vec_print ( n, xs, '  Vector XS:' )
  mu = np.mean ( xs )
  sigma = np.std ( xs )
  xmin = np.ndarray.min ( xs )
  xmax = np.ndarray.max ( xs )
  print ( '' )
  print ( '  mean(XS) = %g' % ( mu ) )
  print ( '  std(XS)  = %g' % ( sigma ) )
  print ( '  max(XS)  = %g' % ( xmax ) )
  print ( '  min(XS)  = %g' % ( xmin ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SCALE_01_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_scale_01_test ( )
  timestamp ( )
 
