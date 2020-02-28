#! /usr/bin/env python
#
def i4vec_variance ( n, x ):

#*****************************************************************************80
#
## I4VEC_VARIANCE returns the variance of an I4VEC.
#
#  Discussion:
#
#    An I4VEC is a vector of I4's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, integer X(N), the vector.
#
#    Output, real VALUE, the variance of the vector.
#
  import numpy as np

  mean = 0.0
  for i in range ( 0, n ):
    mean = mean + float ( x[i] )
  mean = mean / float ( n )

  value = 0.0
  for i in range ( 0, n ):
    value = value + ( float ( x[i] ) - mean ) ** 2

  value = value / float ( n - 1 )

  return value

def i4vec_variance_test ( ):

#*****************************************************************************80
#
## I4VEC_VARIANCE_TEST tests I4VEC_VARIANCE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 March 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ( '' )
  print ( 'I4VEC_VARIANCE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_VARIANCE computes the variance of an I4VEC.' )

  n = 10
  i4_lo = -5
  i4_hi = +5
  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, i4_lo, i4_hi, seed )

  i4vec_print ( n, a, '  Input vector:' )

  value = i4vec_variance ( n, a )

  print ( '' )
  print ( '  Value = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_VARIANCE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_variance_test ( )
  timestamp ( )

