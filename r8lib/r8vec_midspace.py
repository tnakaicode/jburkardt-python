#! /usr/bin/env python
#
def r8vec_midspace ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_MIDSPACE creates a vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    This function divides the interval [a,b] into n subintervals, and then
#    returns the midpoints of those subintervals.
#
#  Example:
#
#    N = 5, A = 10, B = 20
#    X = [ 11, 13, 15, 17, 19 ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the endpoints of the interval.
#
#    Output, real X(N), a vector of linearly spaced data.
#
  import numpy as np
  
  if ( n == 1 ):
    x = ( a + b ) / 2.0
  else:
    a2 = a + ( b - a ) / 2.0 / float ( n )
    b2 = b - ( b - a ) / 2.0 / float ( n )
    x = np.linspace ( a2, b2, n )

  return x

def r8vec_midspace_test ( ):

#*****************************************************************************80
#
## R8VEC_MIDSPACE_TEST tests R8VEC_MIDSPACE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 January 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8VEC_MIDSPACE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_MIDSPACE returns the midpoints of N intervals in [A,B].' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_midspace ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The midspace vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_MIDSPACE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_midspace_test ( )
  timestamp ( )
