#! /usr/bin/env python
#
def r8mat_is_llt ( m, n, a, l ):

#*****************************************************************************80
#
## R8MAT_IS_LLT measures the error in a lower triangular Cholesky factorization.
#
#  Discussion:
#
#    This routine simply returns the Frobenius norm of the M x M matrix:
#      A - L * L' 
#    where L is an M by N lower triangular matrix presumed to be the
#    Cholesky factor of A.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the matrix dimensions.
#
#    Input, real A(M,M), the matrix.
#
#    Input, real L(M,N), the Cholesky factor.
#
#    Output, real VALUE, the Frobenius norm of A-L*L'.
#
  from r8mat_mmt import r8mat_mmt
  from r8mat_norm_fro import r8mat_norm_fro
  from r8mat_sub import r8mat_sub
#
#  D = L * L'.
#
  d = r8mat_mmt ( m, n, m, l, l )
#
#  D = A - L * L'
#
  d = r8mat_sub ( m, m, a, d )
#
#  Take the norm
#
  value = r8mat_norm_fro ( m, m, d )

  return value

def r8mat_is_llt_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_LLT_TEST tests R8MAT_IS_LLT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print
  from r8vec_print import r8vec_print

  m = 4
  n = 4
  a = np.array ( [ \
    [ 2.0, 1.0, 0.0, 0.0 ], \
    [ 1.0, 2.0, 1.0, 0.0 ], \
    [ 0.0, 1.0, 2.0, 1.0 ], \
    [ 0.0, 0.0, 1.0, 2.0 ] ] )

  l = np.array ( [ \
    [ 1.414213562373095, 0.0,               0.0,               0.0 ], \
    [ 0.707106781186547, 1.224744871391589, 0.0,               0.0 ], \
    [ 0.0,               0.816496580927726, 1.154700538379251, 0.0 ], \
    [ 0.0,               0.0,               0.866025403784439, 1.118033988749895 ] ] )

  print ( '' )
  print ( 'R8MAT_IS_LLT_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_LLT tests the error in a lower triangular Cholesky' )
  print ( '  factorization ||A-L*L\'||.' )

  r8mat_print ( m, m, a, '  Matrix A:' )
  r8mat_print ( m, n, l, '  Factor L:' )

  value = r8mat_is_llt ( m, n, a, l )

  print ( '' )
  print ( '  Frobenius norm of A-L*L\' is %g' % (value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_LLT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_llt_test ( )
  timestamp ( )
