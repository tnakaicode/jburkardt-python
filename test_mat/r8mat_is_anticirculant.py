#! /usr/bin/env python
#
def r8mat_is_anticirculant ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_ANTICIRCULANT checks whether A is an anticirculant matrix.
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
#    Input, integer M, N, the row and column dimensions of 
#    the matrix.  M and N must be positive.
#
#    Input, real A(M,N), the matrix.
#
#    Output, bool VALUE, is True if the matrix is an
#    anticirculant matrix.
#
  value = True

  for i in range ( 1, m ):
    for j in range ( 0, n ):

      k = ( ( j + i ) % n )

      if ( a[i,j] != a[0,k] ):
        value = False
        return value

  return value

def r8mat_is_anticirculant_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_ANTICIRCULANT_TEST tests R8MAT_IS_ANTICIRCULANT.
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
  print ( 'R8MAT_IS_ANTICIRCULANT_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_ANTICIRCULANT reports whether a matrix' )
  print ( '  is an anticirculant matrix.' )
#
#  Circulant
#
  m = 4
  n = 5
  a = np.array ( [ \
    [ 0, 1, 2, 3, 4 ], \
    [ 4, 0, 1, 2, 3 ], \
    [ 3, 4, 0, 1, 2 ], \
    [ 2, 3, 4, 0, 1 ] ] )
  r8mat_print ( m, n, a, '  Circulant matrix:' )
  value = r8mat_is_anticirculant ( m, n, a )
  print ( '' )
  print ( '  Anticirculant = %s' % ( value ) )
#
#  Anticirculant.
#
  m = 4
  n = 5
  a = np.array ( [ \
    [ 0, 1, 2, 3, 4 ], \
    [ 1, 2, 3, 4, 0 ], \
    [ 2, 3, 4, 0, 1 ], \
    [ 3, 4, 0, 1, 2 ] ] )
  r8mat_print ( m, n, a, '  Anticirculant matrix:' )
  value = r8mat_is_anticirculant ( m, n, a )
  print ( '' )
  print ( '  Anticirculant = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_ANTICIRCULANT_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_anticirculant_test ( )
  timestamp ( )
