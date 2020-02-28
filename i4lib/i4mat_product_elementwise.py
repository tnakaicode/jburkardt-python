#! /usr/bin/env python
#
def i4mat_product_elementwise ( m, n, a, b ):

#*****************************************************************************80
#
## I4MAT_PRODUCT_ELEMENTWISE returns the elementwise produce to two I4MAT's.
#
#  Example:
#
#    A = [ 1, 2, 3;    B = [ 1, 3, 5;    product = 86
#          4, 5, 6 ]         2, 4, 6 ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, the number of rows.
#
#    Input, integer N, the number of columns.
#
#    Input, integer A(M,N), B(M,N), the two matrices.
#
#    Output, integer VALUE, the elementwise product of A and B.
#
  value = 0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      value = value + a[i,j] * b[i,j]

  return value

def i4mat_product_elementwise_test ( ):

#*****************************************************************************80
#
## I4MAT_PRODUCT_ELEMENTWISE_TEST tests I4MAT_PRODUCT_ELEMENTWISE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 March 2018
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from i4mat_print import i4mat_print

  print ( '' )
  print ( 'I4MAT_PRODUCT_ELEMENTWISE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  I4MAT_PRODUCT_ELEMENTWISE computes the elementwise' )
  print ( '  product of two I4MATs.' )

  m = 2
  n = 3

  a = np.array ( [ \
    [ 1, 2, 3 ], \
    [ 4, 5, 6 ] ] )

  b = np.array ( [ \
    [ 1, 3, 5 ], \
    [ 2, 4, 6 ] ])

  i4mat_print ( m, n, a, '  A:' )
  i4mat_print ( m, n, b, '  B:' )

  t = i4mat_product_elementwise ( m, n, a, b )
 
  print ( '' );
  print ( '  Elementwise product = %d' % ( t ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'I4MAT_PRODUCT_ELEMENTWISE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  i4mat_product_elementwise_test ( )
  timestamp ( )
