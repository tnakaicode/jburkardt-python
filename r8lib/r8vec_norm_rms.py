#! /usr/bin/env python
#
def r8vec_norm_rms ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM_RMS returns the RMS norm of an R8VEC.
#
#  Discussion:
#
#    The vector RMS norm is defined as:
#
#      value = sqrt ( 1/N * sum ( 1 <= I <= N ) A(I)^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2019
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the vector whose norm is desired.
#
#    Output, real VALUE, the norm of A.
#
  import numpy as np

  value = np.sqrt ( (a[0:n]**2).mean() )

  return value

def r8vec_norm_rms_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_RMS_TEST tests R8VEC_NORM_RMS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 July 2018
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'R8VEC_NORM_RMS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM_RMS computes the RMS norm of an R8VEC.' )

  n = 10
  a_lo = - n
  a_hi = + n
  seed = 123456789
  a, seed = r8vec_uniform_ab ( n, a_lo, a_hi, seed )
  r8vec_print ( n, a, '  Input vector:' )
  a_norm = r8vec_norm_rms ( n, a )

  print ( '' )
  print ( '  RMS norm = %g' % ( a_norm ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_RMS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_norm_rms_test ( )
  timestamp ( )
 