#! /usr/bin/env python
#
def r8vec_variance_circular ( n, x ):

#*****************************************************************************80
#
## R8VEC_VARIANCE_CIRCULAR returns the circular variance of an R8VEC.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real X(N), the vector whose variance is desired.
#
#    Output, real VALUE, the circular variance of the vector entries.
#
  import numpy as np

  mean = 0.0
  for i in range ( 0, n ):
    mean = mean + x[i]
  mean = mean / float ( n )

  c = 0.0
  s = 0.0
  for i in range ( 0, n ):
    c = c + np.cos ( x[i] - mean )
    s = s + np.sin ( x[i] - mean )

  value = s * s + c * c

  value = np.sqrt ( value ) / float ( n )

  value = 1.0 - value

  return value

def r8vec_variance_circular_test ( ):

#*****************************************************************************80
#
## R8VEC_VARIANCE_CIRCULAR_TEST tests R8VEC_VARIANCE_CIRCULAR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 April 2016
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_normal_ab import r8vec_normal_ab
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'R8VEC_VARIANCE_CIRCULAR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_VARIANCE_CIRCULAR computes the circular variance of an R8VEC.' )

  n = 10
  a = - np.pi
  b = + np.pi
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, a, b, seed )

  r8vec_print ( n, x, '  Uniform Vector in [-PI,+PI]:' )
  variance_circular = r8vec_variance_circular ( n, x )

  print ( '' )
  print ( '  Circular variance: %g' % ( variance_circular ) )

  n = 10
  a = 0.0
  b = 1.0
  seed = 123456789
  x, seed = r8vec_normal_ab ( n, a, b, seed )

  r8vec_print ( n, x, '  Normal vector, mean 0, variance 1' )

  variance_circular = r8vec_variance_circular ( n, x )

  print ( '' )
  print ( '  Circular variance: %g' % ( variance_circular ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_VARIANCE_CIRCULAR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_variance_circular_test ( )
  timestamp ( )
