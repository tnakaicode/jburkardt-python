#! /usr/bin/env python
#
def fibonacci_floor ( n ):

#*****************************************************************************80
#
## FIBONACCI_FLOOR returns the largest Fibonacci number less than or equal to N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the positive integer whose Fibonacci "floor" is desired.
#
#    Output, integer F, the largest Fibonacci number less than or equal to N.
#
#    Output, integer I, the index of the F.
#
  import numpy as np
  from fibonacci_direct import fibonacci_direct

  i = 0
  f = 0

  if ( 0 < n ):

    i = int ( np.log ( 0.5 * float ( 2 * n + 1 ) * np.sqrt ( 5.0 ) ) \
      / np.log ( 0.5 * ( 1.0 + np.sqrt ( 5.0 ) ) ) )

    f = fibonacci_direct ( i );

    if ( n < f ):
      i = i - 1
      f = fibonacci_direct ( i )

  return f, i

def fibonacci_floor_test ( ):

#*****************************************************************************80
#
## FIBONACCI_FLOOR_TEST tests FIBONACCI_FLOOR.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 February 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'FIBONACCI_FLOOR_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  FIBONACCI_FLOOR computes the largest Fibonacci number' )
  print ( '  less than or equal to N.' )
  print ( '' )
  print ( '     N  Fibonacci  Index' )
  print ( '' )

  for n in range ( 0, 21 ):
    f, i = fibonacci_floor ( n )
    print ( '  %4d  %4d  %4d' % ( n, f, i ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'FIBONACCI_FLOOR_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  fibonacci_floor_test ( )
  timestamp ( )
