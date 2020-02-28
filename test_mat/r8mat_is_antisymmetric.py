#! /usr/bin/env python
#
def r8mat_is_antisymmetric ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_ANTISYMMETRIC checks whether A is an antisymmetric matrix.
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
#    Output, bool R8MAT_IS_ANTISYMMETRIC, True if the matrix is antisymmetric.
#
  import numpy as np
  from r8mat_is_square import r8mat_is_square

  if ( not r8mat_is_square ( m, n, a ) ):
    return False

  t = 0.0
  for i in range ( 0, m ):
    t = t + a[i,i] ** 2
    for j in range ( i + 1, n ):
      t = t + ( a[i,j] + a[j,i] ) ** 2

  tol = 0.00001

  if ( t < tol ):
    value = True
  else:
    value = False

  return value

def r8mat_is_antisymmetric_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_ANTISYMMETRIC_TEST tests R8MAT_IS_ANTISYMMETRIC.
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
  print ( 'R8MAT_IS_ANTISYMMETRIC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_ANTISYMMETRIC reports whether a matrix' )
  print ( '  is antisymmetric.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_antisymmetric ( m, n, a )
  print ( '' )
  print ( '  Antisymmetric = %s' % ( value ) )
#
#  Square, but not antisymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [  0,  5,  1, -2 ], \
    [ -5,  0,  3,  0 ], \
    [  1, -3,  6,  4 ], \
    [  2,  0, -4,  0 ] ] )
  r8mat_print ( m, n, a, '  Not antisymmetric matrix:' )
  value = r8mat_is_antisymmetric ( m, n, a )
  print ( '' )
  print ( '  Antisymmetric = %s' % ( value ) )
#
#  Antisymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [  0,  5, -1, -2 ], \
    [ -5,  0,  3,  0 ], \
    [  1, -3,  0,  4 ], \
    [  2,  0, -4,  0 ] ] )
  r8mat_print ( m, n, a, '  Antisymmetric matrix:' )
  value = r8mat_is_antisymmetric ( m, n, a )
  print ( '' )
  print ( '  Antisymmetric = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_ANTISYMMETRIC_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_antisymmetric_test ( )
  timestamp ( )
