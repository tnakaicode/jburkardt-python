#! /usr/bin/env python
#
def i4vec_dot_product ( n, x, y ):

#*****************************************************************************80
#
## I4VEC_DOT_PRODUCT computes the dot product of two I4VEC's.
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
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the size of the array.
#
#    Input, integer X(N), Y(N), the arrays.
#
#    Output, integer I4VEC_DOT_PRODUCT, the dot product of X and Y.
#
  value = 0
  for i in range ( 0, n ):
    value = value + x[i] * y[i]

  return value

def i4vec_dot_product_test ( ):

#*****************************************************************************80
#
## I4VEC_DOT_PRODUCT_TEST tests I4VEC_DOT_PRODUCT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 December 2015
#
#  Author:
#
#    John Burkardt
#
  import platform
  from i4vec_print import i4vec_print
  from i4vec_uniform_ab import i4vec_uniform_ab

  print ( '' )
  print ( 'I4VEC_DOT_PRODUCT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4VEC_DOT_PRODUCT computes the dot product of two I4VECs.' )

  n = 5
  lo = 0
  hi = 10
  seed = 123456789

  a, seed = i4vec_uniform_ab ( n, lo, hi, seed )
  i4vec_print ( n, a, '  The vector A:' )

  b, seed = i4vec_uniform_ab ( n, lo, hi, seed )
  i4vec_print ( n, b, '  The vector B:' )

  d = i4vec_dot_product ( n, a, b )
  print ( '' )
  print ( '  The dot product is %d' % ( d ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4VEC_DOT_PRODUCT_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4vec_dot_product_test ( )
  timestamp ( )
 
