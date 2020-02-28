#! /usr/bin/env python
#
def r8vec_softmax ( n, x ):

#*****************************************************************************80
#
## R8VEC_SOFTMAX evaluates the SOFTMAX function.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 August 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the vector.
#
#    Input, real X(N), the vector.
#
#    Output, real VALUE(N), the function values.
#
  import numpy as np

  index = np.argmax ( x )
  bottom = np.sum ( np.exp ( x[0:n] - x[index] ) )
  value = np.exp ( x[0:n] - x[index] ) / bottom

  return value

def r8vec_softmax_test ( ):

#*****************************************************************************80
#
## R8VEC_SOFTMAX_TEST tests R8VEC_SOFTMAX.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 August 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_normal_ab import r8vec_normal_ab
  from r8vec2_print import r8vec2_print

  print ( '' )
  print ( 'R8VEC_SOFTMAX_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_SOFTMAX evaluates the softmax function.' )

  n = 10
  seed = 123456789

  x, seed = r8vec_normal_ab ( n, -3.0, +3.0, seed )

  sx = r8vec_softmax ( n, x )

  r8vec2_print ( n, x, sx, '  X, Softmax(X):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_SOFTMAX_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_softmax_test ( )
  timestamp ( )

