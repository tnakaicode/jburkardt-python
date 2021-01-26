#! /usr/bin/env python
#
def r8mat_is_persymmetric ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_PERSYMMETRIC checks an R8MAT for persymmetry.
#
#  Discussion:
#
#    An R8MAT is a matrix of real values.
#
#    A is persymmetric if A(I,J) = A(N+1-J,N+1-I).
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
#    Output, real ERROR_FROBENIUS, the Frobenius error
#    in persymmetry, which will be 0 if the matrix is exactly
#    persymmetric.
#
  import numpy as np
  from r8mat_is_square import r8mat_is_square

  if ( not r8mat_is_square ( m, n, a ) ):
    error_frobenius = float ( 'Inf' )
    return error_frobenius

  error_frobenius = 0.0
  for i in range ( 0, m ):
    for j in range ( n - 1, -1, -1 ):
      error_frobenius = error_frobenius + ( a[i,j] - a[n-1-j,m-1-i] ) ** 2

  error_frobenius = np.sqrt ( error_frobenius )

  return error_frobenius

def r8mat_is_persymmetric_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_PERSYMMETRIC_TEST tests R8MAT_IS_PERSYMMETRIC.
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
  print ( 'R8MAT_IS_PERSYMMETRIC_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_PERSYMMETRIC reports whether a matrix' )
  print ( '  is persymmetric.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_persymmetric ( m, n, a )
  print ( '' )
  print ( '  Persymmetric = %g' % ( value ) )
#
#  Square, but not persymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 4, 3, 2, 1 ], \
    [ 7, 6, 5, 3 ], \
    [ 9, 8, 6, 3 ], \
    [10, 7, 7, 4 ] ] )
  r8mat_print ( m, n, a, '  Not persymmetric matrix:' )
  value = r8mat_is_persymmetric ( m, n, a )
  print ( '' )
  print ( '  Persymmetric = %g' % ( value ) )
#
#  Persymmetric.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 4, 3, 2, 1 ], \
    [ 7, 6, 5, 2 ], \
    [ 9, 8, 6, 3 ], \
    [10, 9, 7, 4 ] ] )
  r8mat_print ( m, n, a, '  Persymmetric matrix:' )
  value = r8mat_is_persymmetric ( m, n, a )
  print ( '' )
  print ( '  Persymmetric = %g' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_PERSYMMETRIC_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_persymmetric_test ( )
  timestamp ( )
