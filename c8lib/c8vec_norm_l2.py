#! /usr/bin/env python
#
def c8vec_norm_l2 ( n, c ):

#*****************************************************************************80
#
## C8VEC_NORM_L2 returns the L2 norm of a C8VEC.
#
#  Discussion:
#
#    The vector L2 norm is defined as:
#
#      C8VEC_NORM_L1 =  sqrt ( sum ( 1 <= I <= N ) abs ( A(I) ) ^ 2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the number of entries.
#
#    Input, complex C(N), the vector.
#
#    Output, real VALUE, the number.
#
  import numpy as np

  value = 0.0

  for i in range ( 0, n ):
    value = value + ( abs ( c[i] ) ) ** 2
  value = np.sqrt ( value )

  return value

def c8vec_norm_l2_test ( ):

#*****************************************************************************80
#
## C8VEC_NORM_L2_TEST tests C8VEC_NORM_L2.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    01 March 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from c8vec_indicator import c8vec_indicator
  from c8vec_print import c8vec_print

  print ( '' )
  print ( 'C8VEC_NORM_L2_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  C8VEC_NORM_L2 computes the L2 norm of a C8VEC.' )

  n = 5
  c = c8vec_indicator ( n )

  c8vec_print ( n, c, '  The indicator vector:' )

  value = c8vec_norm_l2 ( n, c )

  print ( '' )
  print ( '  L2 norm = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'C8VEC_NORM_L2_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  c8vec_norm_l2_test ( )
  timestamp ( )


