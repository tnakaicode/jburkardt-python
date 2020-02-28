#! /usr/bin/env python
#
def r8vec_cheby_extreme ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_CHEBY_EXTREME creates Chebyshev Extreme values in [A,B].
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
#    30 June 2015
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
#    Output, real X(N), a vector of Chebyshev spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  if ( n == 1 ):
    x[0] = ( a + b ) / 2.0
  else:
    for i in range ( 0, n ):

      theta = float ( n - i - 1 ) * np.pi / float ( n - 1 )

      c = np.cos ( theta )

      if ( ( n % 2 ) == 1 ):
        if ( 2 * i + 1 == n ):
          c = 0.0

      x[i] = ( ( 1.0 - c ) * a  \
             + ( 1.0 + c ) * b ) \
             /   2.0
 
  return x

def r8vec_cheby_extreme_test ( ):

#*****************************************************************************80
#
## R8VEC_CHEBY_EXTREME_TEST tests R8VEC_CHEBY_EXTREME.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 June 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8VEC_CHEBY_EXTREME_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_CHEBY_EXTREME returns Chebyshev Extreme values between A and B.' )

  n = 5
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_cheby_extreme ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_CHEBY_EXTREME_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_cheby_extreme_test ( )
  timestamp ( )
 
