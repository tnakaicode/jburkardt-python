#! /usr/bin/env python
#
def r8mat_house_axh ( n, a, v ):

#*****************************************************************************80
#
## R8MAT_HOUSE_AXH computes A*H where H is a compact Householder matrix.
#
#  Discussion:
#
#    The Householder matrix H(V) is defined by
#
#      H(V) = I - 2 * v * v' / ( v' * v )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    24 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of A.
#
#    Input, real A(N,N), the matrix to be postmultiplied.
#
#    Input, real V(N), a vector defining a Householder matrix.
#
#    Output, real AH(N,N), the product A*H.
#
  import numpy as np

  vtv = 0.0
  for i in range ( 0, n ):
    vtv = vtv + v[i] ** 2

  ah = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      ah[i,j] = a[i,j]
      for k in range ( 0, n ):
        ah[i,j] = ah[i,j] - 2.0 * a[i,k] * v[k] * v[j] / vtv
            
  return ah

def r8mat_house_axh_test ( ):

#*****************************************************************************80
#
## R8MAT_HOUSE_AXH_TEST tests R8MAT_HOUSE_AXH.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    19 February 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_house_form import r8mat_house_form
  from r8mat_mm import r8mat_mm
  from r8mat_print import r8mat_print
  from r8mat_uniform_ab import r8mat_uniform_ab
  from r8vec_house_column import r8vec_house_column
  from r8vec_print import r8vec_print

  n = 5

  print ( '' )
  print ( 'R8MAT_HOUSE_AXH_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_HOUSE_AXH multiplies a matrix A times a' )
  print ( '  compact Householder matrix.' )

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789

  a, seed = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, seed )

  r8mat_print ( n, n, a, '  Matrix A:' )
#
#  Request V, the compact form of the Householder matrix H
#  such that H*A packs column 3 of A.
#
  k = 3
  km1 = k - 1
  a_col = np.zeros ( n )
  for i in range ( 0, n ):
    a_col[i] = a[i,km1]

  v = r8vec_house_column ( n, a_col, km1 )

  r8vec_print ( n, v, '  Compact vector V so column 3 of H*A is packed:' )

  h = r8mat_house_form ( n, v )

  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Compute A*H.
#
  ah = r8mat_house_axh ( n, a, v )

  r8mat_print ( n, n, ah, '  Indirect product A*H:' )
#
#  Compare with a direct calculation.
#
  ah = r8mat_mm ( n, n, n, a, h )

  r8mat_print ( n, n, ah, '  Direct product A*H:' )
#
#  Compute H*A to demonstrate packed column 3:
#
  ha = r8mat_mm ( n, n, n, h, a )

  r8mat_print ( n, n, ha, '  H*A should pack column 3:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_HOUSE_AXH_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_house_axh_test ( )
  timestamp ( )
 
