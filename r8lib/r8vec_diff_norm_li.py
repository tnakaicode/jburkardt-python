#! /usr/bin/env python
#
def r8vec_diff_norm_li ( n, a, b ):

#*****************************************************************************80
#
## R8VEC_DIFF_NORM_LI returns the L-infinity norm of the difference of R8VEC's.
#
#  Discussion:
#
#    The vector L-infinity norm is defined as:
#
#      value = max ( 1 <= I <= N ) abs ( A(I) ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries in A.
#
#    Input, real A(N), B(N), the vectors.
#
#    Output, real VALUE, the L-infinity norm of A - B.
#
  value = 0.0
  for i in range ( 0, n ):
    value = max ( value, abs ( a[i] - b[i] ) )

  return value

def r8vec_diff_norm_li_test ( ):

#*****************************************************************************80
#
## R8VEC_DIFF_NORM_LI_TEST tests R8VEC_DIFF_NORM_LI.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 June 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_print import r8vec_print
  from r8vec_uniform_ab import r8vec_uniform_ab

  print ( '' )
  print ( 'R8VEC_DIFF_NORM_LI_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_DIFF_NORM_LI: L-infinity norm of the difference' )
  print ( '  of two R8VEC\'s.' )
 
  n = 5
  r8_lo = -10.0
  r8_hi = +10.0

  seed = 123456789

  v1, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  v2, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )

  r8vec_print ( n, v1, '  Vector V1:' )
  r8vec_print ( n, v2, '  Vector V2:' )

  diff = r8vec_diff_norm_li ( n, v1, v2 )

  print ( '' )
  print ( '  L-Infinity norm of V1-V2: %g' % ( diff ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_DIFF_NORM_LI_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( ) 
  r8vec_diff_norm_li_test ( )
  timestamp ( )

