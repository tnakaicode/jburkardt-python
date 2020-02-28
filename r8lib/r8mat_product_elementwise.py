#! /usr/bin/env python
#
def r8mat_product_elementwise ( m, n, a, b ):

#*****************************************************************************80
#
## R8MAT_PRODUCT_ELEMENTWISE returns the elementwise produce to two R8MAT's.
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
#    Input, real A(M,N), B(M,N), the two matrices.
#
#    Output, real VALUE, the elementwise product of A and B.
#
  value = 0.0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      value = value + a[i,j] * b[i,j]

  return value

def r8mat_product_elementwise_test ( ):

#*****************************************************************************80
#
## R8MAT_PRODUCT_ELEMENTWISE_TEST tests R8MAT_PRODUCT_ELEMENTWISE.
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
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_PRODUCT_ELEMENTWISE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_PRODUCT_ELEMENTWISE computes the elementwise' )
  print ( '  product of two R8MATs.' )

  m = 2
  n = 3

  a = np.array ( [ \
    [ 1.0, 2.0, 3.0 ], \
    [ 4.0, 5.0, 6.0 ] ] )

  b = np.array ( [ \
    [ 1.0, 3.0, 5.0 ], \
    [ 2.0, 4.0, 6.0 ] ])

  r8mat_print ( m, n, a, '  A:' )
  r8mat_print ( m, n, b, '  B:' )

  t = r8mat_product_elementwise ( m, n, a, b )
 
  print ( '' );
  print ( '  Elementwise product = %g' % ( t ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_PRODUCT_ELEMENTWISE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_product_elementwise_test ( )
  timestamp ( )
