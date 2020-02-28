#! /usr/bin/env python
#
def r8vec_scale_ab ( n, x, a, b ):

#*****************************************************************************80
#
## R8VEC_SCALE_AB scales an R8VEC to [A,B].
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 October 2018
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
#    Input, real A, B, the new limits.
#
#    Output, real XS(N), the scaled vector.
#
  import numpy as np

  xs = x.copy ( )
  xmin = np.ndarray.min ( xs )
  xmax = np.ndarray.max ( xs )
  if ( 0.0 < xmax - xmin ):
    xs = a + ( b - a ) * ( xs - xmin ) / ( xmax - xmin )
  else:
    xs = ( a + b ) / 2.0

  return xs

def r8vec_scale_ab_test ( ):

#*****************************************************************************80
#
## R8VEC_SCALE_AB_TEST tests R8VEC_SCALE_AB.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 October 2018
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
  print ( 'R8VEC_SCALE_AB_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SCALE_AB shifts and scales an R8VEC so that' )
  print ( '  it has min A and max B' )

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

  a = -1.0
  b = +1.0
  print ( '' )
  print ( '  Rescale to [%g,%g]' % ( a, b ) )

  xs = r8vec_scale_ab ( n, x, a, b )

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
  print ( 'R8VEC_SCALE_AB_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_scale_ab_test ( )
  timestamp ( )

