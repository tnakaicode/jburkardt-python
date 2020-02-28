#! /usr/bin/env python
#
def r8vec_linspace2 ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_LINSPACE2 creates a vector of linearly spaced values.
#
#  Discussion:
#
#    An R8VEC is a vector of R8's.
#
#    5 points evenly spaced between 0 and 12 will yield 2, 4, 6, 8, 10.
#
#    In other words, the interval is divided into N+1 even subintervals,
#    and the endpoints of internal intervals are used as the points.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 August 2016
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
#    Output, real X(N), a vector of linearly spaced data.
#
  import numpy as np

  x = np.zeros ( n )

  for i in range ( 0, n ):
    x[i] = ( float ( n - i     ) * a \
           + float (     i + 1 ) * b ) \
           / float ( n     + 1 )
 
  return x

def r8vec_linspace2_test ( ):

#*****************************************************************************80
#
## R8VEC_LINSPACE2_TEST tests R8VEC_LINSPACE2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 September 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_print import r8vec_print

  print ( '' )
  print ( 'R8VEC_LINSPACE2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_LINSPACE2 returns evenly spaced values between A and B' )
  print ( '  omitting the endpoints.' )

  n = 4
  x_lo = 10.0
  x_hi = 20.0
  x = r8vec_linspace2 ( n, x_lo, x_hi )

  r8vec_print ( n, x, '  The linspace2 vector:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_LINSPACE2_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_linspace2_test ( )
  timestamp ( )
