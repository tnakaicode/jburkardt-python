#! /usr/bin/env python
#
def r8mat_norm_fro_affine ( m, n, a1, a2 ):

#*****************************************************************************80
#
## R8MAT_NORM_FRO_AFFINE returns the Frobenius norm of an R8MAT difference.
#
#  Discussion:
#
#    The Frobenius norm is defined as
#
#      value = sqrt ( sum ( 1 <= I <= M ) sum ( 1 <= j <= N ) A(I,J)^2 )
#
#    The matrix Frobenius norm is not derived from a vector norm, but
#    is compatible with the vector L2 norm, so that:
#
#      vec_norm_l2 ( A * x ) <= mat_norm_fro ( A ) * vec_norm_l2 ( x ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 July 2015
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
#    Input, real A1(M,N), A2(M,N), the matrices for whose difference 
#    the Frobenius norm is desired.
#
#    Output, real VALUE, the Frobenius norm of A1 - A2.
#
  import numpy as np
 
  value = np.sqrt ( sum ( sum ( ( a1 - a2 ) ** 2 ) ) )

  return value

def r8mat_norm_fro_affine_test ( ):

#*****************************************************************************80
#
## R8MAT_NORM_FRO_AFFINE_TEST tests R8MAT_NORM_FRO_AFFINE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    28 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_uniform_01 import r8mat_uniform_01

  m = 5
  n = 4
  seed = 123456789
  a, seed = r8mat_uniform_01 ( m, n, seed )
  b, seed = r8mat_uniform_01 ( m, n, seed )

  print ( '' )
  print ( 'R8MAT_NORM_FRO_AFFINE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_NORM_FRO_AFFINE computes the Frobenius norm' )
  print ( '  of the difference of two R8MAT\'s;' )

  t1 = 0.0
  for i in range ( 0, m ):
    for j in range ( 0, n ):
      t1 = t1 + ( a[i,j] - b[i,j] ) ** 2

  t1 = np.sqrt ( t1 );

  t2 = r8mat_norm_fro_affine ( m, n, a, b );

  print ( '' )
  print ( '  Expected norm = %g' % ( t1 ) )
  print ( '  Computed norm = %g' % ( t2 ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_NORM_FRO_AFFINE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_norm_fro_affine_test ( )
  timestamp ( )

