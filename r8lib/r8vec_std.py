#! /usr/bin/env python
#
def r8vec_std ( n, a ):

#*****************************************************************************80
#
## R8VEC_STD returns the standard deviation of an R8VEC.
#
#  Discussion:
#
#    The standard deviation of a vector X of length N is defined as
#
#      mean ( X(1:n) ) = sum ( X(1:n) ) / n
#
#      std ( X(1:n) ) = sqrt ( sum ( ( X(1:n) - mean )^2 ) / n )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 August 2017
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
#    Output, real VALUE, the standard deviation of the vector.
#
  import numpy as np

  if ( n < 2 ):

    value = 0.0

  else:

    mean = np.sum ( a[0:n] ) / n

    std = np.sum ( ( a[0:n] - mean ) ** 2 )

    value = np.sqrt ( std / n )

  return value

def r8vec_std_test ( ):

#*****************************************************************************80
#
## R8VEC_STD_TEST tests R8VEC_STD.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 August 2017
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'R8VEC_STD_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_STD computes the standard deviation of an R8VEC.' )

  n = 10
  r8_lo = - 5.0
  r8_hi = + 5.0
  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_std ( n, a )
  print ( '' )
  print ( '  Value = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_STD_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_std_test ( )
  timestamp ( )

