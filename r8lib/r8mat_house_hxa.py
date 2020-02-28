#! /usr/bin/env python
#
def r8mat_house_hxa ( n, a, v ):

#*****************************************************************************80
#
## R8MAT_HOUSE_HXA computes H*A where H is a compact Householder matrix.
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
#    14 March 2015
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
#    Output, real HA(N,N), the product H*A.
#
  import numpy as np

  vtv = 0.0
  for i in range ( 0, n ):
    vtv = vtv + v[i] ** 2

  ha = np.zeros ( ( n, n ) )
 
  for j in range ( 0, n ):
    for i in range ( 0, n ):
      ha[i,j] = a[i,j]
      for k in range ( 0, n ):
        ha[i,j] = ha[i,j] - 2.0 * v[i] * v[k] * a[k,j] / vtv
            
  return ha

def r8mat_house_hxa_test ( ):

#*****************************************************************************80
#
## R8MAT_HOUSE_HXA_TEST tests R8MAT_HOUSE_HXA.
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
  print ( 'R8MAT_HOUSE_HXA_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_HOUSE_HXA multiplies a compact Householder matrix H' )
  print ( '  times a matrix A.' )

  r8_lo = -5.0
  r8_hi = +5.0
  seed = 123456789

  a, seed = r8mat_uniform_ab ( n, n, r8_lo, r8_hi, seed )

  r8mat_print ( n, n, a, '  Matrix A:' )
#
#  Request V, the compact form of the Householder matrix H
#  such that H*A' packs column 3 of A'.
#
  k = 3
  a_row = np.zeros ( n )
  for j in range ( 0, n ):
    a_row[j] = a[k,j]

  v = r8vec_house_column ( n, a_row, k )

  r8vec_print ( n, v, '  Compact vector form V:' )

  h = r8mat_house_form ( n, v )

  r8mat_print ( n, n, h, '  Householder matrix H:' )
#
#  Compute H*A.
#
  ha = r8mat_house_hxa ( n, a, v )

  r8mat_print ( n, n, ha, '  Indirect product H*A:' )
#
#  Compare with a direct calculation.
#
  ha = r8mat_mm ( n, n, n, h, a )

  r8mat_print ( n, n, ha, '  Direct product H*A:' )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_HOUSE_HXA_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_house_hxa_test ( )
  timestamp ( )
 
