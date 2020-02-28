#! /usr/bin/env python
#
def r8vec_fill ( n, value ):

#*****************************************************************************80
#
## R8VEC_FILL sets all entries of an array to a given value.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    John Burkardt.
#
#  Parameters:
#
#    Input, integer N, the number of elements of A.
#
#    Input, real VALUE, the value.
#
#    Output, real X(N), the array.
#
  import numpy as np

  x = value * np.ones ( n )

  return x

def r8vec_fill_test ( ):

#*****************************************************************************80
#
## R8VEC_FILL_TEST tests R8VEC_FILL.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    03 December 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print

  n = 10
  ahi = 10.0
  alo = 0.0

  print ( '' )
  print ( 'R8VEC_FILL_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_FILL sets all entries of an array to a given value.' )

  n = 5
  value = 1.2
  x = r8vec_fill ( n, value )
  r8vec_print ( n, x, '  x=r8vec_fill(5,1.2):' )

  n = 3
  value = -123.456
  x = r8vec_fill ( n, value )
  r8vec_print ( n, x, '  x=r8vec_fill(3,123.456):' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_FILL_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_fill_test ( )
  timestamp ( )
