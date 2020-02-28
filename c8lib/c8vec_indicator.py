#! /usr/bin/env python
#
def c8vec_indicator ( n ):

#*****************************************************************************80
#
## C8VEC_INDICATOR sets a C8VEC to the indicator vector.
#
#  Discussion:
#
#    X(1:N) = ( 1-1i, 2-2i, 3-3i, 4-4i, ... )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of elements.
#
#    Output, complex A(N), the array.
#
  import numpy as np

  a = np.zeros ( n, 'complex' )

  for i in range ( 0, n ):
    a[i] = float ( i + 1 ) - float ( i + 1 ) * 1j

  return a

def c8vec_indicator_test ( ):

#*****************************************************************************80
#
## C8VEC_INDICATOR_TEST tests C8VEC_INDICATOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    12 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from c8vec_print import c8vec_print

  print ( '' )
  print ( 'C8VEC_INDICATOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8VEC_INDICATOR returns the indicator vector.' )

  n = 10

  x = c8vec_indicator ( n )

  c8vec_print ( n, x, '  The indicator vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8VEC_INDICATOR_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_indicator_test ( )
  timestamp ( )

