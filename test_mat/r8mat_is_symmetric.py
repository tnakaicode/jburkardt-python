#! /usr/bin/env python
#
def r8mat_is_symmetric ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_SYMMETRIC checks whether A is a symmetric matrix.
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
#    Output, bool R8MAT_IS_SYMMETRIC, is True if the matrix is symmetric.
#
  import numpy as np
  from r8mat_is_square import r8mat_is_square

  if ( not r8mat_is_square ( m, n, a ) ):
    return False

  t = 0.0
  for i in range ( 0, m ):
    for j in range ( i + 1, n ):
      t = t + ( a[i,j] - a[j,i] ) ** 2

  print ( 'T = %g' % ( t ) )
  tol = 0.00001

  if ( t < tol ):
    value = True
  else:
    value = False

  return value

def r8mat_is_symmetric_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_SYMMETRIC_TEST tests R8MAT_IS_SYMMETRIC.
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
  print ( 'R8MAT_IS_SYMMETRIC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_SYMMETRIC reports whether a matrix' )
  print ( '  is symmetric.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_symmetric ( m, n, a )
  print ( '' )
  print ( '  Symmetric = %s' % ( value ) )
#
#  Square, but not symmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 1, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 1, 0, 1, 0 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Not symmetric matrix:' )
  value = r8mat_is_symmetric ( m, n, a )
  print ( '' )
  print ( '  Symmetric = %s' % ( value ) )
#
#  Symmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 2, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 2, 0, 1, 1 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Symmetric matrix:' )
  value = r8mat_is_symmetric ( m, n, a )
  print ( '' )
  print ( '  Symmetric = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_SYMMETRIC_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_symmetric_test ( )
  timestamp ( )
