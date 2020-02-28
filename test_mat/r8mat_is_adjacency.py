#! /usr/bin/env python
#
def r8mat_is_adjacency ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_ADJACENCY checks whether A is an adjacency matrix.
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
#    Output, bool R8MAT_IS_ADJACENCY, is True if the matrix is an
#    adjacency matrix.
#
  from r8mat_is_square import r8mat_is_square
  from r8mat_is_symmetric import r8mat_is_symmetric
  from r8mat_is_zero_one import r8mat_is_zero_one

  value = True

  if ( not r8mat_is_square ( m, n, a ) ):
    value = False
    return value

  if ( not r8mat_is_symmetric ( m, n, a ) ):
    value = False
    return value

  if ( not r8mat_is_zero_one ( m, n, a ) ):
    value = False
    return value

  value = True
  return value

def r8mat_is_adjacency_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_ADJACENCY_TEST tests R8MAT_IS_ADJACENCY.
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
  print ( 'R8MAT_IS_ADJACENCY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_ADJACENCY reports whether a matrix' )
  print ( '  is an adjacency matrix.' )
#
#  Not square.
#
  m = 5
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, min ( m, n ) ):
    a[i,i] = 1.0

  r8mat_print ( m, n, a, '  Not square matrix:' )
  value = r8mat_is_adjacency ( m, n, a )
  print ( '' )
  print ( '  Adjacency = %s' % ( value ) )
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
  value = r8mat_is_adjacency ( m, n, a )
  print ( '' )
  print ( '  Adjacency = %s' % ( value ) )
#
#  Square, symmetric, but not zero/one.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 2, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 2, 0, 1, 1 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Not zero/one matrix:' )
  value = r8mat_is_adjacency ( m, n, a )
  print ( '' )
  print ( '  Adjacency = %s' % ( value ) )
#
#  Square, symmetric, zero/one.
#
  m = 4
  n = 4
  a = np.array ( [ \
    [ 1, 0, 1, 0 ], \
    [ 0, 1, 0, 0 ], \
    [ 1, 0, 1, 1 ], \
    [ 0, 0, 1, 1 ] ] )
  r8mat_print ( m, n, a, '  Adjacency matrix:' )
  value = r8mat_is_adjacency ( m, n, a )
  print ( '' )
  print ( '  Adjacency = %s' % ( value ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_ADJACENCY_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_adjacency_test ( )
  timestamp ( )
