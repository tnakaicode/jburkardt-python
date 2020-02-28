#! /usr/bin/env python
#
def r8vec_norm_l1 ( n, a ):

#*****************************************************************************80
#
## R8VEC_NORM_L1 returns the L1 norm of an R8VEC.
#
#  Discussion:
#
#    The vector L1 norm is defined as:
#
#      value = sum ( 1 <= I <= N ) abs ( A(I) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), the vector whose L1 norm is desired.
#
#    Output, real VALUE, the L1 norm of A.
#
  value = 0.0
  for i in range ( 0, n ):
    value = value + abs ( a[i] )

  return value

def r8vec_norm_l1_test ( ):

#*****************************************************************************80
#
## R8VEC_NORM_L1_TEST tests R8VEC_NORM_L1.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    06 July 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  n = 10

  print ( '' )
  print ( 'R8VEC_NORM_L1_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_NORM_L1 computes the L1 norm of an R8VEC.' )
 
  r8_lo = - 10.0
  r8_hi = + 10.0

  seed = 123456789

  a, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
 
  r8vec_print ( n, a, '  Input vector:' )

  value = r8vec_norm_l1 ( n, a )

  print ( '' )
  print ( '  L1 norm = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_NORM_L1_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_norm_l1_test ( )
  timestamp ( )

