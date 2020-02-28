#! /usr/bin/env python
#
def r8vec_cheby2space ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_CHEBY2SPACE creates a vector of Type 2  Chebyshev values in [A,B].
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A, B, the first and last entries.
#
#    Output, real X(N), a vector of Type 2 Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):

    theta = float ( n - i ) * np.pi / float ( n + 1 )

    c = np.cos ( theta )

    x[i] = ( ( 1.0 - c ) * a  \
           + ( 1.0 + c ) * b ) \
           /   2.0
 
  return x

def r8vec_cheby2space_test ( ):

#*****************************************************************************80
#
## R8VEC_CHEBY2SPACE_TEST tests R8VEC_CHEBY2SPACE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 July 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8VEC_CHEBY2SPACE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_CHEBY2SPACE returns Type 2 Chebyshev values in [A,B].' )

  n = 9
  x_lo = 10.0
  x_hi = 20.0

  print ( '  Generate %d points in [%g,%g]' % ( n, x_lo, x_hi ) )

  x = r8vec_cheby2space ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_CHEBY2SPACE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_cheby2space_test ( )
  timestamp ( )
 
