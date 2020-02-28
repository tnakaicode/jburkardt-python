#! /usr/bin/env python
#
def r8vec_variance_sample ( n, a ):

#*****************************************************************************80
#
## R8VEC_VARIANCE_SAMPLE returns the sample variance of an R8VEC.
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
#    03 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in the vector.
#
#    Input, real A(N), the vector.
#
#    Output, real VALUE, the variance of the vector.
#
  import numpy as np
  if ( n < 2 ):

    value = 0.0

  else:

    mean = np.sum ( a[0:n] ) / n

    value = np.sum ( ( a[0:n] - mean ) ** 2 ) / ( n - 1 )

  return value

def r8vec_variance_sample_test ( ):

#*****************************************************************************80
#
## R8VEC_VARIANCE_SAMPLE_TEST tests R8VEC_VARIANCE_SAMPLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    02 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'R8VEC_VARIANCE_SAMPLE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_VARIANCE_SAMPLE computes the sample variance of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_variance_sample ( n, a )
  print ( '' )
  print ( '  Sample variance = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_VARIANCE_SAMPLE_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_variance_sample_test ( )
  timestamp ( )

