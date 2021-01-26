#! /usr/bin/env python
#
def r8mat_is_square ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_SQUARE checks whether A is square.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
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
#    Output, bool R8MAT_IS_SQUARE, is True if the matrix is square.
#
  if ( m == n ):
    value = True
  else:
    value = False

  return value

def r8mat_is_square_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_SQUARE_TEST tests R8MAT_IS_SQUARE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_IS_SQUARE_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_SQUARE reports whether a matrix' )
  print ( '  is square.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_square ( m, n, a )
  print ( '' )
  print ( '  Square = %s' % ( value ) )
#
#  Square.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 1, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 1, 0, 1, 0 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Square matrix:' )
  value = r8mat_is_square ( m, n, a )
  print ( '' )
  print ( '  Square = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_SQUARE_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_square_test ( )
  timestamp ( )
