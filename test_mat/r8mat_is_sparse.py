#! /usr/bin/env python
#
def r8mat_is_sparse ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_SPARSE checks whether a matrix is sparse.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the order of the matrix.
#
#    Input, real A(M,N), the matrix.
#
#    Output, real FNORM, the number of nonzero entries divided by M * N.
#
  ival = 0
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( a[i,j] != 0.0 ):
        ival = ival + 1

  fnorm = float ( ival ) / float ( m ) / float ( n )

  return fnorm

def r8mat_is_sparse_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_SPARSE_TEST tests R8MAT_IS_SPARSE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_IS_SPARSE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_SPARSE reports whether a matrix' )
  print ( '  is sparse.' )
#
#  Maximal sparse
#
  m = 3
  n = 4
  a = np.zeros ( [ m, n ] )

  r8mat_print ( m, n, a, '  Zero matrix:' )
  value = r8mat_is_sparse ( m, n, a )
  print ( '' )
  print ( '  Sparseness = %g' % ( value ) )
#
#  Rather sparse
#
  m = 3
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0
  r8mat_print ( m, n, a, '  Identity-like matrix:' )
  value = r8mat_is_sparse ( m, n, a )
  print ( '' )
  print ( '  Sparseness = %g' % ( value ) )
#
#  Hardly sparse
#
  m = 4
  n = 4
  a = np.array ( [ \
    [  0,  1,  2,  3 ], \
    [  4,  5,  6,  7 ], \
    [  8,  9, 10, 11 ], \
    [ 12, 13, 14, 15 ] ] )
  r8mat_print ( m, n, a, '  Hardly sparse:' )
  value = r8mat_is_sparse ( m, n, a )
  print ( '' )
  print ( '  Sparseness = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_SPARSE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_sparse_test ( )
  timestamp ( )
