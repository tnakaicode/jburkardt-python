#! /usr/bin/env python
#
def r8vec_smooth ( n, x, s ):

#*****************************************************************************80
#
## r8vec_smooth smooths an R8VEC.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    Except for the beginning and ending entries, the vector values
#    are replaced by averages of 2*S+1 neighbors.
#
#  Example:
#
#    S = 2
#
#    Z(1)   =                     X(1)
#    Z(2)   = (          X(1)   + X(2)   + X(3) ) / 3
#    Z(3)   = ( X(1)   + X(2)   + X(3)   + X(4)   + X(5) ) / 5
#    Z(4)   = ( X(2)   + X(3)   + X(4)   + X(5)   + X(6) ) / 5
#    ...
#    Z(N-2) = ( X(N-4) + X(N-3) + X(N-2) + X(N-1) + X(N) ) / 5
#    Z(N-1) =          ( X(N-2) + X(N-1) + X(N) ) / 3
#    Z(N) =                       X(N)
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of X.
#
#    Input, real X(N), the vector to be smoothed.
#
#    Output, real Z(N), the smoothed vector.
#
  import numpy as np

  z = np.zeros ( n )

  for j in range ( 1, s + 1 ):
    z[j-1] = np.sum ( x[0:2*j-1] ) / ( 2 * j - 1 )

  for j in range ( s + 1, n - s + 1 ):
    z[j-1] = np.sum ( x[j-s-1:j+s] ) / ( 2 * s + 1 )

  for j in range ( s, 0, -1 ):
    z[n-j] = np.sum ( x[n-(2*j-1):n] ) / ( 2 * j - 1 )

  return z

def r8vec_smooth_test ( ):

#*****************************************************************************80
#
## r8vec_smooth_test tests r8vec_smooth.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 April 2019
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'r8vec_smooth_test' )
  print ( '  r8vec_smooth smooths an R8VEC.' )

  n = 10
  x = np.linspace ( 1, n, n )
  r8vec_print ( n, x, '  The vector X:' )
  s = 2
  z = r8vec_smooth ( n, x, s )
  label = ( '  Vector X using smoothing S = %d' % ( s ) )
  r8vec_print ( n, z, label )

  n = 10
  x = np.linspace ( 1, n, n )
  x = x ** 2
  r8vec_print ( n, x, '  The vector X:' )
  s = 1
  z = r8vec_smooth ( n, x, s )
  label = ( '  Vector X using smoothing S = %d' % ( s ) )
  r8vec_print ( n, z, label )
#
#  Terminate.
#
  print ( '' )
  print ( 'r8vec_smooth_test:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_smooth_test ( )
  timestamp ( )

