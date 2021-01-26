#! /usr/bin/env python
#
def r8mat_is_permutation ( m, n, a ):

#*****************************************************************************80
#
## R8MAT_IS_PERMUTATION checks whether A is a permutation matrix.
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
#    Output, integer IVAL:
#    -1, the matrix is not square;
#    -2, the matrix is not a zero-one matrix.
#    -3, there is a row that does not sum to 1.
#    -4, there is a column that does not sum to 1.
#    1, the matrix is a permutation matrix,
#
  from r8mat_is_zero_one import r8mat_is_zero_one

  if ( m != n ):
    ival = -1
    return ival

  jval = r8mat_is_zero_one ( m, n, a )

  if ( jval != 1 ):
    ival = -2
    return ival

  for i in range ( 0, m ):
    s = 0
    for j in range ( 0, n ):
      if ( a[i,j] == 1 ):
        s = s + 1
    if ( s != 1 ):
      ival = -3
      return ival

  for j in range ( 0, n ):
    s = 0
    for i in range ( 0, m ):
      if ( a[i,j] == 1 ):
        s = s + 1
    if ( s != 1 ):
      ival = -4
      return ival

  ival = 1
  return ival

def r8mat_is_permutation_test ( ):

#*****************************************************************************80
#
## R8MAT_IS_PERMUTATION_TEST tests R8MAT_IS_PERMUTATION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 April 2017
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8mat_print import r8mat_print

  print ( '' )
  print ( 'R8MAT_IS_PERMUTATION_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  R8MAT_IS_PERMUTATION reports whether A is a permutation matrix.' )

  m = 4
  n = 4
  a = np.zeros ( [ m, n ] )
  title = 'Zero matrix'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )

  m = 4
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, m ):
    a[i,i] = 1.0
  title = 'Identity matrix'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )

  m = 4
  n = 4
  a = np.zeros ( [ m, n ] )
  for i in range ( 0, m ):
    a[i,i] = 2.0
  title = '2 * Identity matrix'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )

  m = 4
  n = 4
  a = np.array ( [\
    [0,0,1,0],\
    [0,0,0,1],\
    [1,0,0,0],\
    [0,1,0,0] ])
  title = 'M1'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )

  m = 4
  n = 4
  a = np.array ( [\
    [0,0,1,0],\
    [0,1,0,1],\
    [1,0,0,0],\
    [0,0,0,0] ])
  title = 'M2'
  r8mat_print ( m, n, a, title )
  ival = r8mat_is_permutation ( m, n, a )
  if ( ival == 1 ):
    print ( '%s is a permutation matrix.' % ( title ) )
  else:
    print ( '%s is NOT a permutation matrix.' % ( title ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'R8MAT_IS_PERMUTATION_TEST' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  r8mat_is_permutation_test ( )
  timestamp ( )
