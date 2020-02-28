#! /usr/bin/env python
#
def r8vec_dot_product ( n, v1, v2 ):

#*****************************************************************************80
#
## R8VEC_DOT_PRODUCT finds the dot product of a pair of R8VEC's.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real V1(N), V2(N), the vectors.
#
#    Output, real VALUE, the dot product.
#

  value = 0.0
  for i in range ( 0, n ):
    value = value + v1[i] * v2[i]

  return value

def r8vec_dot_product_test ( ):

#*****************************************************************************80
#
## R8VEC_DOT_PRODUCT_TEST tests R8VEC_DOT_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    04 February 2016
#
#  Author:
#
#    John Burkardt
#
  import platform
  from r8vec_uniform_01 import r8vec_uniform_01
  from r8vec2_print import r8vec2_print

  print ( '' )
  print ( 'R8VEC_DOT_PRODUCT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8VEC_DOT_PRODUCT computes the dot product of two R8VEC\'s.' )

  n = 10
  seed = 123456789
  v1, seed = r8vec_uniform_01 ( n, seed )
  v2, seed = r8vec_uniform_01 ( n, seed )
  r8vec2_print ( n, v1, v2, '  V1 and V2:' )

  value = r8vec_dot_product ( n, v1, v2 )

  print ( '' )
  print ( '  V1 dot V2 = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8VEC_DOT_PRODUCT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8vec_dot_product_test ( )
  timestamp ( )
 
